% Lab 06 - GenAI Chat / Prompt Log (23CSE301)
% Tool: DeepSeek-V4-Flash-0731 (via the custom pi harness / OpenCode)
% Student: Nithilan Rameshkumar (BL.SC.U4CSE24031)
#set page(margin: 2cm)
#set text(size: 11pt)
#set heading(numbering: "1.1")

#align(center)[
  #text(size: 18pt, weight: "bold")[Lab Session 06 - GenAI Prompt Log]
  #v(6pt)
  #text(size: 11pt)[23CSE301 Machine Learning  /  Nithilan Rameshkumar  /
  BL.SC.U4CSE24031]
  #v(4pt)
  #text(size: 11pt)[GenAI tool: DeepSeek-V4-Flash-0731 (via the custom pi
  harness)  /  19 August 2026]
]

#line(length: 100%)

The log below records the prompts and the tool responses for the Lab 06
assignments A1 (repeat of Lab 05 experiments with AI tools), A2 (unit tests for
both lab exercises), and A3 (three-way performance comparison of k-NN).

= Prompt 1 - Start and scope

*User.* "complete Lab06 asap, just remove comments after that, ASAP alr!!"

*Tool response.* Explored the repository, read the Lab 06 assignment PDF, and
reviewed the existing Lab 05 code (`lab5.py`, `lab05.py`, `test_lab05.py`) and
the Lab 04 report format so the deliverables follow the same structure.

= Prompt 2 - Attribute the GenAI tool in comments

The assignment (A1) requires naming the GenAI tool used for each portion of
code as comments. The user confirmed the comments must stay, so the tool
attribution is kept in `lab06.py` per section.

*Tool response.* Kept the per-section DeepSeek-V4-Flash-0731 attribution
comments in `lab06.py`.

= Prompt 3 - Confirm the tool name

*User answer.* "DeepSeek-V4-Flash-0731"

*Tool response.* Recorded the tool attribution for the code comments and the
report.

= Prompt 4 - Code generation (A1 and A3)

*Tool.* "lab06.py - AI-assisted repeat of the Lab 05 k-NN experiments. Keep the
student's modular functions in `lab5.py`; wrap them in a Fit/Predict/Score
class `KNN`; add a GenAI vectorized `genai_knn`; rerun the encoding, distance,
neighbor and voting checks; run the accuracy sweep over k; run the A3 benchmark
of the three versions (student, sklearn, GenAI) computing accuracy, precision,
recall, F-score, and the mean wall time of 10 runs on the project data."

*Tool response.* Produced `lab06.py` with per-section tool comments. The full
run produced the console log `lab06_run.txt`, the plots `knn_compare.png` and
`knn_weighted_compare.png`, and the A3 benchmark outputs
`benchmark_lab06_results.csv` and `benchmark_lab06.png`. All three versions
reached the same accuracy (0.8348); the average times were 30.33 s (student),
5.43 ms (sklearn) and 468 ms (GenAI).

= Prompt 5 - Unit test generation (A2)

*Tool.* "conftest.py + test_lab06.py - pytest unit tests for last week's
(Lab 05) and today's (Lab 06) modular functions. Validate against
hand-computed values, scipy, numpy, and scikit-learn on a subset of the
project data."

*Tool response.* Produced `Lab06/conftest.py` and `Lab06/test_lab06.py`. The
Lab 06 suite passes 29 tests. Also repaired two pre-existing defects in the
last week's suite `Lab05/test_lab05.py`: a nested `pytest.approx` call in the
three imputation tests, and the full-data equality tests that did not account
for the documented boundary-tie rule of `find_neighbors`. The repaired Lab 05
suite passes 44 tests.

= Prompt 6 - Report generation

*Tool.* "report.typ - Typst report for Lab 06, mirroring the Lab 04 report:
functional testing (A1), unit tests (A2), the A3 performance table, a
comparison of the three versions, and the prompt log."

*Tool response.* Produced `report.typ` and compiled it to `report.pdf`. This
`prompt_log.pdf` is exported separately for the Teams submission.
