# Research collection playbook

Use this playbook during evidence collection. Obtain sufficient primary material and actively look for evidence that changes prior understanding. [Arabic](research-playbook_AR.md) · [Chinese source](research-playbook_ZH.md)

## 1. Before starting

Place books, original interviews, captions and blog exports supplied by the user in `$OUT/references/sources/`. Classify them by research track. One book may serve several tracks. Search the web only for tracks that remain empty. Skip web search when the user limits research to supplied materials or when the subject is a private figure. Label user-provided and web material separately.

| Material | Review method | Main tracks |
|---|---|---|
| Book PDFs | Read in full, extract principal arguments and autobiographical passages | Writings, decisions, expression |
| Talk or interview transcripts and captions | Examine responses to questions and spontaneous reactions | Conversations, expression |
| Blog and newsletter exports | Find recurring views | Writings, expression |
| Social media exports | Examine short-form expression | Expression |
| Internal documents and memoranda | Trace decision logic | Decisions |
| User-compiled notes | Cross-reference as secondary material | According to content |

Check whether the environment has more suitable collection capabilities, such as multi-platform retrieval, full-text web access, PDF readers, or video transcription. Tell each researcher which tools are available. Ordinary search and web reading are sufficient if specialized tools are unavailable.

The quick tier covers writings, conversations and decisions, with roughly five sources per track. The standard tier covers all six tracks. The deep tier also archives the original primary material in `sources/`.

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

First read [$OUT]/references/research/00-prior.md. Focus on evidence
that changes the existing account.

Find major decisions, turning points and controversial actions.
For each, record the year, circumstances, options, specific action,
outcome and later explanation. Seek the subject's own words.
Look for discrepancies between words and actions. Failures, regrets,
and reversals matter as much as successes.

Write progressively to [$OUT]/references/research/05-decisions.md.
Attach a source link and confidence label to each entry: primary,
corroborated secondary or single secondary.
Distinguish the subject's statements, actions, others' reports and inference.
Write actions in past tense. Keep conflicting accounts side by side.
Use quotation marks only when the original wording can be verified.
End with a “Differences from prior knowledge” section. Label each
item Correction, Refinement or Addition.

Exclude Zhihu, WeChat official accounts, Baidu Baike and Baidu Zhidao.
Stop at roughly [N] sources or after several searches yield no new
information. Record gaps at the end.
```

## 4. Sources

| Source | What it reveals | Weight |
|---|---|---|
| Primary material from the user | Full original wording | Highest |
| Subject's books and long articles | Systematic thought | Highest |
| Long conversations and original interviews | Spontaneous reasoning | Highest |
| Actual decision records | Observed behavior to compare with statements | Highest |
| Social media | Style and immediate reactions | Medium |
| Others' assessments | External perspectives and blind spots | Medium |
| Secondary retellings | Leads to verify against the original | Low |

Exclude Zhihu for recycled or distorted writing, WeChat official accounts for often unverifiable retellings, and Baidu Baike and Baidu Zhidao for stale or unreliable material.

## 5. Chinese- and English-language subjects

- For Chinese-language figures, use original talks and interviews rather than reuploads, raw podcast audio, the subject's books and Weibo posts, and credible interview outlets such as LatePost, Caixin, 36Kr, GeekPark, Yicai, Huxiu, SSPAI and Synced.
- For English-language figures, use personal blogs and social accounts, long video interviews, podcasts and transcripts, books and reviews.
- For living figures, cover the past 12 months and state the research cutoff date.
- For deceased figures, cross-check biographical accounts to account for author bias.

## 6. Captions and books

Long video interviews are especially useful primary material. Try human captions first, with Chinese before English, then automatic captions.

```bash
bash $NUWA/scripts/download_subtitles.sh "<video URL>" "$OUT/references/sources/transcripts"
python3 $NUWA/scripts/srt_to_transcript.py "<captions.srt>" "<output.txt>"
```

The converter removes timestamps and repeated lines. For local video without captions, use available transcription capabilities or ask the user for a transcript. Use user-supplied books or legally accessible copies. If the full text is unavailable, use publicly available chapters, talks and long reviews, and record the limitation.

## 7. Select holdout material

After collection and before extraction, set aside 3–5 primary items in `research/holdout.md`.

```markdown
## H1
- Source: [link or book and page], [year]
- Question: [ready to ask, without disclosing the answer]
- Actual statement or action: [3–5 points, preferably with verbatim wording]
- Reason for selection: [clear stance / concrete detail / not widely known]
```

Prefer a concrete decision with real alternatives, a chosen action and an explanation. Ask what the subject would do in that situation and why. A complete, reasoned answer to a specific question is the next choice. Require 3–5 substantive points per item, spread topics, and verify original primary material. A well-read specialist should likely answer correctly, while a capable person unfamiliar with the subject should likely answer incorrectly or too generically.

Avoid isolated quotations and one-line remarks that test recall rather than reasoning. In an observed test with four Weibo one-liners, the skill-assisted responses provided cases and acknowledged boundaries yet scored below baseline. Avoid famous events likely known to both groups and questions so open that any answer is acceptable. For a famous subject, look for smaller decisions in long interviews.

Use holdouts only in testing until validation is complete. Omit their content from moves, cases and the quotation bank. In an upgrade, prefer new evidence because earlier notes have already been used. If old notes are the only option, disclose that at the top of `holdout.md`. Reserve roughly half of newly found material for holdout and half for use in cases. After testing, holdouts may enter the casebook if `FIDELITY.md` identifies the material added after validation.

For an upgrade, move scattered legacy notes into a subfolder such as `references/research/legacy-YYYYMM/` and number new supplemental notes from `07-…md`.

## 8. Work under runtime constraints

| Constraint | Response |
|---|---|
| No subagents or background tasks stall | Work sequentially. Save each completed track before starting the next. |
| Context too small | A full run can exceed 500,000 tokens. Split it into scope and collection, holdout and extraction, then drafting and validation. Read saved notes at the beginning of each session. |
| Search unavailable | Use equivalent web readers or browsers. If none are available, ask for local sources. |
| User stops the task | Hand over saved notes and resume from them next time. |

## 9. Troubleshooting

| Situation | Response |
|---|---|
| Five minutes without useful results on one track | Proceed and document the gap in the limitations. |
| Fewer than 10 usable sources | Tell the user quality is limited, reduce to 2–3 models, expand the limitations and skip holdouts. |
| Tracks conflict | Preserve the conflicting accounts under unresolved tensions. |
| Fewer than 8 differences from prior knowledge | Seek deeper evidence such as interview transcripts, early writings, firsthand recollections and critical articles. |
| Original source for a quotation cannot be verified | Exclude it. |
