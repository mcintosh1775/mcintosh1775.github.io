---
title: "Episode 240 Transcript"
draft: false
_build:
  list: never
  render: always
---
```
[00:00:00] McIntosh:

Welcome back to Satoshi's Plebs for episode two forty. I'm Mcintosh. 

[00:00:05] Kenshin:

I am Kenshin. And in today's episode, we are still running Bitcoin. 

[00:00:11] McIntosh:

Which is distinctly different than me running anywhere because that doesn't happen anymore. Trivia for our listeners. Oh, I'm used to that. Nice. Good job. I flubbed But other than that, it was terrific. Thank you, sir. A little bit of trivia. Yeah. In in high school, believe it or not, I know you see me every week, you're like, there's no way anyways, I actually was on the track team in high school. 

[00:00:50] Kenshin:

Oh, me too. 

[00:00:51] McIntosh:

True story. What did you run or did you do another event? Around a thousand meters. Okay. So that's a kilometer? Yeah. Thousand meters. Yeah. Yeah. Kilometers. So that's six tenths of a mile. So basically the half mile. I ran the mile. I was never any good at it but yeah. I could not run fast so like I could not do the 100 yard or 100 meter, the 400 meter, you know, whatever. I had to go the whole way and that just means that the margins were bigger at the finish line by the way. Anyways 

[00:01:27] Kenshin:

I think I also think I also did a 500 a few times. So I think that's a That 

[00:01:33] McIntosh:

would be roughly the mile. Yeah. It'd be the equivalent. 

1,500 meters is is close. Mhmm. Okay. What's up with you this week, sir? 

[00:01:46] Kenshin:

Oh, yeah. I've been hyper focused on launching a project with my wife. So 

[00:01:56] McIntosh:

Raise your hand, please. Very close. Raise your hand. You gotta raise your hand. Say, I Kenshin swear that this week I'm gonna finish this project. 

[00:02:07] Kenshin:

Yeah. I think so. I think so. Swear this week, yes, we'll finish the project and be live next week. 

[00:02:16] McIntosh:

I think yeah. 

[00:02:18] Kenshin:

It's it's exciting and terrifying at the same time. At the same exact time. And 

[00:02:24] McIntosh:

people who've not done this have no idea. 

[00:02:27] Kenshin:

Yeah. 

It's it's a lot of hope behind it and Yeah. Yeah. Well, 

[00:02:37] McIntosh:

I feel like you're going to sweep Northern Europe and you're gonna be the next big thing and then maybe you can hire me to do something. Yeah. Or do nothing. I don't care. Just hire me and pay me, please. 

[00:02:49] Kenshin:

Need to do something with the profits. Right? We need to put them in is 

[00:02:54] McIntosh:

a European way of looking at it. Do something with the profits. I wanna keep the profits anyways. 

[00:03:04] Kenshin:

Right. I have one more thing. I Okay. Because I know you will say something about ordering something. So I ordered also something. Mhmm. But it turns out it's fake. 



[00:03:16] McIntosh:

Uh-oh. 

[00:03:17] Kenshin:

Yeah. I ordered a Casio watch and it's a fifth of the price what I paid from a legitimate store in Sweden. But they yeah. Have But they have, like, third party sellers in there or, you know. And when I and I thought it was a very good deal, so I ordered it in the middle of the night. And that's, like, over a week ago. And then I started No drinking involved, by the way. Maybe summer that night. And then I realized the next day, I started doing some research. I'm like, this watch was never below x. And I'm I bought it for a fifth. X minus. Yeah. 

It's not possible. No. And then I looked online. There is many cases where those watches were so cheap were fake because yeah. They they Did you cancel it? Or No. I cannot cancel it. I I sent a message to the company, and they said they will look into it, but I don't know. I do not want your Chinese counterfeit. Yeah. So I'm a bit disappointed but yeah. I'm sorry. 

[00:04:32] McIntosh:

Yeah. So I did order the microphone this week. Unfortunately, it did not get here quite in time. It is in the hands of UPS. This morning it was in Houston and they promised tomorrow it will be here. So we will see how that works out. 

I'm semi confident but I'm looking forward to that. I'll say that. Oh, I do have one other thing I wanna discuss. So I did an experiment this week and I know I've have I already told you? I did tell you. No, I did. I I remember. I was so excited. I I messaged you. I really was. It was it's look. Don't know if you're not a programmer, if you don't I don't know. I just don't know what to tell you. Just let me blather on. So I I did a thing. I started Claude not Claude. Chad why do they both have to start with a c? 

[00:05:37] Kenshin:

Not I don't know. Stay on It's not in my mind but yeah that's good. 



[00:05:43] McIntosh:

Chad GPT. I turned up the pro account or whatever it is that you have to pay for, and I had a specific task in mind for this first programming challenge. So I spent on Sunday afternoon I spent roughly one hour setting up chat GPT and codex which is this programming tool that you interact with in the Satoshi's Plebs repo. So we have a repo of our code that I use to manage the episode pages and all that kind of stuff. So that was the first hour. It took roughly two hours after that and I'm probably being generous. It was probably less than that, but I'm gonna say two hours. It took two hours after that to get going, tell I literally had two screens. Is this the way that you do this by the way, Kenshin? I had a screen with regular chat GPT over here and I had my codex over here and I would say to chat GPT, okay I wanna do this in codex, tell me what to say. And it would tell me exactly what to say and I would paste it in. What? Do you do that or do you just interact directly with Codex? Yeah. Only with co all the conversation is done in Codex. Interesting. 

Yeah. Okay. So I did that regardless and two hours later I had an application. Now here was the idea. I have a manual process for populating for creating new episode pages, but the pages are all the same format. It's the title, the episode number, the bitcoin price, the block height, the show notes, and the transcript. That's basically it. Oh, and music credits. I think that's everything. So I said, well, I'm gonna give you two blobs of text, the transcript which comes out of Podholm, our host, and the show notes which also comes out of Podholm but it's in a different place. In a file. You're gonna bring those in, you're gonna scrape the data out, and you're gonna build this page. And it wrote this Python script to do this, and it was good. 

Took me about two hours. I was very pleased with that and because I can't let things go, almost as soon as I got done I'm thinking, well man, I'm having to supply really three pieces of information I did not mention. I also had to supply the player ID that on the page it shows like a player that you can listen to the episode and there's a specific bit of data that that comes from in pod home. Mhmm. I'm like, wait. I think all this is in the RSS feed. So for the non technical people in the audience audience or the people who don't work in podcasting in general, the RSS feed is basically the protocol that backs all of this stuff that we do. 

And your data for the episodes are embedded in that And then the player that you listened on, it downloads that feed for that podcast and you get all that information populated out in your app. And I said, well, the transcript's there. I said the episode number's there. I said, the show notes are there. That's how it gets into your player. And so after about an hour, I went back to to chat GPT and I said, hey chat GPT, what if we pulled this from the RSS protocol? And this is one of the big differences, Ken Shin, between an AI and a senior level engineer. 

Not claiming to be one for podcasting mind you but I'm just saying in general. Yeah. This was an architectural decision essentially. ChatGPT did not have the knowledge, the the workspace or whatever you wanna call it to say, hey, instead of getting those from your text files, why don't we just get it from the feed? Does that make sense? Even though that RSS feed is a basic underpinning of podcasting and it knew exactly what this was for. So I said, hey, let's if I provide you with the URL for the for the feed, can you build that? Fifteen minutes. 

Fifteen minutes and I had a tool that you just run and it populates. That's it. Nothing. I can I can provide an episode and it'll go do old ones or I can just run it and it'll be the latest? Mhmm. It commits to the data. It doesn't commit. It saves it to the repo and then all's I do is commit it and push it. It can commit also. Probably. Yeah. Yeah. 

[00:10:55] Kenshin:

I put mine to commit also or I ask it to commit. I it it makes nice messages and stuff. Once I'm happy with it, I'll have it do that. I wanna test on today's episode. But I want to ask you. In codecs, if you do slash model, you choose the model and you choose the the thinking So there I use the model 5.2, not the default model that is a codex model. I use the 5.2, the full model because that's Which burns more tokens essentially. Right? Little bit more but it feels that it's smarter and that's more more general discussions too like those architecture discussions Yeah. A bit better. 



[00:11:40] McIntosh:

Yeah. I was a little surprised it missed that because it seems like a really basic thing to me. But Yeah. But then you need to put the extra high, 

[00:11:50] Kenshin:

the highest level of thinking. Mhmm. And then it really feels 

[00:11:55] McIntosh:

So it's been running with one hand behind its back and it's been working really well. So I guess once I unleash it completely, I'm just gonna rule the world. 

[00:12:04] Kenshin:

Yeah. I I I'm telling you, it's gonna feel different. 

[00:12:09] McIntosh:

I am trying to figure out a good Bitcoin project to build with something like this. I really am and I man, I'm just not coming up with anything. Or even bitcoin adjacent like Noster as long as it involves, you know, Zaps which are bitcoin based. 

I don't know. 

[00:12:27] Kenshin:

Okay. N Y A W. N Wav. 

[00:12:34] McIntosh:

What is this doing? 

[00:12:38] Kenshin:

It's it's not yet another wallet. 

[00:12:41] McIntosh:

Oh, no. I'm not doing a wallet by the way and that's actually part of the problem because there's like 400 out there. Yeah. Yes. No. Yes. No. Okay. Block height as we record unless it's changed in the last couple minutes which I will check. Nope. It has not. 932159 or 932159. Okay. So today's topic, Kenshin. What are we talking about? 

[00:13:13] Kenshin:

Well, someone was running Bitcoin. 

[00:13:16] McIntosh:

Someone was running who was running Bitcoin? 

[00:13:23] Kenshin:

Was Harfeeny. 

[00:13:24] McIntosh:

We just had our whole setup completely. You'll have to excuse us. My internet went out. I have no idea why. And so I'm actually running on my phone at this point. 

But we record locally when we record and then we put it together after the fact essentially. So nothing got lost but man it was it messes you up. So yes, Hal Finney 

[00:13:51] Kenshin:

Yeah. 

[00:13:52] McIntosh:

Was running But I'm big still on breaking up on me. Really? Well maybe let's turn off our video. 

[00:13:59] Kenshin:

Yeah. I think so. Yeah. It's just not enough signal. 

[00:14:04] McIntosh:

Turn off camera. There we go. Okay. Let's give that a try. So Hal Finney was one of the early early contributors to Bitcoin. When so I guess a basic timeline, let's run through this real quick. 10/31/2009, Satoshi posted the white paper. Is that right, Kenshin? 

Does that sound right? Yes. Then in very early January he kind of started things. He mined the Genesis block. What day was that? January 0 was it the 2000 and The Oh sorry the third. Okay. I'm not good with dates by the way ladies and gentlemen. Just ask my wife. But anyways, and then on January 10 late at night 09:30PM, he was a night owl, Hal Finney posted running Bitcoin on Twitter. What what he meant by that is he was he was running a Bitcoin node. He most likely was running a miner as well. Back then, the miners were just using CPUs. Although, I guess in 2010, they started using GPUs. 

So probably another year later. No. But it's it's 

[00:15:37] Kenshin:

2009. 

[00:15:38] McIntosh:

Right. No I understand. A year later, yes, you're correct. Nobody was using GPUs at that point. He most likely was actually running the mining software as well. Now that's not typical these days of course but really really cool to see. 

[00:16:03] Kenshin:

So Yeah. And and then two days later, January 12 is Mhmm. Is the first transaction that Satoshi Nakamoto sent 10 Bitcoins to Halfini. So that was also now. So Like I 

[00:16:18] McIntosh:

wonder it seems to me maybe I'm mistaken. It seems to me that that Hal and Satoshi, basically, they already had they already knew each other. So I wonder how far back that goes. I know there was the crypto what did they call it? Sorry. There was a There you mean list. A mail list of cypherpunks. 

That's what they called it. And I understand Satoshi was not on that list at least under his name although they suspect that he was on it under another name. Now I believe that's correct. And if I'm wrong, I'm sorry. But I don't know if Hal Finney was on that list. 

[00:17:10] Kenshin:

I mean, he must have been to be so early. That was probably the only way you could hear about Bitcoin back then. 

[00:17:24] McIntosh:

10/10/1992, Hal Finney joined the Cypherpunks mailing list. 

[00:17:30] Kenshin:

Wow. '92? 

[00:17:31] McIntosh:

Yes. '92. This man continues. He's just yeah. Amazing. Where where did it go? Well, I'm not gonna take time to look it up. Anyways, so he certainly was. 

My understanding is Satoshi under his name was not on there. Okay. Mhmm. So he posted the Bitcoin. Alright. So Satoshi was on the mailing on the Cypherpunk's mailing list, and he actually posted the Bitcoin white paper there, 10/31/2008. I gotta get my years correct. So I don't know how active he was, but he and Hal would have had some interactions on that mailing list even prior to to Bitcoin. Mhmm. It seems to me they certainly hit it off early on. You know, he Hal was the first person to receive a a Bitcoin transaction. That was the 10 Bitcoin. You know, he was up running a node very early on, so on. 

So we just wanna take a little walk down memory lane so to speak, but we also wanna talk about this kind of as today's topic. And my question would be simply this, are you actually running a Bitcoin node? The nodes are are very important part of the network. Right? I'm gonna go ahead and pull up this statistic real quick. Ken Shin, there is a number which should be right about here. The number Do of you have it? It's 25,000 something. 

[00:19:26] Kenshin:

Yeah. 25,257 

[00:19:30] McIntosh:

right now. So what does that means to to the Bitcoin network just offhand? I've not prepped you for this, but in terms of the Bitcoin network itself, having that number of nodes, providing for us? 



[00:19:49] Kenshin:

Well, it's providing resilience to the network because it's Mhmm. One node goes down and the network is not affected, basically. For for Bitcoin to be offline, every single node of those 25,000 to Right. 57 needs to be offline basically. So that's that's the basis of Bitcoin being decentralized and the whole argument there. 

[00:20:16] McIntosh:

Now that's correct. And there's just I wanna throw this out there. There's two different ways that the nodes can operate. They can either operate in what they call clear text or they can operate on the Tor network. The Tor network is a privacy focused network like your your it does not work the same as a regular Internet connection and it is not as visible. 

It's not traceable, this kind of thing. And there's also a figure in our notes there, Kenshin, on the number I believe or maybe it was where I looked it up. It it the the percentage of TOR versus Clearnet, I believe, is about half and half. Okay? And if you look at various maps of the Bitcoin network, there are gaps. I will say that. It is spread essentially all around the world. But if you look at it, a lot of it is concentrated in The United States and Europe. There are some down in South America. There are some down in Australia, up in that area. There are some in Japan, Korea, that area. 

But there are vast areas that there's either very little or none at all, like basically Africa. There's apparently very few nodes there. Russia, there's a few, but not that many. China would be the same way. I do see some on China but not a whole lot. Canada ironically, I guess there's some down in Montreal and Toronto but in general Canada is quite dark so to speak. Just a lot of areas of the network of the planet that could be a you know, they can have a lot more nodes and there's nothing to keep people from running nodes. One of the things I think a lot of people don't understand about Bitcoin is anyone can run a node. You don't have to be somebody like Hal Finney in order to run a node. 

Do you remember actually, Kenshin, the first time you ran a node? Oh. I completely do not. So I'm just gonna say that. No. It was way 

[00:22:46] Kenshin:

early. Mhmm. It was with a Bitcoin core that you install on Windows. Oh, wow. I'm sorry. You have this graphical interface, you know? Yeah. 

[00:22:59] McIntosh:

Yeah. 

[00:23:00] Kenshin:

That was quite early days and it was a quick experiment, let's say, at the time. So you bought 90 Bitcoin or a 100 Bitcoin and called it a day and got off? You you couldn't buy Bitcoin at the time. Right? What? You just couldn't. 

[00:23:17] McIntosh:

You had to mine it or year was this? I didn't realize you went back that far. 

[00:23:23] Kenshin:

No. But I didn't do much. That's the problem. I didn't stay. 



[00:23:27] McIntosh:

This will never work. 

[00:23:30] Kenshin:

No. I it was exciting, but you couldn't do much. Right. So and I didn't understand it. I don't know. I tried to mine it with CPU in a laptop. 

[00:23:42] McIntosh:

Right. So was it already to the point where they were like GPU and you you weren't Okay. Getting 

[00:23:52] Kenshin:

It's okay. I was getting I was getting something but it was like zero point zero zero something and I thought, oh, this is is too it's nothing. 

[00:24:02] McIntosh:

So now don't really remember exactly to I mean, I cannot tell you, oh, this happened and I found Bitcoin. The earliest records I have were from 2013. 

I have an email from when I logged into Mt. Gox and Mt. Gox in 2013 was hacked. I don't think I lost any bitcoin in that. I'm sure well, I also know I don't have any bitcoin from that era and I'm not just saying that, I don't. But at that point, like you could get an account on Mt. Gox and you could buy bitcoin and it was ridiculously cheap. It was probably a $100. I think think actually my earliest purchase of bitcoin it was $300 and I didn't I did not buy a whole bitcoin. But, you know, the sands of time, I don't know, we didn't understand. We, you know, neither one of us, very few people. 

It is amazing how many people you talk to. How many of them truly did not they did not understand what they were looking at initially. Very, very few people who did. I heard an interview one time. It just blew my mind. Like, the guy heard about Bitcoin, read all up on it in, like, three days' time. Like, he just spent three days just, like, finding everything he could, and that was it. He was done. And this was early, like, this might have been around that same time, like, thirteen or so. 

[00:25:45] Kenshin:

You 

[00:25:46] McIntosh:

know? He he was just all in. And I'm like, how do you do that? I I don't know. I don't. I I don't know. Okay. Anyways, back on topic because one of my resolutions this year is to stay on topic. 



[00:26:05] Kenshin:

Yeah. But do you run a Bitcoin node? Do I? Because 

[00:26:10] McIntosh:

out of the 25,000 

[00:26:11] Kenshin:

online. 

[00:26:12] McIntosh:

How many nodes do I run? So we run one for our lightning setup. I run I guess I run two. I thought I ran three. Maybe I did for a while but now I run two. I run one on the lightning node so you could say you run that one. I'm good for that. We co run that one. And then I have one here on actually the server that we're recording from. I don't keep Bitcoin on it so it's, you know, it's safe in that sense by the way before I get those angry boost and please make them big boost if you're gonna do that. 

I run Bitcoin knots. Run I can never remember. It's the indexing software. 

[00:26:58] Kenshin:

Oh my goodness. Elixiris? 

[00:27:01] McIntosh:

It's a version of it. Yeah it's the rust version I believe but yes it's a version of electress. And then I use my wallet, Sparrow, to connect to that with my Seat Sider. Yeah. 

[00:27:17] Kenshin:

That's good. So 

[00:27:20] McIntosh:

those are the two that I run. Which OS? 

[00:27:23] Kenshin:

What OS is that? 

[00:27:25] McIntosh:

It's Ubuntu on both of them actually. 

[00:27:28] Kenshin:

Okay. So you have installed Bitcoin not on Ubuntu on a Ubuntu server. So to be technical, 

[00:27:35] McIntosh:

if we really wanna go down the weeds here we can, that's fine. I run podman which then runs Bitcoin Knot. 

I run an Ubuntu image on pod man on my Ubuntu server which then 

[00:27:50] Kenshin:

Oh wow. 

[00:27:52] McIntosh:

It's to segregate things. Yeah. Is. Sure. It's complicated and it's more than most people need frankly. You can run it by itself. God forbid you can even run it on Windows just like Kenshin did. I would just say get off Windows. 

[00:28:08] Kenshin:

But I'm not doing that anymore. Don't 

[00:28:13] McIntosh:

I guess this map is actually populating so it's only like 50% done but really overall it really hasn't changed. Anyways, yeah, it's just it sits there, it runs, it enables me to manage my own wallet. 

I don't have to depend on Coinbase or Kraken or whomever. Of course I am decentralizing that network. In my case I specifically and you may disagree with this and this is fine, I don't care. Look, we gotta learn how to live together people. I run knots and I do it because I want competition. I do not want a single platform Bitcoin core in this case providing this the underpinnings for this entire network because if there's ever an issue then we have a severe problem. I think at that point that's all I'm gonna I'm just gonna leave it at that. I've chosen to continue to run knots And I don't see that changing unless something really crazy takes place, which is possible. 

Would love to see more. I know that there is a Rust implementation that they are working on and I would love to see Rust replace the c plus plus that's in Bitcoin Core by the way. A lot of people disagree with that and that's okay. Mhmm. Okay. I I think I've talked about that enough. So what is your setup exactly? How are you doing that? Well, I'm running 

[00:29:59] Kenshin:

one node currently only, I would say, because 

[00:30:04] McIntosh:

I was running two. So I will say the the main one that I run You're running one and a half because you you you should get credit for half the lightning node. 

[00:30:14] Kenshin:

I mean, I have two more sitting not working, but I will explain. So I have one that is my main one Mhmm. 

Which is running start OS Okay. From start nine. Mhmm. And that is the one that is running Bitcoin Notes and Okay. Electros and Mempool Mhmm. And Albihub 

[00:30:43] McIntosh:

I thought Albihub replaced Bitcoin Core or not. No. No? Okay. No. It's only the Lightning ports. Oh, okay. That makes sense. I'm sorry. 

[00:30:54] Kenshin:

Yeah. So it's LND, of course, to be the basis for Mhmm. Albihub and the Datum gateway to do my own mining. But I actually, I'm not using that right now. But, anyway, so I have all these. It starts OS, unfortunately, because, and I I double checked it now, there's still stock conversion 0.30.50.1 Right. Which is from November 2023, which makes me uncomfortable. 



[00:31:26] McIntosh:

That is getting to be quite old and they keep saying, you know, they're going to update it and they don't. And I do not know what's going on there. I don't. Yeah. 

[00:31:36] Kenshin:

And and I can see they have branches open. Mhmm. With version four. 

[00:31:43] McIntosh:

Right. Which has been in development for two years. 

[00:31:47] Kenshin:

Yeah. And it seems in active development like one hour ago. 

[00:31:53] McIntosh:

Some point, yes, they're gonna come out and say, here's version four and everybody's gonna go, great, and move on. But, man, that is a long development cycle. 

[00:32:02] Kenshin:

Yeah. And I I I don't like it. So my other node that I had running for a little while, I was experimenting was nirvati. 

Okay. And near near nirvati, nirvati. Mhmm. And it's a.eu site. Nirvati.eu. 

[00:32:25] McIntosh:

Yeah. And I've got the GitHub link here as well. We'll put these in the show notes. Should be. Nirvati.eu, you said? 

[00:32:36] Kenshin:

Yeah. Okay. It's a GitLab repos. But anyway and they seem very advanced in their setup. You're correct. Sorry, GitLab. They are also in between versions because it's so active development and so early. So in version 0.9, he mentions that they will change a lot the the underlying OS. So I don't want to keep running that until he comes with a new version. Right. So I installed it once. I don't, you know, I don't want to be doing this back and forth. So I'm waiting for the new version to come out which says it's soon. 

Again, soon. So I don't have a node that I I like right now, but I still use my nodes to connect my wallet. Mhmm. And my wallet right now, I was using Sparrow, but because I formatted my computer so many times, I haven't set up Sparrow yet, but I am only using the blue wallet on the phone but with watch only. Okay. My wallet in watch only mode. Mhmm. So I cannot spend. I can only go pick up the money. To lock the keys up for that savings account. Yeah. So and any transactions if I want to pay something, do it with Lightning and I have Albihub there Mhmm. Again in my notes and there I have a few funds that I can use which of course could go bang and I lose them but it's not much. Right. 

I mean, how many Sata have lost opening and closing channels and doing all those things? Mean, it's crazy. 

[00:34:26] McIntosh:

Until this last setup, I lost a lot. And one day I will not think about that but I would regret it if I did. When sats are a dollar and we're using micro satoshis for cents. Yeah. Narvati, I have followed for a while. I hope he comes out with a complete ready to go implementation. And by the way, Nirvati, if you'd like to sponsor this podcast, you're welcome to do so once you get that version out. 

[00:35:02] Kenshin:

And you know the cool thing with Nirvati, he's using Kubernetes Yes. And some other technologies. 

And the and the new OS will be out of the box ready to if you set up two nodes Yes. They will sync together. So if one goes down, you have the other one. 

[00:35:23] McIntosh:

And my understanding is he's also developing it so at least you can easily run it on a VPS versus, like, locally. Mhmm. Start nine. What's the one that starts with a u? There's Umbral, you know, they're designed essentially to set up on your local network and you run them there. But some of us, you know, don't have ISPs for example that play along well with that. And Mhmm. So it's better for us even if it puts more like, it's you you have to protect it better, but it's better for us to have it on a v VPS, a virtual private server. 

Alright. So Navrati looks like they're gonna kinda support that out of the box. Now Kubernetes, as cool as it is, is even more difficult for people to understand than Docker, is what underlies Start Nine or Umbral. I'm not sure that maybe a beginner should be starting with this, but we'll see. He could blow me away. I'm not I'm withholding any judgment until I see the final product. But again, if you want to support the podcast I'm just kidding. Yeah. But 

[00:36:44] Kenshin:

honestly, the I would say I have regretted going with start something yeah. But in a way, even with Umbrew, something that is, let's say, full featured and and Right. Beginner friendly. 

Right. The bad thing is that the moment that either something goes a little bit wrong or the moment that you are more curious to try something and you it's all locked down. You cannot even run sudo commands or if you can, it's very difficult over that session or they have their own setup. And with Nirvati, I found that it's basically I can do whatever I want in parallel to it. So that I'll I I hope he doesn't lock it down. I don't know how the Why don't we wait and see? We'll do like a few a full review 

[00:37:36] McIntosh:

Yeah. When the full version comes out. I'm perfectly willing to do that. 

Yeah. I'm not a big fan of start for the very reasons that you've laid out and I've had problems with umbral. So I've more or less done my own things and I've been happy with that. I run but I'm I'm essentially what they call a I'm a system administrator. Right? Right. I can deal with this stuff, maybe the average person can't and I understand that. 

[00:38:05] Kenshin:

Here is a shout out. Mhmm. I just saw on Noster. It's it's a person called Be So Easy. Be So Easy. Okay. One word. So he he said he tried Umbral Casa OS and Start OS. They work but it started feeling like I was running an OS just to host apps. That's his words. So he says, so I built Yantra, y a n t r a, Yantra. 

Lightweight, isolated, no system takeover, runs on a Pi or laptop. It looks like a a simple web interface with with your containers running or something. It's a GitHub. 

[00:38:55] McIntosh:

I can post. I can I can give you the link? Okay. That sounds good because I am not finding it. It that word means something in like Hindu and it's it's confusing everything. That would be good. I'd take a look at that. I run podman which is basically another it's a different program. It's like docker. A lot of people these days are familiar with docker. Podman is similar but in my opinion it's version. 

Yeah. I well, it does things differently and I believe in a better way but that's just my opinion. So I run my own little docker with with whatever it is that I'm running so I'm kind of hand building my own setup but then I don't have like the fancy web interface either or whatever. That doesn't bother me but it could bother people. I don't know. Okay. Yeah. We'll put that in the show notes, Yantra and we'll put Nirvati. I think Nirvati's also, where's all these Hindu words? Anyways, very cool. Very cool. So look you don't have to make it that complicated. 

You really don't. You can just run if you have a desktop sitting there. Even if you're running Windows, you can run it on a Windows desktop. 

[00:40:21] Kenshin:

Yeah. And and by the way 

[00:40:23] McIntosh:

Go ahead. 

[00:40:25] Kenshin:

Yeah. And and and to make it even less scary, you can run it, as you said, on a Windows with a pruned 

[00:40:33] McIntosh:

setting. Right. 

[00:40:35] Kenshin:

Exactly. You don't even need the whole terabyte of free disk that you need nowadays for a full node. Right. You just need a few gigabytes, twenty forty, I think, or something, and it's fine. Now 

[00:40:49] McIntosh:

I would recommend you could run it on Windows. You can run it on Mac. You can run it on Linux, at least Bitcoin Core. I do not know for sure about knots. Listen. 

I would recommend in any case, do not use this as your wallet. Okay? Just as a security tip, there's a wallet in Bitcoin Core. I'm pretty sure there's one in Bitcoin Not. You can run your own wallet separately just like Kenshin and I do where we run I run Sparrow and he's using, what did you say, blue wallet. Right? You can do something like that. You do not need to use the Bitcoin Core wallet or the, you know, node wallet. I and I would strongly, frankly, recommend that you do not. 

[00:41:47] Kenshin:

Yeah. Agree. And they have a bug right now in Bitcoin Core, the latest version with Yes. We talked about that last Yeah. Restoring wallets in Bitcoin Core. I 

[00:42:01] McIntosh:

just to me, I don't I've never understood well, I understood I understand. 

Words are so difficult sometimes. I understand early on why they bundled the wallet. I don't understand why they do it anymore, but that's just me. Okay. So you could do this to support the network. You could do this to support your privacy, by the way. That's very important and I would highly emphasize that. If you run your own node with a proper setup, probably using electors or some version of that, then, you know, you're good to go in terms of your privacy. It certainly helps. I don't wanna say covers everything but Yeah. And those setups are usually 

[00:42:54] Kenshin:

by default running on Tor network. 

So that's also you don't have to worry about your ISP knowing that you Right. Run a Bitcoin node or anyone else. Right. So it's it's quite private and secure in that way. Okay. 

[00:43:12] McIntosh:

Have we covered this enough, or is there anything else we need to talk about? 

[00:43:15] Kenshin:

Sounds good. Okay. Hopefully, more people run Bitcoin from your 

[00:43:21] McIntosh:

Here's the numbers right now. As we mentioned, 25,257, 77.76% of those are Bitcoin Core, and then twenty two point o 7% are Bitcoin Notes. I'm not gonna tell you which one you should run. That is your choice. As I said, I love diversity. 

So, again, I'd love to see a a Rust implementation in there at 10%. I'd I would love to see some of these numbers a little more even. Alright. What else do we got today, sir? Okay. So our question of the week, Kenshin, is are you running a Bitcoin node? I hope to hear from some of you. I hope to hear some of you say, wow. I just started one up. It's sinking as we speak. If you need any help with that, I'd just throw out you could get ahold of his son, Noster, and, you know, don't need to overwhelm us, but I don't think he will. I think we'd be willing to help you if you need some help. If 

[00:44:28] Kenshin:

you need some help, good luck. 



[00:44:30] McIntosh:

Oh, okay, Grinch. I'll help. Man. 

[00:44:41] Kenshin:

Oh, do we have any supporters? 

[00:44:43] McIntosh:

No. Ken is trying to finish up his website. I get that. Yes. We got supporters. Sorry. Oh, I just spiked the thing and probably blew out everybody's ear eardrums. Yes, Kenshin. We have some supporters this week. There were two, in fact. Why don't you read the first one? 

[00:45:01] Kenshin:

Send it Mike. Mhmm. Happy New Year. Yes, sir. That's me that's me telling you. Send it Mike. Yes. So sent in Mike sent us 1,069 sats, and he says, I don't make price predictions because they aren't of any value. I will make a relative price prediction. I expect Bitcoin to outperform silver and gold in 2026. 

The AI stocks may outperform due to the yet to be announced Winning the AI Pattern spending package that will be a massive bailout to the AI companies who can't make money. I look forward to hearing about the Buffalo ranch. I enjoy a good Buffalo burger. 

[00:45:46] McIntosh:

That's awesome. I enjoy them as well. 

[00:45:51] Kenshin:

Where where do you get the Buffalo burger? So 

[00:45:56] McIntosh:

I may have to go get some water. Hang on. So Ted Turner who married Jane Fonda, he's a celebrity type person, for whatever reason got involved in Buffalo years and years ago, has a huge ranch out west and has a chain of restaurants called Ted's. Is it just Ted's? 

I think it may be. But they serve buffalo or beefalo which is half it's a crossbreed of a buffalo and a cow because some people don't like buffalo because it's a little lean. I don't I I've always enjoyed buffalo whatever the form. That's the only place I've had it and I've only had it a couple of times. But, yeah, I'm unfortunately a long way from that. Send it, Mike. I'm just gonna be honest. Probably at least ten years. I'm pretty sure by then I will not be doing this podcast. But, hey, maybe we can keep in touch and you could come out to the ranch and and have a steak. I've I'll give you a steak. If you're gonna come on out, sure. 

That's that would be awesome. I appreciate it, send it, Mike, and I am completely 100% not surprised you did not make a price prediction. I that we were talking beforehand and and Kensho was like, yep. That sounds that sounds right. We just like to have fun with it. I don't know. I maybe we shouldn't. I'd I am aware. I I'm conscious that we don't wanna be leading people. That's why we shout every week, you know, just DCA. Don't worry about the price. 

[00:47:42] Kenshin:

That's and that's why I gave two price predictions. 

[00:47:45] McIntosh:

Right. And if it if I will agree, it will probably I believe it will outperform silver and gold. And both of them, I expect to do well this year as well. 

So I don't know about the AI stock stuff. I I you may be right. Trump is warming up the printers as we speak. So, you know, I could see that. I could definitely see that. Okay. And then the second one, bullish clips, which is the the bullish bitcoiner. 500 sats. He said or she said, you better believe I listen to this podcast. Thanks for shouting out take my sats. You pretty much got it right. It's like a Shopify but Bitcoin only. Also, the next bullish market is coming up on January 21. He does that the twenty first of every month and that is definitely coming up. 

[00:48:44] Kenshin:

But for me, it looks January 22 because of the time difference. You're 

[00:48:49] McIntosh:

over in Europe. 



[00:48:51] Kenshin:

One year. What can we say? 

[00:48:53] McIntosh:

You know, you can't have everything. You got culture, you got Paris, you got Norway. I mean, there's like fjords and 

[00:49:02] Kenshin:

Vikings So and a request then from my side, if you start the the monthly markets a few hours earlier it will show us January 21 for me You 

[00:49:14] McIntosh:

can never satisfy the customers. Okay. Well there you go maybe something to think about because Europe, by the way, is a pretty big market. Just saying. Come chat with vendors and support this circular economy, the one that we all need to build. Everyone is welcome. You don't need a Nostrad account to join, but you do need Bitcoin to buy. 

Mhmm. Set your reminders and bookmark the link at httpscolon//bullishmarket. That's bullishmarket.onrender.com. I hope I said that clear enough. 

[00:49:56] Kenshin:

Yeah. Or follow bullish on Noster. Noster. 

[00:50:02] McIntosh:

Yep. Which I do and whenever I see those bullish market post I try and repost those. I love to see people doing this type of stuff. Bootstrapping systems. Great stuff. I wished I would have thought of the idea darn it but I didn't. He did. So there you go. News notes. We got a few things to talk about this. Gosh, Kenshin, we are in an hour. I mean, we did have time while we were 

[00:50:35] Kenshin:

Yeah. 



[00:50:37] McIntosh:

Ten minutes. Alright. Let's roll. News and notes. We got a few things. Specifically, I want you to talk about the European stuff, Kenshin, especially now that I can't see your message because of my maybe I can. Actually go ahead. Sorry. Yeah. So talk about that. 

[00:50:58] Kenshin:

Yes. So I have a clip of Christine Lagarde, the president of the European Central Bank. She gave she addressed Europe people. How do you say? Population? 

[00:51:15] McIntosh:

Europeans? 

[00:51:16] Kenshin:

Yeah. The Europeans just before Christmas to wish, Merry Christmas and Specifically, 

[00:51:22] McIntosh:

she would have been addressing the EU. Correct? Or is that Europe in general? Am I being an American here and getting this wrong? 

Is the ECB, is that only for the EU or is that all the countries in Europe? 

[00:51:39] Kenshin:

No. It's for the European Union. Okay. 

[00:51:42] McIntosh:

I was right. Basically, 

[00:51:44] Kenshin:

yeah. They control the euro, not Right. Yeah. If you are not in the European Union, you don't really care what they are saying. And I just saw that Bulgaria entered the chat or the European Union. So that's a bit disappointing. It was cheap and nice in Bulgaria. But anyway, 

[00:52:06] McIntosh:

they they will be destroyed soon enough. Okay. Are we gonna be able to play this clip? 

[00:52:11] Kenshin:

Yes. So Okay. I have a clip that is a minute and something long. 

Okay. So here here it goes. 

[00:52:22] Speaker 2:

We're getting to the close of the year, and for many of us, it's a celebration moment. So to all of you who are celebrating, Merry Christmas. To those who are not celebrating, I hope you are having a lovely time. It's also a time to look back and see how much has been done, and frankly, been a lot of work. One thing that the European Central Bank is proud of is to have achieved our target of 2% medium term. Inflation is down to where we wanted it to be. We've also looked at our strategy going forward, and we took stock of the work done by all the teams to see from a strategy point of view how we're going to go forward and whether our strategy is fit for purpose and whether the ECB is fit for the times we're going through. Difficult times they are. The two other big projects that we have worked on and will continue to work on in '26 are number one, the digital euro. We have completed the cycle of the preparation. The governing council has given its go ahead to move to the next cycle, and we're now waiting for the European Parliament to come up with final legislation that will go ahead for the pilot phase and then the launch. The other project, which is not unrelated, more traditional, but still very efficient and needed is the banknote. 

We are revamping our banknotes. Process is well underway, and we will have new design, new faces possibly, and we look forward to that as well. So to all of you, should know you should know that the European Central Bank is standing strong, pleased that it has reached its price stability target, and determined to make sure that this remains the case and that we are useful for our European compatriots. Have a very happy holiday. 

[00:54:07] McIntosh:

Compatriots. I wonder where that comes from. We are useful. Here's what I find funny. The world is burning. We've got problems galore and she has to highlight, yes, we're gonna put new faces on our bills. 

Like that matters. 

[00:54:25] Kenshin:

And she highlighted an efficient process to do it. It's like, because why why say it? Because it's probably cost millions and millions. Billions. Just, yeah, just to revamp it. And it's like, oh, necessary. She said necessary and efficient. And then she in the beginning, she said difficult times, very difficult times. But we hit our target. And whenever someone says we lowered inflation at 2%, it's like, it's still inflation, it's still going up. A 2% is plus and plus on top of the other insane plus we had the past few years. Well, 

[00:55:08] McIntosh:

I would suspect that it's not actually 2%, but let's just let them have that so to speak. For one thing, the Keynesian economist, which I'm sure she gets all of her advice from, believe that it's necessary that you inflate if only to grow the GDP. 

And that 2% that they steal from you every year amounts to almost a 100% debasement over your lifetime if it stays at 2%, which it doesn't, but let's just go with that. That's what's so frustrating to me anyways. 

[00:55:53] Kenshin:

I don't know what and what they say 2% countries in the European Union 

[00:56:00] McIntosh:

or I believe that's what should be. 

[00:56:03] Kenshin:

The ones who use Euros. 

[00:56:05] McIntosh:

These people do not have your best interest in mind, ladies and gentlemen. And if I were you, I would do whatever I could to keep my family's legacy and wealth and whatever out of their hands. 

[00:56:23] Kenshin:

Yeah. And the biggest telephonic in the room in that that that clip was the digital era. Mhmm. They have the okay from the governing council. 

Which one would that be? And then they're waiting for the European Parliament to draw legislation for it. So there's that hope they will mess it up. 

[00:56:47] McIntosh:

That's That way they can tell whatever you do, whenever you do it, every little detail, it'll all be logged, it'll all be controlled, and eventually it will all be used against you. We One thing that The United States has done right so far is resisted having a central bank digital currency. Alright. We've got two more. Well, talk about the travel rule as well. Sorry. 

[00:57:18] Kenshin:

Yeah. Then I received we have talked about MICA. 

Mhmm. Marketing crypto assets is those European rules that say how to conduct businesses with cryptocurrencies in Europe, and they have some very strict legislations. And so for companies to be compliant, you need to give details when you do transactions, who the sender is and who the receiver of that crypto amount is. And now I got an email from a company which I don't even know who they are. I don't remember using them lately. It's called Uphold. Mhmm. Anyway, it's probably an exchange of some sort. And they said that you even need to give information of whether the wallet is self custodial. 



[00:58:15] McIntosh:

Right. Because 

[00:58:17] Kenshin:

Yeah. Can't allow And then it says, which may require additional steps or if you're using a host hosted wallet by another exchange. And where is it? It was changing. Yeah. If you're sending to or receiving from another exchange, you may be asked to provide counterparty details and select the exchange from a list. Where possible, we'll attempt to gather their required information. Blah blah. In some cases, transactions may be delayed or unavailable if required information cannot be provided. 

[00:59:00] McIntosh:

So there you go. I I don't even know what to tell you, Kenshin. You're using Bitcoin in Europe? No. I'm not. Yeah. 



[00:59:08] Kenshin:

You should not be using Bitcoin in Europe. And you want to do business with Bitcoin or other cryptocurrencies in Europe, you need to comply with all this. I don't know how Stripe does it. Yeah. Be to be honest, and I use Stripe. And Mhmm. When I have used to send to not let's say, to send Bitcoin somewhere, They ask, is that your wallet or someone else's? And they have to, you know, check this or check that. Your wallet, someone else's. You press someone else's. That's it. 

[00:59:50] McIntosh:

Is there a third option? None of your blankety blank blank blank blank blank business? 

[00:59:55] Kenshin:

No. But it's funny because you say someone else is, fine. It's it's okay. I can say someone else. When I used Revolut, the last time I used Revolut was when they complied with this MICA tool, MICA rule before they had to comply with the MICA rule. 

So they complied in advance, a few months in advance be before it came into effect. And that's when I stopped using Revolut with Bitcoin, and they asked specific name to enter to where users are sending the Bitcoin. And that's what where these other exchanges, what I read now, they're doing the same. You need a specific name where you send it to and if it's self custodial or not, and they might block your notes. So it's it sounds very bad. And this is exactly what we want to avoid by having Bitcoin and I mean, we're back into square one with them. 

It's a bit disappointing in that way. 

[01:00:59] McIntosh:

Well, I have more bad news. Pretty much, I guess. I don't know. But I have more news anyways. It's not great. Yeah. In Uganda, I'm not clear on when the election is. I actually thought it was today, but a whole slew of new articles came out in the last couple hours that seems to indicate that it's not, although they do not say when it is. Uganda is in the middle of this election cycle. They have had the same president who's ruled the country since 1986, which is a while ago. He's in his eighties and I think he's seeking his seventh or eighth term. 

And there's a lot of people who say that the election is rigged, it's been rigged and, you know, all that kind of stuff. Well, today, apparently, they cut the Internet in the nation. And the decision this says the decision by the Uganda Communications Commission was taken by the National Security Committee to prevent the quote weaponization of the Internet as well as misinformation. Okay. So we've got this going on. It doesn't look good. The candidate who is running in opposition did something I thought was was very interesting. 

A few weeks ago I think he realized that this was highly likely that this would happen and he started telling his his people, his supporters, you need to start using bit chat. So bit chat is simply a little it's a program that runs on I think on iPhone and Android both. I'm quite sure it does. But it uses Noster, a combination of Noster and actually Bluetooth if there's no Internet available to build a communication network, a mesh network. So it's a way for them to at least somewhat get around this Internet ban that is taking place, to be able to communicate, to be able to organize, and this kind of thing. Now do I think that's gonna change this election? 

I'll be honest. I don't think so. I suspect that the dude that's the incumbent, as they would say, is going to get reelected. But I thought that was a very interesting use of that technology and it should be highlighted. And then there's another situation going on in Iran over in The Middle East. There's massive protests throughout the country. They want the basically, the religious leaders of the country, the shah, out of power. And they're meeting massive resistance against that. The police are, you know, out there. The the government itself is saying that there's like five hundred dead, which I believe the number's actually a lot higher than that. 

But they're officially saying there's like five hundred dead from this day. I believe, today, it may have been it may be tomorrow, at least in my time. And I look. Don't let your kids listen to this if they're in the car. Just turn it off. I'll give you a second to do that. Not the kind of thing I'd really want my kid listening to. But they're actually the government has said they're gonna hang their first protester in the next and whoever it was that was arrested a couple weeks ago in the next day or so. I mean, it's just a brutal, brutal situation. And Bitcoin and bit chat are both being used very heavily in this environment. 

These are freedom tools. And the Bitcoin angle is their national currency. I it's r I a l. I do not know how to say it exactly. Real or something like that. It is down yesterday, I believe, 95% against the US dollar in one day. It had already been falling. But for whatever reason, yesterday it dropped significantly. I mean, people's wealth, people's life savings is evaporating in front of their eyes and Bitcoin, of course, is a way out of that. So I did wanna bring those to your attention. It's not the kind of thing we normally talk about on here, but sometimes I feel like these things are so important. And it's it's great to see these tools being used for freedom purposes. 

You got anything to say about that, Kenshin? Or is that about it? No. 

[01:06:03] Kenshin:

I I never tried this app. I tried something similar before. I think we mentioned it before. I don't remember the name now. The Mhmm. Whatever. But it's a cool app, but, of course, in a country like that, it's very useful. But in for my use case, I would only be able to send to my wife a message here. So Right. 

[01:06:26] McIntosh:

Right. 

[01:06:28] Kenshin:

Okay. It's a cool technology. 

[01:06:30] McIntosh:

Yes. Definitely. Definitely. Alright. So a couple of software updates and then we'll wrap it up and get on out of here. So we've got join market. So join market is something we've talked about in the past. 

If you remember, they have a graphical interface. It's a way to mix your coins. It's a way to anonymize your presence, your Bitcoin profile, whatever you wanna call it. And they have a graphical interface to that called Jam, which I've mentioned in the past. Mhmm. Apparently, that project has been fairly like, the code has not been updated for a while. So somebody kind of cranked things up. They've decided to do it in Python. And this is the second release that I've seen posted about. It's called join market NG or new generation just in case you didn't catch that. 0.9 dot zero. So if you're involved in join market or if you're thinking about being involved in join market, long term this is definitely something you're gonna wanna look at. Because I I think in order for join market to move forward, we're going to need something like this. And we need tools like join market. 

And then the only other thing was Zeus came out with a new alpha version of zero dot 12 dot two. So knowing them by now they probably already got zero dot 12 dot two, the final version out. But man, they crank out releases like crazy. It's something else. Alright. You wanna run through the price or the you want me to do the price and you can do the cap? 

[01:08:06] Kenshin:

Yep. Let's do that. 

[01:08:09] McIntosh:

Alright. So we've got a bitcoin price as we started recording. Will say that because the price has been pushing up all day. 94,180 and in euros that was 80,800. 

So bitcoin woke up today, chose violence and moved from roughly I think 91,000 or so up to this level. We will see where it goes. Our price last January 7 was $94.05 $1.06 which does mean for right this moment we are down 0.36% year to date. Market cap, sir. 

[01:08:52] Kenshin:

Bitcoin market cap at 1,800,000,000,000.0 USD. It's closer to 1.9 now I think. Gold's market cap 31,000,000,000,000 which brings us at 6% of the gold market. 6%? Yep. 

[01:09:08] McIntosh:

By the way, we don't normally mention silver but I will say that silver has been on a tear. I gotta get this in. I'm sorry. I'm sorry. 

Bear with me. Right now it sits at $86.88. It hit $89.22 either late yesterday or today, early today, I'm not sure, but then it dropped a little bit. So Mhmm. Gold, silver, Bitcoin, they're all starting to move. I don't know. You will see. And then our mempool fees so if you're looking to move transactions around on the main net, two sats per v byte, we got 35,000 unprocessed transactions, about 250 megabytes. In the mempool, not a whole lot. Things are fairly cheap. We're oh, we came up with a great statistic. I thank you for digging this up, Kenshin. 43.89% of the way to the next halving. 

I don't even know what we're at. What is it? 3.5 bitcoin per block Three point right 

[01:10:21] Kenshin:

one twenty five. 3.120. 

[01:10:24] McIntosh:

How am I gonna do that math when it halves again? I don't math well. I don't know. But it keeps going down. Price keeps going up. Zoom out. We're looking at 04/11/2028 in about two years and eighty eight days. So Mhmm. I already went through the node count, so we certainly and you did we both did some of it, so we don't need to do that, and off we go. Satoshi's Plebs is a value for value podcast supporting podcasting two point o. We strive to bring you honest bitcoin content every week. We ask, are you getting value from this show? Support it through time, talent, or treasure. Help with our future projects. 

You can stream sats, boost messages, even a 100 sats saying great show or you suck. We'll read it either way. We appreciate our supporters. Check out the apps at podcastapps.com and support Independent Bitcoin Media. If you like the content, would love it if you would write a review on Apple and tell your friends about the podcast. That is the best way for us to grow. This week's music is empty passenger seat by Joe Martin. Brand well, brand new song for us. It's been out for a little bit. Any boost or streaming of Sats during that song will go straight to the artist. 

[01:11:49] Kenshin:

Great. So thanks for joining us again this week. You will hear from us again next Thursday morning. 

We hope this has been helpful, and we would love to hear from you on Noster or on Fountain. Find all our contact info at satoshi-plebs.com. Stay humble this year, those subs, and have a great weekend. We'll talk to you all soon. Bye bye.
```
