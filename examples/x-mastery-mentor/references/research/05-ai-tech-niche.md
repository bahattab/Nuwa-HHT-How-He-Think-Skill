# X/Twitter Content Strategy for AI and Tech

> Research date: 2026-04-06
> Scope: AI and tech creator strategies, building in public, the algorithm, open-source promotion, and Chinese developers reaching international audiences.
> Excluded sources: Zhihu, official WeChat accounts, and Baidu Baike.

---

## 1. Leading Accounts and Strategy Types in AI and Tech

### 1.1 Account Types

| Type | Example account | Core strategy | Followers |
|------|---------|---------|---------|
| **Build in public** | @levelsio (Pieter Levels) | Publish revenue, daily updates, and postmortems | 500,000+ |
| **Learn in public** | @swyx (Shawn Wang) | Publish learning notes and offer feedback | 100,000+ |
| **Technical education** | @karpathy (Andrej Karpathy) | Explain AI concepts clearly and deeply, with video tutorials | One million+ |
| **AI agents and tools** | @steipete (Peter Steinberger) | Share product iteration in real time and publish technical opinions | 200,000+ |
| **Open-source projects** | @ExaAILabs (Exa) | Market via viral side products and showcase APIs | 50,000+ |
| **AI news aggregation** | @AIHighlight | Daily tool picks and quick reports on new models | 100,000+ |

