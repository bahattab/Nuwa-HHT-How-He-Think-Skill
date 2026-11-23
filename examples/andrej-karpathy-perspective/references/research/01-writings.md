# Andrej Karpathy: Research on writings and core arguments

> Research date: 2026-04-05
> Evidence labels: primary = quoted directly from his text or video, secondary = reported or summarized by others, inference = inferred from several contexts.
> Excluded throughout: Zhihu, WeChat official accounts, and Baidu Baike.

---

## 1. Background and career

**Birth.** October 23, 1986, in Bratislava, Slovakia. Moved with his family to Toronto, Canada, aged 15.
**Education**
- University of Toronto: double degree in computer science and physics, 2005–2009.
- University of British Columbia: master's degree in machine learning, 2009.
- Stanford University: doctorate, advised by Fei-Fei Li, completed in 2015 with the dissertation *Connecting Images and Natural Language*.

**Career milestones**
- 2015: Created CS231n, Stanford's first deep learning course, which grew from 150 to 750 students.
- 2015–2017: OpenAI founding team member and research scientist.
- 2017–2022: Tesla AI director, reporting to Elon Musk and leading Autopilot.
- July 2022: Left Tesla.
- February 2023: Returned to OpenAI.
- February 2024: Left OpenAI.
- July 2024: Founded Eureka Labs, an AI-native education company.
- February 2026: Released microgpt, which trains GPT in 200 lines of pure Python with no dependencies.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy) (primary information from his official site, karpathy.ai).

---

## 2. Full list of blog posts (karpathy.github.io)

| Date | Title | URL | Significance |
|------|------|-----|--------|
| 2026-02-12 | microgpt | karpathy.github.io/2026/02/12/microgpt/ | ⭐⭐⭐⭐⭐ Latest major work |
| 2022-03-14 | Deep Neural Nets: 33 years ago and 33 years from now | karpathy.github.io/2022/03/14/lecun1989/ | ⭐⭐⭐⭐ |
| 2021-06-21 | A from-scratch tour of Bitcoin in Python | karpathy.github.io/2021/06/21/blockchain/ | ⭐⭐⭐ |
| 2021-03-27 | Short Story on AI: Forward Pass | karpathy.github.io/2021/03/27/forward-pass/ | ⭐⭐ |
| 2020-06-11 | Biohacking Lite | karpathy.github.io/2020/06/11/biohacking-lite/ | ⭐ |
| 2019-04-25 | A Recipe for Training Neural Networks | karpathy.github.io/2019/04/25/recipe/ | ⭐⭐⭐⭐⭐ Essential practical guide |
| 2018-01-20 | (started posting on Medium instead) | — | Turning point |
| 2016-09-07 | A Survival Guide to a PhD | karpathy.github.io/2016/09/07/phd/ | ⭐⭐⭐⭐ |
| 2016-05-31 | Deep Reinforcement Learning: Pong from Pixels | karpathy.github.io/2016/05/31/rl/ | ⭐⭐⭐ |
| 2015-11-14 | Short Story on AI: A Cognitive Discontinuity | karpathy.github.io/2015/11/14/ai/ | ⭐⭐ |
| 2015-10-25 | What a Deep Neural Network thinks about your #selfie | karpathy.github.io/2015/10/25/selfie/ | ⭐⭐ |
| 2015-05-21 | The Unreasonable Effectiveness of Recurrent Neural Networks | karpathy.github.io/2015/05/21/rnn-effectiveness/ | ⭐⭐⭐⭐⭐ Classic work |
| 2015-03-30 | Breaking Linear Classifiers on ImageNet | karpathy.github.io/2015/03/30/breaking-convnets/ | ⭐⭐ |
| 2014-09-02 | What I learned from competing against a ConvNet on ImageNet | karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/ | ⭐⭐⭐ |
| 2014-08-03 | Quantifying Productivity | karpathy.github.io/2014/08/03/quantifying-productivity/ | ⭐ |
| 2014-07-03 | Feature Learning Escapades | karpathy.github.io/2014/07/03/feature-learning-escapades/ | ⭐⭐ |
| 2012-10-22 | The state of Computer Vision and AI: we are really, really far away | karpathy.github.io/2012/10/22/state-of-computer-vision/ | ⭐⭐⭐ |
| 2011-04-27 | Lessons learned from manually classifying CIFAR-10 | karpathy.github.io/2011/04/27/manually-classifying-cifar10/ | ⭐⭐ |

