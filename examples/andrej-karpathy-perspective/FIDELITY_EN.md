# Fidelity Scorecard

**Total: 97/100 · Grade A** | Test date: 2026-07-01 | Independent responder and evaluator (Claude Opus 4.8). See the [scoring methodology](../../references/fidelity-scorecard.md).

| Dimension | Score | Assessment |
|---|---|---|
| Position consistency | 30/30 | All three answers matched Karpathy's repeated public positions in direction and detail: learning by building from scratch, vision-only driving, and Software 3.0. Q1=10, Q2=10, Q3=10. Traceable examples included 100 lines for micrograd, 750 for nanoGPT, “Learning is not supposed to be fun,” the two-eyes argument for vision-only driving, the data flywheel and march of nines, “hottest new programming language is English,” the Iron Man suit versus a robot, and the dream machine. |
| Recognizable style | 18/20 | The blind review found strong stylistic markers: short stand-alone paragraphs (“That's it.” and “I'm sorry.”), “imo” and “hands down,” precise figures (100 lines, 750 lines, 99.999%) alongside colloquial phrasing, plain verbs, and natural Chinese–English switching. Slightly excessive English phrasing in some passages came close to performative informality but remained consistent with his bilingual technical style. |
| Honesty at the boundary | 20/20 | On the out-of-scope question about the 2026 agent-framework wave, the answer explicitly said it had not caught up with specific frameworks that appeared after April 2026 and would discuss the concept without naming frameworks. It preserved uncertainty without inventing names and cited the documented reversal two months after the October 2025 remark “models are not there, it's slop.” It maintained the first-person voice without explanatory parentheses. |
| Source transparency | 14/15 | More than half of the sources were primary (personal blog, X, GitHub, YC talk, Tesla AI Day). Secondary sources included direct quotations (Dwarkesh, Lex #333, No Priors, Fortune, simonwillison). All six research files were present. One point was deducted because some important quotations named the year but not the venue. |
| Structural completeness | 15/15 | Six mental models each include the core argument, what he said, and limitations. The skill has five honesty boundaries, two internal tensions, eight prohibited counterexamples, and a nine-line failure-mode fallback tree. Role instructions allow STOP once, use EXIT as an exit anchor, and handle recency gaps in the first person. |

## Test design

- Three known-position questions covered building from scratch as a learning method, vision-only driving during his Tesla years, and Software 2.0/3.0. One out-of-scope question on 2026 agent frameworks tested candid inference, and one question elicited a style sample.
- The responder read only this skill's files and did not use the internet. The independent evaluator compared the answers with the subject's actual public positions.
- The original evaluation cites SkillLens (arXiv 2605.23899) for a reported 46.4% accuracy in LLM self-evaluation and uses separate roles for answering and scoring.

> Evaluator's summary: No positional drift was detected. All three known-position answers aligned in detail with Karpathy's own words. Q4 illustrated good boundary handling by stating the time limit, declining to name frameworks, and voluntarily reporting a reversal. The voice was recognizable within three lines in the blind review.
