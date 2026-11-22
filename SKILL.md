---
name: huashu-nuwa
description: |
  Research how a public figure thinks and turn documented mental models, decision heuristics, and communication patterns into a reusable perspective skill. Accepts a named figure or topic, a vague need for a thinking adviser, or a request to update an existing perspective.
  English triggers include "hht", "how does [person] think", "distill [person]", and "create a [person] perspective skill".
  عبارات التفعيل تشمل «كيف يُفكِّر [الشخص]؟»، و«حلِّل طريقة تفكير [الشخص]»، و«أنشئ مهارةً تستخلص منهج [الشخص] في التفكير».
metadata:
  author: "花叔"
  homepage: "https://github.com/alchaincyf"
  repository: "https://github.com/alchaincyf/nuwa-skill"
  version: "2.0.2"
---

## Working language / لغة العمل

Use the language explicitly requested by the user. Otherwise, follow the language of their request. Apply that choice to clarification questions, research summaries, and generated perspective skills. Preserve original titles, quotations, and URLs when needed for source traceability, and label any translated quotation.

استخدم اللغة التي يطلبها المستخدم صراحةً. وإن لم يُحدِّد لغةً، فاتّبع لغة طلبه في أسئلة الاستيضاح، وملخّصات البحث، والمهارات الناتجة. حافظ على عناوين المصادر واقتباساتها وروابطها عند الحاجة إلى تتبُّعها، وبيّن متى يكون الاقتباس مترجمًا.

[Arabic guide](SKILL_AR.md) · [Chinese source](SKILL_ZH.md)

# Nuwa · Research a person's way of thinking

Act as biographer, cognitive researcher, editor, and evaluator. Use documented decisions and verbatim passages to identify recurring ways of thinking. Capture observable actions, mental models, heuristics, speech patterns, tensions, and limitations. Focus on what corrects, deepens, or adds to baseline knowledge. An expert familiar with the subject should recognize the result and learn something from it.

## Routing and paths

A named person or topic goes directly to research. For a vague need, consult [diagnosis](references/diagnose-playbook.md), ask at most two rounds of questions, and suggest 2–3 distinct candidates. For a topic, self-study, private or obscure figure, or limited runtime, consult [special cases](references/special-cases.md). For updates, see below.

`$NUWA` is this skill's directory. `$OUT` is the generated skill directory within the host's skill discovery path. Use `.claude/skills/[person]-perspective/` for Claude Code, `.dsh/skills/…` for DeepSeek Harness, and the equivalent for other hosts. Keep output self-contained. Use the playbooks whenever blocked, operating with limited tools, or failing a gate.

## 0. Define the scope

Identify the subject, scope, intended use, and available primary material. Store user-provided books, transcripts, and blog exports in `$OUT/references/sources/`. Route an existing skill to updating or upgrading. Explain relative costs before research. Quick covers writings, conversations, and decisions at about five sources each and roughly one-third the standard cost. Standard covers six tracks. Deep adds full primary-source archives for publication-quality work. If the user simply names a person, default to standard, a general profile for decision support, and no local corpus.

## 1. Record the baseline

Before looking up sources, write `$OUT/references/research/00-prior.md` with five presumed core ideas or practices, three confident facts, three uncertain claims, and a sentence summarizing the public impression. Spend at most ten minutes. State plainly when prior knowledge is sparse.

## 2. Collect evidence and set aside validation cases

Follow the [research playbook](references/research-playbook.md). Cover writings, long conversations, short-form expression, outside criticism, major decisions, and timeline or recent activity. Use parallel research where available, otherwise work sequentially and save each completed track in `$OUT/references/research/` under its matching 01–06 file. For each finding record source and confidence and distinguish statements, actions, third-party accounts, and inference. Describe concrete actions in past tense with date, situation, conduct, and outcome. Preserve contradictions. End each file with evidence that overturns, deepens, or adds to the baseline.

Before extraction, reserve 3–5 primary sources in `research/holdout.md`, prioritizing decisions with real alternatives and complete reasoned answers. Record the source, question, and actual response or action. Exclude this material from the generated skill. If fewer than ten usable sources leave insufficient material, report that the incremental validation test was skipped.

Run `python3 $NUWA/scripts/merge_research.py $OUT`. Require each planned track to have evidence, a majority of sources to be primary, dedicated criticism, and at least eight additions, refinements, or corrections to the baseline. Seek deeper primary sources if the threshold fails. Show the user the summary, strongest changes, contradictions, gaps, and extraction direction at this one checkpoint. When the user has waived intermediate confirmation, include the summary in the final handoff.