**Medium blog:** https://karpathy.medium.com/
Key article:
- [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) (2017, his most widely cited article).

Source: Direct retrieval from the blog index (primary).

---

## 3. In-depth analysis of key posts

### 3.1 Software 2.0（2017，Medium）
**Source:** https://karpathy.medium.com/software-2-0-a64152b37c35 (primary).

**Core argument**
> “Software 1.0 is the set of instructions humans handwrite in languages such as Python and C++. Software 2.0 is neural network weights, a program produced from data by an optimization algorithm.”

**Comparison of Software 1.0 and 2.0**
- SW1.0: The programmer identifies points in the problem space where particular behaviors are desired and handwrites explicit rules.
- SW2.0: Given input–output pairs, the optimizer searches the program space for the best program, represented by network weights.

**SW2.0 advantages described by Karpathy**
1. Computational uniformity: All operations are matrix multiplications, well suited to hardware acceleration.
2. It can learn knowledge humans cannot state explicitly.
3. Performance improves as data and compute grow, with predictable scaling effects.

**SW2.0 drawbacks and risks acknowledged by Karpathy**
- Results are hard to explain.
- It can fail silently.
- It may encode biases in the data.

**Areas SW2.0 will consume:** Visual recognition, speech processing, image translation, image captioning, game AI, and database queries.

**Tesla case.** As Autopilot evolved, C++ code was progressively deleted and replaced with neural network weights. This is a concrete example of SW2.0 “eating” SW1.0.

---

### 3.2 The Unreasonable Effectiveness of RNNs（2015）
**Source:** karpathy.github.io/2015/05/21/rnn-effectiveness/ (primary).

**Core argument**
> “If ordinary neural network training is optimization in function space, recurrent network training is optimization in program space.”

**Key experiments demonstrating RNN generation**
- Paul Graham essays: Generated structured writing offering startup advice.
- Shakespeare: Learned dialogue structure, speaker names, and complex syntax.
- Wikipedia markdown: Discovered the format of wiki links automatically.
- LaTeX mathematics: Generated mathematical proofs that nearly compiled.
- Linux kernel C code: Generated functions with properly nested parentheses and variable declarations.

**Technical finding.** About 5% of RNN neurons spontaneously learned interpretable algorithms, such as detecting quotation marks or URL boundaries and counting parentheses, without explicit instruction.

---

### 3.3 A Recipe for Training Neural Networks（2019）
**Source:** karpathy.github.io/2019/04/25/recipe/ (primary).

**Two central observations**
1. Neural network training is a “leaky abstraction.” It requires deep understanding and cannot simply be plugged in.
2. Failure is silent. The network can train and perform poorly without an obvious error.

**Six stages**

**Stage 1: Become one with the data**
- Spend a few hours inspecting thousands of samples.
- Understand distributions, patterns, imbalance, and annotation noise.

**Stage 2: End-to-end skeleton and baseline**
- Fix the random seed.
- Disable data augmentation.
- Verify that the loss at initialization is as expected.
- Establish a human baseline.
- Verify architectural feasibility by overfitting one batch.

**Stage 3: Overfit**
- “Don't be a hero.” Copy a proven architecture rather than inventing one.
- Adam + lr=3e-4 provides the most forgiving starting point.

**Stage 4: Regularization, ordered by effectiveness**
1. Obtain more real data (most effective).
2. Data augmentation.
3. Pretraining.
4. Dropout (spatial dropout for ConvNets).
5. weight decay、early stopping

