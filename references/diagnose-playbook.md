# Diagnosis playbook: When the user has a problem but no person in mind

The user brings a need or a question but does not know whose thinking to distill. Work backward from that need to identify the most suitable subject.
Use the table of needs and the candidate format below as starting points. If you have a more precise understanding of the user's circumstances, recommend accordingly.

## 1 · Identify the need

Use one or two follow-up questions to identify the user's primary need:

| Need | Typical wording | Relevant thinking frameworks |
|---|---|---|
| Decisions and judgment | “How can I make better decisions?”, “I always choose wrong”, “Analysis paralysis” | Multiple mental models, inversion, probabilistic thinking |
| Writing and expression | “I want to explain something complex clearly”, “Nobody reads my articles”, “My writing is boring” | Feynman-style simplification, storytelling, analogy |
| Entrepreneurship and business | “I want to build products independently”, “I can't work out the business model”, “I can't find product–market fit” | First principles, leverage, restraint in product design |
| Teaching and communication | “Nobody listens to my lectures”, “Students don't understand”, “I can't convey knowledge efficiently” | Move from the known to the unknown, teach through metaphor, teach the minimum necessary |
| Critical thinking | “I keep getting fooled”, “I want to spot unreliable claims”, “I can't see what really matters” | Falsification, evolutionary perspectives, recognizing cognitive biases |
| Content creation | “My videos get no traffic”, “I don't know what to film”, “My content doesn't stand out” | Attention design, iterative testing, audience psychology |
| Life strategy | “I don't know which career direction to take”, “I never have enough time”, “I feel anxious” | Long-term thinking, choosing sources of leverage, compounding |
| Risk and uncertainty | “How do I handle black swans?”, “I always lose money investing”, “I'm too cautious or too reckless” | Antifragility, convex strategies, managing tail risk |
| Design and products | “The user experience is poor”, “The product doesn't stand out”, “I don't know what to cut” | Minimalism, users' mental models, constraints as a source of creativity |
| Humor and expressiveness | “I'm not interesting when I speak”, “I want to make my content more fun”, “It's too serious” | Absurd contrasts, violated expectations, self-deprecating authority |

Follow-up principles:
- Ask at most two rounds. Do not turn the conversation into a survey.
- If the user has already been clear enough, recommend directly.
- Use follow-ups to distinguish similar needs, such as business decisions versus life decisions.

Example of the intended pace:

```
User: I always feel that I take too long to decide. I think it over and over but still make the wrong choice.

Nuwa: In which situations does this happen most? Business or investment decisions, for example, or choices about your career or life direction?

User: Mostly business, like deciding whether to build a product or accept a partnership.

Nuwa: Understood. Your main need is to make sound business judgments quickly with incomplete information.
I recommend three candidates:
[Show the recommended candidates…]
```

Keep this pace: identify the context with one round of follow-up, confirm the need, then recommend directly. Do not still be asking questions in a third round.

## 2 · Recommend candidates

Recommend two or three candidates based on the need. Candidates may be people or topics.

**Decide first whether to recommend a person skill or a topic skill**
- A specific way of thinking calls for a person skill that distills one person's thinking frameworks.
- A domain methodology calls for a topic skill that combines multiple perspectives. See [special cases](special-cases.md).
- When uncertain, include both types and let the user choose.

**Source A: Existing local skills**
Scan the host's skill directories for all `*-perspective/` folders. Read each `SKILL.md` description and compare it with the user's need. Matching skills can be used immediately without distilling them again. If the scan returns nothing because no perspective skills are installed, skip this step and recommend only from Source B.

**Source B: New candidates for distillation**
Match the most relevant people or topics to the “Relevant thinking frameworks” column. Explain which specific framework from the candidate addresses the user's concrete problem.

Use this format for each candidate:

```
### Candidate 1: [Person or topic]  ⚡ Existing skill / 🆕 Requires distillation

**Core lens**: [A one-sentence description of this person's distinctive way of seeing the world]
**Why it fits**: [Directly connect the perspective to the user's need and explain the match]
**Limitations**: [Name the blind spots and the problems this perspective cannot help with]
```

Recommendation principles:
- Offer no more than three candidates. Choice overload is worse than having no choice.
- Present existing skills first. They are ready to use at no additional cost.
- Make the candidates distinct. Do not recommend three similar people.
- State limitations explicitly. No thinking framework works for everything.
- Name the candidate's specific mental model that fits the need. General praise is not enough.

## 3 · After the user chooses

- If the user picks an existing skill, activate it directly. The task is complete.
- If the user picks a new candidate, return to the distillation workflow in [SKILL.md](../SKILL.md) and begin at “0 · Define the topic.”
- If none are satisfactory, return to step 1 to investigate further or let the user propose another candidate.

[Arabic](diagnose-playbook_AR.md)
