# Ilya Sutskever — Research on conversations, podcasts, and in-depth interviews

> Research date: 2026-04-05
> Research goal: Collect firsthand records of Ilya Sutskever's conversations and identify his thinking patterns, expression, and handling of uncertainty.

---

## List of primary sources

| # | Source | Date | Type | Importance |
|---|------|------|------|----------|
| 1 | Lex Fridman Podcast #94 | 2020-05 | Podcast (1.5h) | ⭐⭐⭐ |
| 2 | NVIDIA GTC — Jensen Huang Fireside Chat | 2023-03-23 | Conference conversation | ⭐⭐⭐⭐ |
| 3 | Dwarkesh Patel Podcast #1 — Building AGI | 2023-03-27 | Podcast (1h) | ⭐⭐⭐⭐ |
| 4 | Scale AI TransformX — What's Next for AI | 2023 | Conference talk | ⭐⭐⭐ |
| 5 | TED AI — The Exciting, Perilous Journey Toward AGI | 2023-10-17 | TED talk | ⭐⭐⭐⭐ |
| 6 | MIT Technology Review exclusive interview | 2023-10-26 | In-depth interview | ⭐⭐⭐⭐ |
| 7 | X/Twitter public statement after the board crisis | 2023-11-20 | Social media | ⭐⭐⭐⭐⭐ |
| 8 | OpenAI departure statement | 2024-05 | Public statement | ⭐⭐⭐ |
| 9 | SSI founding announcement | 2024-06-19 | Public statement | ⭐⭐⭐⭐ |
| 10 | NeurIPS 2024 — Sequence to Sequence: What a Decade | 2024-12 | Academic talk | ⭐⭐⭐⭐⭐ |
| 11 | Musk v. OpenAI sworn testimony in the lawsuit | 2025-10-01 | Legal testimony (10h) | ⭐⭐⭐⭐⭐ |
| 12 | Dwarkesh Patel Podcast #2 — Age of Research | 2025-11-25 | Podcast (1.5h) | ⭐⭐⭐⭐⭐ |

---

## 1. Lex Fridman Podcast #94 (2020)

**Source**: https://lexfridman.com/ilya-sutskever/
**Type**: Primary (full podcast recording and transcript)

### Key quotations

**Belief in deep learning**:
> "I think that we are still massively underestimating deep learning."

**Early intuition about scaling**:
> "Let's make a big neural network, let's train it, and it's going to work much better than anything before it, and it will, in fact, continue to get better as I make it larger. And it turns out to be true."

**The nature of neural networks**:
> "The neural network is really about learning. Its entire being is about learning representations."

> "A small neural network is a little dumb. A big neural network is a little smart."

### Discussion topics
- The AlexNet paper and the ImageNet moment
- Recurrent neural networks and backpropagation
- GPT-2 and language models
- Whether neural networks can reason
- How to build AGI

---

## 2. Jensen Huang Fireside Chat — NVIDIA GTC (2023-03)

**Source**: https://blogs.nvidia.com/blog/sutskever-openai-gtc/ / https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s52092/
**Type**: Primary (video and partial transcript)

### Key quotations

**Next-token prediction as understanding the world (the detective novel analogy)**:
> "Say you read a detective novel. It's like a complicated plot, a storyline, different characters, lots of events. Mysteries, like clues, it's unclear. Then, let's say that at the last page of the book, the detective has gathered all the clues, gathered all the people, and saying, Okay, I'm going to reveal the identity of whoever committed the crime. And that person's name is — now predict that word."

Introduction to the analogy:
> "[I will] give an analogy that will hopefully clarify why more accurate prediction of the next word leads to more understanding — real understanding."

**The two stages of training**:
> "What the neural net learns is some representation of the process that produced the text, and that's a projection of the world." (first stage)

> "[The second stage] is where the fine tuning and the reinforcement learning from human teachers...we are teaching it. We are communicating with it. We are communicating to it. What it is that we want it to be." (second stage)