**Stage 5: Tune hyperparameters**
- Prefer random search to grid search. It better captures differences in sensitivity among parameters.

**Stage 6: Squeeze out the last gains**
- Ensembling (a guaranteed improvement of about 2%).
- Train longer than intuition suggests.

**Overarching principle**
> “Fast and furious training does not work. Success correlates positively with patience and attention to detail.”

---

### 3.4 Deep Neural Nets: 33 years ago and 33 years from now（2022）
**Source:** karpathy.github.io/2022/03/14/lecun1989/ (primary).

**Core argument.** Deep learning has changed little at a high level over 33 years. It remains end-to-end optimization of differentiable neural networks using backpropagation. What changed was scale.

**Comparison by orders of magnitude**
- Parameter count: about 1,000,000 times higher.
- Amount of pixel data processed: about 100,000,000 times greater.
- Training speed: 3,000 times faster on consumer hardware, with another 100-fold increase possible on GPUs.

**Sources of improved performance**
- Modern optimization techniques (Adam, dropout, and data augmentation): about a 60% reduction in error.
- Larger datasets: a moderate contribution.
- Scale: requires more compute.

**Prediction for 2055**
> Practitioners will no longer train models from scratch. They will communicate in natural language with giant foundation models, telling a “10,000,000-times-larger neural-network superbrain” what to do.

---

### 3.5 microgpt (February 2026)
**Source:** karpathy.github.io/2026/02/12/microgpt/ and GitHub Gist (primary).

**Core claim.** Implement complete GPT training and inference in 200 lines of pure Python, with zero dependencies, no PyTorch or NumPy, and no GPU acceleration. This culminates his “decade-long obsession with simplifying LLMs to their most fundamental components.”

**Includes:** A document dataset, tokenizer, automatic differentiation engine, GPT-2-like architecture, Adam optimizer, training loop, and inference loop.

**Expression of belief**
> "Everything else is just efficiency."

This is the latest demonstration of his principle: "If I can't build it, I don't understand it".

---

## 4. YouTube teaching series

### Zero to Hero (Neural Networks: Zero to Hero)
**Home page:** https://karpathy.ai/zero-to-hero.html (primary).
**GitHub repository:** https://github.com/karpathy/nn-zero-to-hero
**Start date:** August 2022.
**Approach.** Language models are the best entry point to deep learning. The knowledge transfers even when one's goal is computer vision.

| # | Title | Duration | Core content |
|---|------|------|---------|
| 1 | The Spelled-Out Intro to Neural Networks and Backpropagation: Building Micrograd | 2h25m | Implement backpropagation from scratch with only high-school calculus. |
| 2 | The Spelled-Out Intro to Language Modeling: Building Makemore | 1h57m | Character-level bigram language model and introduction to PyTorch. |
| 3 | Building Makemore Part 2: MLP | 1h15m | Multilayer perceptrons and overfitting and underfitting. |
| 4 | Building Makemore Part 3: Activations & Gradients, BatchNorm | 1h55m | Gradient-flow analysis and batch normalization. |
| 5 | Building Makemore Part 4: Becoming a Backprop Ninja | 1h56m | Manual backpropagation without autograd. |
| 6 | Building Makemore Part 5: Building a WaveNet | 56m | Hierarchical convolutional network architecture. |
| 7 | Let's Build GPT: From Scratch, in Code, Spelled Out | 1h56m | Build GPT from scratch, following "Attention is All You Need". |
| 8 | Let's Build the GPT Tokenizer | 2h13m | Implement BPE tokenization from scratch and examine its effect on LLM behavior. |

### Other important videos
- **[1hr Talk] Intro to Large Language Models** (November 2023): For a general audience. Covers LLM training, the LLM OS analogy, and safety (jailbreaks and prompt injection).
- **Deep Dive into LLMs like ChatGPT** (February 2025, 3h31m): In-depth analysis of the full training stack and development of mental models.
- **Let's reproduce GPT-2**: Reproduce GPT-2 from scratch.

