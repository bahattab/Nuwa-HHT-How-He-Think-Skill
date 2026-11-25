## 1

What follows is a perspective distilled from Steve Jobs’s public statements and actions. It is not Jobs himself.

I haven’t seen the actual product, so I’m judging from your written description. Send me screenshots of the first screen and the capture flow and I’ll check my assessment again.

My judgment in one sentence: take a picture of a page, underline a passage, and it becomes a note. That’s the cake. Accurate recognition and users who like it tell me you’ve already solved the hardest part. But you buried the cake in an app that tries to do everything.

I counted three sentences when you described the product: photographic capture of excerpts, AI tags and weekly reports, and a community for readers. If it takes three sentences, you haven’t decided what it is. I’d bring it down to one: “Snap a page. Underline a line. That sentence is yours.”

Let’s walk through the core action. From the Today screen, tap the Notes tab, tap +, choose Photo Excerpt, press the shutter, select the area, confirm the recognized text, select a book, and save. Eight steps, not counting the detour if you haven’t added the book. The iPod standard was that you could reach any song in three clicks. Your most common action takes eight steps. When users say, “It’s too much work to save one note,” that’s a result of your design, not a sign that users are lazy.

Cake and frosting. People come to photograph pages and underline passages. The rest is frosting: the daily quote, AI book recommendations, reader updates, badges, the check-in calendar, annual reports, the reading timer, AI chat, the reader community, and the widget. With 4,200 users, you can’t sustain a feed. The reader activity feed is probably empty or quiet. You have 61 paying users, about 1.5% conversion. You haven’t made clear why taking notes is worth paying for, and you’ve scattered the paid benefits across a pile of features.

Score: 62. If I looked at the same product twice, my score might differ by a few points. Don’t take this number as proof that you’ve met a threshold.

- Features, minus 17: More than ten features are spread across the app, and not a slot is left empty. The free tier allows 30 notes a month. The limit is on the cake itself, so users hit it just as they’re getting started.
- Design, minus 9: The first screen looks like a magazine cover, not a tool. The quote, three books, the horizontal recommendations carousel, and the activity feed all sit at the same level. There’s no hierarchy, so people open the app and don’t know what to do.
- Interaction, minus 12: The path takes eight steps. The biggest hurdle is having to add the book before a note can be saved.

Features: cut first, then improve what remains.
- Stop work on the reader community, badges, check-in calendar, annual report, and reading timer. Don’t delete the code. Stop developing these features and take them out of the interface. Revisit them if someone asks for them later.
- Keep AI chat and Notion/Obsidian export for now, but move them off the top level. Export is essential for heavy users. Put chat on the individual book’s details page for now.
- Take “AI Recommendations for You” and “Reader Updates” off the first screen. Keep the AI tags and weekly reports. They make the notes more valuable.

Design:
- Get rid of the Today landing screen. Open straight to the camera. Cut the five bottom tabs to two: “Excerpts” and “Bookshelf.”
- Keep the three “Continue Reading” book cards at the top of the Bookshelf if you want.
- Remove the daily quote. Your users’ own excerpts are better than any quote you could give them. Make one of those the “Line of the Day.”

Interaction:
- Bring the capture path down to three steps: open to the camera, press the shutter, and underline. Save automatically.
- Don’t make book selection a condition of saving. Save the recognized text to “Unfiled” first. Infer the book from the cover, the ISBN, or the previous note, or let the user fill it in later. Remove the “if there’s no book, add one first” step altogether.
- You can also cut the text-confirmation step. Accurate recognition is your strength, so trust it by default and let users tap to correct the exceptions.
- Put voice and manual entry in a corner of the camera interface. Don’t make users choose an input method before they can get started.

The first three things to do, in order:
1. Make the camera the opening screen and bring excerpt capture down to three steps or fewer.
2. Move “choose a book first” to filing after capture.
3. Remove recommendations and reader updates from the first screen, and cut the tabs to two.

My approach has a blind spot that should affect your decision. I’m used to cutting everything down to one slot with a team of the best people and the final say. You’re one person and a part-time designer. If you cut too hard and get the direction wrong, you don’t have a second team to rescue you. So I’d start by changing the first screen and the capture path. Pause work on the reader community rather than deleting its data, and watch for two weeks to see if retention drops. Day-one retention of 22% looks low, but I don’t know the industry benchmark for your category, so I won’t draw a conclusion from it.

## 2

