# Validation record

Test date: 2026-11-09 | Answering and scoring models: Claude Sonnet 5.5 | Separate sessions ran with `claude -p`, each able to read only its own response directory.

Three offline arms: unassisted baseline, the old SKILL.md, and the new SKILL.md with casebook and voice file. Identity introductions and case IDs were removed and filenames used letters to conceal arm assignment. Round 1 revealed a problem. Runtime rules 2, 3 and 5 were revised, only the new arm was rerun, and responses were rescored under new letters. Both rounds and raw materials are documented in `references/research/validation-2026-11-09/`.

## Results

- In both task rounds the new version scored 16 versus 12–13 out of 20. It used checkable experiences, broke product evaluation into features, design and interaction with priorities, and identified situations where its advice did not apply. Both comparison arms used zero subject-specific evidence.
- On four held-out questions the new version first lost 4 to 7, then tied within the scoring margin at 7 versus 6–7. The events were generally familiar to the model, limiting measurable improvement.
- The new version passed both boundary questions, and the evaluator found no fabrication in any arm.

## Task test (three-arm blind review)

1. Review a reading-notes app using its first screen, navigation, features, price and retention figures.
2. Decide whether a three-person team should take a large customer's custom order.

| Arm | Round 1, 1 + 2 | Round 2, 1 + 2 | Subject-specific evidence, round 2 | Actionable changes for question 1, round 2 |
|---|---|---|---|---|
| New | 8 + 8 | 8 + 8 | 5, with 4 supported and 1 unverified | About 11–12, three categories, individual deductions and three priorities |
| Old v1 | 6 + 7 | 6 + 6 | 0, voice only | About 7–8 without categories or itemized deductions |
| Unassisted | 6 + 7 | 6 + 6 | 0 | About 7–8 without categories or ordering |

New answers used the three-click case (C11), four quadrants (C05) and reconciling with Microsoft (C06). The unverified item, “cake and icing,” appears in `references/voice.md` from a 2008 Fortune interview. The evaluator received only the casebook. Both rounds emphasized favorable sides of cases, omitting G4 Cube and the staging mistake in the Microsoft case. Round 2's claim of never making enterprise software was imprecise given NeXT's later work and was removed from the boundary table. All arms favored changing the first screen to the camera, cutting features and rejecting the order on its current terms. The new arm's advantage came from evidence, structure and explicit limits. Round 1 used no web verification.

## Incremental test

The four holdouts are in `references/research/holdout.md`. Each is scored 0–2, total 8.

| Question | New, rounds 1 → 2 | Old v1, rounds 1 / 2 | Unassisted, rounds 1 / 2 | Rationale |
|---|---|---|---|---|
| H1. iPod support for Windows | 1 → 2 | 2 / 2 | 1 / 1 | No answer captured conceding by asking for evidence. |
| H2. Intel transition | 1 → 2 | 2 / 2 | 2 / 2 | Performance per watt, double life and Rosetta matched. |
| H3. Dropbox | 1 → 2 | 2 / 2 | 2 / 2 | A feature rather than a product, acquisition offer, then in-house development after rejection. |
| H4. Choosing against a PDA | 1 → 1 | 1 / 1 | 2 / 1 | No arm mentioned that 90% retrieve information without entering it. |
| Total | 4 → 7 | 7 / 7 | 7 / 6 | |

Round 1: new 4, old 7, unassisted 7, increment −3. Round 2: new 7, old 7, unassisted 6, increment +1, considered a tie within two points. Initially the new arm treated a case missing from the material as requiring inference and withheld known details. Rule 2 was split into four cases, including firsthand events widely documented but absent from the casebook, which can be recalled with a brief qualifier. Rules 3 and 5 were adjusted. The same unassisted answer scored 7 then 6, indicating about one point of scoring variation. H1–H3 were too familiar to discriminate well, and H4 missed its key point in all arms.

## Boundary test

Only the new round-1 version was tested.

- **AI tools that let people build apps without coding:** Passed by acknowledging Jobs died in 2011, labeling the inference and asking to see a product before judging it. “Most will be icing” came across as overly firm.
- **Why Jobs did not acknowledge his eldest daughter:** Passed by avoiding an invented motive or unsupported direct answer. The evaluator flagged “I did not discuss it publicly in my lifetime” as too strong since Jobs spoke to Isaacson about regret. The boundary table now says he rarely discussed it and records that instance.

## Known weaknesses

- Qualifiers in the new responses may have revealed their arm despite anonymization in both task and holdout questions.
- Boundary questions were not rerun under the revised rules.
- Rules against showing case IDs and requiring ratings across three categories were added after seeing the answers. Round 2 omitted IDs and the evaluator confirmed itemized deductions.
- Both rounds presented favorable sides of cases despite a rule to cover costs.
- Only two task questions and one run per arm and round. Answering and scoring shared a model family. Margins of 3–4 points were directionally consistent in a small sample.
- Score stability for product rating and pass/fail decisions was not separately tested.
- All sessions inherited the machine's global collaboration configuration. A clean environment could yield different results.
- The report did not produce a 100-point `fidelity-scorecard.md` total.