---

## 5. Academic papers by citation count and significance

Source: dblp.org and Google Scholar entries (secondary, with citation counts approximate at the time of searching).

| Year | Title | Venue | Co-authors | Core contribution |
|------|------|---------|--------|---------|
| 2017 | Deep Visual-Semantic Alignments for Generating Image Descriptions | IEEE TPAMI | Li Fei-Fei | Multimodal alignment from images to natural-language descriptions |
| 2016 | **DenseCap**: Fully Convolutional Localization Networks for Dense Captioning | CVPR | Justin Johnson, Li Fei-Fei | Dense image captioning |
| 2016 | Connecting Images and Natural Language (doctoral thesis) | Stanford | — | Summary of doctoral research |
| 2017 | PixelCNN++: Improving the PixelCNN with Discretized Logistic Mixture | ICLR | Tim Salimans et al. | Improvement to generative models |
| 2017 | World of Bits: An Open-Domain Platform for Web-Based Agents | ICML | Tianlin Shi et al. | Web-agent benchmark (early agent research) |
| 2015 | ImageNet Large Scale Visual Recognition Challenge | IJCV | Russakovsky, Deng, Fei-Fei et al. | Definition of the ImageNet benchmark |
| 2015 | Visualizing and Understanding Recurrent Networks | CoRR | Justin Johnson, Li Fei-Fei | RNN visualization and explanation |
| 2015 | Deep visual-semantic alignments for generating image descriptions | CVPR | Li Fei-Fei | Early version of image captioning |
| 2014 | Grounded Compositional Semantics for Finding and Describing Images | TACL | Socher, Le, Manning, Ng | Compositional semantics of images and text |
| 2014 | Large-Scale Video Classification with ConvNets | CVPR | Toderici, Li Fei-Fei et al. | Video understanding |
| 2014 | Deep Fragment Embeddings for Bidirectional Image Sentence Mapping | NIPS | Joulin, Li Fei-Fei | Bidirectional image–text embeddings |

**Note correcting a common misattribution.** Simonyan and Zisserman wrote VGGNet (*Very Deep ConvNets for Large-Scale Image Recognition*). Karpathy contributed to the ImageNet challenge paper.

**CS231n.** Founded in 2015 as Stanford's first deep learning course. The videos are freely available online and have more than 800,000 views in total, according to TIME.

---

## 6. The complete Software 1.0 / 2.0 / 3.0 framework

**Sources:** The 2017 Medium article and the 2025 YC AI Startup School talk, both primary.

Karpathy extended the framework to three generations in his 2025 YC AI Startup School talk.

| Generation | Definition | Programming method | Representative platform |
|------|------|---------|---------|
| Software 1.0 | Explicit instructions written by humans in conventional languages | Programmers write code | GitHub |
| Software 2.0 | Neural network weights produced from data by an optimizer | Adjust the dataset and run the optimizer | Hugging Face |
| Software 3.0 | LLMs programmed using natural-language prompts | Write prompts in English | — |

Key claim:
> "Prompts are now programs that program the LLM."
> "Software 3.0 is eating 1.0/2.0." 
> "A huge amount of software will be rewritten."

**Evidence from Tesla.** As Autopilot evolved, neural networks kept expanding and C++ code kept being removed. This is a real case of SW2.0 eating SW1.0.

---

## 7. The LLM OS concept

**Sources**
- X post, September 2023 (primary): https://x.com/karpathy/status/1707437820045062561
- X post, November 2023 (primary): https://x.com/karpathy/status/1723140519554105733
- 1hr Talk Intro to LLMs (November 2023 video, primary).

**Core analogy.** The LLM is the kernel process of a new operating system, beyond just a chatbot.

