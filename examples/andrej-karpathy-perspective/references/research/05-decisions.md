# Andrej Karpathy: Major decisions and actions

> Research date: 2026-04-05
> Sources include Wikipedia, TechCrunch, CNBC, the Lex Fridman Podcast, Karpathy's own Twitter/X posts, BDTechTalks, VentureBeat, and Electrek.
> Quoted passages are translations from the Chinese research notes, except terms already in English in the source.

## 1. Joining OpenAI's founding team (2015)

### Background
Karpathy was pursuing a PhD in Fei-Fei Li's Stanford lab, studying how CNNs could be applied where computer vision and NLP intersect. In 2015 he also interned at DeepMind in deep reinforcement learning. OpenAI announced its founding that year.

### Reasoning
He publicly said he was drawn to OpenAI's unusual combination of academic research freedom and a startup's drive toward practical applications. AI organizations of that kind were rare. He wanted to be an early participant in bringing AI into practice rather than writing papers alone.

### Retrospective
He did not publicly criticize the experience. He characterized the period as foundational to his technical understanding. The source describes two subsequent returns to OpenAI as evidence of continued identification with the organization.

## 2. Leaving OpenAI for Tesla (2017)

### Background
Elon Musk recruited him personally. Tesla Autopilot was at a crucial stage of expansion and needed someone to turn academic deep-learning work into a deployed system. Karpathy saw a chance to test his Software 2.0 approach at real-world scale. His November blog post that year laid it out systematically.

### Reasoning
This was driven by the ability to test an idea. Tesla's fleet of one million cars supplied a real-world data flywheel and made it the largest test bed for the idea that neural networks could replace hand-written rules. Moving from academic research to real-world validation fit his view that he did not truly understand what he could not build.

He described Musk’s management style: “Elon likes small, focused, highly technical teams. He has always resisted expanding the team. … If engineers tell him they do not have enough GPUs, once he hears it twice he calls the person in charge of the GPU cluster directly and then calls Jensen Huang.”

## 3. Tesla's vision-only approach without lidar

### Background and timeline
The technical approach evolved and grew stronger from 2017 to 2022, rather than resulting from one decision. Milestones:

- At the 2021 CVPR keynote, Karpathy laid out the case for vision systematically.
- By the end of 2021 Tesla removed radar and went entirely vision-only.
- In 2022 it also removed ultrasonic sensors.

### Reasoning in Karpathy's public case

- **The data flywheel matters more than the sensor configuration.** “The real question isn’t whether you have lidar. It’s whether you have a fleet that can collect data.”
- **Scaling lidar.** “Collecting, building, and maintaining high-definition lidar maps doesn’t scale.”
- **Generality of vision.** “Once you actually get it working, it is a general vision system that can in principle be deployed anywhere on Earth.”
- **Neural networks surpassing sensor fusion.** “Our deep-learning system is already a hundred times more accurate than radar. Radar is starting to become a limiting factor and introduce noise.”

### Consistency between words and actions
He did not publicly challenge this technical direction after leaving. Tesla FSD kept iterating with vision alone, which to some extent validated the judgment in the market. Safety data on multisensor approaches such as Waymo's nevertheless continued to fuel debate.

## 4. Leaving Tesla (July 2022)

### Reasoning in his public accounts
Official statement: “It was a great honor to help Tesla achieve its goals over the past five years. … I don’t have a specific next step planned, but I’d like to spend more time returning to my longstanding interests in technical work, open source, and education.”

He was more candid on Lex Fridman’s podcast: “Over five years, I got myself into a management position. I spent most of my time in meetings. … This isn’t what I fundamentally enjoy doing.”

### Consistency between words and actions
His departure was consistent with his identity as an engineer. He immediately began publishing technical YouTube videos intensively, including the nanoGPT and makemore series. It was a way to demonstrate values through action.

## 5. Open-sourcing the nanoGPT educational series (from late 2022)

### Reasoning
His reason for writing nanoGPT was direct: “As a little repository to teach people the basics of training GPT.” The idea behind it, which he attributes to Feynman: “If I can’t build it, I don’t understand it.” nanoGPT has about 750 lines and can train GPT-2-class models. The design goal was that “anyone can understand every line.” He went further down the stack with llm.c, implemented directly in C and CUDA.

### Impact
nanoGPT became one of the most widely read pieces of code in AI education and a benchmark and starting point for many later projects.

