---
title: "Episode 238 Transcript"
draft: false
_build:
  list: never
  render: always
---
[00:00:12] McIntosh:

Hey, Kenshin. 

[00:00:13] Kenshin:

Hey, McIntosh. 

[00:00:15] McIntosh:

What is that noise? 

[00:00:17] Kenshin:

Like bells, jingles. 

[00:00:20] McIntosh:

Is Santa coming to town? Oh, 

[00:00:23] Kenshin:

it's coming tomorrow, here at least. Yeah. 

[00:00:26] McIntosh:

Welcome back to Satoshi's Plebs for episode two thirty eight. I'm Macintosh. I am Kenshin. 

[00:00:31] Kenshin:

And in today's episode, we ask, were we wrong about Bitcoin in 2025? 

[00:00:40] McIntosh:

Hold on. Oh, that was awesome. Alright. I hope that was okay with everybody. We're just having a little fun. We are recording here on the December 23, two days after the winter solstice. How's the sun doing up there sweet in Sweden? 

[00:00:57] Kenshin:

Oh. 

It's actually finally from yesterday. Right? It starts getting longer days. That's correct. Yesterday. So that's great. I must say the sun comes up at nine and goes down at 3PM before three 02:50 something. So it's not great. Man. When the sun is crazy. Yeah. And when the sun is up is where we live we're a bit we have some trees around so the sun never comes over the trees actually. So we never get a direct sunlight this time of the year. 

[00:01:33] McIntosh:

So what are we talking about this week Kenshin? 

[00:01:37] Kenshin:

I mean we did some projections. Projections. We had high hopes for 2025 and yeah. 

We it's like a year in review to see how the the year I 

[00:01:50] McIntosh:

don't wanna brag, but there's a lot of podcasts taken this week off and here we are, We Pension and are recording and you will have this before Christmas Day in your hot little hands. So Merry Christmas. 

[00:02:08] Kenshin:

Yeah. Alright. That was a jingle there. 

[00:02:12] McIntosh:

Enough of that. Oh, we're throw in a jingle there? I know. I I heard something you did with a spoon or something. Oh, was a day. I was playing with a key and I dropped it on I dropped it on the desk. What's going on with you, Kenshin? 

[00:02:28] Kenshin:

Well, I'm off work so that's great. 

But just doing a lot of house preparations these days, cleaning up, you know, having family coming over next two days. So nothing much. Trying to get my handle around chat GPT in the last few days and moved all my repo from GitLab to GitHub in the last few days. Why is that? Because I realized GitHub, of course, is more mainstream and for this specific project, I want more mainstream compatibility, let's say. So even Charge GPT and other tools, they have direct connection to GitHub 

[00:03:21] McIntosh:

or Easier Yeah. 

[00:03:22] Kenshin:

To do some stuff. Mhmm. So and I'm like and when I will hire programs in the future, I bet they will prefer GitHub or they will have a GitHub account. So I said, at least for this project, I need to to to go to GitHub. 

So I've been moving things around and doing that. I've been learning better flows, let's say, that I didn't do before and with my super based database background. Better flows, how to push the database changes there. So I'm surprised how, yeah, manual things I was doing before and now I'm doing more and more the the proper way I would say. So, yeah, it's been taking some time to That's good. To learn those new workflows. 

[00:04:13] McIntosh:

Before we move on, I gotta find out tomorrow's the big day. Right? So you're gonna be watching the Disney movie? 

[00:04:25] Kenshin:

Maybe. 

Maybe. I was just trying to remember, do we have TV? I was trying to remember that because we're They don't stream it? Yeah. That's what I thought. They it's probably streamable because we we don't have an actual TV antenna connected. We just stream everything. But I think the Swedish yeah. The Swedish app has that. Yeah. They stream the the the two channels. We never do it. We do it once a year, basically, for things like that. Right. Where my wife's parents are here. But, yeah, I think they will stream it there. So 3PM tomorrow, we should be sitting in front of the TV like a good Swedish family. Swedish people. Yeah. 

Together with the rest of Sweden to watch Mickey Mouse and Santa Claus making presents. 

[00:05:18] McIntosh:

That is that you know, well, we discussed it last year as well. I don't know. That that that tradition just kinda trips me out. It's like, that's that's so funny. Hey. I I'm going to I don't even remember how this came up. But a few minutes ago, well we were talking actually, I do remember. We were talking about energy usage in Europe. Isn't that what everybody talks about? Mhmm. I mentioned Norway because they produce a lot of oil, of course. They sit right there off of a vast oil field and they make good use of that they're smart people. And I learned something today, and I should be ashamed. 

Again, my European history, I need to go back to high school and either get on to my teachers, I'm trying I know I learned European history, I did, but apparently not in enough detail. So I found out today that Norway basically only became an independent country from Sweden of all people in nineteen o five. Yeah. So I looked this up, apparently, I'm gonna give you the short version. Before the Napoleonic Wars, which were in the early eighteen hundreds, Norway was part of Denmark. So I under the way I understand that now, I think I'm I don't think I'm incorrect in this. Essentially, Denmark, the Danes, that's where the Vikings are kind of originated from. 

They moved into Norway and took over that essentially. And because I guess they lost, I don't know. I don't know that much about the Napoleonic Wars other than Napoleon was involved and he did lose. That is true. That's why he got banned to the Isle Of Sicily, I No, wanna it's in the Mediterranean though. Is it Malta? It's a smaller island. Not Patmos, that was John. No, Malta. Anyways he would he was banned to an island and man this is embarrassing. I should've looked this up but I didn't think I was gonna bring it up. Anyways, he lost the war. 

Apparently Denmark was aligned with him and they were forced to cede Norway to Sweden. So that was in the early eighteen hundreds. A hundred years later, basically, Sweden said, go off and do your thing. And then just a few years after that, some dude in Pennsylvania, if I'm remembering correctly, figured out that oil was a thing, that it was we could, like, run cars with it and kind of, wow, Sweden, you lost. Sorry. 

[00:08:15] Kenshin:

I don't know what to say. Yeah. Yeah. If that was fifty years later they would never give up Norway. But 

[00:08:22] McIntosh:

No, probably not. And interestingly enough I also found out that basically Sweden and Norway speak at least very similar languages. It's kinda like different dialects or whatever, which I did not again, I didn't know. I I always have operated under this idea that even though they're all, you know, six foot tall blonde and nice looking, which that's not, what's the word, characterization or whatever. 



[00:08:54] Kenshin:

Beyond that, I assumed that they were super distinct from each other. No. Turns out I was wrong. No. What what I thought, I thought all of the Nordic countries were the same. So I thought Right. Even Finland was the same. But then I went to Finland and it has nothing to do with Sweden and the rest of Scandinavia. 

[00:09:14] McIntosh:

So it is different than the other two? Very different. I guess Denmark is considered to be part of Scandinavia. 

[00:09:20] Kenshin:

Yeah. Right? Yeah. Denmark, Sweden and Norway they're basically the same countries. Right. But Denmark is really attached if I'm on No. There is a a water between Denmark and Sweden but there is a bridge. No. I mean attached to Mainland Europe. Oh, Yeah. Right? Yeah. Yeah. It is. Yeah. 