**Reliability as the frontier**:
> "We'll keep seeing systems that astound us with what they can do. The frontier is in reliability, getting to a point where we can trust what it can do, and that if it doesn't know something, it says so."

**Firm belief in scaling (in 2023)**:
> "I had a very strong belief that bigger is better, and a goal at OpenAI was to scale."

**Reasoning ability**:
> "The term is hard to define and the capability may still be on the horizon."

**GPUs and deep learning**:
> "The ImageNet dataset and a convolutional neural network were a great fit for GPUs that made it unbelievably fast to train something unprecedented."

**How much language humans encounter**:
> "Humans hear a billion words in a lifetime."

### Analytical note
This is one of Ilya's best-known public conversations. The detective novel analogy became one of his most widely quoted explanations. The story helps listeners intuitively understand why next-token prediction is more than acting as a “stochastic parrot.” Note that he still firmly believed in scaling in 2023.

---

## 3. Dwarkesh Patel Podcast #1 (2023-03)

**Source**: https://www.dwarkesh.com/p/ilya-sutskever
**Type**: Primary (full podcast and transcript)

### Key quotations

**Whether next-token prediction can surpass humans**:
> "I challenge the claim that next-token prediction cannot surpass human performance."

> "If your base neural net is smart enough, you just ask it — What would a person with great insight do?"

> "Predicting the next token well means that you understand the underlying reality that led to the creation of that token. It's not statistics."

**AGI timeline (explicit hesitation)**:
> "It's hard to give a precise answer and it's definitely going to be a good multi-year window."

> "I hesitate to give you a number."

**Difficulty of alignment**:
> "I would not underestimate the difficulty of alignment of models that are actually smarter than us."

> "It depends on how capable the model is. The more capable the model, the more confident we need to be."

**The current paradigm**:
> "This paradigm is gonna go really, really far and I would not underestimate it."

**Data (his assessment in 2023)**:
> "The data situation is still quite good. There's still lots to go. But at some point the data will run out."

**Partnership with Microsoft**:
> "Microsoft has been a very, very good partner for us. They've really helped take Azure to a point where it's really good for ML."

### Handling uncertainty
Notice how he reacts to the AGI timeline question. “I hesitate to give you a number” is typical: **he recognizes the question's importance while explicitly declining to give a potentially misleading figure.** He engages with the question while avoiding irresponsible precision.

---

## 4. Scale AI TransformX (2023)

**Source**: https://exchange.scale.com/public/videos/whats-next-for-ai-systems-and-language-models-with-ilya-sutskever-of-openai
**Type**: Primary (video and blog summary)

### Key quotations

**Compute efficiency**:
> "We are nowhere close to being as efficient as we can be with our compute."

**The sentiment neuron principle**:
> "If you predict the next character well enough, you will eventually start to discover the semantic properties of the text."

**Ethical responsibility**:
> "People should also work on methods to try to address the problems that exist with the technology, such as bias and desirable outputs."

> "Whenever possible, they should work on reducing real harms."

**Future progress**:
> "Mundane progress we've seen over the past few years will continue."

---

## 5. TED AI Talk (2023-10-17)

**Source**: https://www.ted.com/talks/ilya_sutskever_the_exciting_perilous_journey_toward_agi
**Type**: Primary (video and transcript)

### Key quotations

**Defining the nature of AI**:
> "Artificial intelligence is nothing but digital brains inside large computers."

**AGI's impact**:
> "AGI will have dramatic and incredible impact on every single area of human activity."

> "The day will come when the digital brains will become as good and even better than our biological brains."

**Safety risks**:
> "For every positive application of AGI, there will be a negative application as well."

> "Maybe it will want to go rogue, being that it is an agent."

**Self-awareness (particularly distinctive phrasing)**:
> "I am me and I am experiencing things. That when I look at things, I see them."

**Unprecedented cooperation (the main argument for optimism)**:
> "People will start to act in an unprecedentedly collaborative way out of their own self-interest."

