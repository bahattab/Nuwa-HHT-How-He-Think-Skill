# Quality Checks + Antipatterns + Analytics Review + Report Template

> Load on demand for Scenario C (content review), Scenario E (account diagnosis), or an analytics review.

---

## Quality Checklist

When reviewing an existing post or thread, check each item:

### Post Checklist
- [ ] Does the hook grab attention within 2 lines?
- [ ] Does the post answer “Who is it for? What is it about? Why should they read it?”
- [ ] Does it include specifics, such as numbers, times, or names?
- [ ] Does it invite replies rather than just likes?
- [ ] Is the post free of external links? (If needed, put them in the first reply.)
- [ ] Will it go out when the target audience is active?

### Thread Checklist
- [ ] Does the first post stand on its own and draw readers in?
- [ ] Does the thread follow a 1/3/1 rhythm?
- [ ] Does each post advance the content? (Rate of Revelation)
- [ ] Is there a TL;DR summary?
- [ ] Is there a clear call to action (CTA)?
- [ ] Is the thread 8–12 posts long?
- [ ] Does it use bullet points instead of walls of text?

### Content Strategy Checklist
- [ ] Did you publish at least 1 thread this week?
- [ ] Did you leave high-quality replies to posts by major accounts?
- [ ] Is there a CTA that directs readers to the newsletter?
- [ ] Did you respond to this week’s trending AI topics?
- [ ] Is the mix of short posts and threads appropriate?

---

## Antipatterns and Pitfalls

### Growth Traps to Avoid

1. **Buying followers or joining follow-for-follow and like-for-like groups**: The numbers look good briefly, but TweepCred plummets in the long run. The algorithm downranks unnatural engagement patterns, so the trade-off is not worth it.
2. **Publishing tool roundups with nothing of your own**: AI is already a crowded field. Everyone publishes posts like “10 AI tools you need,” so they do not stand out. Add your own test data and a distinct point of view if you publish one.
3. **Only translating international AI news**: That gives readers nothing they cannot get elsewhere. Add your own take, such as “Why this matters to developers in China” or “I tested it, and here is what actually happened.”
4. **Chasing trends at the cost of your positioning**: If you jump on every trend, followers will not know what you stand for. Pick only the trends that fit your niche.
5. **Writing a hook without substance**: Clickbait works in the short term but costs you followers over time. Hormozi recommends overdelivering. Promise one thing and deliver three.
6. **Posting without replying**: The weight assigned to conversations is 150×. By not replying, you give up your biggest lever with the algorithm.
7. **Letting threads run too long**: Readers start dropping off beyond 15 posts. The sweet spot is 8–12.

### Platform-Wide Risks to Watch

- **Engagement is down across the platform**: X’s overall engagement rate fell by 48% from 2024 to 2025. That is a platform-wide trend that is not specific to your account.
- **Increasing pay-to-play**: Organic reach for non-Premium users continues to shrink, and reach for posts with external links is almost zero. Premium is a necessity, not an option.
- **User migration**: Some creators are spreading their activity across Bluesky and Threads. For now, X remains the main platform for AI and tech content.

---

## Analytics Review Guide

### Key Metrics in Order of Priority

| Metric | What to Measure | Benchmark |
|------|--------|-----------|
| Engagement rate | Engagements / impressions | >2% is good, >5% is excellent |
| Reply rate | Replies / impressions | Higher is better (the algorithm gives replies the greatest weight) |
| Profile visit rate | Profile visits / impressions | >1% suggests people want to learn more about you |
| Follower growth | Net new followers per week | 5–10 per day during the cold-start phase, 20–50 per day during the growth phase |
| Bookmark rate | Bookmarks / impressions | A high bookmark rate indicates valuable content |
| Newsletter referrals | New subscriptions per week | Any new subscriptions are a good sign. Keep tracking the conversion rate. |

### Review Cadence

- **Daily**: Scan the previous day’s performance and flag high-performing posts with >500 engagements.
- **Weekly**: Analyze the week’s top 3 posts, identify their shared features, and update the template library.
- **Monthly**: Review the follower growth curve, the distribution of content types, and newsletter growth. Adjust next month’s content strategy.

### Diagnostic Framework for Underperforming Posts

Check these in order:
1. **Algorithm**: Is Premium enabled? Was the timing right? Is there an external link?
2. **Hook**: Do the first 2 lines spark curiosity by leaving an open question? Do they give readers a reason to trust you?
3. **Content**: Does each post advance the content? Is there a 1/3/1 rhythm?
4. **Audience**: Do you have enough followers to build engagement velocity? If not, start by reaching people in other accounts’ replies.

---

## HTML Report Template Requirements

Use an Economist-style newspaper layout for the diagnostic report. Include the following:
- **Visual style**: Serif typeface (Georgia), warm paper background (#f5f0e8), red accent (#C7000A), and a grid layout.
- **Data visualization**: Load ECharts.js via CDN. Include at least a topic distribution chart, a time distribution chart, and an engagement funnel.
- **Required sections**:
  1. Banner + masthead (one sentence stating the main finding as the headline)
  2. KPI grid (4 key metrics displayed as large numbers)
  3. Lead (summary paragraph in italics with a red left border)
  4. Content ROI analysis (compare engagement by topic)
  5. Distribution funnel (like rate, bookmark rate, repost rate, and reply rate)
  6. Timing analysis (best times to post and how posting cadence has changed)
  7. Brand narrative (distribution of narrative roles and their engagement performance)
  8. Top 5 recommendations (red numbered circles + title + description + supporting data)
  9. Footer (data period, sample size, and time of analysis)
- **Reference implementation**: `user-data/AlchainHust/report_20260406.html`
