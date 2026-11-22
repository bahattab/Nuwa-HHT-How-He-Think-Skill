# Special cases

Read the applicable section, then return to the workflow in [SKILL.md](../SKILL.md). [Arabic](special-cases_AR.md) · [Chinese source](special-cases_ZH.md)

## 1. Topic skills

For a subject such as value investing, product restraint, or antifragile decision-making, adapt the workflow as follows.

| Step | Person skill | Topic skill |
|---|---|---|
| Scope | Identify the person and focus | Define the topic's boundaries and audience. Does value investing mean the Graham tradition or all schools? |
| Directory | `[person]-perspective/` | `[topic]-framework/`, with the same structure |
| Baseline | Prior knowledge of the person | Prevailing views and what you believe to be the field's consensus |
| Collection | Six tracks about one person | Identify 3–5 central figures or schools, with one or two tracks per figure or school |
| Extraction | Personal moves and models | Document shared positions and disagreements. Collect representative cases from each school. |
| Voice | Model the person's expression | Use neutral, professional language and provide a glossary |
| Tensions | Contradictions within one person's views | Fundamental disagreements between schools |
| Drafting | Standard structure | Omit the persona section and first person. See the variant at the end of `skill-template.md`. |
| Validation | Hold out the person's own statements | Hold out recognized cases and their documented outcomes |

## 2. Studying the user

1. Use user-supplied articles, recordings, decision memoranda, exported conversations, and self-descriptions.
2. Ask the user to write their own baseline account of how they believe they think.
3. Apply the six research tracks to the supplied materials without searching the web.
4. Watch for self-assessment bias. Record discrepancies between actions and self-description. If feasible, ask the user to obtain brief assessments from one or two acquaintances for the external-perspectives track.
5. Hold out actual past decisions. For validation, ask how the user would have chosen in those circumstances.

## 3. Living private figures

- Use only the materials the user supplies and skip web research.
- Before starting, recommend obtaining the person's consent and keeping the output private.
- Messages, email, and documents often provide evidence of real working practices. Focus on observable moves and decision heuristics.
- State in the limitations that the supplied materials reflect one person's perspective on the subject.

## 4. Poorly documented figures

With fewer than 10 usable sources, disclose the limitation during scoping. Reduce the mental models to 2–3 and label each as based on limited evidence. Describe the specific gaps in the limitations. Prioritize firsthand books, internal recordings, or correspondence the user can supply. Skip holdout and incremental testing and explicitly record that the incremental test was omitted.

## 5. Limited runtime

| Constraint | Response |
|---|---|
| No subagents or background jobs stall | Collect sequentially, save each completed track, and use section 6 of `validation-playbook.md` for testing |
| Context window around 200k | Split work into three sessions: scope and collection, holdout and extraction, then drafting and validation. Read saved notes at the start of each session and prefer the quick tier. |
| No network | Ask for user-provided materials and work from them locally |
| Limited budget | Use the quick tier and a lighter model for collection, with a stronger model for extraction and drafting |