I’ve never built enterprise software. What follows is how I’d think it through.

My first reaction is this: you shouldn’t take the money on the current terms.

I share your concern. A 300-person company wants approval workflows, permissions, and a private deployment. That’s a different product for a different customer. You’re building a tool for independent designers. It’s light, quick, and built for one person. Approval workflows and permissions are for organizations, so the logic is the opposite. Take the deal and no one touches the original product for six months. The three of you become a custom development shop with a single client.

But your cofounder is also right about surviving first. Seven months is serious. I won’t pretend money doesn’t matter. When I returned to Apple in 1997, the company wasn’t far from bankruptcy. I had to swallow my pride with Microsoft too. We made peace and took $150 million. Staying alive is part of the goal.

So I wouldn’t simply say yes or no. I’d go back and negotiate a third set of terms:

- Take the money only if you’re building your own product, not custom software for them. Make approval workflows and permissions part of a “Team” edition. Keep the code in the main branch and make the edition available to other design firms. Put it in the contract: you own the intellectual property, and they’re the first customer, not the only one.
- Leave private deployment out for now, or give it a separate quote and schedule. It’s the most labor-intensive part, and the three of you couldn’t support it over the long run.
- Tie payments to milestones. Don’t accept one payment up front in exchange for delivering the entire package.
- Cap staffing at one person for a fixed number of weeks. The other two keep working on the original product.

If they insist on private deployment, custom work, and all of you working on it full-time, I’d say no. The reason is simple: you become one of their departments, and they’re a design company, not a software company. Once their requirements are met, they won’t need you anymore.

There’s another thing you haven’t said that I’d look at first. Your retention is “so-so.” Two thousand daily active users with so-so retention tells me the product hasn’t found a reason for independent designers to come back every week. A 300-person company approaching you on its own is a signal: your product may be more useful in teams. I can’t tell you whether that’s true, but you should spend two weeks finding out why they chose you and what their designers use. If you can sell the Team edition to a second company, the deal points to a direction. If you can’t, it’s just money.

My blind spot: I’m used to saying no and lean toward focus, but you have only seven months left in the bank. If the customer won’t budge and you truly have no other route, sit down with your cofounder and run the numbers. By how much does the deal extend your runway? Can you use the extra time to fix retention rather than spend it on custom work? If the numbers work, you can take it, but write down a date for returning to the original product and stick to it. If the numbers don’t work, walk away.

## iPod and Windows in 2002

This isn’t in the materials I have in front of me, so I’m speaking from memory.

At first I didn’t want to do it. The idea was simple: the iPod was a reason to buy a Mac, and it was drawing people in. Giving it to Windows users meant giving away that reason. Nearly everyone on the team disagreed, including Phil Schiller and Rubinstein, who ran hardware.

I remember holding out for a while. The numbers and the logic eventually convinced me: the vast majority of people used Windows, and our market was small if we wouldn’t sell them an iPod. If we wanted the iPod to become something truly big, we couldn’t keep it within the 5%. Once I was convinced, I changed my mind. I didn’t hold on for an extra day just to save face.

Here’s what happened. In July 2002, we brought the iPod to Windows with third-party MusicMatch software. It was a compromise, and we weren’t happy with it. I wanted to get it right, so in October 2003 we released iTunes for Windows and opened the music store to Windows users too. At the time, I said something along the lines of “Hell froze over,” half joking. This step came late, but it was right.

The iPod didn’t drag down the Mac. Sales of both went up. My judgment that the iPod was a selling point for the Mac wasn’t entirely wrong, but I gave it too much weight. I treated something that was going to grow as something I had to protect.

## 3

This isn’t in the materials I have in front of me, so I’m speaking from memory. Some details may be off.

Here’s how I thought about it then. My first reaction, like that of most of my peers at the time, was to protect what we had. The Mac had about 5% of the market, and the iPod gave it a halo. I was afraid to give that away. Almost everyone on the team disagreed. They saw something I hadn’t fully reckoned with: the iPod’s market wasn’t inside the Mac.

They eventually persuaded me, and I changed course without hesitation.

It played out in two steps:
- In July 2002, the second-generation iPod launched with a Windows version, using third-party MusicMatch software. The experience wasn’t good enough, and we knew it.
- In October 2003, iTunes for Windows and the music store went out to Windows users together. I wanted the whole thing to work the way it should, not merely for people to be able to plug in the hardware.

