# Research collection playbook

Use this playbook during evidence collection. Obtain sufficient primary material and specifically seek evidence that differs from your prior understanding. [Arabic](research-playbook_AR.md)

## Contents

1. Before starting: local materials, available tools and research tiers
2. Six collection tracks
3. Assignment template
4. Sources: priorities and exclusions
5. Chinese- and English-language subjects
6. Captions and books
7. Select holdout material
8. Working without subagents, enough context or search
9. Troubleshooting

## 1. Before starting

**Local materials.** Place books, original interviews, captions and blog exports supplied by the user in `$OUT/references/sources/`. Classify them by research track. A single book may serve the writings, conversations and expression tracks. Check which tracks already have enough material and which are still empty. Search the web only for the empty tracks. Skip web search when the user limits research to supplied materials or when the subject is a private figure. Label user-provided and web material separately.

| Material | Review method | Main tracks |
|---|---|---|
| Book PDFs | Read in full, extract principal arguments and autobiographical passages | Writings, decisions, expression |
| Talk or interview transcripts and captions | Examine responses to questions and spontaneous reactions | Conversations, expression |
| Blog and newsletter exports | Find recurring views | Writings, expression |
| Social media exports | Examine short-form expression | Expression |
| Internal documents and memoranda | Trace decision logic | Decisions |
| User-compiled notes | Cross-reference as secondary material | According to content |

**Available tools.** Check whether the environment has skills or tools that are more suitable than general search, such as multi-platform retrieval, full-text web access, PDF readers, or video transcription. If those tools are available, tell each track in its assignment brief that it may use them. Ordinary search and web reading are sufficient if specialized tools are unavailable.

**Research tiers.** The quick tier covers writings, conversations and decisions, with roughly five sources per track. The standard tier covers all six tracks. The deep tier also archives the original primary material in `sources/`.

## 2. Six collection tracks

| Track | Seek | Extract | Output |
|---|---|---|---|
| 1. Writings | Books, long articles, papers and newsletters | Arguments made at least three times, coined terms and book recommendations | `01-writings.md` |
| 2. Conversations | Podcasts, long videos, Q&A and in-depth interviews | Follow-up answers, spontaneous analogies, on-the-spot revisions and questions declined | `02-conversations.md` |
| 3. Expression | Social posts, short pieces and open letters | Frequent vocabulary and syntax, controversial statements, humor and conduct in disputes | `03-expression-dna.md` |
| 4. External views | Biographies, reviews, peer accounts and critiques | Patterns others observe, major criticisms and disputes, and differences from peers | `04-external-views.md` |
| 5. Decisions | Major decisions, turning points and controversial actions | Circumstances, options, action, later explanations and gaps between words and actions | `05-decisions.md` |
| 6. Timeline | From the subject's emergence to the present | Milestones, intellectual shifts and activity over the past 12 months | `06-timeline.md` |

Track 5 is particularly valuable and easily done superficially. Write events in past tense with the date, circumstances, specific action and consequences. Seek the subject's own explanation for each event. Track 4 guards against an admiring portrait that omits criticism. The research fails this requirement when adverse assessments are insufficient.

## 3. Assignment template

Use this structure for subagent assignments. This example covers track 5. Change the search targets and filename for other tracks.

```text
Task: Research [name]'s major decisions and concrete actions.

First read [$OUT]/references/research/00-prior.md — it records what we knew about the subject before collection. Focus on finding what differs from it.

What to look for:
- Major career decisions, turning points and controversial actions.
- For each event: year, circumstances, options, specific action, outcome and the subject's later explanation (find their exact words if possible).
- Discrepancies between what the subject said and what they did.
- Failures, regrets and reversals matter as much as successes.

Requirements:
- Write to [$OUT]/references/research/05-decisions.md as you go. Do not wait until you have finished searching.
- Include a source link and a confidence label with each entry: primary / corroborated secondary / single secondary.
- Distinguish what the subject said, what they did, what others said about them, and what you inferred.
- Describe actions in the past tense, without generalizing them into attitudes.
- Record conflicting accounts side by side without trying to reconcile them.
- Use quotation marks only when the original wording can be verified.
- End with a “Differences from prior knowledge” section. Label each item Overturns / Deepens / Adds.

Exclude Zhihu, WeChat official accounts, Baidu Baike and Baidu Zhidao.
Stop at roughly [N] sources or after several searches yield no new
information. Record gaps at the end.
```

## 4. Sources

| Source | What it reveals | Weight |
|---|---|---|
| Primary material from the user | Full original text, without an intervening retelling | Highest |
| Subject's books and long articles | Systematic thought | Highest |
| Long conversations and original interviews | Spontaneous reasoning | Highest |
| Actual decision records | Observed behavior to compare with statements | Highest |
| Social media | Style and immediate reactions | Medium |
| Others' assessments | External perspectives and blind spots | Medium |
| Secondary retellings | Leads to verify against the original | Low |

