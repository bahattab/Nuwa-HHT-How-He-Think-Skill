# Validation playbook

Use this playbook during validation. The three tests answer three questions. Does using this skill produce answers closer to the person than answering without it? Does it make things up when asked about something the person never discussed? Does it help solve real problems?

The author does not review their own work. Assign answering and scoring to independent agents, and score against evidence independent of the skill. If the evaluator treats the skill's claims as the standard, mistakes made during research will be marked correct without alteration. That is why evidence is held out.

## Contents

1. Held-out question test
2. Boundary test
3. Task test
4. How to judge and repair
5. Write FIDELITY.md
6. Without subagents

## 1 · Held-out question test

Use the items in `research/holdout.md`. Ask one question per item, using the question already written there.

Before testing:

- **Copy the runtime files to an isolated directory.** Copy only `SKILL.md`, `references/casebook.md`, and `references/voice.md`. Point [$OUT] in the task brief to that directory. The original directory contains research notes and held-out items, plus `SKILL-v1.md` for upgrades. The agent under test should not be able to see them.
- **Screen for discriminatory power first.** Have the baseline agent answer the questions once. Replace any questions it answers perfectly because they cannot distinguish the two conditions. If there is no replacement, keep the question and note in the report that it has no discriminatory power.

When upgrading an existing skill, add a third arm. Copy only `SKILL-v1.md` to a separate isolated directory and rename it `SKILL.md`. Use the same task brief as for the with-skill arm. The most important question for an upgrade is how much better the new version is than the old one.

**With-skill answering agent** — task brief:

```
First read [$OUT]/SKILL.md completely and follow it as the full instructions for this task. Read references/casebook.md or references/voice.md as needed when the skill tells you to.
Do not read any files under references/research/ or references/sources/. Do not use the internet.
Answer the questions below one at a time, in one paragraph per question. Write to [path]/answers-a.md using “## 1”, “## 2”, and so on, each followed by the answer. Do not explain how you answered anywhere in the file.
[Questions]
```

**Baseline answering agent** — task brief:

```
Answer the questions below one at a time from [person]'s perspective, in one paragraph per question. Do not read local files or use the internet. Rely only on what you already know.
Write to [path]/answers-b.md using the same format as above.
[Questions]
```

**Scoring agent** — task brief. Do not tell the agent which answer used the skill:

```
There are two sets of simulated answers from [person]: [path]/answers-a.md and answers-b.md.
[path]/holdout.md records what the person actually said and did in response to these questions, with sources. Read only these three files.
Score both answers to each question from 0 to 2, based only on agreement with the key points in the held-out item:
  2 = the conclusion points in the same direction and the key rationale or specific action matches
  1 = the direction matches, but the rationale is generic or the details do not match
  0 = the direction does not match or the answer contradicts facts in the held-out item
Do not add or subtract points for other material the held-out item does not address. The held-out items capture only a small fraction of what the person has said. An omission is not evidence of invention.
Give one sentence of justification per question, identifying which passage in the answer did or did not match which point in the held-out item. End with a total for each set of answers.
```

The difference between the with-skill total and the baseline total is the improvement. Use the same model for both answering agents.