| Conventional OS | LLM OS |
|--------|--------|
| CPU | LLM (processor) |
| RAM | Context window (working memory) |
| File system | Embedding database (vector retrieval) |
| System calls | Tool and API calls |
| Long-running programs | Agents |
| I/O devices | Multimodal input and output (vision, audio) |

---

## 8. Key terms and coined concepts

### 8.1 Vibe Coding (February 2025)
**Source:** https://x.com/karpathy/status/1886192184808149383 (primary).

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."

**Background.** The February 6, 2025 post mentions using Cursor Composer, Sonnet, and SuperWhisper to code with voice commands.

**Impact.** The post reportedly drew 4.5 million views. Merriam-Webster listed the term under slang and trending words in March 2025. The Collins English Dictionary named it its 2025 word of the year.

### 8.2 Jagged Intelligence
**Sources:** https://x.com/karpathy/status/1882518317585650084 and 2025 LLM Year in Review (both primary).

> "LLMs exhibit amusingly jagged performance characteristics: simultaneously a genius polymath and a confused and cognitively challenged grade schooler, seconds away from getting tricked by a jailbreak."

This is a structural consequence of optimization through RLVR rather than a training defect. Capabilities rise sharply in the particular domains covered by RLVR, producing an uneven capability landscape.

### 8.3 LLMs as "Summoned Ghosts"
**Source:** 2025 LLM Year in Review (primary).

> "LLMs are not evolved animals but summoned ghosts—entities optimized under entirely different constraints than biological intelligence."

The argument is that LLMs differ fundamentally from biological intelligence in their neural architectures, training data, training algorithms, and optimization pressures. Understand them as a “new kind of entity in the space of intelligence,” instead of through animal evolution.

### 8.4 LLMs and "Anterograde Amnesia"
**Source:** 2025 YC AI Startup School talk (primary).

The comparison is to the protagonist of *Memento*: the LLM cannot consolidate long-term memories and relies on the context window alone.

---

## 9. The Eureka Labs mission statement

**Source:** https://eurekalabs.ai/ (primary), published July 16, 2024.

**Mission:** Build a new kind of AI-native school.

**Core belief**
> "Subject matter experts who are deeply passionate, great at teaching, infinitely patient and fluent in all languages are very scarce and cannot personally tutor all 8 billion people on demand."

**Solution.** Teachers and AI teaching assistants work together. Teachers design courses, and AI assistants are optimized to guide students through them, supporting, amplifying, and extending the reach of the teachers' work.

**Vision**
> "If we are successful, it will be easy for anyone to learn anything, expanding education in both reach (a large number of people learning something) and extent (any one person learning a large amount of subjects, beyond what may be possible today unassisted)."

**First product:** LLM101n: Let's Build A Storyteller, an undergraduate-level course in which students train their own AI.

---

## 10. Learning philosophy

Sources: Twitter/X posts and the Stanford advice page (primary).

### Core tenet 1: Learning should not be fun
> "Learning is not supposed to be fun. It doesn't have to be actively not fun either, but the primary feeling should be that of effort."

### Core tenet 2: Resist the "shortification of learning"
**Source:** https://x.com/karpathy/status/1756380066580455557 (primary, February 2024).

> "There are a lot of videos on YouTube/TikTok etc. that give the appearance of education, but if you look closely they are really just entertainment."

Prescription: Close the tabs with quick blog posts and "seek the meal": textbooks, documentation, papers, manuals, and long articles. Set aside four hours to read, take notes, reread, restate, process, and work with the material.

### Core tenet 3: Build to understand
> "If I can't build it, I don't understand it."

This tenet runs through micrograd, makemore, nanoGPT, and microgpt. Each shows real understanding by building from scratch.

### Core tenet 4: Read primary sources
His recommended LLM reading list includes primary papers such as Attention is All You Need, GPT-2, and InstructGPT, in preference to secondary interpretations.

---

## 11. Key views from the Dwarkesh Patel podcast