[00:09:39] McIntosh:

Which that's always that always throws me off. Right? It sticks out into the North Sea. Yeah. I was correct. I was what I was thinking anyways. Alright. Well, there you go. Today's educational lesson. 

[00:09:52] Kenshin:

Oh, yeah. And nap Napoleon was exiled to Saint Helena Island in the middle of the Atlantic. 

[00:10:01] McIntosh:

Wait. Yeah. Thought it was in the Mediterranean. I believe you. It's on Look. I'm bad at this stuff. Obviously, I'm really bad at Europe. I'm so sorry. Maybe this is why our European numbers are so low. Mean Maybe we need to investigate that. I've been meaning to talk to you about that actually. I was looking at our stats and we got some places we gotta prop some things up. 



[00:10:26] Kenshin:

Yeah. 

[00:10:27] McIntosh:

Let me download that. Okay. There it is. Oh, wow. It's really in the middle of Really? It was I thought it was up near he's he was that far down? Yeah. It's basically South Africa kind of or middle I guess they were afraid he was gonna like try and take over the world or something. I don't know. I 

[00:10:47] Kenshin:

had no clue either. But it's it's hard with history where you cannot know everyone's history. I mean, it's like barely know American history. Well, true. 

[00:10:58] McIntosh:

Right. Yes. You didn't even know about the Boston Tea Party. No. What was that? Never mind. We're not going down that road again. 



[00:11:08] Kenshin:

Right. Alright. 

[00:11:11] McIntosh:

I think for us you know we're we're kind of pretty low key this year I think. I was telling you earlier we're gonna be going out with some friends tonight to go see some Christmas lights. Tomorrow we don't watch Disney. We do watch Christmas movies, and it was kind of funny. I joke when I say this, but I am semi serious. This is gonna sound crazy. There's things in this movie that I can't recommend. It's it's rated R and it's rated R for a reason, but National Lampoon's Christmas Vacation is not only hysterically funny, I think it actually gives a really good picture. 

Very exaggerated, but a really good picture of Christmas. Certainly back in the eighties and nineties. Maybe not so much today, but it was filmed in like, I think it came out in like nineteen nineties, so it portrayed that era very well. Chevy Chase is the main actor which he's a well known comedian. He plays the father and I don't know. Anyways, we'll probably watch that at some point. What was the name? Maybe we should It's called Christmas Vacation. I think it's rated R. It may be PG-thirteen. I hope it's not rated R actually. Here I am recommending rated r movies. 

I think it's p g 13, actually, now that I think about it. It was this says it was '89. And it's at National Lampoon's Christmas Vacation and that is not it. Yeah. PG 13. So I mean there are some things that are inappropriate. I would not want my small child watching them. That kind of thing. But overall it's it's very very funny and I'm dead serious. It's it's like, I don't know, they managed to get it. That's kind of like what it was. Extremely exaggerated, whatever, but yeah. Yeah. And that's kind of it. Know, we're gonna kind of celebrate a quiet Christmas here with our family. I we will be having Christmas dinner here at our house with our family and some extended family and that's about it. Cool. 



[00:13:32] Kenshin:

Nice. Any cool gifts? 

[00:13:38] McIntosh:

Don't know what Santa's bringing. What are you talking about? So I I have actually taken over the kind of the gift buying in large part for our family. Don't know why I'm whispering like nobody can hear. Don't want anybody to hear this. No. Actually everybody in the family knows this. I started doing this, it's been a bit now, three three, four years ago. Mhmm. I really enjoy gift giving and so I offered to start doing that and I have done so. So I go out and you know do all things. This year I will say this, there's gonna be a lot of art supplies that are coming to the Macintosh household this year. It's funny because it's the children, they didn't talk to each other about this, but three of them, in fact, are asking for art supplies. And in fact, I even had some art supplies on my list too because one of the things I want to do in 2026 is try and learn to watercolor. It's something I've been wanting to do for a long time. Wow. 

And I really kind of want to work on that. I don't know, I don't know. 

[00:14:57] Kenshin:

We'll see. Good luck. 

[00:15:01] McIntosh:

I think I might need that Christmas miracle is what I might need. But I am going to try. I've learned that if I don't try I will never do it. Have 

[00:15:13] Kenshin:

I told you last year how the gifts are coming in the how Santa is bringing the gifts in Sweden? In a sleigh? No. But I mean What? No. The gifts are coming on the twenty fourth right after this Disney movie, right? Okay. In the afternoon then. So what happens is the father in the family usually, he remembers that he needs to go buy the newspaper during that Mickey Mouse thing. Right? Right. So he leaves the house, comes back dressed as Santa Claus with a big bag and he brings the gifts to the family. That's how they did. Yeah. 



[00:15:58] McIntosh:

I've never dressed up as Santa. I I don't know. We we we have we just have presents under the tree. Yeah. And wrapped mostly and, you know, some in bags and like gift bags with the stuff. 

[00:16:16] Kenshin:

We do the same. We had actually quite a fun interaction with our son a few days ago and he said something about Santa coming with a gift or something. Mhmm. And I look at my wife and and we're like, wait a second. She thinks Santa is real? We never because I'm pretty sure we told him that it's fake and everything. We didn't want him to to get to get sucked into this for his whole childhood, basically. Right? Right. 

So and he starts to talk like, oh, what should we leave for Santa? Like a little biscuit or something and milk and all this? And I'm thinking, oh, shit. Oh, sorry. What should we do now? How should we treat this? And then also my wife is like, I don't know. What should we do? I'm like, okay. But let's let's just ask him now and Right. Let's get it over with because I I don't want to to keep doing playing this this Right. This story. And then I told him like, but you know, Santa is not real. Right? He said, yes. I know. He said, very you know, in obvious ways. Right. And he's six years old. Right? And he was really funny. He said, yeah. Of course, I know. But but at school, some kids were saying that he's real. But I told them he was not real. And I'm like, oh, no. 

Yeah. So he's 

[00:17:42] McIntosh:

ruining Christmas already for everyone. That's a fun age. Do we do? Do we tell them? Do we not? Do we you know? Do they go tell the other kids? Yeah. It's kinda crazy. Alright. Oh, one final thing. Sorry, I forgot. I told y'all last week I was looking at the IPTV stuff. Oh, yeah. Man, I can't make it. I can make it work but I'm not going to. It is too much trouble. The services that provide it are super shady. Mhmm. Stuff changes all the time like you it would just be a lot of work. I'm just gonna have to, I don't know, figure this out different ways for these different feeds or whatever. 

I don't know. Anyways, I'm a little disappointed but it is what it is. Alright. Block height as we start this recording was four excuse me. It it was 929162 so we continue to churn nine two nine one six two. Uh-huh. That's right. Yeah. Okay. It's now nine two nine one six four because we've been chatting quite a bit. So yeah. Alright. So today's topic. I just wanna take a few minutes and we are gonna probably keep this, well, we're gonna keep this to an hour tops. But you know, we're gonna we're gonna do a year a year end review. I always wanna be honest where we where we have failures, where we have successes, where we see things going, and we'll go ahead and make a few predictions I guess. Just by the way, programming note, we will not actually have a recording next week. 