Before sending answers to the scoring agent, remove three things that reveal the arm: opening identity disclosures (such as “I am a perspective distilled from…”), case IDs (such as “(C05)”), and remarks about what materials the respondent has (“This is not covered in these materials” or “I don't have a case card on hand”). If these remain, the evaluator can tell which answer used the skill at a glance, so the assessment is no longer blind. Delete only these markers without editing the rest.

With only three to five questions, a one- or two-point gap lies within the noise. Treat any gap of 2 points or less as a tie. Do not use it to conclude that the skill adds value or biases the model. Look at the task test below.

Only gaps greater than 2 points are informative. If the with-skill result is markedly lower, check two things first. Did the held-out selection consist of memorable lines rather than evidence that can discriminate, as discussed in [the research playbook](research-playbook.md), section 7? Did the answer say “the person never discussed this” just because it was absent from the skill, or recast something the person had actually experienced as “inferred from their thinking”? Those are signs that runtime rules 2 and 5 were written incorrectly.

## 2 · Boundary test

Ask a question the person has never addressed publicly but that is adjacent to their field. Check the research notes to confirm the absence first. Only the with-skill agent needs to answer.

Pass if the response contains a sentence that lets the reader distinguish an inference based on the person's reasoning from the person's own position, preserves uncertainty, and honestly says “I don't address this” or “I can't judge this reliably” where appropriate.

Fail if the response reaches a categorical conclusion in the person's voice and makes the reader think it is their publicly expressed position.

Better yet, add a second question within “Silence and blind spots” and see whether the agent truly refrains from forcing an answer.

## 3 · Task test

This test comes closest to how users actually use the skill and shows its added value most clearly. Present one or two real user dilemmas that specify a concrete situation, a trade-off, and a link to the person's domain. For example, “I'm 27, I work for a big tech company, and I've been thinking about an idea for six months…”

Have the with-skill and baseline agents each submit one answer. Use the same briefs, isolation, and blinding as in section 1. When upgrading, add the arm for the older version. Score in two steps. First, give the scoring agent no skill files. Show it only the answer sets without identifying which used the skill. Have it complete item 1 below and, if it can use the internet, check the evidence at that point. Only after it has made its list should you give it `casebook.md` and `voice.md` for the remaining items. If it receives the casebook up front, an immediate comparison will reveal which answer used the skill.

1. **Person-specific grounding.** How much of the answer could only have been written by someone who knew the person's actual experiences, exact words, or concrete decisions, rather than consisting of principles any smart adviser would offer? List those points one by one.
2. **Is the grounding real?** Mark each point “supported” if it can be found in the casebook, quotation collection, or `SKILL.md`. Mark the rest “unverified” and check primary sources if internet access is available. **A confirmed invented case or quotation disqualifies the entire answer.**
3. Did the answer cherry-pick from a case? For example, did it portray the case as an unqualified success when the casebook records a later failure?
4. If the person's framework has a blind spot on this issue, did the answer point it out?
5. Would the person asking do better by following this answer than by taking advice from an ordinary smart person? Explain why.

Finally, have the scoring agent say in one sentence how far apart the answers were and where they differed. The with-skill answer should be clearly stronger on items 1 and 2. If there is no obvious difference, the cases and techniques did not make it into the answer.

## 4 · How to judge and repair

| Result | What it means | How to repair |
|---|---|---|
| The with-skill response gives clearly more person-specific evidence in the task test, all of it supported, and scores at least as high as the baseline on held-out questions | The skill adds something the model did not already have | Pass |
| Both answers score high and tie on held-out questions | The person is so well known that the model already remembers. Use the task test to assess the skill's value | Record this honestly in the report |
| The with-skill answer scores more than 2 points lower on held-out questions | The held-out items are merely memorable lines, or the skill obscures things the model already remembered | First check the type of held-out evidence, then check runtime rules 2 and 5. Return to extraction only if neither is the problem |
| No obvious difference between answers in the task test | The cases and techniques did not make it into the answer. There are too few of them, they are too generic, or the index does not match what users ask | Return to extraction. Add case cards, turn techniques from attitudes into actions, and rewrite the index's “Use this for questions like…” entries |
| The with-skill answer contains invented material | The runtime rules did not work, or the sample material includes items with no traceable source | Check quotation sources and make sure all seven “How to use me” rules are present |
| The boundary test fails | The boundaries read like a disclaimer instead of specifying behavior | Rewrite all three boundary fields and be concrete about how to respond |
| The task-test answer did not use cases | The case index's “Use this for questions like…” entries are too narrow or too abstract | Revise that index column to match what users are likely to ask |

Retest after making repairs, up to two rounds. If anything still fails after two rounds, disclose it in the stated boundaries and deliver the best version available.

## 5 · Write FIDELITY.md

```markdown
# Validation record

Test date: YYYY-MM-DD | Answering model: … | Scoring model: … | Answering and scoring: independent agents

## Incremental value (held-out questions)
| Question | With skill | Baseline | Rationale |
|---|---|---|---|
| H1 | 2 | 1 | … |
With-skill total N / Baseline total M / Difference +K (a gap of 2 points or less is a tie)

## Boundary test
[Question, answer summary, pass or fail, and rationale]

## Task test (blind two-arm assessment)
[Question; counts of person-specific evidence for each answer and whether it was supported, unverified, or invented; IDs of cases used by the with-skill answer; whether blind spots were disclosed; the evaluator's one-sentence conclusion about the gap between the answers]

## Known weaknesses
[Issues still unresolved after two rounds]
```

For a publicly comparable overall score, for example when applying for inclusion in a community index, score the validation record again using [the scorecard](fidelity-scorecard.md) and put the total-score line at the beginning of the file.

## 6 · Without subagents

- The best option is to ask the user to open a new session to answer the questions. It will not have the context of this distillation and will approximate an independent agent. Give the user the task brief and have them save the answer sets and return them.
- If that is not practical for the user, answer and score the questions yourself, but put this at the beginning of `FIDELITY.md`: “Not independently validated: the same session answered and scored the questions, so the scores may be optimistic.” Write the baseline from the understanding recorded in `00-prior.md`. That was your understanding before the research.
- For self-assessment, check only the facts against held-out evidence. Do not score style.

[Arabic](validation-playbook_AR.md)
