local function latex_escape(s)
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("([%%$#_{}&])", "\\%1")
  s = s:gsub("~", "\\textasciitilde{}")
  s = s:gsub("%^", "\\textasciicircum{}")
  return s
end

function Header(el)
  if el.level >= 4 then
    local title = latex_escape(pandoc.utils.stringify(el))
    return pandoc.RawBlock(
      "latex",
      "\\par\\vspace{0.9em}\\noindent\\textbf{" .. title .. "}\\par\\vspace{0.35em}"
    )
  end
end