> "Companies that are competitors will share technical information to make their AI safe."

### Analytical note
This TED talk is Ilya's most public address to a general audience. Note how he discusses safety. Rather than claiming that AI will certainly get out of control, he says “maybe it will want to go rogue.” His optimism rests on a particular argument: **cooperation driven by self-interest, rather than moral appeals, will bring about safety.**

---

## 6. MIT Technology Review exclusive interview (2023-10-26)

**Source**: https://www.technologyreview.com/2023/10/26/1082398/exclusive-ilya-sutskever-openais-chief-scientist-on-his-hopes-and-fears-for-the-future-of-ai/
**Type**: Primary (in-depth interview article)
**Note:** The original is paywalled. The following quotations come from several secondary analyses.

### Confirmed key positions

**Consciousness**:
In the interview he suggested that ChatGPT might have a little consciousness “if you squint,” and that some people would choose to merge with machines in the future. This echoes his February 2022 tweet:

> "it may be that today's large neural networks are slightly conscious" (2022-02-09, X/Twitter)

**Certainty about AGI**:
> "At some point we really will have AGI."

**Shift toward safety**:
The interview shows how his fears shifted his life's work from developing capabilities to pursuing safety.

### Reactions to the “slightly conscious” tweet
The tweet sparked considerable controversy:
- Yann LeCun replied directly: "Nope. Not even for true for small values of 'slightly conscious' and large values of 'large neural nets'."
- Melanie Mitchell, Emily Bender and others responded mockingly
- Sutskever gave no evidence or further explanation, exemplifying his style: **put forward a provocative intuition and leave it undefended.**

---

## 7. OpenAI Board Drama — Public statement (2023-11)

**Type**: Primary (X/Twitter post and legal testimony)

### The only public statement (2023-11-20)

> "I deeply regret my participation in the board's actions. I never intended to harm OpenAI. I love everything we've built together and I will do everything I can to reunite the company."

**Source**: https://x.com/ilyasut/status/1726590052392956028

### Musk v. OpenAI sworn testimony (2025-10-01) — detailed disclosures

**Source**: Reporting from multiple outlets (Calcalist/Ctech, Decrypt, The Information)
**Type**: Primary (legal testimony, about ten hours)

**Allegations against Altman in the written memo**:
> "Sam exhibits a consistent pattern of lying, undermining his execs, and pitting his executives against one another."

**His motivation**:
> "I wanted them to become aware of it. But my opinion was that action was appropriate."

**How long he considered removing Altman**:
Asked how long he considered firing Altman, he answered:
> "At least a year."

Asked what he was waiting for:
> "That the majority of the board is not obviously friendly with Sam."

**The unexpected employee reaction**:
> "I had not expected them to cheer, but I had not expected them to feel strongly either way."

**The Anthropic merger proposal (strong opposition)**:
> "I really did not want OpenAI to merge with Anthropic. I just didn't want to."

**Reflections on the board process**:
> "One thing I can say is that the process was rushed. I think it was rushed because the board was inexperienced."

**Reasons for leaving OpenAI**:
> "Ultimately, I had a big new vision. And it felt more suitable for a new company."

Asked further about SSI's research direction, **he declined to provide more detail**.

### Analytical note
This is the most human moment in Ilya's public record. Key points:
1. **He posted one tweet** and ended public comment on the board crisis, an extremely restrained response.
2. His legal testimony revealed far more than any public interview, suggesting that his public silence was deliberate.
3. "I had not expected them to feel strongly either way" shows that he badly misjudged organizational dynamics.
4. He regretted the execution rather than his judgment of Altman.

---

## 8. SSI founding announcement (2024-06-19)

**Source**: https://ssi.inc / https://x.com/ilyasut/status/1803472978753303014
**Type**: Primary

### Key statements

> "We will pursue safe superintelligence in a straight shot, with one focus, one goal, and one product."

> "SSI is our mission, our name, and our entire product roadmap, because it is our sole focus."