## 6. Returning to OpenAI (February 2023)

After publishing educational material intensively during his break, he returned a few months before GPT-4's release. His main responsibilities were forming a new team focused on midtraining and synthetic-data generation. He also helped improve GPT-4.

## 7. Leaving OpenAI again (February 2024)

### His original remarks, as conveyed by the source
“Hi everyone, yes, I left OpenAI yesterday. First, nothing ‘happened.’ This wasn’t the result of any specific event, issue, or drama (but please keep the conspiracy theories coming, they’re very entertaining :)). In fact, working at OpenAI for the past year or so was great. The team is very strong, the people are excellent, and the roadmap is exciting.”

**Consistency.** This was his second choice to prioritize personal projects over a large company. The pattern is stable: join a large organization for a time, contribute, then return to independent work.

## 8. Founding Eureka Labs (July 2024)

### Reasoning
He positioned Eureka Labs as an AI-native school. Its mission was to scale education by using an AI teaching assistant to extend the reach of course material written by human experts. Its first product was LLM101n.

This followed the educational thread of his career: Stanford CS231n, a deep-learning course that grew from 150 to 750 students, the YouTube Zero to Hero series, nanoGPT and llm.c, then Eureka Labs.

He never treated education as a side job. Even during his busiest time at Tesla, he maintained open educational resources. Eureka Labs made that continuing work his main job.

## 9. Introducing vibe coding and facing criticism (February 2025)

### Main point of the original post
“There’s a new kind of coding I call ‘vibe coding.’ You go entirely by feel, embrace exponential growth, and even forget the code exists. … I always Accept All and never read the diff.”

### Reaction and criticism
The term went viral, was entered by Merriam-Webster, and became the Collins English Dictionary word of the year for 2025. Criticism came from Andrew Ng, Simon Willison, and security researchers. The latter reported a 2.74-fold vulnerability rate in AI-collaborative code.

### Karpathy's response
He did not fully concede. He posted about the pace of AI-assisted coding in professional work and how it differed from vibe coding. His response supplied context rather than conceding the point.

In March 2026 he used vibe coding to create a chart of labor-market exposure to AI. After it was misread, he deleted the post, explaining: “It was badly misunderstood. This was a two-hour Saturday-morning project.”

## Patterns across decisions

### Engineering identity comes before job titles.

He leaves when he feels management is turning him into a different person. He does not hold on to organizational power.

### Education runs through his career.

Eureka Labs was the culmination of 20 years of work.

### Commit heavily at technical inflection points.

He entered ahead of peaks: OpenAI in 2015, Tesla in 2017, and OpenAI again on the eve of GPT-4 in 2023. This reflects early judgments about trends.

### Build to verify understanding.

nanoGPT, llm.c, CS231n, and LLM101n all use the ability to build from scratch as the ultimate test.

### Respond to criticism by adding context.

In the vision debate, criticism of vibe coding, and the deleted-chart incident, his response was essentially, “You misunderstood this. Let me give you the context.”


### Consistency between words and actions

- He said he preferred technical work to management, and left management jobs in practice.
- He said education was a long-term interest, and founded Eureka Labs.
- He said building from scratch was the only way to understand, and wrote nanoGPT and llm.c.

### Open questions about consistency

- He did not fully explain publicly how vibe coding coexists with his commitment to understanding through construction.
- His response to Tesla engineers' internal concerns about removing radar has never been fully disclosed.

## Key sources

- [Karpathy's account of leaving OpenAI](https://x.com/karpathy/status/1757600075281547344)
- [His account of leaving Tesla](https://x.com/karpathy/status/1547332300186066944)
- [Original vibe coding post](https://x.com/karpathy/status/1886192184808149383)
- [Software 2.0 blog post (2017)](https://karpathy.medium.com/software-2-0-a64152b37c35)
- [Lex Fridman Podcast #333](https://lexfridman.com/andrej-karpathy/)
- [TechCrunch on leaving OpenAI](https://techcrunch.com/2024/02/13/andrej-karpathy-is-leaving-openai-again-but-he-says-there-was-no-drama/)
- [Case for vision at CVPR 2021](https://bdtechtalks.com/2021/06/28/tesla-computer-vision-autonomous-driving/)
- [Introduction to Eureka Labs](https://techcrunch.com/2024/07/16/after-tesla-and-openai-andrej-karpathys-startup-aims-to-apply-ai-assistants-to-education/)