## 3. Extract reasoning patterns

Follow the [extraction framework](references/extraction-framework.md).

- Extract 5–8 observable moves with their triggers and at least one source each.
- Require 3–7 mental models to appear across at least two domains, predict a stance on a new problem, and distinguish the subject from general expert judgment. State evidence and failure conditions. Downgrade partially validated models to heuristics.
- Write 5–10 situation–response heuristics with real examples.
- Write case cards with situation, conduct, verbatim rationale, outcome and hindsight, application by analogy, and source. Minimums are 6 quick, 12 standard, and 20 deep.
- Correct at least two common misreadings with primary evidence. Document syntax, diction, rhythm, humor, and confidence with sourced passages.
- Preserve at least two unresolved tensions. Distinguish documented expertise, plausible inference, and silence or failure. Report blind spots in the work, baseline bias, and new evidence that could overturn the result.

## 4. Build the deliverables

Use the [skill template](references/skill-template.md). Write a runtime `$OUT/SKILL.md` of no more than 350 lines with invocation, role, moves, mental models, heuristics, misreadings, voice, case index, tensions, limitations, and sources. Store the full case cards and quotation bank in `references/casebook.md` and `references/voice.md`. Adapt the structure to the subject while retaining those essentials. Run `python3 $NUWA/scripts/quality_check.py $OUT` and resolve failures.

## 5. Validate

Follow the [validation playbook](references/validation-playbook.md). Use independent answerers and a blind evaluator when available. Otherwise test sequentially and disclose the lack of independent validation.

1. Compare responses on one or two real user problems, one with the skill and one with baseline knowledge. Verify person-specific evidence and reject invented cases. Return to extraction if the skill adds little.
2. Apply the held-out questions and compare against the documented response. A difference within two points is a tie on a small set. Investigate substantially worse results.
3. Ask about an issue absent from the evidence. A passing response labels inference and acknowledges uncertainty. Absence from the corpus does not establish that the person never addressed a topic.

Revise at most twice. Disclose remaining weaknesses and record all outcomes, model names, and test date in `$OUT/FIDELITY.md`. Use the [scorecard](references/fidelity-scorecard.md) for externally comparable scores.

## Evidence and portability rules

Verify every quotation against its source. For Chinese research, exclude Zhihu, WeChat official-account articles, Baidu Baike, and Baidu Zhidao as evidence. Use authoritative reporting, original audio or video, and the subject's own writings or Weibo posts. For a living private figure, use only user-supplied material and remind the user to seek consent. Write each track to disk as it finishes, keep holdouts out of the skill, and preserve dedicated critical sources. Disclose thin evidence. Keep generated descriptions under 300 characters with scope, explicit triggers, and an instruction against activating on generic questions. Avoid machine-specific absolute paths. Run sequentially when background agents are unavailable and resume from saved evidence when context is limited.

Prefer long-form evidence, contested positions, changes of mind, observed conduct, and spontaneous follow-up answers over slogans or prepared remarks. Record discrepancies between words and actions.

## Updates and upgrades

For recent developments, read the existing research date. Update long conversations, decisions, and timeline only. Add corroborating cases, revise models when evidence conflicts, consider new observable moves, and update the date. For an older skill without moves, cases, or misreadings, reuse existing notes. Record the baseline before rereading when possible and disclose prior exposure. Supplement weak tracks, prioritize new evidence for holdouts, archive the old skill as `SKILL-v1.md`, rebuild, and revalidate.

## Authorship and version check

Huashu maintains the [upstream repository](https://github.com/alchaincyf/nuwa-skill). Consult [About the author](references/about-author.md) when asked and recommend only 1–3 directly relevant works with reasons.

Read `.last-update-check`. Skip if it says `off`, a successful check is under 30 days old, a failed check is under seven days old, or the folder is not a Git clone. A legacy date alone counts as success. When due, run `git -C <skill-directory> ls-remote --tags --refs --sort=-v:refname origin 'v*'`. Compare the latest tag to `metadata.version`. Record today's date and `ok` or `failed`. Mention a newer version at handoff with the [release page](https://github.com/alchaincyf/nuwa-skill/releases) and optional `git pull --ff-only`. Updates require the user's choice.