> "We approach safety and capabilities in tandem, as technical problems to be solved through revolutionary engineering and scientific breakthroughs."

> "We plan to advance capabilities as fast as possible while making sure our safety always remains ahead."

> "Our singular focus means no distraction by management overhead or product cycles, and our business model means safety, security, and progress are all insulated from short-term commercial pressures."

### Analytical note
SSI's announcement was highly polished, with every word considered. Its core message **reframes safety and capabilities as one technical problem**, rather than as two opposing constraints. This is Ilya's direct response to OpenAI's tension between safety and commercialization.

---

## 9. NeurIPS 2024 — Sequence to Sequence: What a Decade

**Source**: NeurIPS 2024 Test of Time Award talk (video available on YouTube)
**Type**: Primary
**Background:** Ilya returned to the academic conference to accept the award and give a talk, his first major public appearance after leaving OpenAI.

### Key quotations

**The end of pretraining**:
> "Pre-training as we know it will unquestionably end."

**Data as a finite resource**:
> "While compute is growing through better hardware, better algorithms and larger clusters, the data is not growing because we have but one internet."

**Data as fossil fuel (important analogy)**:
> "You could even go as far as to say that data is the fossil fuel of AI. It was created somehow, and now we use it, and we've achieved peak data — and there'll be no more. So we have to deal with the data that we have."

**Superintelligence, in characteristic Ilya phrasing**:
> "This is obviously what's being built here."

Characteristics of superintelligence:
> "Agentic, reasons, understands and is self-aware."

**Timing and method (a particularly characteristic line)**:
> "I'm not saying how... and I'm not saying when. I'm saying that it will."

### Analytical note
This talk distills Ilya's core thinking traits:
1. **Comparing peak data to fossil fuel:** He explains technical trends with familiar ideas.
2. **"I'm not saying how, I'm not saying when, I'm saying that it will"** — This is his signature approach to uncertainty: **strong certainty about the direction, openness about the route.**
3. This was when he publicly changed course, moving from belief in scaling in 2023 to declaring the end of the pretraining era in 2024.

---

## 10. Dwarkesh Patel Podcast #2 (2025-11-25)

**Source**: https://www.dwarkesh.com/p/ilya-sutskever-2
**Type**: Primary (full podcast and transcript)
**Importance**: Highest. This is Ilya's most in-depth public conversation since leaving OpenAI.

### Key quotations

**The stages of AI development**:
> "2012 to 2020 was an age of research, 2020 to 2025 was an age of scaling, and 2026 onward will be another age of research."

**Limits to scaling (change of position)**:
> "I don't think that's true at all." (asked whether another 100-fold increase would transform AI)

He later clarified on X:
> "Scaling the current thing will keep leading to improvements. In particular, it won't stall. But something important will continue to be missing."

**The finite supply of data**:
> "The data is very clearly finite."

> "We're back to the age of research again, just with big computers."

**Fundamental criticism of generalization**:
> "These models somehow just generalize dramatically worse than people. It's a very fundamental thing."

> "The thing which I think is the most fundamental is that these models somehow just generalize dramatically worse than people."

**The gap between benchmarks and reality**:
> "How can the model, on the one hand, do these amazing things, and then on the other hand, repeat itself twice?"

> "This disconnect between eval performance and actual real-world performance, which is something that we don't today even understand."

**RL efficiency**:
> "RL provides a relatively small amount of learning for the compute it uses."

**SSI's direction**:
> "We are squarely an 'age of research' company."

> "The main thing that distinguishes SSI is its technical approach."

> "Right now, we just focus on the research, and then the answer to that question will reveal itself."

**The state of the AI industry**:
> "There are more companies than ideas by quite a bit."

**Research taste (highly distinctive)**:
> "There's no room for ugliness."

> "It's beauty, simplicity, elegance, correct biological inspiration. All of those things need to be present at the same time."

**Safety and superintelligence**:
> "What is the concern of superintelligence? If you imagine a system that is sufficiently powerful...we might not like the results."

