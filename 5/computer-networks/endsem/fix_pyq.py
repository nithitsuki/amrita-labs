#!/usr/bin/env python3
"""Fix and finalise the paper bank.

Two jobs, both idempotent:
  1. Renumber the CNE3 questions to match the printed paper, Q1a to Q10.
     The extractor split them as Q2a/Q2b/Q2c and Q3a..Q5b, which does not
     match either the paper or the answer file.
  2. Rebuild the coverage map table and the per-unit totals from whatever
     headings are actually in the file, so the table can never drift again.

Run from anywhere. Writes _parts/90-pyq.org in place.
"""
import re
import pathlib

PATH = pathlib.Path(__file__).parent / '_parts' / '90-pyq.org'

RENAMES = [('Q2a', 'Q2'), ('Q2b', 'Q3'), ('Q2c', 'Q4'),
           ('Q3a', 'Q5'), ('Q3b', 'Q6'), ('Q4a', 'Q7'),
           ('Q4b', 'Q8'), ('Q5a', 'Q9'), ('Q5b', 'Q10')]

UNIT_ORDER = {'CO1': 0, 'CO2': 1, 'CO3': 2, 'CO4': 3, 'CO5': 4, 'CO6': 5}


def split_blocks(lines):
    """Return (preamble, [blocks]) where a block starts at a `** CNEx` line."""
    pre, blocks, cur = [], [], None
    for line in lines:
        m = re.match(r'^\*\* (CNE\d)\b', line)
        if m:
            if cur:
                blocks.append(cur)
            cur = {'paper': m.group(1), 'lines': [line]}
        elif cur:
            cur['lines'].append(line)
        else:
            pre.append(line)
    if cur:
        blocks.append(cur)
    return pre, blocks


def renumber_cne3(lines):
    """Rename CNE3 question headings, only inside the CNE3 block."""
    out, in_cne3 = [], False
    for line in lines:
        if re.match(r'^\*\* CNE\d', line):
            in_cne3 = line.startswith('** CNE3')
        if in_cne3:
            for old, new in RENAMES:
                line = re.sub(r'^(\*\*\* )' + old + r'(\s{2,})',
                              lambda m, n=new: m.group(1) + n + m.group(2),
                              line)
        out.append(line)
    return out


def fix_refs(lines):
    """Rename CNE3 cross-references anywhere in the file.

    'CNE3 Q2a' is unambiguous, so a global replace is safe. The coverage
    table and the triage lists sit outside the CNE3 block, so a scoped
    replace would miss them.
    """
    out = []
    for line in lines:
        for old, new in RENAMES:
            line = line.replace('CNE3 ' + old, 'CNE3 ' + new)
        out.append(line)
    return out


def build_table(lines):
    pre, blocks = split_blocks(lines)
    rows = []
    for b in blocks:
        for line in b['lines']:
            m = re.match(r'^\*\*\* (Q\S+)\s{2,}(.*?)\s{2,}\[([0-9?]+)\]\s{2,}\[(CO\d)\??\]', line)
            if m:
                rows.append((m.group(4), b['paper'], m.group(1),
                             m.group(2), int(m.group(3))))
    rows.sort(key=lambda r: (UNIT_ORDER[r[0]], r[1],
                             int(re.sub(r'\D', '', r[2]) or 0)))

    tbl = ["| Unit | Paper |   Q | Topic                            | Marks |",
           "|------+-------+-----+----------------------------------+-------|"]
    for co, paper, q, topic, marks in rows:
        tbl.append(f"| {co:<4} | {paper:<5} | {q:>3} | {topic[:32]:<32} | {marks:>5} |")

    tot = {}
    for co, _, _, _, marks in rows:
        tot[co] = tot.get(co, 0) + marks
    summary = ["", "| Unit       | Marks |", "|------------+-------|"]
    summary += [f"| {k:<10} | {v:>5} |" for k, v in
                sorted(tot.items(), key=lambda x: UNIT_ORDER[x[0]])]
    summary += [f"| *total*    | {sum(tot.values()):>5} |", ""]
    return '\n'.join(tbl) + '\n' + '\n'.join(summary), rows


HEAD = ("** Coverage map\n\n"
        "Unit is the course outcome the paper tags the question with. CNE2\n"
        "prints no CO tags, so its units are inferred from the topic.\n\n")

TAIL = """
The three full papers are the honest guide, and each is 100 marks split
like this.

| Paper | CO1 | CO2 | CO3 | CO4 | CO5 |
|-------+-----+-----+-----+-----+-----|
| CNE1  |  20 |  20 |  15 |  25 |  20 |
| CNE2  |  25 |  22 |  13 |  13 |  27 |
| CNE5  |  20 |  15 |  20 |  25 |  20 |
|-------+-----+-----+-----+-----+-----|
| mean  |  22 |  19 |  16 |  21 |  22 |

So the real exam is roughly even across the five units. CO4 and CO5
together carry about 43 marks of the 100. Those are the two units your
earlier notes never reached.

"""


def main():
    text = PATH.read_text().split('\n')
    text = fix_refs(renumber_cne3(text))

    # rebuild the coverage block in place
    start = next(i for i, l in enumerate(text) if l.startswith('** Coverage map'))
    end = next(i for i, l in enumerate(text) if l.startswith('** Repeated questions'))
    table, rows = build_table(text)
    text = text[:start] + (HEAD + table + TAIL).split('\n') + text[end:]

    PATH.write_text('\n'.join(text))
    print(f'{len(rows)} questions, {sum(r[4] for r in rows)} marks')


if __name__ == '__main__':
    main()