**Source:** https://www.dwarkesh.com/p/andrej-karpathy (secondary summary, with the original podcast as the primary source).

**AGI timeline.** Still 10 years away. The problems are solvable but difficult.

**Critique of reinforcement learning (a counterintuitive view)**
> "Reinforcement learning is terrible."

The argument is that outcome rewards are “sucking supervision through a straw.” They compress rich trajectory information into a single reward signal and propagate noise through learning. Humans learn mainly through reflection, synthetic data generation (thinking), and distillation during sleep, rather than primarily by RL.

**Model collapse.** Synthetic data generation can fail because models produce a collapsed distribution, and repeated self-sampling dangerously narrows diversity. Training on model-generated content reduces performance. Maintaining entropy requires an external source, such as human interaction or varied experience.

**Cognitive Core vision.** Future systems will separate knowledge and cognition. A cognitive core of about one billion parameters would discard encyclopedic memory and retain reasoning algorithms, retrieving knowledge when needed as humans do.

**Continuity of computing.** Karpathy rejects a sharp split between AI and ordinary computer science. Progress is evolutionary: “We are abstracting ourselves very, very slowly,” as when compilers took over from assembly. AGI may emerge through continuous improvement rather than an abrupt leap.

---

## 12. Recurrent core arguments (beliefs expressed at least three times)

The following core positions recur across settings and are ordered by number of confirmations.

### Argument 1: Building from scratch is the only route to understanding ★★★★★
**Occurrences:** micrograd (video and code), the makemore series, nanoGPT, the microgpt blog post, the LLM101n course design philosophy, and PhD advice.
**Characteristic wording**
> "If I can't build it, I don't understand it."

### Argument 2: Neural network training can fail silently and requires great care and visualization ★★★★★
**Occurrences:** Recipe for Training NNs (2019), Zero to Hero, and CS231n material.
**Characteristic wording**
> "Neural net training is a leaky abstraction." 
> "A 'fast and furious' approach does not work."

### Argument 3: Software is undergoing a fundamental paradigm shift (SW1.0 → 2.0 → 3.0) ★★★★★
**Occurrences:** Software 2.0 (2017), 1hr Intro to LLMs (2023), YC Startup School (2025), and several X posts.
**Characteristic wording**
> "Software 2.0 will eat through Software 1.0."
> "A huge amount of software will be rewritten."

### Argument 4: LLMs are a new computing infrastructure, beyond a mere tool ★★★★
**Occurrences:** The LLM OS post (2023), 1hr Talk (2023), the YC talk (2025), and 2025 LLM Year in Review.
**Characteristic wording:** The LLM is the operating-system kernel, the context window is RAM, and there is the *Memento* analogy.

### Argument 5: LLMs are an entirely new kind of entity that biological or human frameworks cannot explain ★★★★
**Occurrences:** 2025 LLM Year in Review, several "summoned ghosts" posts, and the short-story article.
**Characteristic wording**
> "LLMs are not evolved animals but summoned ghosts."
> "Jagged Intelligence" 

### Argument 6: AI education should be democratized, giving everyone access to the best material ★★★★
**Occurrences:** Free access to CS231n, the free Zero to Hero series, the Eureka Labs mission statement, and open-sourcing LLM101n.
**Characteristic wording**
> "If we are successful, it will be easy for anyone to learn anything."

### Argument 7: The essence of deep learning has not changed in 33 years, while the scale has ★★★
**Occurrences:** 33 years ago and 33 years from now (2022), the Lex Fridman podcast, and several interviews.
**Characteristic wording**
> "Not much has changed in 33 years on the macro level."

### Argument 8: Data quality and quantity are the core competitive advantage of SW2.0, ahead of architectural innovation ★★★
**Occurrences:** The Tesla Data Engine description, Recipe for Training NNs (“getting more real data is the most effective regularization”), and Zero to Hero.
**Characteristic wording:** "Get more real data" comes first among regularization methods.

---

## 13. Recommended reading and resources (intellectual influences)