I will be out of town. Yeah. So we will not be able to record. So I'm afraid we're gonna have to take one off. Now we recorded 48 episodes including this one. So fifty two weeks, 48 episodes. I actually think we did pretty good. We took four weeks off essentially for various things, work and vacation and whatever. So that's pretty cool between January and December of this year. So let's start with just the raw data. So let's start with the price. When we started in January, by the way, that was episode number one ninety one, I believe was that first episode in January, our price was sitting at about 94,000. 

We had an all time high. As we all know, back in October, it was the sixth or seventh or eighth, something like that. It was right around there. And it was 122,000 basically. And right now, I guess we'll go ahead and record the current price which I I looked up. Yeah. I have updated it. So Okay. That's correct price. 85,700. Not so good. So we're down 19 about 19% from last December. Wait. Yes. Wait. What did I do wrong? 

[00:20:57] Kenshin:

I just updated them. Now, those are in the wrong spot or I don't know. I thought I thought I updated them just now. 

[00:21:15] McIntosh:

What's our current price? 

That that sounds right from what I saw just 

[00:21:23] Kenshin:

I I even put links. I I corrected a lot of things. 

[00:21:27] McIntosh:

Did it like go right back up? 

[00:21:30] Kenshin:

Hold on. No. No. It's Cracking. Yeah. I think the notes have been mixed up. That that price now comes under the social media stuff. 

[00:21:48] McIntosh:

$87.06 

[00:21:49] Kenshin:

94. Oh, no. That wait. 

[00:21:53] McIntosh:

But I I thought I looked at it when we started recording and it was 85,000. 

[00:22:00] Kenshin:

Completely misread it? Wait. No. You're in the wrong row. Row 568. There I updated. That's the right place. 

[00:22:09] McIntosh:

Okay. 

[00:22:11] Kenshin:

Do you see Row 568? 

[00:22:13] McIntosh:

I don't have line numbers on here but I'm looking. 

What is the actual price right now? $87.07 

[00:22:21] Kenshin:

70. 

[00:22:22] McIntosh:

Okay. And that's what's in there? Let me fumble around here. Why am I not? Why? Okay. Find a page. $80.87 $7.70. Yeah. Bitcoin price. Okay. I got it. Yeah. Yeah. But that's gonna throw off our our other stuff. Alright. Well, that's okay. We'll have to make do. $87.07 70. So let me back this up a little bit. I gotta remember that price. Mhmm. It'll be fun. Okay. So this year when we started, our price was about 94,000. A lot of optimism, frankly. Think well, we'll we'll talk about that some more. We we spent a good portion of the year going up. We hit a 122,000 in October, somewhere around the sixth or seventh, and then we've gone down or sideways since then. We're sitting at $87,007.70. 

Right at $87,007.70 right now. So we're down roughly 20 from even from December 2024. We're down about 34% or so from the all time high. That's kind of the bare facts. I I think it would be safe to say, Kenshin, you and I both started the year with a lot of expectations for Bitcoin price this year. Is that fair enough? Oh, yeah. When did we actually break a 100,000 for the first time? Do you it was it seemed like it was February, March? Earlier. Trading. 

[00:24:03] Kenshin:

Was it earlier? I I have a link of a chart there. 

[00:24:08] McIntosh:

You can Okay. I'm gonna bring up trading view so I can look at this stuff on the fly as well. 

Already. 

[00:24:18] Kenshin:

So over hundreds, we were there. January 17. 

[00:24:30] McIntosh:

Okay. So it was early, very early in this in the year. Okay. 

[00:24:34] Kenshin:

Oh, but So we broke that 100 We had already range. Sorry. We had already crossed a 100 in December. 

[00:24:42] McIntosh:

Oh, my bad. Yeah. Hang on. December 5. Let me look at my data. Yeah. Yeah. 

[00:24:49] Kenshin:

Okay. You're right. You're right. You're right. Yeah. It was all the expectation with Trump and everything. 

[00:24:55] McIntosh:

Right. Right. Yeah. You're right. So we broke it and then it dropped back down in very early January. And then we we went and started climbing back up. 

Yeah. That's right. We fell into March and then went sideways and then it started climbing. And to me, I I know what I I remember what I was saying. I was saying basically a 150 to two fifty by the end of this year, which of course we still got seven days, so here's to hoping. And this would be kind of the end of the four year cycle and so on and so forth. So I was and honestly still am a proponent of a four year cycle until proven otherwise. You gave of something as well, do you want to share that? Yeah. Yeah. My prediction was we would be 

[00:26:02] Kenshin:

above Microsoft's market cap by this time. Right. Because this time last year it was the situation where Microsoft were considering to invest in Bitcoin. 

Yep. And they voted 99.7% they voted no. Right? We said well you made a mistake. That's crazy. That was my attitude. You made a mistake. Apparently they did not but that's okay. Yeah. So I see Microsoft's market cap right now it's at 3,600,000,000,000.0 and 

[00:26:35] McIntosh:

Bitcoin is basically 1.7, isn't it? Right. So we're still under 2,000,000 2,000,000,000,000. We sit there kinda languishing. So we were both wrong and I'm okay with that and I'll tell you why. Basically every time we make any kind of prediction whether it's a day out, a week out, a month out, or a year out, we we we're religious, I'll I'll say that, in telling you what you should be doing, and and it's very simple. You should be DCA ing. 

It's it's so easy to sit here and look at these prices and go, oh man, I'm in the dumps where Sats Sats are cheap right now and you should be taking advantage of that. Mhmm. And maybe we do go down some more. I do not know. We can speculate, we'll give a prediction for next year. I'm sure we will. I'm not sure at this point what I'm gonna say. I'm not ready We for may have to wait till the next episode. We can we can defer one episode for the first January episode, right? Yeah. But you know, it is that's just look, that's just it's just fun and I don't wanna say it's fun and games, but that's just what people do. 

But your consistent strategy should simply be doing DCA and I always wanna emphasize that. So alright. So that is one thing we did not do very good on. I guess we should have started with something up, man. What's up with that? Okay. Yep. We got a roller coaster. We got a lot of sideways. This is what Bitcoin does. It I it's almost like it's a an actual thing that's just like trying to shake you from your Bitcoin. You And I'm I think very briefly on here, I've even speculated to an extent that's what Wall Street is actually doing. There's fairly strong evidence at this point that there have been forced sell offs essentially of Bitcoin for, during the majority of the trading days recently for, like, the last month now, last three, four weeks. 

And it's coming from companies like BlackRock. I mean, you can trace back where, you know, there are ways of doing that. And, basically, they they they dropped the price at the start of the trading day, and and every day it kinda climbs up a little bit and then they drop it again. So we end up in this sideways crazy market. Why are they doing that? I don't know. They've got a strategy for accumulating more Bitcoin. All I know is I don't sell my Bitcoin. I only buy more Bitcoin. I try and use Bitcoin with other people but that's not Bitcoin for my savings. 

[00:29:36] Kenshin:

