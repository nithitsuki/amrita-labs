#!/usr/bin/env python3
"""Normalise one answers fragment for the CN endsem answers file.

Target shape, for every paper:

    * CNE<n> answers
    ** Q<n>  topic  [marks]
    *** Answer

Fragments in _parts arrive in two shapes:

  A. no parent heading, questions at level 2
        ** Q1 ...
        *** Answer

  B. one or two parent headings, questions one level below the parent
        ** CNE2 answers
        *** CNE2 Q1 ...
        **** Answer

The script finds each paper block, works out the shift that puts the parent
at level 1, and applies the same shift to the rest of the block.
"""
import re
import sys
import pathlib

PARENT = re.compile(r'^(\*+)\s+(CNE\d+)\s+answers\s*$')
HEADING = re.compile(r'^(\*+)\s')
BOLD = re.compile(r'\*\*(?=\S)([^*\n]+?)\*\*(?!\*)')


def shift_line(line: str, delta: int) -> str:
    if delta == 0 or not line.startswith('*'):
        return line
    m = HEADING.match(line)
    if not m:
        return line
    stars = max(1, len(m.group(1)) + delta)
    return '*' * stars + line[len(m.group(1)):]


def min_heading_level(lines):
    levels = [len(HEADING.match(l).group(1)) for l in lines if HEADING.match(l)]
    return min(levels) if levels else 0


def main(path: str) -> None:
    p = pathlib.Path(path)
    lines = [BOLD.sub(r'*\1*', l) for l in p.read_text().split('\n')]
    paper_hint = re.search(r'CNE\d', p.name).group(0)

    # split into blocks that begin at a paper parent heading
    blocks = []
    current = None
    preamble = []
    for line in lines:
        m = PARENT.match(line.strip())
        if m:
            if current:
                blocks.append(current)
            current = {'paper': m.group(2), 'level': len(m.group(1)), 'lines': [line]}
        elif current:
            current['lines'].append(line)
        else:
            preamble.append(line)
    if current:
        blocks.append(current)

    out = []
    if not blocks:
        # shape A: whole file is one paper, questions already at level 2
        body = preamble
        # strip leading blank lines
        while body and not body[0].strip():
            body.pop(0)
        minimum = min_heading_level(body)
        delta = 2 - minimum if minimum else 0
        out.append(f'* {paper_hint} answers')
        out.append('')
        out.extend(shift_line(l, delta) for l in body)
    else:
        stripped = [l for l in preamble if l.strip()]
        if stripped:
            out.extend(stripped)
            out.append('')
        for b in blocks:
            delta = 1 - b['level']
            out.extend(shift_line(l, delta) for l in b['lines'])

    text = '\n'.join(out)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    print(text.rstrip('\n'))


if __name__ == '__main__':
    main(sys.argv[1])
