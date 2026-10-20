"""Corpus construction: documents, cited passages and provenance.

Each Markdown document is split into passages under its section headings. Every
passage keeps a stable identifier (``<doc_id>#p<n>``), the heading path it belongs to,
its language and a reference to the document's SHA-256 checksum, so that any answer
can be traced back to an exact source.
"""
import datetime as _dt
import hashlib
import json
import os
import re
from dataclasses import asdict, dataclass, field

from .text import detect_lang

SKIP_SECTIONS = {
    "references", "contents", "acronyms", "table of contents", "contact",
    "তথ্যসূত্র", "সূচিপত্র", "সূচীপত্র", "সংক্ষিপ্ত রূপ", "যোগাযোগ",
}
MAX_WORDS = 140


@dataclass
class Document:
    doc_id: str
    title: str
    path: str
    sha256: str
    lang: str
    publisher: str = "BAPIL"
    data_class: str = "P0"
    retrieved: str = ""
    n_passages: int = 0


@dataclass
class Passage:
    pid: str
    doc_id: str
    heading: str
    text: str
    lang: str
    order: int = 0
    meta: dict = field(default_factory=dict)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


_IMG = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]*)\)")
_ANGLE = re.compile(r"<(https?://[^>]+)>")
_EMPH = re.compile(r"(\*\*|__|\*|`)")
_LATEX = re.compile(r"\\[a-zA-Z]+(\{[^}]*\})?")
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)


def clean_markdown(text):
    text = _HTML_COMMENT.sub(" ", text)
    text = _IMG.sub(" ", text)
    text = _LINK.sub(r"\1", text)
    text = _ANGLE.sub(r"\1", text)
    text = _LATEX.sub(" ", text)
    lines = []
    for line in text.splitlines():
        s = line.strip()
        if re.fullmatch(r"\|?[\s:\-|]+\|?", s) and "-" in s:
            continue  # table separator row
        if s.startswith("|"):
            s = " ; ".join(c.strip() for c in s.strip("|").split("|"))
        is_item = bool(re.match(r"^([*\-+]|\d+\.)\s+", s))
        s = re.sub(r"^[*\-+]\s+", "", s)
        s = re.sub(r"^\d+\.\s+", "", s)
        s = _EMPH.sub("", s)
        if is_item and s and s[-1] not in ".;:!?।":
            s += ";"  # keep list items apart when lines are joined into a passage
        lines.append(s)
    return "\n".join(lines)


def _strip_front_matter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def split_markdown(doc_id, text):
    """Split Markdown into passages, keeping the heading path of each passage."""
    text = _strip_front_matter(text)
    passages = []
    path = []
    buf = []
    skipping = False
    in_code = False

    def flush():
        nonlocal buf
        body = clean_markdown("\n".join(buf)).strip()
        buf = []
        if skipping or not body:
            return
        paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        chunk, words = [], 0
        for para in paras:
            w = len(para.split())
            if chunk and words + w > MAX_WORDS:
                _emit(" ".join(chunk))
                chunk, words = [], 0
            chunk.append(para.replace("\n", " "))
            words += w
        if chunk:
            _emit(" ".join(chunk))

    def _emit(body):
        if len(body.split()) < 4:
            return
        n = len(passages) + 1
        heading = " > ".join(path)
        passages.append(Passage(pid="%s#p%d" % (doc_id, n), doc_id=doc_id, heading=heading,
                                text=re.sub(r"\s+", " ", body).strip(), lang=detect_lang(body), order=n))

    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            buf.append(line)
            continue
        m = None if in_code else re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush()
            level = len(m.group(1))
            title = clean_markdown(m.group(2)).strip()
            path = path[: level - 1] + [title]
            norm = re.sub(r"[^\w\s\u0980-\u09ff]", "", title).strip().lower()
            # sections listed in SKIP_SECTIONS (and everything under them) are not indexed
            skipping = any(re.sub(r"[^\w\s\u0980-\u09ff]", "", p).strip().lower() in SKIP_SECTIONS for p in path) \
                or norm in SKIP_SECTIONS
        else:
            buf.append(line)
    flush()
    return passages


def load_markdown(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    doc_id = os.path.splitext(os.path.basename(path))[0]
    title = doc_id
    m = re.search(r"^#\s+(.+)$", _strip_front_matter(text), re.M)
    if m:
        title = clean_markdown(m.group(1)).strip()
    passages = split_markdown(doc_id, text)
    doc = Document(doc_id=doc_id, title=title, path=path.replace(os.sep, "/"), sha256=sha256_file(path),
                   lang=detect_lang(text[:20000]), retrieved=_dt.date.today().isoformat(),
                   n_passages=len(passages))
    return doc, passages


def collect_paths(inputs):
    """Markdown files given directly, or found at the top level of given directories (README files excluded)."""
    paths = []
    for item in inputs:
        if os.path.isdir(item):
            for name in sorted(os.listdir(item)):
                if name.endswith(".md") and not name.endswith(".src.md") and name.lower() != "readme.md":
                    paths.append(os.path.join(item, name))
        elif item.endswith(".md"):
            paths.append(item)
    return paths


def build_corpus(inputs):
    docs, passages = [], []
    for p in collect_paths(inputs):
        d, ps = load_markdown(p)
        if ps:
            docs.append(d)
            passages.extend(ps)
    return docs, passages


def corpus_version(docs):
    h = hashlib.sha256()
    for d in sorted(docs, key=lambda x: x.doc_id):
        h.update(("%s:%s;" % (d.doc_id, d.sha256)).encode())
    return h.hexdigest()[:12]


def save_corpus(path, docs, passages):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    data = {"version": corpus_version(docs), "documents": [asdict(d) for d in docs],
            "passages": [asdict(p) for p in passages]}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    return data["version"]


def load_corpus(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    docs = [Document(**d) for d in data["documents"]]
    passages = [Passage(**p) for p in data["passages"]]
    return docs, passages
