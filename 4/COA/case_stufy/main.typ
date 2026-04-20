// ── x86-64 vs ARMv8 Case Study ──────────────────────────────────────────
#set document(title: "x86-64 vs ARMv8: A Case Study", author: "")
#set page(
  paper: "a4",
  margin: (x: 2.4cm, y: 2.4cm),
  header: [
    #set text(size: 8pt, fill: luma(140))
    #smallcaps[Case Study] #h(1fr) x86-64 vs ARMv8
    #line(length: 100%, stroke: 0.4pt + luma(200))
  ],
)
#set text(font: "New Computer Modern", size: 10.5pt, lang: "en")
#set par(justify: true, leading: 0.65em)
#show heading.where(level: 1): h => {
  v(1em)
  block(
    fill: rgb("#1a1a2e"),
    inset: (x: 10pt, y: 6pt),
    radius: 4pt,
    width: 100%,
    text(fill: white, size: 12pt, weight: "bold", h.body)
  )
  v(0.4em)
}
#show heading.where(level: 2): h => {
  v(0.6em)
  text(fill: rgb("#16213e"), size: 10.5pt, weight: "bold", h.body)
  v(0.2em)
}

// ── Title Block ────────────────────────────────────────────────────────────
#align(center)[
  #v(0.5em)
  #text(size: 20pt, weight: "extrabold", fill: rgb("#1a1a2e"))[
    x86-64 vs ARMv8
  ]
  #v(0.2em)
  #text(size: 11pt, fill: luma(80))[A  Case Study in ISA Design]
  #v(0.15em)
  #text(size: 9pt, fill: luma(95))[made by nithilan rameshkumar, bl.sc.u4cse24031]
  #v(0.3em)
  #line(length: 60%, stroke: 1.5pt + rgb("#e94560"))
  #v(0.8em)
]

// ── Introduction ───────────────────────────────────────────────────────────
= Introduction

#columns(2)[
  *x86-64* is the 64-bit version of x86 and is common in PCs and servers.
  It keeps compatibility with older software, so the design is a bit complex.

  #colbreak()

  *ARMv8* is ARM's 64-bit ISA. It is widely used in phones and
  is now also popular in laptops and cloud systems.
]

// ── 1. Architecture Type ───────────────────────────────────────────────────
= 1 · Architecture Type

#table(
  columns: (1fr, 1fr, 1fr),
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f0f4ff") } else { white },
  inset: 8pt,
  stroke: none,
  table.header(
    text(fill: white, weight: "bold")[Property],
    text(fill: white, weight: "bold")[x86-64],
    text(fill: white, weight: "bold")[ARMv8],
  ),
  [ISA Family],   [CISC],                       [RISC],
  [Encoding],     [Variable-length],            [Fixed 32-bit],
  [Main Focus],   [Compatibility + performance],[Efficiency + simplicity],
  [Common Use],   [PCs and servers],            [Mobile and newer laptops],
)

#v(0.4em)
x86-64 uses a CISC style with more complex instructions.
ARMv8 follows RISC and keeps instructions simpler and more regular.

// ── 2. Registers ───────────────────────────────────────────────────────────
= 2 · Registers

== x86-64 Registers
x86-64 has *16 general-purpose 64-bit registers* (`RAX` to `R15`).
It also has smaller views (`EAX`, `AX`, `AL`), which come from older x86 design.

#table(
  columns: (auto, auto, 1fr),
  fill: (_, row) => if row == 0 { rgb("#e94560") } else if calc.odd(row) { rgb("#fff0f0") } else { white },
  inset: 7pt,
  stroke: none,
  table.header(
    text(fill: white, weight: "bold")[Register Set],
    text(fill: white, weight: "bold")[Count],
    text(fill: white, weight: "bold")[Notes],
  ),
  [GP (64-bit)],   [16], [`RAX`-`R15`],
  [SIMD/FP],       [16], [`XMM0`-`XMM15`],
  [Flags],         [1],  [`RFLAGS`],
  [Instruction Ptr],[1], [`RIP`],
)

== ARMv8 Registers
ARMv8 has *31 general-purpose 64-bit registers* (`X0`-`X30`) plus `SP`
and `XZR`. The register model is cleaner than x86-64.