### Essential papers from Karpathy's introductory LLM reading list
Source: The LLM reading list at karpathy.ai (primary).

1. Attention is All You Need (the original Transformer paper).
2. Language Models are Unsupervised Multitask Learners (the GPT-2 paper).
3. Training Language Models to Follow Instructions（InstructGPT）
4. Llama 2: Open Foundation and Fine-Tuned Chat Models
5. RLAIF: Scaling Reinforcement Learning from Human Feedback with AI
6. Training Compute Optimal Language Models（Chinchilla）
7. Sparks of Artificial General Intelligence: Early Experiments with GPT-4

### Recommended learning resources
- CS231n notes, written by Karpathy himself.
- The textbook *Deep Learning* (Goodfellow et al.).
- *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (recommended for beginners).
- Read original papers directly and go beyond secondary explanations.

**Inferred intellectual influences (speculation)**
- Affinity with Feynman's teaching method. “Build from scratch” corresponds to “if you can teach it to someone else, you understand it.”
- Deep knowledge of LeCun's work. The “33 years ago” post directly reproduces LeCun's 1989 paper.
- Personal correspondence with Bahdanau, inventor of the attention mechanism. He published their private email exchange with permission.

---

## 14. Known contradictions and tensions (recorded without reconciliation)

**Tension 1: Criticism of RL and praise for RLVR**
- On the Dwarkesh podcast, he said "Reinforcement learning is terrible" and criticized outcome-based rewards.
- In 2025 LLM Year in Review, he strongly praised RLVR (Reinforcement Learning from Verifiable Rewards) as the most important training paradigm shift of 2025.

One possible distinction is that he criticizes conventional sparse-reward RL, such as policy gradients, while praising RLVR with verifiable rewards. The original does not always distinguish the two clearly.

**Tension 2: Modest forecasts and a bold vision**
- "AGI still a decade away" is a modest 10-year forecast.
- At the same time, he describes an educational revolution where “anyone can learn anything” and a future in which “a lot of software will be rewritten.”

These points can coexist but create tension. His forecasts are relatively conservative, whereas his actions, such as founding Eureka Labs and betting on SW3.0, assume change is imminent.

**Tension 3: Opposition to the "shortification of learning" while making many explanatory videos**
He criticizes YouTube material that feels educational but functions as entertainment, while his Zero to Hero series is itself hosted on YouTube.
A possible distinction is that his videos demand substantial cognitive effort, last more than two hours, and require hands-on work. That makes them “effortful” by his definition.

---

## 15. Source index

| Source | URL | Reliability |
|------|-----|--------|
| Personal blog (karpathy.github.io) | http://karpathy.github.io/ | Primary |
| Medium blog | https://karpathy.medium.com/ | Primary |
| Official personal site | https://karpathy.ai/ | Primary |
| Zero to Hero course page | https://karpathy.ai/zero-to-hero.html | Primary |
| X account | https://x.com/karpathy | Primary |
| Official Eureka Labs site | https://eurekalabs.ai/ | Primary |
| Annual review on bearblog | https://karpathy.bearblog.dev/ | Primary |
| dblp publications list | https://dblp.org/pid/04/9925.html | Primary (bibliographic database) |
| Google Scholar | https://scholar.google.com/citations?user=l8WuQJgAAAAJ | Primary (bibliographic database) |
| Summary of the YC Startup School talk | https://www.latent.space/p/s3 | Secondary (with full transcript) |
| Dwarkesh podcast | https://www.dwarkesh.com/p/andrej-karpathy | Secondary (with complete conversation) |
| Wikipedia biography | https://en.wikipedia.org/wiki/Andrej_Karpathy | Secondary (reliable synthesis) |
| Stanford personal page | https://cs.stanford.edu/people/karpathy/ | Primary |
| Wikipedia entry on vibe coding | https://en.wikipedia.org/wiki/Vibe_coding | Secondary (supplementary confirmation) |
