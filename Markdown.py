markdown_summary = """
# Markdown Syntax for Jupyter Notebooks

## Headers
\`\`\`markdown
# H1
## H2
### H3
#### H4
##### H5
###### H6
\`\`\`
- Example:
  \`\`\`markdown
  # This is an H1
  ## This is an H2
  ### This is an H3
  \`\`\`

## Emphasis
\`\`\`markdown
*Italic* or _Italic_
**Bold** or __Bold__
***Bold and Italic*** or ___Bold and Italic___
\`\`\`
- Example:
  \`\`\`markdown
  *Italic* and **Bold**
  \`\`\`

## Lists

### Unordered List
\`\`\`markdown
- Item 1
  - Subitem 1
- Item 2
\`\`\`
- Example:
  \`\`\`markdown
  - Item 1
    - Subitem 1
  - Item 2
  \`\`\`

### Ordered List
\`\`\`markdown
1. Item 1
2. Item 2
   1. Subitem 2.1
\`\`\`
- Example:
  \`\`\`markdown
  1. Item 1
  2. Item 2
     1. Subitem 2.1
  \`\`\`

## Links
\`\`\`markdown
[Link Text](https://example.com)
\`\`\`
- Example:
  \`\`\`markdown
  [OpenAI](https://openai.com)
  \`\`\`

## Images
\`\`\`markdown
![Alt Text](https://example.com/image.jpg)
\`\`\`
- Example:
  \`\`\`markdown
  ![OpenAI Logo](https://openai.com/logo.png)
  \`\`\`

## Blockquotes
\`\`\`markdown
> This is a blockquote.
\`\`\`
- Example:
  \`\`\`markdown
  > This is a blockquote.
  \`\`\`

## Code

### Inline Code
\`\`\`markdown
\`Inline code\`
\`\`\`
- Example:
  \`\`\`markdown
  \`print("Hello, World!")\`
  \`\`\`

### Code Blocks
\`\`\`markdown
\`\`\`
code block
\`\`\`
\`\`\`
- Example:
  \`\`\`\`markdown
  \`\`\`
  print("Hello, World!")
  \`\`\`
  \`\`\`\`

## Horizontal Line
\`\`\`markdown
---
\`\`\`
- Example:
  \`\`\`markdown
  ---
  \`\`\`

## Tables
\`\`\`markdown
| Header 1 | Header 2 |
|----------|----------|
| Row 1 Col 1 | Row 1 Col 2 |
| Row 2 Col 1 | Row 2 Col 2 |
\`\`\`
- Example:
  \`\`\`markdown
  | Header 1 | Header 2 |
  |----------|----------|
  | Row 1 Col 1 | Row 1 Col 2 |
  | Row 2 Col 1 | Row 2 Col 2 |
  \`\`\`

## LaTeX for Mathematical Expressions
\`\`\`markdown
Inline: \$E = mc^2\$
Block: \$\$E = mc^2\$\$
\`\`\`
- Example:
  \`\`\`markdown
  Inline: \$E = mc^2\$

  Block:
  \$\$
  E = mc^2
  \$\$
  \`\`\`

## Line Breaks
- Use two spaces at the end of a line, or an empty line to create a new paragraph.
\`\`\`markdown
Line 1  
Line 2

New paragraph
\`\`\`
- Example:
  \`\`\`markdown
  Line 1  
  Line 2

  New paragraph
  \`\`\`

## Combining Text Formatting
- Markdown allows combining different styles.
\`\`\`markdown
**Bold and _italic_**
\`\`\`
- Example:
  \`\`\`markdown
  **Bold and _italic_**
  \`\`\`

---

This summary covers the essential Markdown syntax used in Jupyter notebooks. For more advanced formatting, you can refer to the [Markdown Guide](https://www.markdownguide.org/basic-syntax/) or the [Jupyter Notebook documentation](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).
"""

with open("markdown_summary.py", "w") as file:
    file.write(markdown_summary)