Yeah. Is that fair? Yeah. I mean, and and we were all excited. Oh, ETFs and Wall Street and Bitcoin will go up because everybody will be buying it and now Hey. You're getting ahead of us now. Hold on. No. 



[00:29:51] McIntosh:

You're right though. I mean Yeah. I I we'll just go ahead and talk about that. That was actually our next item. That is a theme. Right? We we both did it. Maybe me more than you. Oh, did. I think that's a Yeah. But, yeah, we both did sitting there going I remember I think this is in the notes somewhere. There was one point during the year when I talked about the statistic that the ETFs alone were buying more bitcoin than the miners were mining on a daily basis. Yeah, was like 600% 

[00:30:27] Kenshin:

more something like that. Yeah. 

[00:30:29] McIntosh:

The supply, there's not enough supply for the demand and that's just talking about the ETFs. 

One thing that always brings me hope in this, and these ETFs have continued to buy, but one thing that brings me hope in this is that as long as the supply is less than the demand, the price ultimately will go up. It's basic economics. 

[00:30:58] Kenshin:

Yeah, exactly. And at the time I remember the mathematics were saying that if they kept buying the same rate we would run out of available Bitcoin supply by June or something, by summer. And obviously that didn't happen but Right. So it's yeah. Everybody was too optimistic they would keep buying like crazy. Of course, also then it goes to the US government with a strategic Bitcoin reserve. 

That's the expectation. Now 

[00:31:35] McIntosh:

you're hurting me. We need to talk about that though. That expectation was very high. 

[00:31:40] Kenshin:

I even remember telling some family members like, yep. Well, US is gonna buy now. That's the last time you see Bitcoin at whatever price that was. Right. That didn't or it happened, but no one cared. And no meaningful Bitcoin was bought from US. Right? 

[00:32:00] McIntosh:

Yeah. In fact, if I'm remembering correctly, and I would have to look this up to make sure, but when Trump actually announced the SBR, the price went down. Do you remember that? Am I 

[00:32:14] Kenshin:

I don't. But I mean, every announcement from from Trump and Bitcoin went down, I think, basically this year, 

[00:32:23] McIntosh:

unfortunately. 

Okay. So let's talk about so there was a later statistic here we should talk. 75% of the coin base volume is now institutional. You wanna take that one? 

[00:32:36] Kenshin:

Yeah. That was earlier this year. When was that? That was do you know? Wait. I can't I don't follow your your notes here. Sorry. 

[00:32:51] McIntosh:

What? Not my notes. It's Claude's. I had Claude, just FYI, had Claude go through all of our podcasts for the last year via the RSS feed which I'm kind of proud of. I pointed it at the feed so it could pull the transcripts. Yeah. And so it kind of came up with all this. I never could have come up with this on my own. 75% of the coin base volume is is institutional 

[00:33:16] Kenshin:

buying. I remember that. Yeah. I remember it too. Yeah. 

I can talk about it. Where is it? Well, 

[00:33:24] McIntosh:

let me kick you off. Retail hasn't come in on this cycle. No. Is that fair? 

[00:33:32] Kenshin:

I don't know. Or did they come for a split second and left? I'm not sure what happened. But not in the expectations or the amount that we expected the amount that they have done before. Right? So yes, the 75% of Coinbase volume was institutions, and that was the 600% of institutions buying above the mining rate. So that was basically only them basically buying buying the supply six times over. 

[00:34:12] McIntosh:

I only remember so during past cycles let me let me back up. During past cycles, it was routine during the bull You could tell when the price was jumping because Coinbase would just not be available. Like, it'd be down. 

It really it was not good. I think that's only happened once this cycle. I And it was There was one day Yeah. 

[00:34:40] Kenshin:

And was it when bitcoin was down or 

[00:34:44] McIntosh:

I don't remember. And to be honest, I don't. But that just another little metric kinda to show you. I mean, retail by and large would be the ones who are buying using like Coinbase. MicroStrategy isn't buying using that Coinbase web interface. They're going to what they call over the counter OTC. You'll hear this term if you stick around long enough. And basically it's a way for companies like MicroStrategy or iBit, which is BlackRock's ETF, they don't buy using kind of the Coinbase or Kraken or whomever that interface. They they place their orders directly with the company and the company fulfills those orders. 

Because it's we're not talking about thousands of dollars, we're talking about millions of dollars of Bitcoin. Does that make sense? Yeah. And if they the idea is now, I don't agree with this by the way, I don't. I I that's not a fair market. But the idea is if they were to do that, it would depress the price because they're making that buy, you know, through the same interface that you and I would use if we were buying off that platform. Mhmm. Well, okay. What's different? Well, I don't know. Michael Saylor's special? I told I don't know. I'd love to buy right after Michael Saylor bought all his Bitcoin or no. Actually, no. That would not be good because Yeah. It it'd be good for the Bitcoin I already had because it would push the price up actually. I'm thinking about it the wrong way. Anyways, you get the idea. 

They're dealing with that that buying and selling over the counter, not directly through the website. 

[00:36:35] Kenshin:

Yeah. That makes sense. And then they buy it with with the loans. Right? With zero interest loans that they get. So, yeah, we cannot compete with that either. 

[00:36:46] McIntosh:

Okay. What else did we have in talking about institutions? BlackRock had record ETF outflows not inflows Yeah. Back in November. Yeah. Mhmm. And that would be simply because the, you know, we'd reached the peak or whatever people decided that and so now they're they're institutional selling was happening. 

Yeah. Here's would actually emphasize this. Institutions are traders not just and that in my opinion is unfortunate. Yeah. Let's take I don't wanna pick on BlackRock but let's just continue. They shouldn't be playing games with Bitcoin that was bought with my shares of iBit stock. Does that make sense? But that's what goes on and they're not the only institution certainly to do that. Yeah. I mean again, we go back to this that's everybody 

[00:37:51] Kenshin:

was excited about, yeah, Wall Street getting in the game, but then, of course, they play with their own set of rules and their own fiat games and then we're surprised how they manipulate the price like that. 



[00:38:07] McIntosh:

Should not be that Frankly, a lot of these companies are we don't have any comprehension really of of how big and powerful that they are. Yeah. Right? I mean, BlackRock literally has trillions of dollars under management AUM, 

[00:38:22] Kenshin:

assets under management. And some some people who analyze the those games that you also mentioned how the price was manipulated recently. That's was it 10AM every morning? The price would would down. And I think that was 10AM eastern time. Yeah. And then it was not only one company. That that's that's the 

[00:38:43] McIntosh:

frustrating part. There was three or four. Yeah. Yeah. It's like they were coordinating it and I believe they were but we can't prove that. 

And that's not I mean, I can just see Matt O'Dell. Oh, that's just the market. Well, yeah. I 

[00:39:00] Kenshin:

don't know. I think think it sure. It's a free market and that's fine and I think we are in this phase where where they were big enough against Bitcoin that they can do that. But we will reach a point like we used to be ten years ago that one person could be big enough to affect the price with one transaction. Now we don't get that anymore. Michael Seller buys, nothing happens basically. Now That's a great point. Yeah. Now the institutions are involved and they affect the price. We will reach a point in five, ten years where they will not be able to to affect the price either. So they will not be playing those games. 

