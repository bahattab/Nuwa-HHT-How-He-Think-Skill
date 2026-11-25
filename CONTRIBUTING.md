# Contributor Guide

Thank you for wanting to contribute to the Nuwa ecosystem. Read this page first to find the right route for your contribution and save everyone some back-and-forth.

## One Core Rule

**`SKILL.md` is the core asset of this repository. We do not accept external PRs that modify it.** The maintainer has tested and refined each line of the Nuwa methodology through successive versions (see the darwin-skill workflow). Only the maintainer makes changes to this file.

We still welcome your ideas. If you find a bug in the methodology or see a way to improve it, **open an issue for discussion**. The maintainer will implement accepted ideas in SKILL.md and credit you in the commit. For example, the description length-limit bug reported in PR #59 was handled this way.

## Contributing a Persona Skill

Use the community index, not `examples/`. The `examples/` directory holds the maintainer’s official examples, which follow a common quality standard. If you have distilled a persona skill, use this process:

1. **Put it in your own GitHub repository** (one repository per skill, with the stars and maintenance rights staying with you).
2. **Run the fidelity assessment** using [references/fidelity-scorecard.md](references/fidelity-scorecard.md) and add a `FIDELITY.md` file to your repository.
3. **Open a PR to add a link to your repository in [COMMUNITY.md](COMMUNITY.md)**. A single line is enough.

This gives your work its own home and star count. You can continue to improve it on your own schedule, independent of this repository.

### Requirements for Listing in COMMUNITY.md

- Use the Nuwa workflow to distill the persona. Include the underlying research in `references/research/` so the repository is self-contained and its sources can be traced.
- Include sections on “Honesty Boundaries” and “Antipatterns.”
- Achieve grade B or higher (70 points or more) on the fidelity scorecard, and put `FIDELITY.md` in the repository root.
- The key fields in `FIDELITY.md` (test date, total score, and scores for each dimension) must contain actual results from tests run independently by two agents. Do not use placeholders such as “pending,” “estimated,” “TBD,” or “YYYY-MM-DD,” or submit estimated scores. Automated checks reject these.
- Pass the ethics checks below.

When you submit a PR for inclusion, a bot checks the formal requirements above and posts a comment with a ✅/❌ checklist. Push a fix and the checks rerun automatically. After the automated checks pass, the maintainer reviews compliance with the ethics rules and the quality of the content before merging.

## Ethics Rules

Do not submit any of the following. They are not eligible for listing.

- Skills based on **living private individuals** (coworkers, former partners, or other private people) without their consent.
- Skills intended for impersonation, harassment, or fraud.
- Skills covering high-stakes areas such as medicine, law, or investing unless they include an explicit disclaimer and state that they cannot replace a qualified professional.

## Other Ways to Contribute

| Contribution | How to Submit |
|------|--------|
| Methodology bug or improvement idea | Open an issue for discussion. Do not open a PR that edits SKILL.md directly. |
| Fix for a utility script in scripts/ | Open a PR directly and include steps to reproduce the issue. |
| README translation or documentation typo | Open a PR directly. |
| Related tool, collection, or orchestration project | Open a PR to add it to COMMUNITY.md. |

## PR Checklist

- [ ] The PR does not modify `SKILL.md`.
- [ ] There are no stray files such as `.DS_Store`.
- [ ] The PR serves one purpose. Do not bundle multiple personas into one PR.
- [ ] The description explains what changed, why it changed, and how it was verified.

---

## English Summary

- **`SKILL.md` is the core asset and does not accept external PRs.** Found a bug or improvement? Open an issue. The maintainer implements accepted ideas and credits you in the commit.
- **Persona skills go to the community index, not `examples/`.** Host the skill in your own repository (you keep the stars), run the [fidelity scorecard](references/fidelity-scorecard.md) (grade B or above), then open a PR with a one-line entry in [COMMUNITY.md](COMMUNITY.md).
- **Ethics**. Do not distill living private individuals without consent or submit skills intended for impersonation or harassment. Medical, legal, and financial personas need explicit disclaimers.
