# Research on X/Twitter's Recommendation System

> Research date: 2026-04-06
> Coverage: From the first open-source release in 2023 to the second release in January 2026.
> Evidence tiers: 🟢 Official disclosures or inspectable source code | 🟡 Established media coverage or data analysis | 🔴 Inferences from community tests.

---

## 1. Evolution of the Recommendation Architecture

### 1.1 The Three-Stage Pipeline

🟢 **Source: Open-source GitHub code**

X has used the same three-stage recommendation architecture from the first open-source release in 2023 (`twitter/the-algorithm`) to the 2026 Grok version (`xai-org/x-algorithm`).

| Stage | Function | Implementation |
|------|------|----------|
| **Candidate sourcing** | Selects around 1,500 candidates from hundreds of millions of posts | In-network content from followed accounts and out-of-network ML retrieval |
| **Ranking** | Predicts engagement probabilities and scores candidates | Phoenix (Grok transformer model) |
| **Filtering and blending** | Deduplicates, ensures diversity, inserts ads | Home Mixer orchestration layer |

- Sources: [GitHub - xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | [GitHub - twitter/the-algorithm](https://github.com/twitter/the-algorithm)

### 1.2 Grok Takes Over Recommendations (October 2025 to January 2026 Open Release)

🟢 **Sources: Elon Musk's posts and the GitHub release**

**Timeline:**
- **September 2025**: Musk announced, “The algorithm will be purely AI by November,” and pledged to release the code every two weeks.
- **October 2025**: Grok began to replace traditional heuristics across the system.
- **November 2025**: The Following feed switched to Grok ranking as well.
- **January 20, 2026**: xAI released `xai-org/x-algorithm` on GitHub, opening the Rust rewrite.

**Key changes:**
- Rewritten from Scala into a hybrid architecture using **Rust (62.9%) and Python (37.1%)**.
- The core transformer architecture comes from Grok-1 and is adapted to recommendations.
- Grok reads each post and watches each video, processing over 100 million items daily.
- The team pledged to push code updates and developer notes every four weeks.

- Sources: [Elon Musk post](https://x.com/elonmusk/status/1969081066578149547) | [@XEng post](https://x.com/XEng/status/2013471689087086804) | [TechCrunch coverage](https://techcrunch.com/2026/01/20/x-open-sources-its-algorithm-while-facing-a-transparency-fine-and-grok-controversies/) | [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174/)

### 1.3 Four Core Modules (2026 Open-Source Release)

🟢 **Sources: Repository code and README**

| Module | Language | Role |
|------|------|------|
| **Home Mixer** | Rust | Orchestration layer that receives gRPC requests and coordinates the pipeline |
| **Thunder** | Rust | In-memory post store that consumes Kafka events and supports sub-millisecond in-network queries |
| **Phoenix** | Python/JAX | Grok transformer ranker that predicts engagement probabilities |
| **Candidate Pipeline** | Rust | Reusable framework: Sources retrieve → Hydrators enrich → Filters filter → Scorers score → Selector returns the top N |

- Sources: [xai-org/x-algorithm README](https://github.com/xai-org/x-algorithm/blob/main/README.md) | [Phoenix README](https://github.com/xai-org/x-algorithm/blob/main/phoenix/README.md) | [DeepWiki analysis](https://deepwiki.com/xai-org/x-algorithm)

### 1.4 Promptable Feeds

🟡 **Sources: Musk's posts and media reports**

Users can adjust their feed with natural-language instructions, such as “Show me more tech innovations, less politics.” This follows from embedding Grok directly in the recommendation engine.

- Musk announced the feature in September 2025.
- The January 2026 open-source release includes a promptable feeds interface.
- Sources: [WebProNews](https://www.webpronews.com/xs-promptable-algorithm-musks-bid-to-hand-users-the-feed-controls/) | [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-moving-to-personalized-ai-powered-algorithm/760698/)

---

## 2. Engagement Weights

### 2.1 Exact Weights (Verifiable in the Open Code)

🟢 **Sources: xai-org/x-algorithm open code and confirmation from Social Media Today**

X is the only major social platform to open-source its recommendation algorithm twice, making its interaction weights public.

| Interaction | Weight | Relative to a like | Description |
|----------|------|---------------------|------|
| **Conversational reply** (reply plus author engagement) | +75 | **150×** | The original author replies to or likes your reply |
| **Reply** | +13.5 | **27×** | An ordinary reply |
| **Profile click** | +12.0 | **24×** | A user opens your profile and likes or replies |
| **Click into conversation** | +11.0 | **22×** | A user opens the conversation and replies or likes |
| **Dwell time over two minutes** | +10.0 | **20×** | A user enters the conversation and stays over two minutes |
| **Repost** | +1.0 | **2×** | A repost |
| **Like** | +0.5 | **1× (baseline)** | Reference value |
| **Bookmark** | ~+10 | **~20×** | Community estimate, not an exact official figure |

**Key insight: Depth of conversation matters most.** A reply chain that earns a response from the author is worth more than 150 likes.

⚠️ **About weights in different versions:**
- Weights in the initial 2023 release and the 2026 version differ slightly.
- Figures such as “Reply 27×, Retweet 40×” in early community analyses came from simplified calculations based on the 2023 version.
- In 2026, repost weight fell sharply, from about 20× to about 2×, and conversations gained more weight.
- This document uses the 2026 open-source release as its reference.

- Sources: [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/) | [posteverywhere.ai source-code analysis](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Typefully analysis](https://typefully.com/blog/x-algorithm-open-source)

### 2.2 Negative Signals and Penalties

🟢 **Source: Open code**

| Negative signal | Penalty weight | Effect |
|----------|----------|------|
| **Report** | −369× | Nearly stops distribution altogether |
| **Block, mute, or Show Less** | −74× | Greatly reduces recommendations to that user |

🟡 **Source: Media analysis**

| Negative signal | Effect |
|----------|----------|
| **External links** | Reach decreases 30–50%; median engagement on link posts from non-Premium accounts has been zero since March 2025 |
| **More than two hashtags** | Reduces reach by around 40% and is treated as a spam signal |
| **Repeated content or links** | Gradually reduces visibility, potentially triggering a shadowban in severe cases |

- Sources: [posteverywhere.ai](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Tweet Archivist](https://www.tweetarchivist.com/how-twitter-algorithm-works-2025)

---

## 3. Premium Subscription Visibility Boost

### 3.1 Algorithmic Multipliers

🟢 **Source: Open-source code**

| Context | Premium multiplier | Description |
|------|-------------|------|
| **In-network (followers' feeds)** | **4×** | Four times as likely to appear in feeds of people who follow you |
| **Out-of-network (non-followers' feeds)** | **2×** | Twice as likely to appear in feeds of people who do not follow you |

### 3.2 Observed Results

🟡 **Sources: Buffer's analysis of 18.8 million posts and media coverage**

- Premium accounts get about **10 times** the reach per post of standard accounts.
- The gap for Premium+ widened further after 2025.
- Premium replies rank higher by default in popular discussions. Q1 2026 figures show 30–40% more reply impressions.
- Since March 2026, posts with external links from non-Premium accounts have had zero median engagement.

### 3.3 TweepCred and Premium

🟡 **Source: Circleboom analysis**

Premium subscribers receive an immediate +100 TweepCred boost, raising the starting score from −128 to −28 and substantially shortening the account's cold start.

- Sources: [Circleboom](https://blog-content.circleboom.com/does-x-premium-boost-algorithm/) | [posteverywhere.ai](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Buffer data](https://buffer.com/resources/data-best-content-format-social-media/)

---

## 4. TweepCred Account Reputation Score

🟢 **Source: TweepCred module in the open code**

### 4.1 Basic Mechanism

- Every X account has a hidden reputation score: **TweepCred**.
- Range: **−128 to +100**.
- New accounts start at **−128**.
- Minimum for standard distribution: **+17**. Content below that score is throttled.
- Premium subscribers immediately get a **+100 boost**.

### 4.2 Influencing Factors

🟡 **Source: Community reverse engineering**

TweepCred is a weighted composite score like PageRank, based on the following factors:

| Factor | Effect |
|------|------|
| Following-to-followers ratio | Following vastly more users than follow you → negative |
| Engagement quality | High-quality conversations → positive |
| Account history | Older account and consistent behavior → positive |
| Tweet language and bio | Complete profile → positive |
| Consistency of posting style | Sudden major shift → negative |
| **Grok tone score (added in 2025)** | Positive and constructive content → positive |

⚠️ **New in 2025**: Grok AI now scores the **tone (sentiment)** of every post. Positive, constructive content is distributed more widely.

- Sources: [Circleboom TweepCred analysis](https://circleboom.com/blog/tweepcred-what-it-is-why-it-matters-and-how-to-increase-your-score-on-x-twitter/) | [Radaar](https://www.radaar.io/resources-121/blog-388/are-you-ready-to-discover-the-hidden-x-algorithm-secrets-behind-tweepcred-shadow-hierarchy-and-dwell-time-in-2025-15361/)

---

## 5. Treatment of Content Types

### 5.1 Text vs. Video: Is X the Only Platform Where Text Beats Video?

🟡 **Sources: Buffer's analysis of over 45 million posts and several media outlets**

**Conclusion: The picture is complicated and the data conflict.**

| Data source | Finding |
|----------|------|
| Buffer data, 2025–2026 | Median engagement for text posts (0.48%) slightly exceeds video |
| Several SEO and marketing agencies | Native video earns around 10× more engagement and preferential distribution |
| 2026 social strategy report | User preferences for short video (37%) and text (36%) are nearly even |

**More precisely**: Among major social platforms, **X is where text posts come closest to, or even surpass, video**. It is too simple to say text crushes video. Native video gets extra distribution weight, but good text posts can match video in actual engagement.

### 5.2 How the Algorithm Treats Each Format

🟡 **Source: Synthesis of several analyses**

| Format | Algorithmic treatment |
|----------|----------|
| **Text only** | Consistently the highest engagement rates, especially for sparking conversation |
| **Native video under 2:20** | Distribution boost; completion rate is a key signal |
| **Image post** | Increases dwell time, a positive signal |
| **External-link post** | ⚠️ Heavy penalty: reach decreases 30–50%; nearly invisible for non-Premium accounts |
| **Quote post** | More weight than a plain repost |
| **Thread** | Engagement across several posts adds up, producing good overall results |

- Sources: [Buffer](https://buffer.com/resources/data-best-content-format-social-media/) | [Sprout Social](https://sproutsocial.com/insights/twitter-algorithm/) | [SocialBee](https://socialbee.com/blog/twitter-algorithm/)

---

## 6. Key Time Windows

### 6.1 The Golden 30 Minutes and Engagement Velocity

🟡 **Source: Agreement across several analysts**

- **The first 30 minutes** are decisive: engagement speed tells the algorithm whether to push a post to a larger audience.
- More broadly, **the first two hours** also matter.
- **Velocity beats volume**: 100 likes in ten minutes beat 500 gathered in three days.
- The algorithm's logic: early engagement acts as a quality stamp.

### 6.2 Dwell Time

🟢 **Source: Weight definitions in the open code**

- A user spending over two minutes on your post or conversation adds +10 weight, about 20× a like.
- Short dwell time is treated as a low-quality signal and leads to reduced distribution.
- This means the algorithm favors **long pieces people want to finish** over **short pieces they scroll past**.

### 6.3 Best Posting Times

🟡 **Sources: Buffer's analysis of one million posts, Sprout Social, and SocialPilot's analysis of 50,000 accounts**

| Dimension | Recommendation |
|------|------|
| **Best hours** | Weekdays 9 a.m.–2 p.m. local time; 12–6 p.m. is next best |
| **Best days** | Tuesday, Wednesday, and Thursday (Tuesday is best) |
| **Worst day** | Saturday |
| **Posting frequency** | **3–5 per day** is optimal, 2–3 hours apart |
| **Upper limit** | Growth slows above five posts per day |
| **Lower limit** | Growth is markedly weaker below one post per day |

⚠️ The figures describe English-speaking users worldwide. Chinese-language creators should adjust for their audience's time zone (for example, the reference window for readers in Beijing time corresponds to approximately 9 p.m.–2 a.m. EST).

- Sources: [Buffer](https://buffer.com/resources/best-time-to-post-on-twitter-x/) | [Sprout Social](https://sproutsocial.com/insights/best-times-to-post-on-twitter/) | [SocialPilot](https://www.socialpilot.co/insights/best-time-to-post-on-twitter) | [Tweet Archivist](https://www.tweetarchivist.com/twitter-posting-frequency-guide-2025)

---

## 7. Shadowbans

### 7.1 Four Types

🟡 **Sources: Shadowban testing tools and community analysis**

| Type | Symptom |
|------|------|
| **Search Suggestion Ban** | Username does not appear in search suggestions |
| **Search Ban** | Posts do not appear in search results |
| **Ghost Ban** | Replies are invisible to others |
| **Reply Deboosting** | Replies are collapsed under “Show more replies” |

### 7.2 Triggers

🟡 **Sources: Pixelscan and several guides**

| Behavior | Risk |
|------|----------|
| Mass following or unfollowing in a short period | 🔴 High (mass unfollowing can trigger a three-month shadowban) |
| Liking 200+ posts within an hour | 🔴 High (automation detection) |
| Sending many replies to people outside your following list | 🟡 Medium |
| Repeatedly posting the same link or hashtag | 🟡 Medium |
| Using suspicious third-party tools | 🔴 High |
| Publishing content that many people report | 🔴 High (−369× penalty) |

### 7.3 Detection

- Online tool: Enter a username at [shadowban.yuzurisa.com](https://shadowban.yuzurisa.com/) to check for all four restrictions.
- Manual check: Ask someone who does not follow you to search for your username or look for your replies.

### 7.4 Recovery

🟡 **Source: Agreement across several guides**

1. **Stop the triggering behavior immediately**. Stop altogether instead of tapering off.
2. Delete repetitive or low-quality posts and ones with excessive links or hashtags.
3. Revoke access for suspicious third-party apps.
4. **Wait 48–72 hours**. Automatic shadowbans usually lift during this interval.
5. Full recovery takes **2–14 days**.
6. During recovery, post normally, infrequently, and with an emphasis on quality.

- Sources: [Pixelscan guide](https://pixelscan.net/blog/twitter-shadowban-2025-guide/) | [Tweet Archivist](https://www.tweetarchivist.com/twitter-shadowban-complete-guide-2025) | [Multilogin](https://multilogin.com/blog/twitter-shadow-bans/)

---

## 8. Advertising and Organic Growth

### 8.1 Paid vs. Organic Performance

🟡 **Sources: WebFX and media reports**

| Metric | Paid promotion | Organic posting |
|------|----------|----------|
| Average click-through rate | 1–3% | 0.5–1.5% |
| Premium account reach | — | About 10× that of ordinary accounts |
| Engagement on link posts, non-Premium | — | 0 (after March 2026) |

### 8.2 Key Findings

🟡 **Source: Several analyses**

- The paid and organic algorithms **operate independently**. Paying does not trigger a reduction in organic traffic.
- The structural trend is still declining organic reach, a widespread phenomenon rather than one unique to X.
- New followers acquired through ads **do affect** later organic performance. More followers mean more in-network distribution.
- Premium is effectively **the least expensive ad spend**. Its 4× and 2× visibility boosts outperform equivalent ad spending.

- Sources: [WebFX](https://www.webfx.com/blog/social-media/x-twitter-marketing-benchmarks/) | [Avenue Z](https://avenuez.com/blog/2025-2026-x-twitter-organic-social-media-guide-for-brands/)

---

## 9. Impact of Community Notes

### 9.1 Impact on Post Performance

🟢 **Source: University of Washington research (September 2025)**

| Metric | Change after a Community Note |
|------|--------------------------|
| Reposts | **Down 46%** |
| Likes | **Down 44%** |
| Views | Small impact (feed algorithm does not actively downrank posts with a note) |

### 9.2 Key Details

- X **does not actively reduce** the algorithmic distribution of posts with a Community Note.
- The decline mainly comes from **changed user behavior**: after seeing a note, users repost and like less.
- **Timing** is crucial. Notes added after 48 hours have almost no effect because the content has already circulated.
- Notes addressing **manipulated media**, such as fake photos or video, have the largest effect.

### 9.3 Implications for Creators

🔴 **Inference and strategic advice**

- Cite a source when publishing factual claims likely to cause controversy.
- A Community Note does not directly lower the algorithmic weight, but **sharply reduces engagement indirectly** (reposts −46%).
- A noted post may get the same views yet lose roughly half its ability to spread.
- Constructive, sourced content is less likely to get a note.

- Sources: [University of Washington study](https://www.washington.edu/news/2025/09/18/community-notes-x-false-information-viral/) | [Wikipedia - Community Notes](https://en.wikipedia.org/wiki/Community_Notes)

---

## 10. Key Implications for Creators

### 10.1 Optimization Priorities by Return on Investment

| Priority | Strategy | Rationale |
|--------|------|------|
| **P0** | Start conversations and reply to each comment | Conversational replies carry 150× weight |
| **P0** | Subscribe to Premium | 4×/2× visibility, a TweepCred boost, and visibility for link posts |
| **P1** | Build engagement in the first 30 minutes | Engagement speed determines distribution |
| **P1** | Write long posts worth stopping to read | Dwell time carries 20× weight |
| **P2** | Post from 9 a.m. to 2 p.m. on weekdays | Best time according to the data |
| **P2** | Avoid external links or put them in the comments | Reach penalty of 30–50% |
| **P3** | Keep a positive, constructive tone | Grok's tone score affects distribution |
| **P3** | Use no more than two hashtags | More than two triggers spam classification |

### 10.2 Practices to Avoid

| Behavior | Consequence |
|------|------|
| Mass following or unfollowing in a short period | Three-month shadowban |
| Using automation to inflate engagement | Permanent damage to account reputation |
| Frequent external links on a non-Premium account | Posts are nearly invisible |
| Posting content that gets reported | −369× penalty; content disappears |
| Abruptly changing posting patterns | Lower TweepCred |

### 10.3 What X Offers That Other Platforms Do Not

- **Only major platform to open-source its algorithm twice**: Enables precise optimization.
- **Text-friendly**: Unlike some platforms, it does not force you into video.
- **Conversation-driven**: Rewards deep exchanges rather than shallow interactions.
- **Promptable feeds**: Users can customize recommendations, giving good niche content lasting value.

---

## Appendix: Source List

### Official and Primary Sources
- [xai-org/x-algorithm GitHub](https://github.com/xai-org/x-algorithm) — Grok algorithm released as open source in January 2026.
- [twitter/the-algorithm GitHub](https://github.com/twitter/the-algorithm) — First open-source release in 2023.
- [Elon Musk post (September 2025)](https://x.com/elonmusk/status/1969081066578149547) — Announces a fully AI-driven algorithm.
- [@XEng post (January 2026)](https://x.com/XEng/status/2013471689087086804) — Announces the open-source release of the new algorithm.

### Established Media Coverage
- [TechCrunch: X open sources its algorithm](https://techcrunch.com/2026/01/20/x-open-sources-its-algorithm-while-facing-a-transparency-fine-and-grok-controversies/)
- [Social Media Today: Key ranking factors](https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/)
- [Social Media Today: Grok algorithm shift](https://www.socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174/)

### Data Analysis
- [Buffer: Best content format in 2026 (45 million+ posts analyzed)](https://buffer.com/resources/data-best-content-format-social-media/)
- [Buffer: Best time to post (one million posts analyzed)](https://buffer.com/resources/best-time-to-post-on-twitter-x/)
- [Sprout Social: Twitter algorithm 2026](https://sproutsocial.com/insights/twitter-algorithm/)
- [University of Washington: Community Notes study](https://www.washington.edu/news/2025/09/18/community-notes-x-false-information-viral/)

### In-Depth Community Analyses
- [posteverywhere.ai: Source-code analysis](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works)
- [Typefully: Algorithm update analysis](https://typefully.com/blog/x-algorithm-open-source)
- [Circleboom: In-depth TweepCred analysis](https://circleboom.com/blog/tweepcred-what-it-is-why-it-matters-and-how-to-increase-your-score-on-x-twitter/)
- [nibzard: Rust and Python architecture analysis](https://nibzard.github.io/twitter-algorithm-tufte/)
- [ByteByteGo: Illustrated algorithm architecture](https://blog.bytebytego.com/p/the-algorithm-that-powers-your-x)
- [Pixelscan: Shadowban guide](https://pixelscan.net/blog/twitter-shadowban-2025-guide/)
- [DeepWiki: x-algorithm repository analysis](https://deepwiki.com/xai-org/x-algorithm)
