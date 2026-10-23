-- Pandoc Lua filter for the BAPIL Blueprint PDFs.
--  * uses the vector PDF version of every figure instead of the PNG
--  * turns "Image paragraph + *Figure N. caption*" into a real figure with that caption
--  * turns "**Table N.** title" placed before a table into the table caption
--  * replaces the "Contents" heading with the LaTeX table of contents
--  * keeps front-matter headings (before Part I or Chapter 1) out of the table of contents
--  * turns "# Part ..." / "# অংশ ..." headings into part divider pages listed in the contents
--  * "List of Figures" / "List of Tables" headings become the LaTeX lists

local function starts_with(s, prefix)
  return s:sub(1, #prefix) == prefix
end

local function is_fig_caption(blk)
  if blk.t ~= "Para" or #blk.content < 1 or blk.content[1].t ~= "Emph" then return false end
  local s = pandoc.utils.stringify(blk.content[1])
  return starts_with(s, "Figure ") or starts_with(s, "চিত্র ")
end

local function is_tab_caption(blk)
  if blk.t ~= "Para" or #blk.content < 1 or blk.content[1].t ~= "Strong" then return false end
  local s = pandoc.utils.stringify(blk.content[1])
  return starts_with(s, "Table ") or starts_with(s, "সারণি ")
end

local function single_image(blk)
  if (blk.t == "Para" or blk.t == "Plain") and #blk.content == 1 and blk.content[1].t == "Image" then
    return blk.content[1]
  end
  if blk.t == "Figure" then
    local img = nil
    pandoc.walk_block(blk, { Image = function(i) img = i end })
    return img
  end
  return nil
end

local function split_label(inlines)
  -- first sentence-ending token ("." or "।") ends the label; label is made bold
  local label, rest, done = {}, {}, false
  for _, il in ipairs(inlines) do
    if not done then
      table.insert(label, il)
      if il.t == "Str" and (il.text:match("%.$") or il.text:match("।$")) then done = true end
    else
      table.insert(rest, il)
    end
  end
  if not done then return inlines end
  local out = { pandoc.Strong(label) }
  for _, il in ipairs(rest) do table.insert(out, il) end
  return out
end

-- Web addresses: keep "https://" (or "http://") together, so that a line never breaks inside the
-- scheme ("ht" / "tps://"); a line may end after the scheme, and the rest of the address may still
-- break anywhere (xurl). Only plain
-- autolinks whose address has no characters that need escaping in LaTeX are changed.
function Link(el)
  if not FORMAT:match("latex") then return nil end
  local url = el.target
  if pandoc.utils.stringify(el.content) ~= url then return nil end
  local scheme, rest = url:match("^(https?://)(.+)$")
  if not scheme or rest:find("[%%#&{}~\\^$]") then return nil end
  return pandoc.RawInline("latex",
    "\\href{" .. url .. "}{\\mbox{\\nolinkurl{" .. scheme .. "}}\\allowbreak\\nolinkurl{" .. rest .. "}}")
end

function Image(img)
  img.src = img.src:gsub("%.png$", ".pdf")
  return img
end

local in_front = true
local has_chapters = false

local function is_part(t)
  return starts_with(t, "Part ") or starts_with(t, "অংশ ")
end

local function tex_escape(s)
  return (s:gsub("([&%%$#_])", "\\%1"))
end

local function part_page(title, desc)
  local label, name = title:match("^(.-):%s*(.+)$")
  if not label then label, name = title, "" end
  local tex = "\\clearpage\n\\thispagestyle{empty}\n\\vspace*{0.30\\textheight}\n\\begin{center}\n" ..
    "{\\large\\bfseries " .. tex_escape(label) .. "}\\par\\vspace{0.8em}\n" ..
    "{\\Huge\\bfseries " .. tex_escape(name) .. "}\\par\\vspace{1.6em}\n"
  if desc and desc ~= "" then
    tex = tex .. "\\begin{minipage}{0.72\\textwidth}\\centering\\itshape " .. tex_escape(desc) .. "\\end{minipage}\n"
  end
  tex = tex .. "\\end{center}\n\\addcontentsline{toc}{part}{" .. tex_escape(title) .. "}\n\\clearpage"
  return pandoc.RawBlock("latex", tex)
end

function Pandoc(doc)
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" then
      local t = pandoc.utils.stringify(b)
      if starts_with(t, "Chapter 1:") or starts_with(t, "অধ্যায় ১:") or (b.level == 1 and is_part(t)) then has_chapters = true end
    end
  end
  local out = {}
  local i = 1
  local blocks = doc.blocks
  while i <= #blocks do
    local b = blocks[i]
    local nxt = blocks[i + 1]
    local img = single_image(b)
    if b.t == "Header" then
      local t = pandoc.utils.stringify(b)
      if t == "Contents" or t == "সূচিপত্র" then
        table.insert(out, pandoc.RawBlock("latex", "\\bapiltableofcontents"))
        i = i + 1
        goto continue
      end
      if t == "List of Figures" or t == "চিত্রের তালিকা" then
        table.insert(out, pandoc.RawBlock("latex", "\\listoffigures"))
        i = i + 1
        goto continue
      end
      if t == "List of Tables" or t == "সারণির তালিকা" then
        table.insert(out, pandoc.RawBlock("latex", "\\listoftables"))
        i = i + 1
        goto continue
      end
      if b.level == 1 and is_part(t) then
        in_front = false
        local desc = ""
        if nxt and nxt.t == "Para" and #nxt.content == 1 and nxt.content[1].t == "Emph" then
          desc = pandoc.utils.stringify(nxt)
          i = i + 1
        end
        table.insert(out, part_page(t, desc))
        i = i + 1
        goto continue
      end
      if starts_with(t, "Chapter 1:") or starts_with(t, "অধ্যায় ১:") then in_front = false end
      if has_chapters and in_front then
        b.classes:insert("unnumbered"); b.classes:insert("unlisted")
      end
      table.insert(out, b)
    elseif img and nxt and is_fig_caption(nxt) then
      img.caption = {}
      img.src = img.src:gsub("%.png$", ".pdf")
      local cap = split_label(nxt.content[1].content)
      local fig = pandoc.Figure({ pandoc.Plain({ img }) }, { pandoc.Plain(cap) })
      table.insert(out, fig)
      i = i + 2
      goto continue
    elseif is_tab_caption(b) and nxt and nxt.t == "Table" then
      local cap = {}
      for _, il in ipairs(b.content) do table.insert(cap, il) end
      nxt.caption = { long = { pandoc.Plain(cap) }, short = cap }
      table.insert(out, nxt)
      i = i + 2
      goto continue
    else
      table.insert(out, b)
    end
    i = i + 1
    ::continue::
  end
  doc.blocks = out
  return doc
end
