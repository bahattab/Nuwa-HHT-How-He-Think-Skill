# Fidelity Scorecard

> A release quality report for a perspective skill. It answers one question: **When this skill runs, does it actually sound like the subject, and is it honest?**
>
> Background: [SkillLens](https://arxiv.org/abs/2605.23899) reports that LLMs assessed skill quality with just 46.4% accuracy when evaluating their own work, close to random. The scorecard therefore has two firm rules:
>
> 1. **The answering and scoring agents must be independent. An agent must never evaluate its own answers or use them to attest to their own accuracy.**
> 2. **Scoring evidence must be independent of the skill under test.** Agent independence does not guarantee evidence independence. If the scorer treats the skill's own statements as the subject's real positions, any misunderstanding introduced during research will be scored as correct. For position questions, use only sealed holdout materials and primary sources found independently.

## Five Dimensions (100 Points Total)

| # | Dimension | Points | What to test | How to test |
|---|---|---|---|---|
| 1 | Position consistency | 30 | Does the skill answer in line with the subject's publicly stated positions? | Use three known-position questions worth 10 points each. Award 10 when both direction and details are right, 6 when the direction is right but details drift, and 0 for a different stance. **Judge against the sealed holdout (`references/research/holdout.md`) or independently found primary sources, never the skill itself.** If reliable independent evidence is unavailable, mark the question as unverifiable and replace it. Do not assume the answer is right. |
| 2 | Recognizable style | 20 | Can a reader identify the subject from the expression alone, without seeing the name? | Have the scorer read the answers blind. Check whether syntax, word choice, and analogies show the subject's distinctive style or sound like generic AI output. |
| 3 | Honesty at the boundary | 20 | When the subject has not addressed a question publicly, does the skill label its inference or confidently make something up? | Ask one out-of-scope question. Award full points if the answer explicitly says “This is an inference based on the framework” and retains uncertainty. Award 0 if it presents an inferred answer as the subject's own position. |
| 4 | Source transparency | 15 | Can the supporting research be traced to its sources? | Inspect the skill files for a research sources section, more than 50% primary sources, attribution for key quotations, and a source for every casebook card. |
| 5 | Structural completeness | 15 | Does the skill have all the components it needs to prevent drift and operate honestly? | Run `scripts/quality_check.py`. Award 15 if all required checks pass, and deduct 3 for each ✗. For legacy skills lacking moves and a casebook, apply the older standard: 3–7 mental models, at least 3 honesty boundaries, at least 2 pairs of internal tensions, and role-play rules with anti-drift constraints. |

## Incremental Value (Reported Separately, Excluded from the Total)

The total answers whether the skill is faithful and honest. Incremental value answers a different question: **What does the skill add compared with asking the model to portray the subject directly without it?**

Have an agent who reads no files answer the same position questions. Score its answers against the same independent evidence. The incremental value is the with-skill score minus the baseline score. See section 1 of [the validation playbook](validation-playbook.md). Record the incremental value on the line immediately below the total in `FIDELITY.md`.

For famous subjects, the baseline may already be high, so a small gain does not mean the skill is useless. Check instead whether the task test draws on real cases. A negative gain calls for reworking the skill because it has led the model astray.

## Grades

| Grade | Score | Meaning |
|---|---|---|
| A | ≥85 | Excellent at release and safe to use as a thinking adviser |
| B | 70–84 | Passes with documented weaknesses in individual dimensions |
| C | 55–69 | Usable with caution. Read the honesty boundaries first. |
| D | <55 | Not recommended for use until reworked |

## Procedure

1. **Prepare questions.** Use three known-position questions, one out-of-scope question, and one question to sample style. Prefer the sealed holdout. For legacy skills without one, the scoring agent independently retrieves primary sources and establishes the expected answers before drafting questions.
2. **Answering agent.** Read only the skill's `SKILL.md` and its linked runtime files, such as the casebook and voice file. Do not read `references/research/`, which contains the holdout. Activate the persona according to the skill, answer the questions, and do not access the web. For the incremental test, start a separate baseline agent using the same model, with no files.
3. **Scoring agent.** Use a separate agent that receives the answers, this rubric, and the sealed holdout or primary sources it located independently. Assess position consistency only against this evidence and cite the source used for each question. Open the skill files only for source transparency and structural completeness.
4. **Report.** Create `FIDELITY.md` in the skill directory. Include the total and grade, dimension scores, incremental scores, the reason for each judgment and **the source that supports it**, whether the evidence is independent of the skill creation process, any unverifiable questions, the test date, and the models used to answer and score.

## Results Format (FIDELITY.md Template)

```markdown
# Fidelity Scorecard

**Total: NN/100 · Grade X** | Test date: YYYY-MM-DD | Answering/scoring: two independent agents

Incremental value: with skill NN / baseline NN / +NN (position questions checked against the sealed holdout)

| Dimension | Score | Rationale summary |
|---|---|---|
| Position consistency | NN/30 | ... |
| Recognizable style | NN/20 | ... |
| Honesty at the boundary | NN/20 | ... |
| Source transparency | NN/15 | ... |
| Structural completeness | NN/15 | ... |

## Test Record
[For each question: prompt, answer summary, verified position and source, and judgment]
```

## Relationship to the Nuwa Workflow

- Validation in step 5 of Nuwa (see [the validation playbook](validation-playbook.md)) is **internal quality control**, a checkpoint during creation.
- The scorecard is the **external report**, an inspection performed after creation that anyone can reproduce.
- Community-contributed perspective skills must score B or higher for inclusion in the [community index](../COMMUNITY.md). See the [contribution guide](../CONTRIBUTING.md).

## Anti-Gaming Rules

- Keep the tested dimension hidden from the answering agent.
- Keep the scoring agent out of answering and require public evidence independent of the skill.
- Avoid questions that the skill already includes in example dialogues, so the answering agent cannot simply repeat a supplied answer.
- For important conclusions, use two independent scorers. If their totals differ by more than 10 points, request human review.

[Arabic](fidelity-scorecard_AR.md)