So we are I think we are in this first first couple of years of this adoption with Wall Street. Right. We need to go through that pain. 

[00:39:49] McIntosh:

Now one thing remains to be seen, at least one thing. If this truly was a four year cycle and we are now post October, we really should look that up, but whatever the day And we're in the downward slope, we buy the projections, we basically should have a year to go straight down, and then, you know, that's kind of the bottom. Will the institutions keep that run from being so steep? In other words, prior bull runs 50 to 80% drop, which is insane. 

Will that happen this time? 

[00:40:34] Kenshin:

Oh, is that a prediction? 

[00:40:36] McIntosh:

We will make it next week if we do maybe we should make a list. Yeah. But I don't know but will this same I guess the question that will have to be answered is are they going to continue to buy when the price goes down or do they jump on to the bandwagon so to speak and sell sell sell and then try and buy at the bottom? 

[00:41:04] Kenshin:

Yeah. I think they will try to time it because they timed the top. Right? And that they timed it for sure pretty good and a lot of people came out and and said that basically the last two months. 



[00:41:17] McIntosh:

So If that's true, then should we have a 50 to 80% drawdown? 

[00:41:21] Kenshin:

Not necessarily. I don't think so. Because we didn't have however percent up this time. Right? Mhmm. So we already see that the volatility is not so high anymore. 

[00:41:35] McIntosh:

Well, how low have we been? 84? I'm not sure if it's gone lower than that. 80? Yeah. I think we went to 80. 80? Yeah. I think so. We did go to 80. Yeah. But I don't really think we went at least for very long at all below that. I guess we'll see. I mean, 80% from 01/22. 

[00:41:57] Kenshin:

01/26 wasn't it? Oh, 01/26. 

[00:42:01] McIntosh:

Why? These numbers are not right. 



[00:42:03] Kenshin:

I I really should've 30 cleaned this up. I'm 6.5% 

[00:42:07] McIntosh:

down. Yeah. So that's almost 40. 

[00:42:10] Kenshin:

I mean it's easy to say we will not go lower but why not? Previous and that's that's the question right? Because previous lows have always been around the previous previous cycles top. Theoretically if we go down to seventy, sixty nine, let's say 70 and we say one twenty six minus one, that's 44.5%. 

[00:42:41] McIntosh:

Go for it. Do it. So I wanna go down that low. So worst case scenario, 

[00:42:46] Kenshin:

that's that's what it seems. Worst case scenario, if nothing really bad happens in the world, if that makes sense. 

Yeah. Because I mean Well, 

[00:42:56] McIntosh:

I'm sorry. We're not even gonna bring the world into this discussion. No. That does make sense. Now, we also had the fifty eight k gang who were maybe less noisy but, you know, there are people out there who still believe that we're going down to 58 k. 

[00:43:17] Kenshin:

I I don't know. Yeah. Don't know. I don't I don't think so. I I think that would be quite low for Bitcoin. Well, 

[00:43:24] McIntosh:

we will kick that prediction to next week. Just like we will kick any other prediction to next week. One more thing that fits here is that 

[00:43:33] Kenshin:

I I hear a lot in other podcasts now that they're saying, oh, the four year cycle is already broken. 

Yeah. Because We don't have proof of that. No. They say because it's gonna be the second or what did they say? It's gonna be a red year instead of a green year and that would break it. But it hasn't been broken if you count on months. If you put remember the calculations that we did in this analysis based on months, one hundred and fifty two months of a bull market and fifty two months of a bear market. This is still standing. That four year cycle is still intact, precisely intact. 

[00:44:16] McIntosh:

We'll see. We'll see. I hate predictions or next week. Hold on. Okay. Yeah. Alright. Let's talk about the government for a little bit because we spent a good bit of time this year talking about the government. We did have some good things happen. I before we dive into this though, I don't remember any specific predictions. 

We probably made a prediction based around the SBR, the strategic Bitcoin reserve of The US. Was that a million coins a year? What did they say? Or a million coins Well, for He 40 said he wanted a million coins. Yeah. Yeah. He was trying to get it. That was a big target. That one never happened. And I don't think we said he was gonna have a million coins this year. No. I probably said something along the lines of we'll get a strategic Bitcoin reserve, which we did. But I probably think I I was leaning towards the fact that we would have a regular buy because that's the smart thing to do. 

Apparently, that's not the case, at least at this point. We also did not get any cap gains relief. That stinks. In fact, I would argue that basically in terms of the policy of the US government other than some clarity because of various bills and whatever that they've passed, we've not really gotten anything new. 

[00:45:45] Kenshin:

Well, less negative stance towards Bitcoin I would say. Yes. There's choke 

[00:45:53] McIntosh:

point But no real look, you've you've got developers who are being put in jail Right. For writing software. You've got $600,000 $600,000. 

600,000 Bitcoin that are in US custody. Some people would argue that it's not theirs, at least the majority of it. There's no clear plan for moving forward with that. Trump just waves his hands and says things like, you know, we're gonna lead the world in Bitcoin or crypto because he's hawking, you know, whatever it is that he's hawking these days. Yeah. It's nice that, you know, Operation Chokepoint three point o isn't going on. But beyond that, we've not really made any meaningful progress as a nation and I am talking about The United States here in terms of terms of Bitcoin. 



[00:46:55] Kenshin:

Yeah. I think the focus has been too much on crypto honestly and that that's the most disappointing part to see also. So we I think we we expected at least I expected that it will be more Bitcoin focused and less crypto and that that was instantly destroyed with the Trump coin. 

[00:47:17] McIntosh:

Yeah. He's that I will say this. I have been disappointed by Trump's fetish because I don't know what else to call it with stuff like his Trump coin and the coin he made for his wife and all of this garbage that it's so obvious that it's just a 

[00:47:44] Kenshin:

a money grab. I mean, it's it's human greed. 

I think it's expected in a way. It's it's just disappointing, but it's not unexpected because it's human greed is the easy thing to do to instantly get hundreds of millions of dollars, basically. And it's disappointing and it's a lot have to do, of course, with his family and his sons and all of this. Right. But yeah. But I mean, they need to go through that journey, unfortunately. 

[00:48:15] McIntosh:

I know that there are people out here in our audience who would disagree with what I am about to say, but I'm going to say it and I believe it. I believe The United States as a nation state should be mining Bitcoin. 

If for no other reason than there are already other countries who are doing so. And I believe that's actually how we should be supplying the the SBR. 

[00:48:43] Kenshin:

Right. I agree. That will be great. 

[00:48:46] McIntosh:

Well, there's a lot of people who just they think the government should just stay out of Bitcoin but that's not that's not the world we live in. I'll say it that way. I mean, if we want bitcoin to be 

[00:48:59] Kenshin:

money in the future. Yeah. Right. 

[00:49:02] McIntosh:

The government has to be involved to some level. But we know that we know that Russia is mining bitcoin. We know that Bhutan is mining Bitcoin. We know that El Salvador is mining Bitcoin. It is highly suspect that China is actually mining Bitcoin as well, although I'm not convinced of that. No. 



[00:49:21] Kenshin:

