#let report(
  title: none,
  subtitle: none,
  author: none,
  abstract: none,
  date: none,
  toc: false,
  lof: false,
  lot: false,
  body
) = {
  
  // color variables
  let econ-red = rgb("#e3120b")
  let econ-blue = rgb("#01516c") //006ba2
  let econ-teal = rgb("#169C7F")
  let econ-black = rgb("#303033")


  //set document(title: title, author: author)
  set document(title: title, author: (author,))

  set page(
    paper: "us-letter",
    fill: rgb("#f8faf7"), // page background color
    margin: (left: 2cm, right: 2.5cm, top:2cm, bottom:2cm),
    //header line
    header: context {
      if counter(page).get().at(0) > 1 {
        rect(
          fill: econ-red, 
          width: 10%, 
          height: 4pt, 
          stroke: none
        )
      }
    },
    // Footer needs context to access the counter
    footer: context {
      set text(8pt, fill: econ-blue)
      //line(length: 20%, stroke: 1pt + rgb("#e3120B")) //9c1633
      grid(
        columns: (1fr, 1fr),
        [© 2026 JLM],
        align(right, counter(page).display())
      )
    }
  )

  set text(font: "Helvetica Neue", size: 10.5pt)
  set par(justify: true)

  // Heading Styles
  show heading.where(level: 1): it => {
    set text(fill: econ-red, size: 22pt, weight: "bold")
    //upper(
      it.body
    //)
    v(0.2em)
  }

  // Style for H2
  show heading.where(level: 2): it => {
    set text(fill: econ-blue, size: 18pt, weight: "bold")
    it.body
    v(0.2em)
  }
  
  // Style for H3
  show heading.where(level: 3): it => {
    set text(fill: econ-teal, size: 16pt, weight: "bold")
    it.body
    v(0.1em)
  }


  // title, subtitle, author, date
  block(width: 100%, {
    // 1. Wrap the text elements in an align(center) so they all move together
    v(15em)
    align(center, {
      // Title
      text(fill: econ-red, weight: "bold", size: 31pt)[#title] //set title size
      v(0.5em)
      
      // 2. The line is already centered, but ensure it has space
      align(center, line(length: 20%, stroke: 2pt + econ-red))
      v(1em)
      
      // Subtitle
      if subtitle != none {
        text(size: 18pt, style: "italic", fill: econ-blue)[#subtitle]
        v(5em) 
      }

      // 3. Author and Date (Now properly centered by the outer align)
      text(size: 15pt, style: "italic", fill: econ-black)[#author]
      v(2em)
      text(fill: rgb("#666666"), size: 12pt)[#date]
    })
  })

  // Abstract Section
  if abstract != none {
    pagebreak(weak: true)
    v(1em)
    // Wrap everything in a center alignment block
    align(left, {
      // Abstract Heading
      text(fill: econ-red, weight: "bold", size: 16pt)[Abstract]
      v(0.5em) 
      
      // Abstract Content
      // Set a maximum width so the lines don't span the whole page (better for centering)
      block(width: 90%, {
        set text(size: 10.5pt, style: "italic")
        set par(justify: true) // Centered text usually looks better non-justified
        abstract
      })
    })
    
    v(2em) 
    pagebreak(weak: true)
  }

  // Outlines often need context in newer Typst versions 
  // if they are inside complex layout blocks
  if toc {
    context outline(title: "Table of Contents")
    pagebreak(weak: true)
  }
  
  if lof { 
    context outline(
      title: "List of Figures",
      target: figure.where(supplement: [Figure])
    ) 
    pagebreak(weak: true)
  }


  if lot {
    context outline(
      title: "List of Tables",
      //target: figure.where(kind: table)
      target: figure.where(supplement: [Table])
      )
    pagebreak(weak: true)
  }

  // change bibliography title
  set bibliography(title: "References", style: "apa")

  show bibliography: it => {
    pagebreak(weak: true)
    v(0.5em)
    it
  }

  body
}
