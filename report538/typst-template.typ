#let report(
    title: none,
    author: none,
    date: none,
    abstract: none,
    toc: none,
    toc_depth: 3,
    content,
    bib_file: none,
) = {
    // justify paragraphs
    set par(justify: true)

    // page layout
    set page(
        paper: "us-letter",
          fill: rgb("#f8faf7"), // page background color
        margin: (top: 1in, bottom: 1in, left: 1in, right: 1in),
        header: rect(
          fill: rgb("#e3120b"), 
          width: 10%, 
          height: 4pt, 
          stroke: none
        )[],
        footer: rect(
          fill: rgb("#f8faf7"), 
          width: 100%, 
          stroke: none
        )[#align(center)[©2026 JLM]],
    numbering: "1",
    )

    // headings
    show heading.where(level: 1): it => {
      pagebreak()
      set text(
        font: "Helvetica Neue",
        fill: rgb("#004761"),
        size: 22pt,
        weight: "semibold"
        )
      set align(left)
      block(below: 1em, it)
    }

    show heading.where(level: 2): it => {
      set text(
        font: "Helvetica Neue",
        fill: rgb("#00a398"),
        size: 18pt,
        weight: "semibold"
        )
      set align(left)
      block(below: 1em, it)
    }

    show heading.where(level: 3): it => {
      set text(
        font: "Helvetica Neue",
        fill: rgb("#00a398"),
        size: 14pt,
        weight: "semibold"
        )
      set align(left)
      block(below: 1em, it)
    }

v(1fr) // Use 1fr above and below to push it to the middle

// title
  if title != none {
  // Use 1fr above and below to push it to the middle 
    block(
      below: 5em,
      width: 100%,
      align(center, text(
        font: "Helvetica Neue",
        weight: "bold",
        size: 34pt, // title size
        fill: rgb("#e3120b"),
        title))
    )
  }

  // author
  if author != none {
    block(
      below: 2em,
      width: 100%,
      align(center, text(
        font: "Helvetica Neue",
        weight: "bold",
        size: 22pt,
        fill: rgb("#00313a"),
        author))
    )
  }

  // date
  if date != none { 
    block(
      width: 100%,
      align(center, text(
        font: "Helvetica Neue",
        style: "italic",
        size: 12pt,
        fill: rgb("#4b4f54"),
        date))
    )
  }
  v(1fr) // Use 1fr above and below to push it to the middle

// Style the Abstract
  pagebreak() // add page break before abstract

  if abstract != none {
    // 1. Label and styling for the entire block
    pad(x: 2em, top: 1em, bottom: 1em)[
      #text(weight: "bold")[Abstract:] \
      
      // 2. Styled and Justified Abstract Text
      //#set align(justify)

      #set text(
        font: "Helvetica Neue",
        style: "italic",
        size: 12pt,
        fill: rgb("#4b4f54")
      )
      
      #abstract
    ]
  }

  // Table of Contents
  show outline.entry.where(level: 1): it => {
    v(12pt, weak: true)
    set text(font: "Helvetica Neue", weight: "bold")
    it
  }

  outline(
    title: [Table of Contents
      #v(14pt)
    ],
    depth: toc_depth,
    indent: 1.5em,
    target: heading.where(outlined: true) 
  )

  // list of tables
  outline(
    title: [List of Tables
      #v(14pt)
    ],
    target: figure.where(kind: table),
  )

  // list of figures
  outline(
    title: [List of Figures],
    target: figure.where(kind: image),
  )

  // body text
  set text(
        lang: "en",
        region: "US",
        font: "Helvetica Neue",
        size: 12pt,
        fill: rgb("#4b4f54"),
    )
  
  content
  
  // bibliography
  if bib_file != none {
        pagebreak()
        // Optional: Style the bibliography heading
        set heading(numbering: "1")
        bibliography(
            bib_file,
            title: "References",
            style: "apa" // You can change this to "chicago-author-date", etc.
        )
  }

}