Not lately with what happened. 

[00:49:24] McIntosh:

Why are we not mining Bitcoin? Oh, well, we've got American mining. Well, that's just a private company. That's one of the ones that's headed up by Trump Junior, I think. I don't know. I I don't keep up with all that. But, yeah. Why is America not mining bitcoin? With there's got to be places where there are massive amounts of excess power that they could hook into. Okay. Time to move on off of that. But in good news, there were a number of developments including one fairly recently about states becoming more involved in Bitcoin. Texas, we just recently reported, was the first state to actually purchase Bitcoin. They have approved well, they did a $5,000,000 iBIT ETF purchase, so in theory, that's at least the equivalent of 5,000,000 of Bitcoin. 

They have approved a $10,000,000 fund for that. They have plans that they're working on to put self custody into place. So, to me, those are some solid steps towards Texas, you know, becoming a bitcoin hodler. There were others as well, smaller steps. In my view, this may be something you don't have as much of an opinion on, Kenshin, simply because of the scope of it. But the states are kind of moving along as I would expect. I think it's going to be a slow process in general. Yeah. But it is good to see that some of these states are starting to make some solid moves. There's actually a place speaking of excess power. Like, believe it or not, Alaska has a hydroelectric dam up at Homer, Alaska, which if you look on the map is down on the coast of Alaska. 

And the Army Corps of Engineers built a dam in the nineteen fifties right after World War two for some reason, and I don't remember, but they generate power off this dam. It's a very, very tiny town, Homer, Alaska. And because of this giant hydro powered dam complex, they are paying some of the cheapest power, if not the cheapest power in The United States. It's like literally retail is like 4¢ per kilowatt, which is one third of what I pay. Wow. I could move to Homer, Alaska, buy a warehouse and plug in miners and be extremely profitable. 

Yeah. In fact, I've thought about that many times actually. 

[00:52:18] Kenshin:

One sixth of what I've yeah. Wow. It's crazy. Anyways. 

[00:52:26] McIntosh:

Okay. Sorry. Well, we did have some things go backwards, and and I have El Salvador on here. You wanna go ahead and talk about this? But Yeah. Very quickly, there were others. There was a, I should have looked this up. Central C A R, Central African Republic. One of the African nations had legalized Bitcoin and, you know, made lots of good moves and then they pretty quietly rolled that back and I believe that was early this year. Is that the IMF involved again? I bet. You know what? I don't know, but it is highly likely. Alright. Why don't you jump in there on El Salvador? 



[00:53:09] Kenshin:

Yeah. Well, we talked about it last week also that and was it happened earlier this year that El Salvador took a new loan and from the they agreed to drop the legal tender from yeah, their rules And they agreed to not spend loan money to buy Bitcoin. So, yeah, that was it felt like a loss at that time. But as the weeks moved on, we saw that El Salvador kept buying Bitcoin. Nothing really changed in terms of how you could use Bitcoin in El Salvador. And some people came up and and came out and said that basically it's it's, yeah. Just paper talk. 

It didn't change anything in practice. And they kept DCA and 1 Bitcoin a day and in some days they bought 10 or 11 Bitcoin here and there. Right. So not terrible but still a bit disappointed to see that they didn't use Yeah. It didn't go better this year let's say. It went a little one step backwards instead of as we would have hoped to see some steps Right. Forward with adoption and and 

[00:54:26] McIntosh:

yeah. How to use Bitcoin in a better ways In my mind, the jury is still out on El Salvador for a number of reasons. I I don't know. I think this might have been overblown but still maybe not ideal. 

I don't think that they should be dealing with the IMF at all. Exactly. But they they clearly feel like they should be because they took a loan from them. 

[00:54:50] Kenshin:

But it's once again it's that game of if someone comes and ask for their loan you need to do something about it. Right? And and the only thing that you can do is take another loan from the same people. I think that's clearly what happened because if someone comes to The US and ask for the loan back, US doesn't have 30 how much is that? 38,000,000,000,000, why We just print more money. Yeah. Exactly. I mean, because the exact same thing happened to Greece and I believe the exact same thing happened to many many other countries. 



[00:55:25] McIntosh:

Yep. They're in a tough spot. Yeah. Things are better in a lot of ways than they certainly were a few years ago, but I do think the jury's still out. I think time will tell. Let's throw out a few more of those little sayings. Right? I want you to talk about Europe. There's, some things on there about Europe, and then I'm gonna talk about China. 

[00:55:46] Kenshin:

Yeah. Europe was not very fun this year. First of all, we have so much talk about the e euro which actually it's a bit of a comedy for now. I don't take it too seriously because it's it's just fun and games. Who knows? Maybe next year we'll see something more serious come up with that. I hope not. 

But then we had the MICA, m I c a, that was the markets in crypto assets it's called. That forced a lot of companies to comply with some stricter cryptocurrency rules that they applied and yeah. Basically, if you're trading with crypto, you need to to to say if an address is yours or whose address is it that you send money to. Some companies just closed completely instead of complying with MICA. Right. Some companies now just have passed this or are compliant now and I know Strike is. I know Relay Relay is also complying. They were very proud. They were of of the first to comply. 

Revolut is also complying. But, yeah, it's not a good rule, so it's it's very bad rule. Essentially, when you want to send money from one of those apps, it asks you, is that your Bitcoin address or whose address is it? Something like that. Strike is good because it asks you is it yours or someone else's and you can put someone else's and they don't ask who or what or anything else. In the system it just goes out just someone else and that's it. Revolut, you need to put the specific name and all all the hoopla. So that's not good. And then Europe has been really trying to to fight end to end encryption. 



[00:57:52] McIntosh:

Right. What what was the name? I thought that was gonna get passed earlier 

[00:57:58] Kenshin:

this year. Yeah. That was actually scary. And basically, Signal and other companies would not be able to offer end to end encrypted chat applications and I mean that that would be a big problem for I would assume for Bitcoin too, right, essentially because we use For Bitcoin usage, I'm sure. Yeah. They're in Europe. So I don't know. It's a lot of scary things like that that they're trying to pass in Europe. This, thankfully, didn't pass. Another rule they tried to pass, but I think it was last year, it was essentially, if you had the soft custody wallet, you would be deemed criminal. 

Right? So they didn't want anyone to soft custody their own keys, basically, which is crazy again. So that was a big talk for a while even in Sweden. I saw it in some news. So, yeah, Europe is fighting, how do you say, tooth and nail, right? To keep control and take away all those tools that keep our anonymity or privacy. And I don't like it. Thankfully nothing bad happened this year except this Mica which brought some stricter rules in place. Unfortunately, I had to yeah. I'm KYC now, basically, most of my coins, which is bad. 

I cannot really avoid it anymore in Europe. So that's the worst thing that happened. But Yeah. Yeah. 

[00:59:37] McIntosh:

Let's hope. Alright. Let's hope for better. Let's hope for a better 2026. Can we do that? Realistically speaking. Yeah. Let's see. Hopefully. I don't wanna call for insurrection, but maybe tar and feathering will make a comeback. I don't know. Just Who? What? What do you say? Tar and feathering? 

