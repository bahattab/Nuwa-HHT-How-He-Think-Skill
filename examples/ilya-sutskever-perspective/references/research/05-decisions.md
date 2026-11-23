# Ilya Sutskever: Major decisions, turning points, and controversial actions

> Research date: 2026-04-05
> Sources: Wikipedia, TechCrunch, Time, Fortune, Axios, CNBC, Gizmodo, Decrypt, Dwarkesh Patel Podcast, Calcalist, EA Forum, LessWrong, The Neuron, and Israel Hayom
> Excluded sources: Zhihu, Baidu Baike, and WeChat Official Accounts

---

## 1. Academic decision: Studying under Hinton

### Background
Ilya Sutskever was born in Russia, then the Soviet Union, in 1986. He moved to Israel at age five and to Canada at age sixteen. At the University of Toronto, he completed a bachelor's in mathematics (2005), a master's in computer science (2007), and a PhD in computer science (2013).

### Choice
He chose Geoffrey Hinton as his supervisor, backing neural networks at a time when mainstream AI research still kept deep learning on the margins.

### Reasoning
Sutskever had an early intuition about the potential of neural networks. Mainstream researchers then tended toward symbolic AI and statistical methods, and Hinton's connectionist approach was considered a minority position. Choosing Hinton meant backing a direction others doubted.

### Outcome
In 2012 he developed AlexNet with Hinton and Alex Krizhevsky. Its decisive victory in ImageNet is regarded as the start of the deep learning revolution. Hinton later said: "Ilya thought we should do it, Alex made it work, and I got the Nobel prize."

### Key details
- Sutskever believed neural network performance would improve with more data, an early sign of his intuition about scaling.
- The emergence of the large ImageNet dataset happened to validate that intuition.
- This was the intellectual starting point for his later bets on scaling.

**Confidence in the facts: High** (cross-checked against several primary sources).

---

## 2. Joining Google Brain (2012–2015)

### Background
After AlexNet's success, Sutskever spent about two months as a postdoctoral researcher under Andrew Ng at Stanford. He then returned to Toronto to join DNNResearch, founded by Hinton. Google acquired DNNResearch in 2013, and Sutskever joined Google Brain as part of the acquisition.

### Choice
He moved from academia to industry, joining Google Brain.

### Reasoning
Google offered computing power and data resources that academia could not match. The acquisition was a package deal in which Hinton, Krizhevsky, and Sutskever all joined, so it was not entirely an independent personal decision.

### Work at Google
- Developed sequence-to-sequence learning with Oriol Vinyals and Quoc Viet Le, creating a core framework for modern machine translation and language modeling.
- Helped develop TensorFlow in its early stages.
- Participated in the AlphaGo paper as one of the co-authors.

### Outcome
His Google work, particularly his experience with sequence-to-sequence learning, provided the technical foundation for advancing the GPT series at OpenAI.

**Confidence in the facts: High**.

---

## 3. Leaving Google and co-founding OpenAI (2015)

### Background
In late 2015, Elon Musk, Sam Altman, and others were preparing to establish a nonprofit AI lab. Sutskever was a recruitment priority.

### Choice
He gave up Google's favorable conditions, including its resources, compute, and team, to join a nonprofit AI organization that did not yet exist.

### Decision process [confirmed]
The decision was difficult. According to Musk's public account in 2023:
- Sutskever repeatedly wavered. He said several times that he would join OpenAI, only for DeepMind's Demis Hassabis to persuade him to stay.
- After going back and forth several times, he decided to join OpenAI.
- Musk said, "Ilya joining was the linchpin for OpenAI being ultimately successful".

### Reasoning
- Sutskever said he had enjoyed working at Google but wanted to do more.
- OpenAI's nonprofit structure and mission to benefit humanity may have appealed to him.
- As chief scientist, rather than a member of a large Google team, he could direct the technical work.

### Outcome
- Became one of OpenAI's six board members.
- Received the chief scientist title and overall responsibility for the research direction.
- OpenAI's subsequent core technical breakthroughs, including the GPT series, took place under his scientific leadership.

### Consistency between statements and actions
The tension between his initial idealism, which centered on a nonprofit serving humanity, and OpenAI's later commercialization foreshadowed the 2023 board crisis.