> "It should be something like...care for sentient life, care for people, democratic, one of those, some combination thereof."

**AGI timeline**:
> "I think like 5 to 20." (years, when asked when human-level learning systems might appear)

**The missing principle, which he declines to discuss**:
> "There is a machine learning principle that I have opinions on. But unfortunately, circumstances make it hard to discuss in detail."

> "You know, that is a great question to ask, and it's a question I have a lot of opinions on. But unfortunately, we live in a world where not all machine learning ideas are discussed freely, and this is one of them."

**Emotion and value functions**:
He sees emotions as analogous to value functions, mechanisms that signal success and failure.

**The source of human generalization**:
He speculates that “neurons use more compute than we think,” so the computational complexity of biological neurons may be underestimated.

### Observers' comments
Outside observers noted: “the negative space in his answers — the things he refused to say — paints a clear picture of where he thinks the industry is wrong, and what SSI is likely building.”

### Analytical note
This is the most important single source for understanding Ilya. Key findings:

**Change in position**:
- 2023: "This paradigm is gonna go really, really far"
- 2025: "I don't think that's true at all" (on whether scaling 100-fold would transform AI)
- He does not reject scaling, but says that “something important will continue to be missing.”

**Pattern of declining to answer**:
He declines to discuss precisely what he considers most important. “Unfortunately, circumstances make it hard to discuss in detail” is his standard refusal. The implication is that he knows but cannot say.

**Research aesthetics**:
“There's no room for ugliness” is one of his most distinctive expressions. He treats scientific research as an aesthetic pursuit. Good research needs to be both correct and elegant.

---

## 11. Other important quotations by topic

### World models in neural networks
> "When we train a large neural network to accurately predict the next word in lots of different texts from the Internet, what we are doing is that we are learning a world model." (GTC 2023)

> "These models are not just memorizing the internet... a model that just memorized the internet would be useless."

> "My perspective has been for a long time that everything is a neural net. The brain is a neural net. The mind is a neural net."

### Certainty about AGI
> "It is abundantly clear that just scaling up the existing neural network paradigm is going to lead to AGI." (note: his position in 2023)

> "AGI, if it's created, will be the most impactful technology ever invented in human history."

> "It's hard to communicate the visceral sense of what's coming."

> "It is important to appreciate that AGI is not just another piece of technology... it's a thing that can think."

> "There is a non-trivial chance that AGI will be achieved in the next 10 years."

### Safety
> "Superintelligence is a technology that could end human history. We should treat it with the seriousness it deserves."

> "If you build a very powerful AI, you need to be sure it will do what you want it to do."

> "It's not enough to say 'let's not build it.' Someone will build it. We need to figure out how to build it safely."

> "The problem is that a superintelligence, by its very nature, will be very good at achieving its goals."

### Discovery and research
> "When you get a glimmer of a really big discovery, you should follow it. Don't be afraid to be obsessed."

> "The most important discoveries are often the ones that seem obvious in retrospect."

> "Simplicity is a sign of truth. If your theory is very complicated, it's probably wrong."

> "The ideas are out there, floating in idea-space, and we just need to discover them."

> "You need to have a very deep belief that what you are doing is important."

> "It is important to have a taste for what is a good research direction."

### Hinton
> "Thanks to working with Geoff, I had the opportunity to work on some of the most important scientific problems of our time and pursue ideas that were both highly unappreciated by most scientists, yet turned out to be utterly correct."

---

## 12. Communication style analysis

### How he expresses uncertainty
| Pattern | Example | Meaning |
|------|------|------|
| Reluctance to give a number | "I hesitate to give you a number" | The question matters, but a figure may mislead. |
| Direction settled, route open | "I'm not saying how, I'm not saying when. I'm saying that it will." | He trusts his intuition about the destination and remains candid about uncertainty over the route. |
| Explicit uncertainty | "I'm actually not sure if my statement about Intel is correct" | Willing to acknowledge an unreliable recollection on the spot. |
| Probabilistic wording | "maybe I believed them only 50% on the inside" | Quantifies his past confidence in hindsight. |
| Explicit hedge | "I'll hedge a little bit" | Explicitly flags the qualification. |