> Sources: firsthand observation (X profiles) + [Amperly: 31 Best AI Twitter Accounts 2026](https://amperly.com/best-artificial-intelligence-twitter-accounts/) + [X: Future Stacked AI account recommendations](https://x.com/FutureStacked/status/2018353141465440693)

### 1.2 Close Look at Key Creators

#### Pieter Levels (@levelsio) — A Pioneer of Building in Public

**Content mix** (firsthand observation):
- **Revenue milestone posts**: He posts a Stripe screenshot at each new monthly recurring revenue (MRR) milestone. A post about reaching $10,000 MRR in three weeks with 318 customers drew many reposts.
- **Technical decisions in real time**: Tests of new models such as Flux, A/B test results, and landing-page conversion rates rising from 1% to 4%.
- **Transparency about failure**: Openly says 97% of his projects failed.
- **Replication across projects**: Shows how he copies working strategies from one project to another.

**Key figures**:
- Current revenue about $138,000 per month (November 2025 figures).
- PhotoAI accounts for 70% of revenue ($106,000 a month), with the rest including InteriorAI and RemoteOK.
- One TikTok added $7,000 in MRR for PhotoAI in a day.

**What makes it work**: Building in public is not just sharing progress. It gives the audience a stake. Watching you go from zero to $100,000 MRR, they start thinking like investors: they want you to succeed and spread the word themselves.

> Sources: [FastSaaS: How Pieter Levels Built a $3M/Year Business](https://www.fast-saas.com/blog/pieter-levels-success-story/) + [X: @levelsio PhotoAI $10K MRR](https://x.com/levelsio/status/1631715500010135552) + [X: @levelsio PhotoAI $150K/mo](https://x.com/levelsio/status/1850305637303160853)

#### swyx (@swyx) — Learn in Public and Pick Up What They Put Down

**Core ideas**:
1. **Learn in public**: Do not study privately and lurk. Blog, make tutorials, ask and answer on forums, and make YouTube videos. Create “learning exhaust,” the useful by-products of studying.
2. **Pick up what they put down**: An industry leader releases something new and needs feedback. Write a review, explanation, or tutorial and tag them. They will repost praise of their work all day.
3. **Macro-tweeting**: Regularly revisit old posts, especially predictions you got right.

**In practice**:
- Publishes a daily AI newsletter, Latent Space. Twitter is his public notebook.
- Tweets because he needs public notes, writes a newsletter because he needs a searchable AI news database, and draws charts because he needs to explain concepts. **The audience's benefit is a by-product.**
- Coined the definition of the “AI Engineer” role.

**Lesson for Huashu**: This suits people with deep knowledge who do not do original research. **You do not need to invent anything new. Explain someone else's invention clearly and tag the creator.**

> Sources: [swyx.io: Learn in Public](https://www.swyx.io/learn-in-public) + [swyx.io: Pick Up What They Put Down](https://www.swyx.io/puwtpd) + [swyx.io: How to Thought Lead (2026)](https://www.swyx.io/lead)

#### Andrej Karpathy (@karpathy) — A Benchmark in Technical Education

**Content traits** (firsthand observation):
- Does not chase trends, but every post has depth.
- Admits what he does not know and shares where learning is hard.
- Builds long-term assets through educational videos such as the Zero-to-Hero AI series on YouTube.
- Founded Eureka Labs, an AI-native education company, turning his educational content on Twitter into a product.

**Why it works**: Low frequency, high quality, and Feynman-style explanation. When Karpathy posts, the AI community pays attention because he does not add noise.

> Sources: [X: @karpathy](https://x.com/karpathy) + [karpathy.ai](https://karpathy.ai/) + [Karpathy’s three-folder method for a personal AI knowledge base](https://www.digitaltoday.co.kr/en/view/45521/karpathy-reveals-personal-ai-knowledge-base-built-with-three-folders)

#### Peter Steinberger (@steipete) — From iOS Veteran to AI Agent Pioneer

**Career shift**: Thirteen years of native iOS development as PSPDFKit's founder, then vibe coding in 2025, then OpenClaw (an open-source AI agent), and then OpenAI in 2026.

**Content strategy**:
- Shares candid technical views, for example that “vibe coding” is a derogatory label because building with AI actually takes skill.
- Shares the development of OpenClaw in public, such as posting that there were 600 commits in a day and PRs rose from 2,700 to 3,100.
- Joining OpenAI gave him a dual role as an insider and a public voice.

> Sources: [OpenClawAI Blog: Vibe Coding Is a Slur](https://openclawai.io/blog/openclaw-creator-advice-playful-building/) + [X: @steipete joining OpenAI](https://x.com/steipete/status/2023154018714100102)

---

## 2. What AI and Tech Creators Should Know About X's 2026 Algorithm

### 2.1 Three-Stage Ranking Pipeline

1. **Candidate selection**: Out of 500 million daily tweets, select about 1,500 candidates for each user (50% in-network and 50% out-of-network).
2. **Machine-learning ranking**: A neural network analyzes thousands of features and outputs ten probability labels.
3. **Grok-driven update** (January 2026): A transformer model reads every post and video and makes five billion ranking decisions a day.

### 2.2 Signal Weights

| Interaction | Weight | Multiplier relative to likes |
|---------|------|-------------------|
| Like | ×1 | 1× |
| Bookmark | ×10 | 10× |
| Link click | ×11 | 11× |
| Profile click | ×12 | 12× |
| Reply | ×13.5 | 13.5× |
| Repost | ×20 | 20× |
| **Conversation (reply plus author reply)** | **×75** | **150×** |

**Key insight**: One good conversation has the algorithmic value of 150 likes. This explains why prominent AI and tech creators actively reply to comments.

### 2.3 Algorithm Details Specific to AI and Tech

**Engagement velocity is the strongest signal**:
- Engagement in the first 15–30 minutes determines everything.
- More than ten interactions in 15 minutes leads to exponential distribution.
- Fewer than three interactions in 15 minutes means the tweet stalls.
- **Response**: Post when your audience is most active. For a global AI and tech audience, try 8–10 a.m. Pacific time, which the source gives as 11 p.m.–1 a.m. in Beijing.

**Time decay**: Visibility halves every six hours. AI news is time-sensitive, so responding quickly matters.

**External-link penalty**:
- Link tweets lose 30–50% of reach, with almost no engagement for non-Premium users.
- **Workaround**: Leave the link out of the main post and put it in the first reply.
- After March 2026 the link penalty was largely removed for Premium users.

**X Premium boost**: Paying users get a two- to fourfold reach boost. This is an essential investment for creators serious about X.

> Sources: [PostEverywhere: How X Algorithm Works 2026](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) + [Teract: Twitter Algorithm 2026 Deep Dive](https://www.teract.ai/resources/twitter-algorithm-2026) + [Sprout Social: Twitter Algorithm 2026](https://sproutsocial.com/insights/twitter-algorithm/)

---

## 3. Content Strategies Specific to AI and Tech

### 3.1 Content Formats and Performance

| Format | Engagement | Suggested frequency | Example |
|---------|--------|---------|------|
| **Quick review of a model or product** | Very high | Post when a topic is trending | “GPT-5.3 is out. I tested three use cases…” |
| **Building-in-public update** | High | Two to three times a week | MRR screenshots, feature launches, user feedback |
| **Technical tutorial or thread** | High | Weekly | A tutorial thread of 8–12 tweets |
| **Demo video or GIF** | High | When there is a result | A 15–30 second product demo |
| **Hot take or controversial opinion** | Medium to high | Use cautiously | “Vibe coding is a slur” |
| **Research paper explainer thread** | Medium | Weekly | Break down key findings in plain language |
| **Tool comparison or review** | Medium | Two to three times a month | Screenshots and a table of test results |
| **Personal story or reflection** | Medium | Occasionally | Starting a business or changing careers |
| **Memes or humor** | Highly variable | Use cautiously | AI-related memes |

### 3.2 Responding Quickly to a New Model

The most distinctive opportunity in AI is a **new model release**, such as GPT-5, Claude Opus, or DeepSeek. This sets the field apart from other tech sectors.

**Response timeline**:
1. **Zero to one hour after release**: Share a quick take with an initial reaction and one clear point of view.
2. **One to six hours after release**: Post a demo or test results with screenshots and a GIF.
3. **Six to 24 hours after release**: Publish a deep thread with systematic tests, comparisons, and a point of view.
4. **One to seven days after release**: Publish an in-depth article or video with a full review and practical use cases.

**OpenAI's approach**: Within minutes of launch, Sam Altman asked users on Twitter what they wanted to do with it. The community made the content instead of receiving one-way promotion.

> Sources: [FutureSocial: How OpenAI Used Twitter Replies to Create Launch Content](https://futuresocial.beehiiv.com/p/openai-used-twitter-replies-create-launch-content) + firsthand observation

### 3.3 A Practical Guide to Building in Public

**What to share**:
- MRR milestones and Stripe screenshots. Use [BrandBird MRR Meter](https://www.brandbird.app/tools/twitter-mrr-meter) to generate standardized images.
- Feature launches and demo screenshots or videos.
- Postmortems on what failed.
- Technology stack choices and the rationale behind decisions.
- Screenshots of user feedback.
- Monthly or quarterly recap threads.

**What not to share**:
- Exact acquisition cost (CAC) and unit economics, which are competitively sensitive.
- Customers' personal information.
- Exact implementation details of your core competitive advantage.

**Formatting tips**:
- Start threads with a hook: “Week 12 of building [Product]: Hit $2K MRR...”
- End with a call to action: “Follow along for weekly updates.”
- Visual content draws five times more engagement.
- Answer every reply within an hour.

**Case figures**:
- AudioPen: Built in 12 hours → 100 paying users in two days → #1 on Product Hunt → $73,000 in revenue in the first two months.
- SiteGPT: 24,000+ Twitter followers → #1 on Product Hunt → $15,000 MRR in June → $95,000 MRR.
- An indie developer: Reached 2,400 Twitter followers in four months and hit $8,000 MRR on launch.

> Sources: [OpenTweet: Build in Public Guide](https://opentweet.io/blog/build-in-public-twitter-guide-saas-founders) + [Teract: Twitter Strategy for Indie Hackers 2026](https://www.teract.ai/resources/twitter-strategy-indie-hackers-2026) + [AudioPen Starter Story](https://www.starterstory.com/stories/audiopen) + [SiteGPT Rise to $15K MRR](https://www.indiehackers.com/post/from-side-hustle-to-ai-star-sitegpts-rise-to-15k-mrr-ff15fee186)

### 3.4 Thread-Writing Practices

**Evidence**: Threads of 8–12 tweets perform 47% better than short threads, according to Sprout Social's 2026 figures. Threads overall get three to five times the engagement of individual tweets.

**Template** for AI and tech:

```
Tweet 1 (hook): A surprising figure or counterintuitive point plus “Thread”
Tweets 2–3: Background and problem definition
Tweets 4–8: Core argument, steps, or findings
Tweets 9–10: Practical execution, code, or screenshots
Tweet 11: Summary and key takeaways
Tweet 12: Call to action (follow, bookmark, or repost)
```

**Thread types specific to AI**:
1. **“I tested X and the results surprised me”**: A hands-on test of a new model or tool.
2. **“N lessons from zero to $X,000 MRR”**: A building-in-public recap.
3. **“This paper changed how I think”**: A research paper explainer.
4. **“X vs. Y: An in-depth comparison”**: A side-by-side tool or model review.
5. **“I used AI to do X and saved N hours”**: A practical case study.

> Sources: [AI Free Forever: 15 Best Viral Threads 2026](https://aifreeforever.com/blog/15-best-twitter-thread-examples-that-went-viral) + [Teract: Twitter Algorithm 2026](https://www.teract.ai/resources/twitter-algorithm-2026)

---

## 4. Visual Content: Code Screenshots, GIFs, and Video Demos

### 4.1 Performance by Format

| Format | Engagement rate | Best duration or size | Use case |
|------|--------|-------------|---------|
| Plain text | 0.1% | Ideally 120–130 characters | Views and hot takes |
| Image or screenshot | 0.08% | 16:9 landscape | Code screenshots and data tables |
| GIF | Moderate | A 3–8 second loop | Feature demos and interactions |
| Video | 0.42% | 15–30 seconds | Product demos and tutorials |
| Thread | Three to five times a single tweet | 8–12 posts | In-depth content, tutorials, and reviews |

**Note**: X is the sole major platform where text can hold its own against video. But video engagement of 0.42% is far above images at 0.08%.

### 4.2 Tools and Tips for Code Screenshots

- **[Snappify](https://snappify.com/)**: Create polished code images and add an avatar and username.
- **[Pika](https://pika.style/templates/code-image)**: Generate code screenshots with a choice of themes.
- **[Codeshot](https://codeshotapp.com/)**: Choose a theme and export at Twitter dimensions.

**Key principles**:
- Highlight important lines rather than pasting an entire page of code.
- Add annotations or highlighting to show what matters.
- Treat the first frame as a billboard: bold text, high contrast, clear promise.

### 4.3 Best Practices for Video Demos

- **16:9 landscape** works best for demos and screen recordings.
- **15–30 seconds** is the best duration to maximize completion.
- **Assume people watch muted**. Put the essential information in captions.
- **The first frame is the thumbnail**. It acts as a billboard in the feed.
- **After posting the main video, reply in a thread** with highlights, timestamps, and links.

> Sources: [ScriptStorm: Twitter Video Best Practices](https://scriptstorm.ai/blog/twitter-video-best-practices-length-format-engagement) + [Snappify](https://snappify.com/) + [Codeshotapp](https://codeshotapp.com/posts/how-to-share-code-on-twitter/)

---

## 5. Promoting Open-Source Projects

### 5.1 Key Twitter/X Promotion Steps

1. **GitHub Social Preview**: Upload an attractive promo image in repository settings to make shared links stand out. Many projects overlook this.
2. **Keep talking**: Share small updates, your coding journey, and technical decisions regularly.
3. **Cross-tag in list articles**: Include similar projects in a list and tag their maintainers on Twitter. They will like or repost it.
4. **Awesome lists**: Submit a PR to an awesome-xxx list on GitHub.
5. **Publish cross-platform**: Post Tuesday to Thursday, 8–10 a.m. Pacific time, and adjust the wording for each platform.

**Key finding**: Tweets have a significant positive effect on earning new stars and attracting contributors. An active Twitter community plays an important role in attracting contributors, as an academic study found.

### 5.2 Viral Side Products: Exa's Twitter Wrapped

**Case**: Exa, an AI search engine, acquired 1.7 million users with a tool called Twitter Wrapped.

**Execution**:
- Released on December 26. AI analyzed a user's X account to generate a personalized year in review, roasts, and predictions.
- Half a million views within four hours.
- After four days: 59,000 reposts and 13.6 million views.

**Why it worked**: Like Spotify Wrapped, it is **personalized content that people naturally want to share**. Users share their results, friends get curious and generate their own, and the cycle continues.

**Lesson**: AI products can spread widely by creating **a free, personalized, shareable side product**. The main product need not go viral if its entry point does.

> Sources: [Indie Hackers: Exa Twitter Wrapped](https://www.indiehackers.com/post/tech/exa-an-ai-powered-search-engine-gains-1-7m-users-with-viral-twitter-wrapped-vUAEDrWM4ELz5UHcbyjG) + [DEV: Promoted Open Source Repo to 6K Stars](https://dev.to/wasp/how-i-promoted-my-open-source-repo-to-6k-stars-in-6-months-3li9) + [FreeCodeCamp: 4.5K Stars in 6 Months](https://www.freecodecamp.org/news/how-to-get-more-engagement-with-your-open-source-project/) + [arXiv: Impact of Twitter Mentions on GitHub](https://arxiv.org/html/2401.02755)

---

## 6. X Strategies for Chinese AI Developers Reaching Global Audiences

### 6.1 Success Cases

**Han Xiao (@hanaborxiao) — Founder of Jina AI**:
- Founded Jina AI in 2020 after working at Tencent AI. It is headquartered in Berlin with research centers across San Francisco, Beijing, and Shenzhen.
- Acquired by Elastic in 2025.
- Strategy: Mostly English content, open-source community management, and speaking at global conferences.
- Active on the LF AI Foundation board, using open source to build international trust.

**DeepSeek team**:
- Founder Liang Wenfeng keeps a very low profile and barely uses social media.
- DeepSeek's technical papers are nevertheless discussed widely on X and spread by others.
- The case shows that **when a product is good enough, the community will spread it for you**.

### 6.2 Challenges and Strategies Specific to Chinese Developers

1. **Language barrier**: English writing is a necessary hurdle, but it need not be perfect. AI audiences are more accepting of non-native speakers.
2. **Time zones**: Adapt posting times to audiences in North America and Europe (8–10 a.m. Pacific time).
3. **Building trust**: Open-source contributions are the strongest trust asset internationally.
4. **Differentiation**: Firsthand information about the Chinese AI ecosystem, such as DeepSeek technical details and domestic AI use cases, is uniquely valuable to global audiences.
5. **Bilingual strategy**: Run Chinese and English content separately without mixing them.

> Sources: [Han Xiao Bio](https://hanxiao.io/about/) + [AI Berlin: Interview Han Xiao](https://ai-berlin.com/blog/article/interview-with-dr-han-xiao-ceo-and-co-founder-of-jina-ai) + [Nature: How China Created DeepSeek](https://www.nature.com/articles/d41586-025-00259-0) + firsthand observation

---

## 7. AI and Tech Topics and the Conversion Path

### 7.1 Ten Topic Types by Engagement

1. **Quick reviews of new models and features**: Test right away and share your view. Highest engagement and the shortest window.
2. **Building-in-public milestones**: MRR screenshots and user-count breakthroughs. High engagement and strong trust building.
3. **Practical tutorial threads**: “How to use X to do Y.” High bookmark rates and good long-tail traffic.
4. **Side-by-side tool reviews**: “How Claude, GPT, and Gemini perform in scenario X.” High search value.
5. **Hot takes and contentious views**: “Vibe coding is a slur.” Strong discussion but some risk.
6. **Personal failures and lessons**: “I did X and lost Y.” Relatable and builds authenticity.
7. **Research paper explainers**: Break things down simply. Medium engagement with a strong expertise signal.
8. **Resource roundups**: “The ten best X tools.” High bookmark rates.
9. **Industry predictions**: “Five AI trends in 2026.” Variable results, with high returns if correct.
10. **Memes and humor**: AI-related memes spread easily but do not establish expertise.

### 7.2 Content-to-Conversion Path

```
X posts and threads → Personal brand awareness
    |
Blog and newsletter (in-depth content) → Email list
    |
Product Hunt or GitHub launch → User acquisition
    |
Paid products, consulting, and courses → Revenue
```

**Key point**: X content builds trust and an audience rather than converting directly. Conversion happens through in-depth material such as the newsletter and blog, and during product launches.

---

## 8. Tactics at a Glance

### 8.1 Publishing Rhythm

| Format | Frequency | Timing |
|---------|------|------|
| Regular posts (views and small updates) | Three to five a day | Two to three hours apart |
| Thread (in-depth content) | Once or twice a week | Tuesday to Thursday |
| Replies | 70% of posting volume | Throughout the day |
| Quick review of a new model | Whenever one appears | Within an hour of release |

### 8.2 Growth Formula

**Zero to 1,000 followers**:
- Spend 70% of effort replying and 30% publishing.
- Reply to major industry accounts with something useful to add.
- Apply swyx's PUWTPD strategy: Review what prominent creators release or make tutorials for it.

**1,000 to 10,000 followers**:
- Define three to five recurring content themes.
- Build expertise with one or two threads a week.
- Start building in public.

**10,000+ followers**:
- Build in-depth content assets through a newsletter or blog.
- Use the existing audience for product launches.
- Start doing selective promotional collaborations.

### 8.3 Growth Tactics Specific to AI

1. **Model release day is your Super Bowl**: Everyone is browsing AI news, so relevant content already has an audience.
2. **Free tools are an acquisition entry point**: Exa's Twitter Wrapped and Pieter's free AI experiments are examples.
3. **Open source accelerates trust**: Open-source projects get much more trust on X than closed-source products.
4. **Screenshots beat descriptions**: Use visual evidence such as Stripe screenshots, product demos, or code output.
5. **Threads are your long-form tool**: A thread on X does the work of a blog post on other platforms.
6. **Replies are the most underrated growth lever**: One good reply carries the algorithmic weight of 13.5 likes.

---

## 9. How AI and Tech Differ From General Twitter Strategy

| Dimension | General Twitter | AI and tech |
|------|------------|------------|
| **Timeliness** | Can schedule in advance | New models call for replies within hours |
| **Depth** | Mostly short, quick posts | Threads and technical analysis are core assets |
| **Visuals** | Attractive images and infographics | Code screenshots, terminal recordings, demo GIFs |
| **Trust** | Personal brand stories | Open-source contributions, technical depth, transparent revenue |
| **Audience** | Broad consumer audience | Developers and founders, valuable but hard to fool |
| **Links** | Avoid where possible | Share essential GitHub and blog links in replies |
| **Growth route** | Followers become brand partnerships | Followers become users and open-source contributors |
| **International reach** | Strong localization | AI is naturally global and English is the common language |
| **Proof** | Follower and engagement counts | Whether you can actually build and ship something |

---

## 10. Recommendations for Huashu's X Strategy

These recommendations reflect the research and Huashu's position as an AI-native coder, independent developer, and media creator with over 300,000 followers:

1. **Position clearly**: “A Chinese independent developer building products with AI.” That offers distinct value on English-language X, combining firsthand information on China's AI ecosystem with an independent developer's story.
2. **Content themes**: Building in public with product data, hands-on AI tool tests, and views from China's AI ecosystem.
3. **Respond quickly**: When a new model drops, review it quickly from a Chinese developer's point of view to stand out.
4. **Turn products into content**: Development stories for products such as the kitten fill-light app and GLM Code naturally suit building in public.
5. **Make threads the main format**: Post a thread weekly, focus on replies day to day, and do not chase daily volume.
6. **Show visual proof**: Add a screenshot, GIF, or video to every product-related post.
7. **Keep languages separate**: Use English on X and Chinese on official WeChat and Xiaohongshu accounts, without mixing them.

---

*Research complete. Sources appear at the end of each section, distinguishing firsthand observations from secondary analysis. Main finding: Success in AI and tech on X is not about content marketing tricks. It is about doing real work and sharing it openly. Building and learning in public are ways of working, not just strategies.*