**Confidence in the facts: High** (Musk's testimony as a primary source).

---

## 4. OpenAI's technical decisions

### 4a. Choosing the GPT/Transformer approach

**Background:** OpenAI initially explored several approaches, including reinforcement learning and robotics. Sutskever promoted language models based on large-scale unsupervised pretraining.

**Key bets:**
- Large-scale unsupervised text pretraining could unlock general capabilities.
- The Transformer architecture, introduced in Google's 2017 paper "Attention is All You Need," was well suited to scaling.
- GPT-1 (2018), GPT-2 (2019), GPT-3 (2020), and GPT-4 (2023) were all completed under Sutskever's scientific leadership.

**Confidence in the facts: High**.

### 4b. Betting on the scaling hypothesis

**Background:** In 2020, Sutskever led research on neural scaling laws at OpenAI, establishing power-law relationships between model performance and scale, measured in parameter count, data, and compute.

**Choice:** He made "bigger is better" a core OpenAI strategy.

**Reasoning:**
- The idea dates to AlexNet and the intuition that performance improves with more data.
- Scaling laws provided a mathematical prediction framework.
- He advanced this approach with Dario Amodei, who later left to found Anthropic, and others.

**Outcome:**
- The success of GPT-3 and GPT-4 validated the scaling hypothesis.
- OpenAI became a global leader in AI for a time.

**Later change of position** [important tension]:
- In his December 2024 NeurIPS talk, he said "pre-training as we know it will end" and introduced "peak data," explaining that "we have but one internet".
- In a November 2025 interview with Dwarkesh Patel, he explicitly characterized 2020–2025 as the scaling era and 2026 onward as the research era.
- Asked whether 100 times more scaling would change everything, he answered "I don't think that's true".
- He later clarified on X that scaling current methods would still improve them, but "something important will continue to be missing".

**Consistency between statements and actions:** This is a major change in position. Sutskever moved from being a central advocate of scaling to questioning it. That need not be a contradiction. He may believe scaling worked in 2020–2025 but has now reached a ceiling. What is he doing at SSI? If it is no longer scaling, what new direction is he backing? He declines to say.

**Confidence in the facts: High** (public talks and interviews).

---

## 5. The November 2023 board incident [most important]

This was the most controversial decision of Sutskever's career and the event that reveals the most information.

### 5a. Preparation (at least one year)

**Confirmed facts** (source: sworn testimony on October 1, 2025, lasting nearly ten hours):
- Sutskever spent at least a year considering Altman's removal.
- He waited until "the majority of the board is not obviously friendly with Sam".
- He wrote a 52-page memo organized as a brief, accusing Altman of:
  - "a consistent pattern of lying"
  - "undermining his execs"
  - "pitting his execs against one another"
- The memo was sent to independent directors through disappearing emails to prevent leaks.
- CTO Mira Murati took screenshots of parts of the memo.

**Key weaknesses** [note]:
- Sutskever acknowledged in his testimony that nearly all of the memo's allegations came from a single source, CTO Mira Murati.
- He acknowledged not cross-checking with other executives.
- He conceded that he relied on "secondhand knowledge".
- In retrospect: "In hindsight, I realize that I didn't know it".

**Confidence in the facts: High** (sworn testimony).

### 5b. Removal (November 17, 2023)

**Timeline:**
- November 17: The board announced Altman's removal.
- November 18, the next day: Discussion of a merger with Anthropic began.
- November 20: Sutskever publicly said he "deeply regrets" his role.
- November 21: Altman was reinstated.

**Sutskever's motives** [multiple sources]:
1. **Safety concerns:** He believed Altman was deploying and commercializing AI too quickly and taking excessive risks.
2. **Management concerns:** The memo recorded allegations of lying and manipulation.
3. **Structural tension:** The nonprofit mission versus commercial pressure.

**Anthropic merger plan** [confirmed]:
- Within 48 hours of the dismissal, the board discussed a merger with Anthropic.
- Board member Helen Toner was "the most supportive" of a merger.
- Toner even said "destroying OpenAI could be consistent with the mission".
- Sutskever openly opposed it: "I really did not want OpenAI to merge with Anthropic. I just didn't want to."
- Anthropic raised practical obstacles and the plan did not proceed.

**Confidence in the facts: High** (sworn testimony).

### 5c. Employee pushback and regret

**Confirmed facts:**
- Of 770 employees, 738 signed a petition asking for Altman to be reinstated.
- Several executives resigned immediately.
- Sutskever admitted, "I had not expected them to feel strongly either way". He had expected employee indifference.
- He subsequently posted publicly on X that he "deeply regrets" his participation.

**Sutskever's retrospective assessment:**
- He admitted the process was "rushed".
- He attributed this to the fact that "the board was inexperienced".

### 5d. Consistency between statements and actions

**Tensions:**
1. He spent a year carefully preparing the removal but did not do elementary cross-checking, relying on Murati alone.
2. He said he was fighting for safety, then said he "deeply regrets" his participation three days later.
3. His opposition to an Anthropic merger suggests he did not want to destroy OpenAI, yet he initiated action that nearly did so.
4. The 52-page memo suggests deliberation, but he completely misjudged the employee reaction.

**Possible explanations:**
- His core concern about AI safety was genuine, but he lacked the ability to execute his plan well.
- As a scientist rather than a manager or politician, he badly underestimated organizational dynamics.
- His public regret might have been a tactical move to preserve his position more than a genuine change of mind.

**Confidence in the facts: High** (direct testimony and public statements).

---

## 6. Leaving OpenAI (May 2024)

### Background
After the November 2023 incident, Sutskever's position became awkward. He retained the chief scientist title but was marginalized in practice.

### Choice
He formally announced his departure on May 14, 2024.

### Public statements
- X post: "The company's trajectory has been nothing short of miraculous, and I'm confident that OpenAI will build AGI that is both safe and beneficial under the leadership of @sama"
- Later told Calcalist: "Ultimately, I had a big new vision...it felt more suitable for a new company"

### Collapse of the Superalignment team
- Jan Leike, the team's co-lead, resigned days after Sutskever's departure.
- Leike publicly complained that OpenAI's "safety culture and processes have taken a backseat to shiny products".
- He said the team was "under-resourced" and "sailing against the wind".
- OpenAI subsequently dissolved the entire Superalignment team.
- It had been founded in 2023 with a commitment of 20% of computing power.

### Consistency between statements and actions
- Sutskever's exceptionally cordial public departure announcement praised Altman's leadership, in sharp contrast with his 52-page memo of allegations.
- Possible reasons include an equity agreement preventing public criticism or a strategic choice.
- Jan Leike's resignation statement indirectly supports the view that Sutskever's longstanding safety concerns were genuine.

**Confidence in the facts: High**.

---

## 7. Founding SSI (June 2024 to the research date)

### 7a. Founding decision

**Date:** Announced on June 19, 2024.

**Co-founders:**
- Daniel Gross, former Apple AI lead and Y Combinator partner.
- Daniel Levy, former OpenAI researcher.

**Office locations:** Palo Alto and Tel Aviv.

**Core position:** "Our first product will be the safe superintelligence, and it will not do anything else up until then"

### 7b. Funding strategy

**Timeline:**
- September 2024: Raised US$1 billion from a16z, Sequoia, DST Global, and SV Angel.
- March 2025: Raised another US$2 billion at a US$32 billion valuation, led by Greenoaks Capital with US$500 million, alongside Alphabet, NVIDIA, a16z, Lightspeed, and DST Global.
- As of 2025: About 20 employees, zero revenue, and a US$32 billion valuation.

**Funding logic:** It relied almost entirely on Sutskever's personal reputation. There was no product, no revenue, and no public technical roadmap.

### 7c. Operating strategy

**Confirmed:**
- SSI does not build products or provide services. It does one thing: safe superintelligence.
- It partnered with Google Cloud in April 2025 for TPU computing capacity.
- Sutskever declines to disclose any technical details.

**Leadership changes** (mid-2025):
- Sutskever declined an attempted acquisition by Meta.
- In July 2025, co-founder Daniel Gross left to join Meta Superintelligence Labs.
- Sutskever took over as CEO, and Daniel Levy became president.

### 7d. Consistency between statements and actions

**Tensions and questions:**

1. **Safety and commerce:** Sutskever left OpenAI because commercial pressures affected safety. SSI nevertheless took US$3 billion in venture capital, and investors will expect returns. How long can it remain "insulated from short-term commercial pressures"?

2. **A scaling skeptic who still depends on compute:** If the scaling era is over, why does he still need Google TPUs and US$3 billion? What exactly is SSI doing?

3. **Time pressure:** He criticized OpenAI for rushing, but SSI faces pressure too. It cannot spend 20 years pursuing "patient research" because investors would not tolerate it.

4. **Transparency:** He publicly supports AI safety and the public's right to know but keeps SSI's technical direction completely secret.

5. **Loss of a co-founder:** Meta recruited Daniel Gross just over a year after SSI was founded, suggesting possible problems with team cohesion or direction.

**Confidence in the facts: Medium to high** (funding confirmed, but almost no public information about the technical direction or internal affairs).

---

## 8. Evolution of his philosophy across decisions

### Early period (2012–2020): Pure technological optimism
- Believed scaling would unlock everything.
- Promoted progressively larger GPT models.

### Middle period (2020–2023): Awakening to safety
- Pushed to establish the Superalignment team.
- Became increasingly concerned about AI existential risk.
- Discussed the possibility of people merging with machines in a 2023 MIT Technology Review interview.

### Later period (2024 to research date): Philosophical turn
- NeurIPS 2024: "pre-training as we know it will end".
- Dwarkesh Patel interview in 2025:
  - AI could exceed human capabilities in 5–20 years.
  - Discussed the necessity of emotion in cognition, citing patients who lost emotional capacity after brain injury.
  - AI agents might need an "intrinsic concern for sentient beings".
  - If most conscious entities in the future are AIs, "caring about sentient life dilutes human primacy".
  - The long-term equilibrium might be a human–machine merger.

### External criticism
- The safety strategy depends on AI sentience, an unverified philosophical assumption.
- "safe superintelligence" may not exist in an absolute sense.
- The underlying reasons for his shift from firmly advocating scaling to questioning it are unknown.

---

## 9. Summary of Sutskever's decision patterns

### Consistent characteristics
1. **Intuition-driven:** From AlexNet to GPT to SSI, he made major decisions on the basis of strong intuitions before full validation.
2. **A scientist's mindset:** Strong at technical judgment but repeatedly miscalculates in organizational management and political maneuvering.
3. **Underlying idealism:** A genuine sense of mission motivated him both to join OpenAI and found SSI.
4. **Insular information gathering:** The 52-page memo relied on one source. He completely misjudged the employee response.

### List of tensions
| Area | Early position | Later position or conduct | Degree of tension |
|---|---|---|---|
| Scaling | Central advocate | Says the era is over | Moderate (explainable as a change of mind) |
| OpenAI's mission | Nonprofit idealism | Praised Altman's leadership when leaving | High (contrasts with the 52-page allegations) |
| Acting for safety | Initiated the removal | Expressed deep regret three days later | High |
| Transparency | Supports the public's right to know | Keeps SSI completely secret | Medium to high |
| Commercialization | Criticized commercialization at OpenAI | SSI took US$3 billion in venture capital | Moderate (different structure, similar pressures) |

### What to watch
- What is SSI actually researching? What is his "big new vision"?
- How long can a US$32 billion valuation with zero revenue last?
- Will SSI change direction after Daniel Gross's departure?
- Will Sutskever's view that emotions are necessary for cognition be reflected in SSI's technical approach?

---

## Sources

### Primary sources (sworn testimony, personal statements, and public talks)
- Ilya Sutskever's sworn testimony (October 1, 2025, Elon Musk v. OpenAI).
- NeurIPS 2024 talk.
- Dwarkesh Patel podcast interview (November 2025).
- Calcalist Tech interview.
- Public statements on X/Twitter.

### Reporting from leading outlets

- [TechCrunch: Ilya Sutskever departs](https://techcrunch.com/2024/05/14/ilya-sutskever-openai-co-founder-and-longtime-chief-scientist-departs/)
- [Time: Sutskever leaves OpenAI](https://time.com/6978195/ilya-sutskever-leaves-open-ai/)
- [Fortune: Sutskever deeply regrets](https://fortune.com/2023/11/20/ilya-sutskever-openai-cofounder-deeply-regrets-resign/)
- [Axios: Sutskever regrets firing](https://www.axios.com/2023/11/20/sam-altman-fired-openai-board-illya-sutsever-regrets)
- [CNBC: SSI founding](https://www.cnbc.com/2024/06/19/openai-co-founder-ilya-sutskever-announces-safe-superintelligence.html)
- [CNBC: Sutskever becomes CEO](https://www.cnbc.com/2025/07/03/ilya-sutskever-is-ceo-of-safe-superintelligence-after-meta-hired-gross.html)
- [Gizmodo: Deposition details](https://gizmodo.com/former-openai-exec-explains-why-he-tried-to-do-a-coup-against-sam-altman-2000680769)
- [Decrypt: Inside the deposition](https://decrypt.co/347349/inside-deposition-showed-openai-nearly-destroyed-itself)
- [The Neuron: Secret memo and Anthropic merger](https://www.theneuron.ai/explainer-articles/ilya-sutskevers-secret-memo-and-the-plot-to-merge-openai-with-anthropic)
- [Israel Hayom: SSI in Tel Aviv](https://www.israelhayom.com/2025/03/06/a-secret-ai-startup-in-tel-aviv-got-30b-this-israeli-raised-pioneer-did-it/)
- [Wikipedia: Ilya Sutskever](https://en.wikipedia.org/wiki/Ilya_Sutskever)
- [Wikipedia: Safe Superintelligence Inc.](https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc.)
- [EA Forum: Dwarkesh interview highlights](https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/highlights-from-ilya-sutskever-s-november-2025-interview)