#table(
  columns: (auto, auto, 1fr),
  fill: (_, row) => if row == 0 { rgb("#0f3460") } else if calc.odd(row) { rgb("#f0f4ff") } else { white },
  inset: 7pt,
  stroke: none,
  table.header(
    text(fill: white, weight: "bold")[Register Set],
    text(fill: white, weight: "bold")[Count],
    text(fill: white, weight: "bold")[Notes],
  ),
  [GP (64-bit)],   [31], [`X0`-`X30`],
  [Zero Reg],      [1],  [`XZR`],
  [Stack Pointer], [1],  [`SP`],
  [SIMD/FP],       [32], [`V0`-`V31`],
  [Flags],         [1],  [`NZCV`],
)

#v(0.4em)
Main difference: ARM has more GP registers (31 vs 16), so it usually needs
fewer memory spills.

// ── 3. Instruction Sizes ───────────────────────────────────────────────────
= 3 · Instruction Sizes

#columns(2)[
  == x86-64
  Instructions are *variable-length* (1 to 15 bytes). This gives flexibility
  but makes decoding harder.

  #table(
    columns: (auto, 1fr),
    fill: (_, row) => if row == 0 { rgb("#e94560") } else if calc.odd(row) { rgb("#fff0f0") } else { white },
    inset: 6pt, stroke: none,
    table.header(text(fill:white,weight:"bold")[Length], text(fill:white,weight:"bold")[Example]),
    [1 B], [`NOP`],
    [2-3 B], [Simple instructions],
    [4-8 B], [Memory instructions],
    [Up to 15 B], [Complex/vector instructions],
  )
  #colbreak()

  == ARMv8
  Instructions are *fixed 32 bits* (4 bytes) in ARMv8, so decoding is easier
  and instruction boundaries are clear.

  #table(
    columns: (auto, 1fr),
    fill: (_, row) => if row == 0 { rgb("#0f3460") } else if calc.odd(row) { rgb("#f0f4ff") } else { white },
    inset: 6pt, stroke: none,
    table.header(text(fill:white,weight:"bold")[Length], text(fill:white,weight:"bold")[Notes]),
    [32 bits], [All ARMv8 instructions],
    [16/32 bits], [Older ARM modes used mixed sizes],
  )
]

So, x86-64 is flexible but complex; ARMv8 is simpler for hardware decode.

// ── 4. Pipelining & Hazards ────────────────────────────────────────────────
= 4 · Pipelining and Hazards

== Overview

Both use modern pipelining and out-of-order execution in real CPUs.

#table(
  columns: (1fr, 1fr, 1fr),
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f0f4ff") } else { white },
  inset: 8pt,
  stroke: none,
  table.header(
    text(fill: white, weight: "bold")[Aspect],
    text(fill: white, weight: "bold")[x86-64],
    text(fill: white, weight: "bold")[ARMv8],
  ),
  [Decode],           [Complex, variable-length], [Simpler, fixed-length],
  [Register handling],[Legacy aliases exist],      [Cleaner model],
  [Power use],        [Usually higher],            [Usually better],
  [Performance],      [Very strong in high-end CPUs], [Strong and efficient],
)

== Data Hazards
Both use techniques like forwarding and register renaming to reduce stalls.
x86-64 has extra complexity from partial registers.

== Control Hazards
Both depend on branch prediction. Wrong predictions cause pipeline flushes and
performance loss.

// ── Summary ────────────────────────────────────────────────────────────────
= Summary

#table(
  columns: (1fr, 1fr, 1fr),
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") }
                    else if calc.odd(row) { rgb("#f0f4ff") }
                    else { white },
  inset: 8pt,
  stroke: none,
  table.header(
    text(fill: white, weight: "bold")[Dimension],
    text(fill: white, weight: "bold")[x86-64],
    text(fill: white, weight: "bold")[ARMv8],
  ),
  [ISA class],        [CISC],            [RISC],
  [GP Registers],     [16],              [31],
  [Instr. size],      [1-15 bytes],      [Fixed 32 bits],
  [Decode],           [Harder],          [Easier],
  [Power efficiency], [Medium],          [High],
)

x86-64 is still excellent for compatibility and high-end desktop/server use.
ARMv8 is simpler and often more power-efficient, which is why it is growing
fast in phones, laptops, and cloud.