### How he declines questions
| Pattern | Example | Analysis |
|------|------|------|
| Confidentiality for competitive reasons | "Unfortunately, circumstances make it hard to discuss in detail" | Standard formula: acknowledges an answer, but declines on competitive grounds. |
| Acknowledges without answering | "That is a great question to ask, and it's a question I have a lot of opinions on. But..." | Affirms the value of the question before declining. |
| Silence | Posted just one tweet after the board crisis | Most extreme refusal: avoids public discussion entirely. |

### Cadence
Observers say:
- "He doesn't give a lot of interviews"
- "He is deliberate and methodical when he talks"
- "Long pauses when he thinks about what he wants to say and how to say it"
- He pauses noticeably to think before responding and does not pad the silence.

### Analogies and explanations
| Analogy | Topic | Source |
|------|------|------|
| Detective novel | Next-token prediction = understanding the world | GTC 2023 |
| Fossil fuel | Data are finite | NeurIPS 2024 |
| Digital brains | The nature of AI | TED 2023 |
| Value functions | The function of emotion | Dwarkesh 2025 |

### Key moments when his position changed

| Date | Position | Quotation |
|------|------|------|
| 2023-03 | Scaling will go very far | "This paradigm is gonna go really, really far" |
| 2023-03 | Data remain sufficient | "The data situation is still quite good" |
| 2024-12 | Pretraining will end | "Pre-training as we know it will unquestionably end" |
| 2024-12 | Peak data has been reached | "We've achieved peak data — and there'll be no more" |
| 2025-11 | A 100-fold increase is not enough | "I don't think that's true at all" |
| 2025-11 | Return to the age of research | "We're back to the age of research again, just with big computers" |
| 2025-11 | LLM generalization is fundamentally inadequate | "These models somehow just generalize dramatically worse than people" |

---

## 13. Secondary source index

The following analyses help explain Ilya's thinking and are secondary sources:

| Source | URL | Value |
|------|-----|------|
| Zvi Mowshowitz analysis | https://thezvi.substack.com/p/on-dwarkesh-patels-second-interview | Point-by-point critical analysis of Dwarkesh #2 |
| EA Forum summary | https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/ | Structured summary of Dwarkesh #2 |
| The Neuron breakdown | https://www.theneuron.ai/explainer-articles/unpacking-dwarkeshs-ilya-sutskever-interview-on-agi-asi-and-how-to-build-both-safely | Inferences about SSI's strategy |
| AI Disruption Pub | https://aidisruptionpub.com/p/ilya-predicting-the-next-token-is | In-depth interpretation of the GTC detective novel analogy |
| LessWrong discussion | https://www.lesswrong.com/posts/bMvCNtSH8DiGDTvXd/ | Community discussion of Dwarkesh #2 |
| Antoine Buteau | https://www.antoinebuteau.com/lessons-from-ilya-sutskever/ | Quotation compilation |
| LifeArchitect.ai | https://lifearchitect.ai/ilya/ | Quotation and timeline compilation |
| The Neuron (Memo) | https://www.theneuron.ai/explainer-articles/ilya-sutskevers-secret-memo-and-the-plot-to-merge-openai-with-anthropic | Detailed coverage of the 52-page memo |

---

## 14. Sources to add or still outstanding

- [ ] Full October 2023 MIT Technology Review article (paywalled)
- [ ] Full transcript of the NeurIPS 2024 video
- [ ] Original Musk v. OpenAI testimony (court filing)
- [ ] Full transcript of Lex Fridman Podcast #94 (available at happyscribe.com)
- [ ] Ilya's talk at the 2018 AI Frontiers Conference
- [ ] Early views on deep learning from 2015 (compiled by Nathan Lambert at interconnects.ai)
- [ ] Any public conversation or panel with Hinton
