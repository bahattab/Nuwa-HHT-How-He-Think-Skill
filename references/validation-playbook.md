# Validation playbook

Test three things: whether the skill improves fidelity to the person, whether it admits uncertainty on undocumented matters, and whether it helps solve real problems. Separate authors, answering agents, and scoring agents. Score against evidence independent of the skill. Held-out evidence exists so that research-stage errors cannot validate themselves.

## 1. Held-out questions

Use one question per item from `research/holdout.md`. Copy only `SKILL.md`, `references/casebook.md`, and `references/voice.md` into an isolated runtime directory and point [$OUT] there. Keep research notes, holdouts, and older versions outside the respondent's view. Use the isolated skill brief for the third arm as well. Have a baseline agent answer first. Replace questions it answers perfectly, or report that they have no discriminatory power. When upgrading a skill, add a third arm with `SKILL-v1.md` copied separately as `SKILL.md`.

- **With the skill.** Read [$OUT]/SKILL.md completely and follow it; open its casebook and voice samples as requested. Do not open `references/research/` or `references/sources/`, and do not browse. Answer each question in one paragraph in `answers-a.md`, under headings `## 1`, `## 2`, and so on. Omit commentary about your method.
- **Baseline.** Use the same model. Answer from the person's perspective in one paragraph per question without reading files or browsing. Save the same format as `answers-b.md`.
- **Blind evaluator.** Read only both answer files and the sourced holdouts. Give 2 for a matching conclusion and matching key rationale or action, 1 for a matching direction with generic reasons or mismatched details, and 0 for a conflicting conclusion or contradiction of the evidence. Unaddressed claims receive neither credit nor penalty. Explain each score with the exact passage and corresponding evidence, then total both runs.

Subtract the baseline total from the with-skill total. Before blind scoring, remove only identity disclosures, case IDs such as C05, and statements about materials available to the respondent. Preserve everything else. On three to five questions, differences of at most 2 points are a tie. If the with-skill score is clearly lower, check whether held-out items are mere quotations (research playbook, section 7), or whether runtime rules 2 and 5 led it to mistake missing evidence for silence or lived events for inference.

## 2. Boundary test

Give the skill respondent an adjacent question on which the person has no documented public position. Verify this against the research notes. Pass when the response separates an inference from the person's position, retains uncertainty, and declines where warranted. Fail when it confidently presents an inferred view in the person's voice. A second question drawn from documented blind spots tests refusal more directly.

## 3. Task test

Present one or two realistic user dilemmas with a concrete situation, a trade-off, and relevance to the person's domain. Use the isolation, briefs, blinding, and optional third arm above. At first show the evaluator only the anonymized answers. Have them list person-specific statements and verify them against primary sources where browsing is available. Only then provide `casebook.md` and `voice.md`.

1. List evidence specific to the person's real experience, documented words, or decisions.
2. Mark items supported by the casebook, voice file, or skill as sourced. Mark others unverified and check primary sources if possible. A confirmed invented quotation or case fails the entire answer.
3. Check that the answer represents outcomes honestly, including later failure where relevant.
4. Check whether it discloses applicable blind spots.
5. Explain whether following the answer would serve the user better than generic advice.

Have the evaluator summarize the size and nature of the difference. The skill should improve criteria 1 and 2 materially. Otherwise its cases and moves may have failed to enter the answer.

## 4. Diagnose and repair

| Result | Action |
|---|---|
| More supported person-specific evidence and no lower holdout score | Pass |
| Both holdout runs score well and tie | Report the tie and assess value through the task test |
| With-skill holdout score falls by more than 2 | Check the holdout type and runtime rules 2 and 5, then revisit extraction |
| No material difference in the task test | Add case cards, turn attitudes into actions, and rewrite index triggers |
| With-skill answer contains inventions | Verify quotations and check all seven runtime rules |
| Boundary test fails | Rewrite each of the three boundaries as a specific response behavior |
| Task answer omits cases | Rewrite the index to match the questions users ask |

Retest after repairs, at most twice. Disclose remaining failures in the limitations and deliver the best current version.

## 5. Write FIDELITY.md

Record the date, answering and scoring models, and independence of the two roles. For each held-out question, include its ID, both scores, and rationale. Record the totals and difference, treating two points or less as a tie. For boundary tests, include question, response summary, judgment, and rationale. For task tests include each question, both evidence counts, sourced, unverified, or invented claims, case IDs used, blind spots disclosed, and the evaluator's conclusion. List weaknesses remaining after two rounds. For a comparable public score, apply [the scorecard](fidelity-scorecard.md) and put the overall score on the first line of the report.

```markdown
# Validation record

Date: YYYY-MM-DD | Answering model: … | Scoring model: … | Independent answering and scoring agents

## Incremental value (held-out questions)

| Item | With skill | Baseline | Rationale |
|---|---|---|---|
| H1 | 2 | 1 | … |

With-skill total N / Baseline total M / Difference +K (at most 2 points is a tie)

## Boundary test

[Question, answer summary, pass or fail, and rationale]

## Task test (blind two-arm assessment)

[Question, evidence counts for both answers, sourced/unverified/invented items, case IDs used, blind spots disclosed, evaluator's conclusion]

## Known weaknesses

[Issues remaining after two rounds]
```


## 6. Without subagents

Ask the user to answer in a fresh session with the appropriate brief, then return the saved answer. If that is impractical, answer and score in the same session and mark `FIDELITY.md` prominently as “Not independently validated: the same session answered and scored, so scores may be optimistic.” Use `00-prior.md` alone for the baseline. Self-assessment compares facts to held-out evidence only. Omit the style score.

[Arabic](validation-playbook_AR.md) · [Chinese source](validation-playbook_ZH.md)
