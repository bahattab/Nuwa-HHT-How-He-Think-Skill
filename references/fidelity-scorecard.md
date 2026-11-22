# Fidelity scorecard

This report evaluates whether a perspective skill stays faithful to the subject and acknowledges uncertainty. The original guide cites [SkillLens](https://arxiv.org/abs/2605.23899) for a reported self-evaluation accuracy of 46.4%. Use independent answering and scoring agents. Position scores require evidence independent of the skill, such as held-out material or primary sources found by the evaluator.

| Dimension | Points | Scoring |
|---|---:|---|
| Position consistency | 30 | Three known-position questions. Award 10 for correct direction and details, 6 for correct direction with inaccurate details, and 0 for a different stance. Use `references/research/holdout.md` or independently located primary evidence. Mark unverifiable questions and replace them. |
| Recognizable style | 20 | Blind-read the answers. Assess syntax, vocabulary and analogies for recognizable features of the subject's expression. |
| Honesty at the boundary | 20 | Ask one out-of-scope question. Award full points for labeling inference and preserving uncertainty, and 0 for presenting an inference as the subject's own position. |
| Source transparency | 15 | Check for a source section, more than 50% primary sources, attribution for key quotations, and a source for each case card. |
| Structural completeness | 15 | Run `scripts/quality_check.py`. Award 15 for all required checks, deducting 3 for each failure. Legacy skills lacking moves and casebooks need 3–7 mental models, at least 3 limitations, at least 2 tensions, and role instructions that prevent drift. |

## Incremental value

Report separately from the total. Have an agent using the same model answer the same position questions without reading any files. Score both runs against independent evidence. Subtract the baseline score from the with-skill score and record both next to the total in `FIDELITY.md`. See section 1 of `validation-playbook.md`. For famous subjects, a high baseline can leave little room for improvement. Inspect whether the task test uses actual cases. Revise a skill that scores below baseline.

| Grade | Score | Interpretation |
|---|---:|---|
| A | 85 or more | Suitable as a thinking adviser |
| B | 70–84 | Passes with documented weaknesses |
| C | 55–69 | Use carefully and read the limitations |
| D | Below 55 | Revise before use |

## Procedure

1. Prepare three known-position questions, one out-of-scope question, and one style sample. Prefer holdouts. For legacy skills without them, the evaluator independently obtains primary evidence before writing the questions.
2. The answering agent reads only the runtime skill, casebook, voice file, and other linked runtime resources. Exclude `references/research/` and web access. Use a separate baseline agent with the same model and no source files for the incremental test.
3. Give the independent evaluator the answers, rubric, and holdout or independently found primary evidence. Cite the evidence for each position judgment. Read the skill files only to assess source transparency and structure.
4. Record the total and grade, date, answering and scoring models, score per dimension, incremental scores, questions, answer summaries, reasons, evidence and its independence, and unverifiable items in `FIDELITY.md`.

Step 5 of the skill workflow is internal validation. This scorecard is the reproducible external report. Community submissions require grade B or better. See [Community](../COMMUNITY.md) and [Contributing](../CONTRIBUTING.md).

Keep the tested dimension hidden from the answering agent. Keep the scorer out of the answering process and rely on independent public evidence. Avoid existing sample dialogues. For important conclusions, use two independent scorers and request human review if their totals differ by more than 10.

[Arabic](fidelity-scorecard_AR.md) · [Chinese source](fidelity-scorecard_ZH.md)