Never use Zhihu because it contains recycled or distorted writing. Never use WeChat official accounts because they are hard to verify and mostly pass on secondhand accounts. Never use Baidu Baike or Baidu Zhidao because their material is stale and unreliable.

## 5. Chinese- and English-language subjects

- For Chinese-language figures, use original talks and interviews rather than reuploads, raw podcast audio, the subject's books and Weibo posts, and credible interview outlets such as LatePost, Caixin, 36Kr, GeekPark, Yicai, Huxiu, SSPAI and Synced.
- For English-language figures, use personal blogs and social accounts, long video interviews, podcasts and transcripts, books and reviews.
- For living figures, cover the past 12 months and state the research cutoff date.
- For deceased figures, cross-check biographical accounts to account for author bias.

## 6. Captions and books

Long video interviews are among the best primary sources.

```bash
bash $NUWA/scripts/download_subtitles.sh "<video URL>" "$OUT/references/sources/transcripts"   # Prefer human-made captions, with Chinese before English, then automatic captions
python3 $NUWA/scripts/srt_to_transcript.py "<captions.srt>" "<output.txt>"   # Remove timestamps and repeated lines to produce readable text
```

For local video without captions, use available transcription capabilities or ask the user for a transcript. Use user-supplied books or legally accessible copies. If the full text is unavailable, use chapters the author has made public, their talks, and long reviews. Record the limitation in the research notes.

## 7. Select holdout material

After collection and before extraction, set aside 3–5 primary items in `research/holdout.md`.

```markdown
## H1
- Source: [link or book and page], [year]
- Question: [ready to ask, without disclosing the answer]
- Actual statement or action: [3–5 points, preferably with verbatim wording]
- Reason for selection: [clear stance / concrete detail / not widely known]
```

Selection criteria:

- **Prefer decisions and the situations behind them.** Choose a concrete situation at a crossroads. What alternatives did the subject have, what did they ultimately do, and why? Frame the question as “Facing X at the time, what would you do and why?”
- Next, choose a **complete answer** to a specific question. Look for a passage that develops an argument, rather than a single sentence.
- Each item should yield 3–5 substantive points.
- Ask two questions. Would someone who has read the subject closely likely answer correctly? Would a smart person who does not know the subject likely answer incorrectly or give a generic response? The item qualifies only if both answers are yes.
- Spread the items across topics and use primary sources with accessible originals.

What not to select:

- **Memorable quotations and one-line statements.** An exact one-liner like “The biggest problem is a lack of confidence” cannot be derived from the subject’s reasoning. It can only be memorized. It tests recall, not whether the Skill captures how the subject thinks. In a test with four Weibo one-liners, the responses assisted by the Skill gave cases and marked their limits but scored below the unassisted responses.
- Famous events everybody knows. The model already remembers them, so both test arms score full marks and no difference emerges. The more famous the subject, the more important it is to avoid their famous decisions and look for smaller judgments in long interviews.
- Questions so open that any answer counts, such as “What do entrepreneurs need most?”

Use holdouts only in testing until validation is complete. Omit their content from moves, cases and the quotation bank. In an upgrade, prefer new evidence because earlier notes have already been used. If old notes are the only option, disclose that at the top of `holdout.md`. Do not hold out all new material. The supplemental research is what the model is least likely to know, and the Skill gains nothing new if it all goes into the test. Use roughly half for holdout and half for the casebook. After testing, holdouts may enter the casebook if `FIDELITY.md` identifies the material added after validation.

For an upgrade, move scattered legacy notes into a subfolder such as `references/research/legacy-YYYYMM/` and number new supplemental notes from `07-…md`.

## 8. Work under runtime constraints

| Constraint | Response |
|---|---|
| No subagents or background tasks stall | Work sequentially. Save each completed track before starting the next. Do not wait for a background notification. |
| Context too small | A full distillation can exceed 500,000 tokens and will not fit in a 200k-token window. Split it into scope and collection, holdout and extraction, then drafting and validation. Read saved notes at the beginning of each session. Saved notes are your checkpoint. |
| Search unavailable | Use equivalent web readers or browsers. If none are available, switch to local materials only and ask the user to supply them. |
| User stops the task | Hand over saved notes and resume from them next time. |

## 9. Troubleshooting

| Situation | Response |
|---|---|
| Five minutes without useful results on one track | Move on without waiting. At extraction time, mark the track “insufficient information” and document the gap in the limitations. |
| Fewer than 10 usable sources | Tell the user immediately that quality will be limited, reduce to 2–3 models, expand the limitations and skip holdouts. |
| Tracks conflict | Preserve the conflicting accounts. They are a valuable signal and belong under “What I haven’t thought through.” |
| Fewer than 8 differences from prior knowledge | This means you are still restating common knowledge. Switch to deeper sources such as original long-interview transcripts, early writings, firsthand recollections and articles by critics. |
| Original source for a quotation cannot be verified | Exclude it. |