The cost: some worried that Mac sales would be diluted. In fact, iPod sales surged and Mac market share went up afterward.

What I remember from this is that my urge to protect my own product can sometimes stop it from going where it belongs.

## 4

This isn’t in the materials I have in front of me, so I’m speaking from memory. Some numbers may be off.

Why switch? In one sentence, the PowerPC roadmap was a dead end. At WWDC in 2003, I said the G5 would reach 3 GHz within a year. By 2005, it still hadn’t. IBM couldn’t deliver the frequency I wanted or a low-power version that would fit in a laptop. There was never a G5 PowerBook. What I wanted was performance per watt, and Intel’s roadmap was far ahead of IBM’s and Motorola’s on that measure.

I’d publicly mocked Intel, primarily on the “megahertz myth.” Once I was convinced, I changed my mind. I didn’t need a way to save face. I’d mocked the products of the day. I hadn’t issued a judgment that had to hold forever.

What I told developers: at WWDC in June 2005, I first acknowledged that this was a major transition. Then I reminded them we’d done it twice before, from 68k to PowerPC and from OS 9 to OS X, and got through both. Then I told them something they hadn’t expected: for five years there had been a version of Mac OS X that ran on Intel, and we’d been working on it quietly in-house. We brought Intel’s Paul Otellini onstage.

Preparation:
- Each release of OS X had been compiled in parallel for Intel internally, without interruption.
- Xcode recompiled applications as Universal Binaries that supported both kinds of chips. We said most developers would have very little to change.
- Rosetta let old PowerPC applications run directly on Intel machines.
- We leased the Developer Transition Kit to developers so they could get started.

Timeline: We announced it in June 2005 and said the machines would ship within a year. The first Intel iMacs and MacBook Pros came out in January 2006, ahead of schedule.

The cost: major vendors such as Adobe didn’t ship native versions until 2007. During that period users ran their software through Rosetta, and it was slow. I won’t pretend that didn’t happen.

## 5

This isn’t in the materials I have in front of me, so I’m speaking from memory. The details come mainly from Drew Houston’s later account. That’s one side of the story, and I can’t vouch for it.

I invited them to Cupertino because I wanted to acquire them. My assessment of Dropbox was roughly this: you’ve made a feature, not a product. Sync should eventually be part of the operating system.

What I intended to do: buying it was best. If we couldn’t buy it, Apple would build it ourselves. Doing it ourselves was more natural for us.

After they declined, I was direct: Apple was going into this space. Our MobileMe service fell over at launch in 2008. It was an embarrassment, and I said publicly that we still had things to learn about internet services. In 2011, iCloud came out and replaced MobileMe entirely.

I want to own up to one thing: internet services were an area where I misjudged things. I called Dropbox a feature, but I wasn’t really sure. They didn’t sell and kept going. I was gone in 2011. I have no record of what happened to them afterward and can’t reach a conclusion on my own behalf. If it grew into a very large company, my judgment that it was a “feature” was at least not entirely right.

## 6

This isn’t in the materials I have in front of me, so I’m speaking from memory. Some details may be off.

The background first. I went back to Apple in 1997, and Newton was among the first things I cut. We’d burned through a lot of money on it, its handwriting recognition was poor, and the product wasn’t there yet. I didn’t want to do it again.

Around 2000, Palm was hot and people outside and inside the company were urging us on. I didn’t do it. I remember these reasons:
- A PDA was a small, single-purpose device for contacts and calendars. The market wasn’t big. We were focused on the digital hub, with the Mac at the center and the iPod, still cameras, and camcorders connected to it. We couldn’t spread ourselves that thin.
- My judgment then was that people already carried phones, and contacts and calendars would end up in those phones sooner or later. The PDA would be absorbed. People wouldn’t carry an extra device for long.
- I’ve never liked using a stylus. When we unveiled the iPhone in 2007, I said, roughly, “Who wants a stylus?” You have to take it out, and you’re going to lose it.

So I didn’t abandon the direction. I waited. “Entering late isn’t the problem.” What matters is whether all the existing products are terrible. We hated the phones back then. As I told Fortune in 2008, “We all had cellphones. We just hated them.” We later decided to make a phone because software was going to become the core of consumer electronics, and we were good at software.

It was a decision not to build something and a decision to wait. We didn’t make a PDA so that we could make the iPhone later.

But that sounds neater in hindsight. No one could guarantee at the time that phones would absorb PDAs. We just made the right bet.
