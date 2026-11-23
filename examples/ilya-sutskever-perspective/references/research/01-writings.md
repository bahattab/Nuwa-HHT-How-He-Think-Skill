# Ilya Sutskever: Research on academic papers, writings, and core ideas

> Research date: 2026-04-05
> Researcher: Claude Opus 4.6
> Excluded sources: Zhihu, WeChat Official Accounts, and Baidu Baike were not used.

---

## 1. Background at a glance

**Ilya Sutskever** (born in Russia in 1985, moved to Israel at age five, later moved to Canada)

| Date | Event |
|---|---|
| 2005 | Bachelor's in mathematics from the University of Toronto (entered directly from grade 11) |
| 2007 | Master's in computer science at the University of Toronto, supervised by Geoffrey Hinton, thesis: *Nonlinear Multilayered Sequence Models* |
| 2012 | Co-created AlexNet with Krizhevsky and Hinton, launching the deep learning revolution |
| 2012 | Stanford postdoctoral researcher (about two months in Andrew Ng's lab) |
| 2013 | Google acquired DNNResearch → joined Google Brain |
| 2013 | PhD in computer science from the University of Toronto, thesis: *Training Recurrent Neural Networks* |
| 2014 | Created the Seq2Seq algorithm at Google Brain |
| December 2015 | Left Google, co-founded OpenAI, and became chief scientist |
| July 2023 | Established the Superalignment team at OpenAI |
| November 2023 | Participated in the board's removal of Sam Altman and later publicly expressed regret |
| May 2024 | Left OpenAI |
| June 2024 | Founded SSI (Safe Superintelligence Inc.) |
| March 2025 | SSI valued at US$32 billion and raised US$2 billion |
| July 2025 | Became SSI CEO |

Sources: [Wikipedia](https://en.wikipedia.org/wiki/Ilya_Sutskever), [University of Toronto](https://www.cs.toronto.edu/~ilya/) | Confidence: primary and authoritative secondary sources

---

## 2. Important academic papers

### 2.1 Landmark papers in chronological order

#### 1. ImageNet Classification with Deep Convolutional Neural Networks (AlexNet, 2012)
- **Authors:** Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
- **Core contribution:** A deep CNN substantially outperformed traditional methods on ImageNet, sparking the deep learning revolution.
- **Citation count:** Extremely high. Google Scholar shows more than 780,000 total citations for Sutskever, with this paper among his most cited.
- **Paper:** [NeurIPS 2012](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks)
- **Confidence:** Primary source.

#### 2. Sequence to Sequence Learning with Neural Networks (Seq2Seq, 2014)
- **Authors:** Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **Core contribution:** Mapped an input sequence to a fixed-dimensional vector using a multilayer LSTM, then decoded it into a target sequence. This laid a foundation for machine translation and dialogue systems.
- **Paper:** [arXiv:1409.3215](https://arxiv.org/abs/1409.3215)
- **Confidence:** Primary source.

#### 3. Recurrent Neural Network Regularization (2014)
- **Authors:** Wojciech Zaremba, Ilya Sutskever, Oriol Vinyals
- **Core contribution:** Proposed an RNN regularization method that improved training stability.
- **Paper:** [arXiv:1409.2329](https://arxiv.org/abs/1409.2329)
- **Confidence:** Primary source.

#### 4. Language Models are Unsupervised Multitask Learners (GPT-2, 2019)
- **Authors:** Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever
- **Core contribution:** Demonstrated that a language model could learn to perform multiple tasks in a zero-shot setting. GPT-2, with 1.5 billion parameters, achieved state-of-the-art results on seven of eight language modeling benchmarks.
- **Paper:** [OpenAI](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- **Confidence:** Primary source.

#### 5. Language Models are Few-Shot Learners (GPT-3, 2020)
- **Authors:** Tom Brown, Benjamin Mann, … Ilya Sutskever, and others
- **Core contribution:** A 175-billion-parameter model demonstrated strong few-shot performance, validating the scaling hypothesis.
- **Confidence:** Primary source.

#### 6. Weak-to-Strong Generalization (Superalignment's first result, December 2023)
- **Team:** OpenAI's Superalignment team, co-led by Sutskever.
- **Core contribution:** A GPT-2-level model supervised GPT-4, which generalized to near GPT-3.5 performance. The work showed that weak supervisors can guide strong models.
- **Paper:** [OpenAI](https://openai.com/index/weak-to-strong-generalization/)
- **Confidence:** Primary source.

### 2.2 Other important collaborations

| Paper or project | Sutskever's role | Description |
|---|---|---|
| TensorFlow | Core contributor | Helped develop it while at Google Brain |
| AlphaGo | One of the collaborators | Listed among many contributors |
| CLIP | Oversaw it while at OpenAI | Multimodal contrastive learning |
| DALL-E | Oversaw it while at OpenAI | Text-to-image generation |

Sources: [Wikipedia](https://en.wikipedia.org/wiki/Ilya_Sutskever), [Google Scholar](https://scholar.google.com/citations?user=x04W_mMAAAAJ&hl=en) | Confidence: primary and authoritative secondary sources

### 2.3 Doctoral dissertation

- **Title:** *Training Recurrent Neural Networks* (2013)
- **Supervisor:** Geoffrey Hinton
- **Master's thesis:** *Nonlinear Multilayered Sequence Models* (2007)

---

## 3. Sutskever's List of recommended reading

### Background

Around 2020, Sutskever emailed John Carmack a list of about 30 papers and blog posts, with this note:

> **"If you really learn all of these, you'll know 90% of what matters today."**

Sources: [GitHub reconstruction](https://github.com/dzyim/ilya-sutskever-recommended-reading), [Turing Post analysis](https://www.turingpost.com/p/ilya-sutskever-reading-list), [mattprd.com](https://www.mattprd.com/p/openai-cofounder-27-papers-read-know-90-ai) | Confidence: secondary. The original email was not published, but multiple independent sources cross-checked the contents of the list.

### Full list as reconstructed by the community

1. **The Annotated Transformer** — Sasha Rush et al. | [Link](https://nlp.seas.harvard.edu/annotated-transformer/)
2. **The First Law of Complexodynamics** — Scott Aaronson | [Link](https://scottaaronson.blog/?p=762)
3. **The Unreasonable Effectiveness of Recurrent Neural Networks** — Andrej Karpathy | [Link](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
4. **Understanding LSTM Networks** — Christopher Olah | [Link](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
5. **Recurrent Neural Network Regularization** — Zaremba, Sutskever, Vinyals | [arXiv](https://arxiv.org/abs/1409.2329)
6. **Keeping Neural Networks Simple by Minimizing the Description Length of the Weights** — Hinton & van Camp
7. **Pointer Networks** — Vinyals et al. | [NeurIPS](https://papers.nips.cc/paper/5866-pointer-networks)
8. **ImageNet Classification with Deep Convolutional Neural Networks** — Krizhevsky, Sutskever, Hinton
9. **Order Matters: Sequence to Sequence for Sets** — Vinyals et al. | [arXiv](https://arxiv.org/abs/1511.06391)
10. **GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism** — Huang et al. | [arXiv](https://arxiv.org/abs/1811.06965)
11. **Deep Residual Learning for Image Recognition** — Kaiming He et al.
12. **Multi-Scale Context Aggregation by Dilated Convolutions** — Fisher Yu & Vladlen Koltun
13. **Neural Message Passing for Quantum Chemistry** — Justin Gilmer et al.
14. **Attention Is All You Need** — Vaswani et al.
15. **Neural Machine Translation by Jointly Learning to Align and Translate** — Bahdanau et al.
16. **Identity Mappings in Deep Residual Networks** — He et al.
17. **A Simple Neural Network Module for Relational Reasoning** — Santoro et al.
18. **Variational Lossy Autoencoder** — Xi Chen et al.
19. **Relational Recurrent Neural Networks** — Santoro et al.
20. **Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton** — Aaronson et al.
21. **Neural Turing Machines** — Alex Graves et al.
22. **Deep Speech 2** — Amodei et al.
23. **Scaling Laws for Neural Language Models** — Kaplan et al.
24. **A Tutorial Introduction to the Minimum Description Length Principle** — Peter Grunwald
25. **Machine Super Intelligence** — Shane Legg (doctoral dissertation of the DeepMind co-founder)
26. **Kolmogorov Complexity and Algorithmic Randomness** — Shen, Uspensky, Vereshchagin
27. **CS231n: Convolutional Neural Networks for Visual Recognition** (Stanford course)

**Analysis of the list:** Topics span compression theory (MDL and Kolmogorov complexity), sequence modeling (RNNs, LSTMs, and Transformers), vision (CNNs and ResNet), reasoning (relational networks), and scaling laws. Two pieces by Scott Aaronson on complexity theory and Shane Legg's dissertation on superintelligence are especially noteworthy. They show that Sutskever's thinking extends well beyond engineering and into the foundations of information theory and complexity theory.

**Book based on the list:** Richard Heimann's *Sutskever's List: Foundational Ideas of Modern AI*, published by Simon & Schuster. [Link](https://www.simonandschuster.com/books/Sutskevers-List/Richard-Heimann/9781633434790)

---

## 4. Major talks and interviews

### 4.1 NeurIPS 2024 talk: “Pre-Training as We Know It Will End” (December 2024)

**Main arguments:**
- Pretraining will end “unquestionably,” because the data supply will not grow.
- **Exact quotation:** "While compute is growing through better hardware, better algorithms and larger clusters, the data is not growing because we have but one internet."
- **Exact quotation:** "You could even go as far as to say that data is the fossil fuel of AI. It was created somehow, and now we use it, and we've achieved peak data."
- Possible paths forward include synthetic data, which he called “a big challenge,” more computation at inference time, and agentic AI.
- Superintelligence is “clearly the direction of the field.”

Sources: [dlyog.com](https://dlyog.com/papers/one_internet_v1), [machine.news](https://www.machine.news/ilya-sutskever-peak-data-ai-openai/), [Hacker News discussion](https://news.ycombinator.com/item?id=42413677) | Confidence: primary source

### 4.2 First Dwarkesh Podcast interview (March 2023)

**Main arguments:**
- **"Predicting the next token well means that you understand the underlying reality that led to the creation of that token."** Predicting the token amounts to understanding the reality that produced it.
- Next-token prediction has no inherent ceiling: “If your underlying neural network is smart enough, you just ask it: What would a person with great insight and ability do?”
- A single mathematical definition of alignment is unlikely: “Rather than implement one mathematical definition, I think we'll implement several.”
- Do not underestimate the difficulty of aligning superhuman AI: Consider “models that can misrepresent their own intentions.”
- Humans may choose to “become part AI.”
- Deep learning was an inevitable discovery. Without key individuals, it would have been delayed by only about a year.

Sources: [Dwarkesh Podcast](https://www.dwarkesh.com/p/ilya-sutskever) | Confidence: primary source

### 4.3 Second Dwarkesh Podcast interview (November 2025)

**Main arguments, with substantial changes since the first interview:**
- **“We are moving from the age of scaling to the age of research.”** 2012–2020 was the research era, 2020–2025 the scaling era, and 2026 onward a return to research.
- Current AI models generalize “far worse than humans.” **Generalization is the greatest bottleneck.**
- Current methods will “go some distance and then stall.” They will not lead directly to AGI.
- New kinds of systems are needed, which “we do not yet know how to build.”
- Another hundredfold increase in scale would make a difference without transforming AI capabilities.
- Superintelligence is a superlearner rather than an all-knowing database, like “a gifted 15-year-old very eager to get started.”
- Ideas rather than compute are the bottleneck for AI.
- Alignment may be easier if AI is itself conscious, through mirror neurons or empathy.
- Long-term equilibrium might require a Neuralink++-style merger of humans and AI.

Sources: [Dwarkesh Podcast](https://www.dwarkesh.com/p/ilya-sutskever-2), [EA Forum analysis](https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/highlights-from-ilya-sutskever-s-november-2025-interview) | Confidence: primary source

### 4.4 NVIDIA GTC interview with Jensen Huang (March 2023)

**Main arguments:**
- **"When we train a large neural network to accurately predict the next word in lots of different texts from the Internet, what we are doing is that we are learning a world model."**
- **"This text is actually a projection of the world."** Text is a projection of the world.
- **"Really good compression of the data will lead to unsupervised learning."**
- **"I had a very strong belief that bigger is better."**
- His reaction when Transformer appeared: “oh my god, this is the thing”.
- Reliability rather than capability is the greatest current obstacle.

Sources: [lifearchitect.ai](https://lifearchitect.ai/ilya/) | Confidence: primary source

### 4.5 MIT Technology Review interview (October 2023)

**Main arguments:**
- Superintelligence may arrive within ten years.
- AGI will reduce healthcare costs and improve quality by a factor of 1,000 each.
- **"One possibility—something that may be crazy by today's standards but will not be so crazy by future standards—is that many people will choose to become part AI."**
- **"It's going to be monumental, earth-shattering. There will be a before and an after."**
- His work shifted from building the next generation of GPT to preventing loss of control over superintelligence.

Sources: [MIT Technology Review](https://www.technologyreview.com/2023/10/26/1082398/exclusive-ilya-sutskever-openais-chief-scientist-on-his-hopes-and-fears-for-the-future-of-ai/) | Confidence: primary source

### 4.6 Simons Institute talk: “An Observation on Generalization” (2023)

**Core theory:**
- Compression and prediction are fundamentally equivalent: **“There is a one-to-one correspondence between all compressors and all predictors.”**
- Kolmogorov complexity is the theoretical limit of ultimate compression.
- Neural networks are programmable computers, and SGD searches the space of programs.
- iGPT validated the compression framework in the visual modality.
- Open questions include why learned representations are linearly separable and why autoregression outperforms masking.

Sources: [Simons Institute](https://simons.berkeley.edu/news/observation-generalization), [Notes](https://sumanthrh.com/post/notes-on-generalization/) | Confidence: primary source

---

## 5. Superalignment blog (official OpenAI)

### Introducing Superalignment (July 2023)

- Sutskever and Jan Leike co-led the team.
- OpenAI pledged 20% of its compute over the next four years.
- The approach was to use deep learning generalization to enable weak supervisors to control strong models.
- This was Sutskever's last major technical direction at OpenAI.

Sources: [OpenAI](https://openai.com/index/introducing-superalignment/) | Confidence: primary source

---

## 6. SSI founding statement (June 2024)

**Full mission statement:**

> "We are building safe superintelligence. We are the world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence. SSI is our mission, our name, and our entire product roadmap, because it is the most important technical problem of our time. We approach safety and capabilities in tandem, as technical problems to be solved through revolutionary engineering and scientific breakthroughs. We plan to advance capabilities as fast as possible while making sure our safety always remains ahead."

**Key term:** Sutskever coined “straight-shot SSI lab” to describe an organization aiming directly at superintelligence and building no interim products.

**Exact quotation:** "first product will be the safe superintelligence, and it will not do anything else up until then"

Sources: [ssi.inc](https://ssi.inc), [CNBC](https://www.cnbc.com/2024/06/19/openai-co-founder-ilya-sutskever-announces-safe-superintelligence.html) | Confidence: primary source

---

## 7. Core beliefs (recurring at least three times)

These are genuine beliefs he repeatedly expressed, distilled from multiple independent sources.

### Belief 1: Compression is understanding
- “Predicting the next token means understanding the underlying reality that produced it” (Dwarkesh, 2023).
- “Good compression leads to unsupervised learning” (GTC, 2023).
- “There is a one-to-one correspondence between compressors and predictors” (Simons, 2023).
- His reading list includes compression theory, such as MDL and Kolmogorov complexity.
- **Frequency: At least five appearances across 2016–2024.**
- **Assessment: This is his core epistemological position.**

### Belief 2: Scale was key, but his view is changing
- “I had a very strong belief that bigger is better” (GTC, 2023).
- Scaling is predictable and reliable (multiple sources).
- “Scaling era, 2020–2025” → “research era, 2026 onward” (Dwarkesh, 2025).
- A hundredfold increase makes a difference without being transformative (Dwarkesh, 2025).
- **Record of tension:** In 2023 he was still calling scale the master principle, whereas by 2024–2025 he explicitly declared its era over. This represents a genuine change in thinking rather than a contradiction. He developed the scaling paradigm and was among the first to acknowledge its limits.

### Belief 3: Safety and capability are inseparable
- “Safety and capabilities are two sides of the same coin” (multiple sources).
- The SSI statement says to “approach safety and capabilities in tandem.”
- Founded Superalignment (July 2023).
- Left OpenAI to found SSI (June 2024).
- **Frequency: At least five appearances.**
- **This belief drove his two most consequential career decisions.**

### Belief 4: Superintelligence will arrive
- “AGI will be the most impactful technology ever invented in human history” (multiple sources).
- “It's going to be monumental, earth-shattering” (MIT Technology Review, 2023).
- “Clearly the direction of the field” (NeurIPS, 2024).
- **Frequency: At least five appearances and no wavering.**

### Belief 5: Generalization is the core unsolved problem
- “These models somehow just generalize dramatically worse than people” (Dwarkesh, 2025).
- His Simons Institute talk focused on the information-theoretic basis of generalization.
- Reliable generalization is a prerequisite for superintelligence in his view.
- **Frequency: At least three appearances, with continued emphasis in 2023–2025.**

### Belief 6: Humans may or should merge with AI
- “many people will choose to become part AI” (MIT Technology Review, 2023).
- Becoming “part AI” strikes him personally as an attractive option (Dwarkesh, 2023).
- Long-term equilibrium might require Neuralink++-style integration (Dwarkesh, 2025).
- **Frequency: Three appearances.**

### Belief 7: AI may already have a slight degree of consciousness
- **"it may be that today's large neural networks are slightly conscious"** (February 2022 tweet).
- Alignment may be easier if AI is conscious (Dwarkesh, 2025).
- **Frequency: Two to three appearances, with considerable controversy.**
- **Yann LeCun opposed the idea, while Karpathy and Altman seemed to support it.**

---

## 8. Coined terminology and original concepts

| Term or concept | Meaning | First use |
|---|---|---|
| **Straight-shot SSI lab** | A lab going straight to superintelligence without intermediate products | SSI founding statement (June 2024) |
| **Age of Scaling → Age of Research** | Two stages in AI development | Dwarkesh Podcast (November 2025) |
| **Peak Data** | Internet training data have reached their peak | NeurIPS 2024 |
| **Data as fossil fuel** | Data are nonrenewable, like fossil fuels | NeurIPS 2024 |
| **Weak-to-strong generalization** | Alignment paradigm using a weak model to supervise a strong one | Superalignment paper (December 2023) |
| **Compression = prediction equivalence** | One-to-one correspondence between compressors and predictors | Simons Institute talk (2023) |
| **Superintelligent 15-year-old** | Metaphor for a superlearner rather than an omniscient database | Dwarkesh, 2025 |

---

## 9. Technical-direction decisions at OpenAI

### 9.1 Choosing GPT
- As chief scientist, Sutskever advanced a path from unsupervised pretraining to the GPT series.
- He saw the 2017 Sentiment Neuron work as GPT-1's precursor.
- His judgment when the Transformer appeared was “oh my god, this is the thing.” He immediately redirected the team to that architecture.

### 9.2 Scaling laws
- Sutskever championed the “bigger is better” belief within OpenAI.
- He included the scaling laws paper by Kaplan and colleagues on his reading list, indicating that he considered it a fundamental discovery.
- The belief directly drove resource-allocation decisions from GPT-2 to GPT-3 to GPT-4.

### 9.3 Superalignment team
- Established in July 2023 and co-led by Sutskever and Jan Leike.
- OpenAI pledged 20% of its compute for alignment research.
- The team produced the weak-to-strong generalization paper.
- It gradually disbanded after Sutskever's departure.

### 9.4 Altman's removal
- On 2023-11-17, Sutskever participated in the board's removal of Sam Altman.
- He wrote a 52-page memo containing allegations against Altman.
- Forty-eight hours later (November 18, as recorded in the source), there was discussion of merging OpenAI with Anthropic.
- On November 20, he tweeted publicly that he regretted his role.
- Much of the memo came from CTO Mira Murati and was not independently verified.
- In 2025, he gave nearly ten hours of videotaped testimony in Musk v. OpenAI.

Sources: [Decrypt](https://decrypt.co/347349/inside-deposition-showed-openai-nearly-destroyed-itself), [WinBuzzer](https://winbuzzer.com/2025/11/03/ilya-sutskever-deposition-reveals-how-sam-altmans-2023-firing-was-planned-for-over-a-year-xcxwbn/) | Confidence: primary testimony plus authoritative secondary sources

---

## 10. Honors and awards

| Year | Award |
|---|---|
| 2015 | MIT Technology Review 35 Innovators Under 35 |
| 2022 | Fellow of the Royal Society (FRS) |
| 2022, 2023, 2024 | NeurIPS Test of Time Award (three consecutive years) |
| 2023, 2024 | Time 100 Most Influential People in AI |
| 2025 | Honorary doctorate from the University of Toronto |
| 2026 | US National Academy of Sciences Award for the Industrial Application of Science |

Sources: [Wikipedia](https://en.wikipedia.org/wiki/Ilya_Sutskever) | Confidence: authoritative secondary source

---

## 11. Key tensions and changes in thinking (without reconciling them)

### Tension 1: Is scale sufficient?
- **2023 position:** “Scaling up the existing neural network paradigm is going to lead to AGI” and “bigger is better.”
- **2025 position:** “The scaling era is over,” “current methods will stall,” and “we need something we don't yet know how to build.”
- **Nature:** The change reflects a genuine intellectual shift rather than a contradiction. In two years, he went from a leading believer in scaling to one of the first to announce its limits.

### Tension 2: AI consciousness
- **2022:** Tweeted that large neural networks might be slightly conscious.
- He has never published a paper or detailed argument in support of the position.
- The scientific community raised substantial objections, including LeCun.
- **Nature:** A claim based on intuition without sufficient argument, which he has never withdrawn.

### Tension 3: Altman's removal
- **2023-11-17:** Participated in the removal and wrote a 52-page memo containing allegations.
- **2023-11-20:** Publicly said he “deeply regret” his participation, as quoted in the notes.
- **Acknowledged in testimony:** The memo process was rushed, and the information was not independently verified.
- **Nature:** There is a genuine tension between the action and his subsequent statement.

---

## 12. Source summary and confidence ratings

### Primary sources (Sutskever's direct work)
- Academic papers, including AlexNet, Seq2Seq, and the GPT series.
- Two Dwarkesh Podcast interviews (March 2023 and November 2025).
- NeurIPS 2024 talk.
- NVIDIA GTC 2023 conversation.
- MIT Technology Review 2023 interview.
- Simons Institute 2023 talk.
- February 2022 tweet about consciousness.
- SSI founding statement.
- Musk v. OpenAI testimony.

### Authoritative secondary sources
- Wikipedia entry.
- [Antoine Buteau's compilation](https://www.antoinebuteau.com/lessons-from-ilya-sutskever/)
- [EA Forum analysis](https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/)
- [The Zvi analysis](https://thezvi.substack.com/p/on-dwarkesh-patels-second-interview)
- [Decrypt deposition coverage](https://decrypt.co/347349/)

### Reading-list reconstruction sources
- [GitHub: dzyim version](https://github.com/dzyim/ilya-sutskever-recommended-reading)
- [GitHub: Justmalhar version](https://github.com/Justmalhar/ilya-sutskever-reading-list)
- [mattprd.com](https://www.mattprd.com/p/openai-cofounder-27-papers-read-know-90-ai)
- [Turing Post](https://www.turingpost.com/p/ilya-sutskever-reading-list)
- Note that the original email has never been published. All versions are community reconstructions.

---

*Research complete. The notes covered nine primary sources and five authoritative secondary sources. They identified one major change in thinking (scale), one unsupported assertion (AI consciousness), and one inconsistency between action and statement (the Altman episode).*