[00:59:59] Kenshin:

What's feathering? Ah, tar tar and feathering. Yeah. Yeah. Yeah. I I was reading a lot of Lucky Luke comics back in the day. Yeah. 

[01:00:09] McIntosh:

Yeah. That's tough. 

Alright. China, been pretty quiet until very recently. It looks like over in Western China, they're clamping down on Bitcoin mining, making them register, making them take all their servers offline. I saw estimates that four four hundred to 500,000 miners were put offline. Now these were probably older miners Mhmm. But still it's a lot of hash power. Looking at about a 10% hash rate drop. Right now, in fact, I just looked. Looks like on Christmas Day, we will have our next adjustment, and it will be a downward of adjustment of about a percent, 1.2% or so. Right. Yeah. And that will be the third consecutive one in a row. So Yeah. It's been a while since that has happened. 

The miners like it. Those of us who are still online, 

[01:01:08] Kenshin:

I will say No. Need to check Austrian. I haven't checked for a while. I have my legal minor Not as 

[01:01:17] McIntosh:

dramatic as in 2021 when they did their crackdown on mining. And I guess mining has never officially been reapproved since then. Thought that had changed but apparently not. So as big a investor in Bitcoin as China is, it's surprising to me that they don't mine. I mean, the vast majority of the hash rate is now in The US. It's like 50%. No. That's not very good. It no. It's not. And it's American. I say that. It this is exactly where we were at when China stopped mining. They were at, like, 50 or so percent, and now that's us. 

A lot of that hash rate moved to America, seriously. Yeah. You guys need to get cracking. There's cheap power over Norway. I'm just Yeah. 

[01:02:15] Kenshin:

There is. Yeah. They're actually And you you can speak the language. I I now know you can speak the language so you're good to go. They are actually mining and there was a report that they they mine is over 80% or something is renewable energies up there or something. Sure. 

[01:02:31] McIntosh:

They have tons of hydropower. Yeah. Mhmm. Let's talk about the economy in general. To me, I don't I think we were pretty much spot on. I have slowed down in my predictions of the end is, you know, near like tomorrow near. 

Everything is still on track. Japan, their interest rates are rising. That's disrupting the carry trade market. We have documented that. I still personally believe that China is in worse shape than what is being portrayed. I know their their real estate market is in shambles. They have been building a huge amount of power. There's no doubt about that. And they've been buying a huge amount of gold, but in a lot of ways I think their economy is super weak. Mhmm. The United States, we have continued to, you know, print money. We're roughly, well right now we're at $38,000,000,000,000 in debt. 

I think we're growing now at a point roughly where we're it's like $2,000,000,000,000 a year in debt. And the reality is when Trump starts spending money over the next six months because of the midterms, and this is something we brought up a number of times, that debt is going to accelerate. Mhmm. I fully expect that we leave $20.26 $3,000,000,000,000 a year in debt. Alright. It's just like Lin Alden says, nothing stops that train. So, you know, we spent an entire episode. It was episode two thirty five, in fact, going over how things are kind of breaking down. If you just go back to 1970 or so and look at the data, it is astonishing the differences. 

Like tomato soup, 10¢ versus a dollar 20 now. I mean, that's Yeah. That's 12 x. Right? Yeah. The average first time home buyer age just hit 40 years. We're at an all time high of credit card debt, On and on and on and on. It's just endless. And this has to end somewhere and we can either default or we can print more money. Mhmm. And we're not going to default. And I don't know what's going to happen when we really get serious. We're going try and control it as long as possible. They hope that somehow AI and robotics is going to build us out of this. Yeah. 



[01:05:14] Kenshin:

I I don't think it's possible. Didn't Trump say Bitcoin will pay for they will Yeah. I'm sure he did. Buy Bitcoin and it will pay for all the debt or something. He threw that in some at some point. I have seen plans of like bitcoin backed bonds instead of like the US treasury bonds. 

[01:05:34] McIntosh:

That actually is an interesting angle on this. It would not hurt bitcoin and I think it might actually help the US government. So I maybe we come up with something but if we continue doing what we've always done which is what we have been doing for decades now, we will end up in a ditch. 

And we're teetering on the edge right now. And I'm not saying it's 2026, but the end is coming. It has to. So Yeah. 

[01:06:07] Kenshin:

I just remembered before we go to the very positive ones. The big top pick last year was that we Bitcoin was above silver, remember? 

[01:06:21] McIntosh:

Above silver? Yeah. Oh, you mean the market Yeah. The market is silver. Is silver taking it over? 

[01:06:26] Kenshin:

Taking it over, it's more than double. 

[01:06:30] McIntosh:

Yeah. We bring up the price of silver on here from time to time. It has hit a new all time high today. Seriously? It is now as we talked $71.36 

[01:06:43] Kenshin:

which is just nuts. Silver is almost as valuable as Apple. 

If you open that link I send you, silver is at 4,000,000,000,000. 

[01:06:52] McIntosh:

Oh, right. 

[01:06:53] Kenshin:

Yep. I got it right here. It's at the fourth spot and Bitcoin is 1.75. Gold is at 31,000,000,000,000. Yeah. Silver is like the the basically behind Nvidia and Apple, the same as Apple basically. Right. 

[01:07:09] McIntosh:

Yep. Yep. Believe, well, maybe we'll make this a prediction. Oh, I'm almost entirely convinced. Look how close it is. This is an easy one because silver is going to continue. I have talked about this. It is in a forty five year cup and handle pattern. I see no reason why it should stop. 

And it's not just that. It's not just a chart. It is the fundamentals of what is going on. Silver will be right behind gold. Not right behind. Not because it's gold is much much 

[01:07:45] Kenshin:

bigger market cap. Yeah. But it will be number two. It's not so foreign. It's half 1,000,000,000,000 away from being number two. 

[01:07:51] McIntosh:

Yeah. Yeah. It's only half 1,000,000,000,000 from number two. Yeah. And Nvidia, we could wake up tomorrow and Nvidia could be in the toilet. I mean it's 

[01:08:03] Kenshin:

Yeah. Mean Maybe it's not, maybe it is. It's it's an iffy thing. But the the AI news are incredible how from month to month or week to week they're changing the Right. The sentiment with some new model comes out from China or from or from AMD, they announce something with a new chip or whatever. So, yeah, those change. Let's 

[01:08:25] McIntosh:

let's wrap this up by talking about some Bitcoin. Can we do that? Yeah. 

I don't think anything's changed. Do you? No. In terms of Bitcoin's future, in terms of what it can do, 

[01:08:40] Kenshin:

you know, we've already talked about the price. The price is just the price, but where are we going in the long term? No. Actually in terms of of the future, it's never been more positive in terms of the adoption even though they're playing those fiat games with Wall Street, the adoption is still adoption. Banks are officially now, have the green lights to support Right. Cryptocurrencies. So those things are yet to be played out. Right? We haven't seen those things materialize because they they just got the okay. 

Yeah. I mean, normal people like our families and stuff, they still don't know about Bitcoin. So they Right. They will come on board eventually. So I think the the future is is brighter than ever. It nothing bad has happened. 

[01:09:33] McIntosh:

