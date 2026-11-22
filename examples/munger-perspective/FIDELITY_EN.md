# Validation record

Test date: 2026-11-09 | Answering model: Claude Sonnet (`claude -p --model sonnet`, network disabled, Read only) | Scoring: Claude Sonnet (independent process, web verification permitted for task grading) | The two agents ran in separate fresh sessions.

The same eight questions were run in three isolated arms: upgraded skill (v2), pre-upgrade SKILL.md, and unassisted baseline. Identity openings were removed and answers shuffled under m1/m2/m3 (old/new/baseline). The questions, raw answers and evaluation are in `references/research/validation-20261109/`. No 100-point total was produced under `fidelity-scorecard.md`.

## Task test (three-arm blind review, 0–10 per question)

T1: Should a 32-year-old product manager at a large company take a pay cut to co-found an AI tools business? T2: How should a 12-person team split a 1 million bonus?

| Arm | T1 | T2 | Subject-specific evidence | Fabrication |
|---|---:|---:|---|---|
| New skill | 9 | 8 | T1 cited the partnership fund losing half its value (C02), Li Lu (C11), and missing Google. T2 used the law firm's peer-rated fee allocation (C03). The evaluator found support for all of them and independently verified Li Lu more precisely than the casebook. | None |
| Old skill | 5 | 4 | Used inversion and circle of competence as labels, with no concrete experience. T2 proposed setting rules without a vote and keeping amounts private, the opposite of Munger's law-firm practice. | None |
| Baseline | 5 | 4.5 | Used inversion only and imported Bezos's regret minimization into T1. | None |

The evaluator found the new skill approximately four points stronger, and characterized the others as generic good advice in Munger's voice. The new version attributed a lesson about avoiding forced sales to Munger without a direct quote in the casebook, omitted his own leverage during the partnership period and the criticism that Li Lu's annualized returns merely matched the index, and failed to give numeric allocations in T2.

For T1 the new skill flagged its lack of software and early platform expertise, survivorship bias in forced-sale advice coming from a rich person, and the gap between a spouse not objecting and being able to bear the risk. For T2 it flagged the distinction between partners and employees. The other arms raised none of these points.

## Incremental test (held-out questions, 0–2 each)

Compared with `research/holdout.md`.

| Question | New | Old | Baseline | Rationale |
|---|---:|---:|---:|---|
| H1. Coal stock | 1 | 0 | 0 | New answer got cheap steelmaking coal right, but named Warrior Met with an unverified label and called the stake small where the held-out evidence said it was large. Others denied any action. |
| H2. Apartments | 2 | 2 | 2 | All mentioned long-term fixed rates and putting in more money after buying. |
| H3. Japanese trading houses | 1 | 1 | 1 | All mentioned yen borrowing. None captured the rare no-brainer framing or the 0.5% versus 5% spread. |
| H4. Looking back at Berkshire | 0 | 0 | 0 | All mentioned missed opportunities. None mentioned using too little leverage. |

Totals: new 4, old 3, baseline 3 out of 8. A difference within two points is a tie under the manual, and does not show incremental value. H4 demonstrated that the model did not know the late view that Berkshire was too cautious, and the skill properly omitted the held-out evidence. H2 could be answered from common sense and discriminated poorly.

## Boundary test

- **B1. Is building a product alone with AI coding worthwhile?** New skill passed: disclosed lack of evidence and reasoned from the framework, then noted mistakes judging software and early platforms. Old skill failed: answered yes if downside is limited without marking inference.
- **B2. Why is Bitcoin technically unviable?** New skill passed with a minor issue: disclosed lack of technical research, separated stance from analysis and acknowledged the price had not followed its view, but did not explicitly label inference. Old skill failed by inventing a concession (“I was wrong for longer than they were”) and making technical assertions.

## Post-test changes (not retested)

1. The forced-sale lesson and evidence for mental model 3 now explicitly identify the lesson as inferred from actions and require mentioning Munger's own leverage.
2. Case-index entries C02 and C11 now flag Munger's leverage and the criticism that returns only matched the index.

## Known weaknesses

- Held-out questions showed no gain. Revealing the late events about coal and Berkshire in the casebook would compromise their independence.
- The two task questions used one answering model (Sonnet) and one run per arm, with no repeat measurements.
- The scorer received the casebook to check claims, so the blind was incomplete. Only Google and Li Lu were independently verified online.
- The old skill calls for web research before answering and was tested without it.
- C07, the Good Samaritan Hospital episode, had only Lowe's biography as a source and was not independently checked.
