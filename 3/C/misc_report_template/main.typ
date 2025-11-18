#set page(paper: "a4", margin: 1in)
#set par(justify: true)

// Configuration Variables
#let project-title = "Project Title"
#let project-subtitle = "A PROJECT REPORT"
#let enrollment = (
  ("BL.EN.U4CSE22-----", "Name1"),
  ("BL.EN.U4CSE22-----", "Name2"),
  ("BL.EN.U4CSE22-----", "Name3"),
)
#let guide-name = "GUIDE NAME AND DESIGNATION"

// Font Size Configuration
#let title-size = 22pt
#let heading-size = 16pt
#let subheading-size = 14pt
#let normal-size = 14pt
#let small-size = 14pt //names
#let body-size = 14pt

// PAGE 1: Title Page
#align(center)[
  #text(size: title-size, weight: "bold")[#project-title]
  #v(0.6cm)

  #text(size: normal-size, weight: "semibold")[#project-subtitle]
  #v(1.5cm)

  #text(size: normal-size, weight: "bold", style: "italic")[Submitted by]
  #v(0.6cm)

  #for (id, name) in enrollment [
    #text(size: small-size)[#id] #h(2cm) #text(size: small-size)[#name] \
  ]
  #v(1cm)

  #text(size: normal-size, weight: "bold")[in partial fulfillment for the award of the]

  #text(size: subheading-size, weight: "bold")[BACHELOR OF TECHNOLOGY] \
  #text(size: normal-size)[IN]

  #text(size: normal-size)[COMPUTER SCIENCE AND ENGINEERING]
  #v(1cm)

  #image("logo.svg")
  #v(1cm)

  #text(size: normal-size, weight: "semibold")[AMRITA SCHOOL OF COMPUTING, BENGALURU]
  #v(0.4cm)

  #text(size: normal-size, weight: "semibold")[AMRITA VISHWA VIDYAPEETHAM]
]


// PAGE 2: Acknowledgements Page
#pagebreak()
#align(center)[
  #text(size: heading-size, weight: "bold")[ACKNOWLEDGEMENTS]
]
#v(1cm)
#set par(justify: true, leading: 0.65em)
#set text(size: body-size)

The satisfaction that accompanies successful completion of any task would be incomplete without mention of people who made it possible, and whose constant encouragement and guidance have been source of inspiration throughout the course of this project work.

We offer our sincere pranams at the lotus feet of *"AMMA", MATA AMRITANANDAMAYI DEVI* who showered her blessing upon us throughout the course of this project work.

We owe our gratitude to *Prof. Manoj P.*, Director, Amrita Vishwa Vidyapeetham Bengaluru Campus. We would like to place our heartfelt gratitude to *Dr. Gopalakrishnan E.A.*, Principal, Amrita School of Computing and Amrita School of Artificial Intelligence, Bengaluru for his valuable support and inspiration.

It is a great pleasure to express our gratitude and indebtedness to our project guide #text(fill: red, weight: "bold")[#guide-name], Department of Computer Science and Engineering, Amrita School of Computing, Bengaluru for her/his valuable guidance, encouragement, moral support, and affection throughout the project work.

We would like to thank express our gratitude to project panel members for their suggestions, encouragement, and moral support during the process of project work and all faculty members for their academic support. Finally, we are forever grateful to our parents, who have loved, supported and encouraged us in all our endeavors.


// PAGE 3: Abstract Page
#pagebreak()
#align(center)[
  #text(size: title-size, weight: "bold")[ABSTRACT]
]

#text()[
  one paragraph abstract text goes here.
]

// PAGE 4: TABLE OF CONTENTS
#pagebreak()
#align(center)[
  #text(size: heading-size, weight: "bold")[TABLE OF CONTENTS]
]
#v(0.5cm)
#outline()

//PAGE 5: CHAPTER 1 INTRODUCTION (and start of chapters)
#pagebreak()

// Function to create chapter pages with proper headers
#let chapter(chapter-name, chapter-num, chapter-title, body) = {
  // Set up page headers and footers for this chapter
  set page(
    header: [
      #set text(size: small-size)
      #table(
        columns: (1fr, 1fr),
        stroke: none,
        inset: 5pt,
        align: (left, right),
        [#chapter-name], 
        [#datetime.today().display("[month repr:long], [year]")]
      )
    ],
    footer: context [
      #set text(size: small-size)
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        [Dept. of CSE, ASC, Bengaluru],
        [Page | #counter(page).display()]
      )
    ]
  )
  
  // Chapter heading
  [
    #align(center)[
      #text(size: heading-size, weight: "bold")[ = CHAPTER - #chapter-num]
      #v(0.3cm)
      #text(size: heading-size, weight: "bold")[#chapter-title]
    ]
    #v(1cm)
    
    // Chapter body content
    #body
  ]
}

// Reset page counter for content
#counter(page).update(1)

// CHAPTER 1: INTRODUCTION
#chapter("Introduction", "1", "INTRODUCTION")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)
  
  == Chapter 1.1
]

// CHAPTER 2: LITERATURE REVIEW 
#pagebreak()
#chapter("Literature Review", "2", "LITERATURE REVIEW")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)
  
  
]
// CHAPTER 3: SYSTEM SPECIFICATIONS
#pagebreak()
#chapter("System Specifications", "3", "SYSTEM SPECIFICATIONS")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)
  
  
]

// CHAPTER 4: SYSTEM DESIGN
#pagebreak()
#chapter("System Design", "4", "SYSTEM DESIGN")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)
  
  
]

// CHAPTER 5: SYSTEM IMPLEMENTATION
#pagebreak()
#chapter("System Implementation", "5", "SYSTEM IMPLEMENTATION")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)
  
  
]

// CHAPTER 6: SYSTEM TESTING
#pagebreak()
#chapter("System Testing", "6", "SYSTEM TESTING")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)
  
  
]

// CHAPTER 7: RESULTS AND ANALYSIS
#pagebreak()
#chapter("Results and Analysis", "7", "RESULTS AND ANALYSIS")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)
  
  
]

// CHAPTER 8: CONCLUSION AND FUTURE SCOPE
#pagebreak()
#chapter("Conclusion and Future Scope", "8", "CONCLUSION AND FUTURE SCOPE")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)
  
  
]

// CHAPTER 9: REFERENCES
#pagebreak()
#chapter("References", "9", "REFERENCES")[
  #set text(size: body-size)
  #set par(justify: true, leading: 0.65em)

  // To use a bibliography, you would typically use a .bib file
  // and the bibliography function.
  // For example:
  // #bibliography("references.bib", style: "ieee")

  // For now, here are the example references from the image, manually formatted.
  [
    [1] R.E. Uhrig, "Introduction to Artificial Neural Networks", Industrial Electronics, Control, and Instrumentation, Proceedings of the IEEE IECON 21st International Conference, Vol. 1, pp. 33-37, 1995.
  ]
  #v(0.5em)
  [
    [2] Domenico Luca Carn, Domenico Grimaldi, "ANN based demodulator for UMTS signal measurements", Measurement Journal, Vol. 39, Issue. 10, pp. 877-883, 2006.
  ]
]