I would say the average person in Europe and The United States has heard of Bitcoin. They know what it is in terms of, oh, it's this crypto that's Yeah. You know, super high in price. They may even know it's got the biggest market cap. What they don't know is the fundamentals of it. They don't understand there will only ever be 21,000,000 bitcoin. They don't understand how the mining network works. They don't understand that no person nor country controls Bitcoin, that it's decentralized. 

All of the things that we talk about, that we love about Bitcoin, many people, the average person out there does not understand that yet. And they may never fully understand it, but there will be a time when the average person does understand that neither China, Russia, nor The United States, nor Europe, nor Africa, nor South America control Bitcoin, that it is uncontrollable. They will understand that there is a limited amount of Bitcoin that you can there's only so many and we will not mine it forever. We will not, you know, it's like eventually it will come to an end. They will understand some of these basic fundamental things. They may not understand every detail and they don't need to. 

But we're still heading that way. We spent an entire episode back in February, eight different myths about Bitcoin that are still quite common that are so easily debunked. 

[01:11:09] Kenshin:

Right? Yeah. I brought in into the show news one time that I talked to a friend of mine and I he's a bright person. 

[01:11:20] McIntosh:

He had no clue He was in education. 

[01:11:22] Kenshin:

Yeah. And he had no clue about the details. The 21,000,000, the Right. Difficulty adjustment, all those things. And so, yeah, as you said, they heard about Bitcoin and then it's like, yeah. Okay. Whatever. This this Internet fake Internet money. Right? 

So, yeah, I think we're still good. So, yeah, I mean, it's easy, especially for me also, it's easy to get down a bit with some of those things because we're we're on top of the news every week. So it's it's easy to get a bit disappointed and, yeah, a bit down, let's say, but realistically speaking, we've never been better Right. Including those, yeah, US issues, government news and stuff. So even there, that's good enough where we are now for the adoption. 

[01:12:27] McIntosh:

Alright. We got a lot of stuff right this year. We got some things wrong. We certainly did not get the price correct. But again, this isn't some price prediction show, and I don't ever want it to be that. We have fun with it. 

But, again, just keep those daily buys or weekly. Is there anything else you wanna cover? We've got a lot of stuff here and I we're overtime. So 

[01:12:57] Kenshin:

Yeah. I mean, it's a lot. 

[01:13:00] McIntosh:

We could've done two episodes with this without any problem. Yeah. It's a year full of data and 

[01:13:06] Kenshin:

comments and news. Alright. 

[01:13:09] McIntosh:

Well, we're gonna go ahead and move on to our supporters. We got a boost from Syndicate Mike about episode two thirty seven from El Salvador to Africa, fighting monetary control. This made me feel good. I appreciate this, send it, Mike, because you, in a lot of ways, put together kind of what I was trying to unsuccessfully say. He said, monarchies, I feel like you guys arrived at where I generally fall. 

They can work in small kingdoms with good monarchs but generally are bad news. Many kings will think long term like how can I extract maximum power and money from my people in the long term? And I 100% agree with that. Long term thinking isn't always better. It's finding the appropriate priority between long term and short term that is needed. Democracy is the best bad form of government that we found. I do agree with that and it is not perfect by any means. To answer the question of the week, I usually download as I queue a few podcast to listen to. Mhmm. That's how I do it, sir. Yeah. But 

[01:14:16] Kenshin:

then I don't Why don't you do the question? I'm sorry. But then I I don't listen to all of them. So then I end it. I I saw now my phone. I have like thirty thirty or 40 downloaded 

[01:14:25] McIntosh:

podcast. You need to automatically delete after thirty days because you're never gonna get back to it. Yeah, you're right. 



[01:14:32] Kenshin:

Okay, question of the week. What did you learn this year? What are your predictions for 2026? So please send us a boost with your thoughts and predictions. So next episode, we will read those predictions and we'll have our own predictions. So that will be a fun episode. And that episode will be from January, January. Right? So we will not have an episode next week. 

[01:14:58] McIntosh:

Nope. We will take off the rest of the year. I guess we're all gonna be like everybody else anyways. See you next year. Satoshi's 

[01:15:07] Kenshin:

what was that? I will see you next year. 

[01:15:10] McIntosh:

Satoshi's Plebs is a value for value podcast supporting podcasting two point o. We strive to bring you honest Bitcoin content every week. We ask, are you getting value from this show? Support it through time, talent, or treasure. 

You can help with our future projects or you can stream sats and boost with messages, even a 100 sats saying great show or you suck. We'll read it either way. Check out the apps at podcastapps.com and support Independent Bitcoin Media. If you'd like the content, I would love it if you would write a review on Apple. Look, I'm gonna ask you if we can do this, Ken Shin. Yeah. We have no reviews on Apple Podcasts. If you go on Apple Podcasts and write a good review. Or a bad one. Not just Or? Hey, it's a great show. Write a thoughtful review please whether it's good or bad and you tell me who you are because that may not be connected to your Apple stuff. 

You can DM me on Oster. You could email me at McIntosh@Satoshi's-Plebs.com, although I don't get there very often to read that. You can boost me. I will send you can we send them 10,000 sats? Is that Woah. Yeah. Sure. I'm glad you were sitting down. We need to. Why not? We need to get this going and I've I've I I don't know what else to do. Yeah. Whether we like it or not, Apple is a huge part of the podcast ecosystem and not having reviews and whatever on Apple is hurting us. 

[01:16:47] Kenshin:

Is it is it for Bitcoiners? Is that a good place to leave a review on a Bitcoin podcast thinking 

[01:16:54] McIntosh:

for privacy concerns? I believe so. I think you think the average person is not on fountain or whatever. They're still using Apple Podcasts. No. But for privacy concerns. 



[01:17:05] Kenshin:

Does it show your real name? 

[01:17:07] McIntosh:

Well, they don't have to. And that's why I say, look, that's up to you. You yeah. I believe if you leave it on there, your your Apple Cloud account, whatever is tied to that. If you're just not comfortable doing that, then don't do it. But you don't have to do like, you can DM me and tell me who you are so I can get you the stats. We can handle that privately. That's not what I'm saying. But, yeah, we gotta get some reviews going on there. So this is a one time thing. Do it. First come, first serve? First come. So it's one first person whose name isn't Kenshin Alright. By the way. 

I 

[01:17:57] Kenshin:

don't have any Apple products. 

[01:18:03] McIntosh:

So please do that. Tell your friends about the podcast. That's the best way for us to grow. This week's music again is Top Hat Orchestra, a couple more Christmas songs. I do not know which ones. But again, I'll throw a couple of different ones on there. Any boost or streaming of sat during that song those songs, will go straight to the artist. 

[01:18:26] Kenshin:

Great. So thanks again for joining us this week for this review episode. We hope this has been entertaining we would love to hear from you on Noster or We are always entertaining sir. Yes. 

So find our contact info. You can find all of this on at satoshis.plebs.com. Stay humble this year those SaaS, and have a great end of the year. 

[01:18:57] McIntosh:

We will talk to you all soon. Bye bye. Merry Christmas. 

[01:19:02] Kenshin:

And happy New Year.
