---
title: "Episode 244 Transcript"
draft: false
_build:
  list: never
  render: always
---
McIntosh:00:00:01 Welcome back to Satoshi's Plabs for episode two forty four. I'm Mcintosh.

Kenshin:00:00:06 I am Kenshin. And today, we're talking about Bitcoin fees, the mempool, and UTXO hygiene.

McIntosh:00:00:22 You are getting really good at that.

Kenshin:00:00:25 Yeah. I I was on the enter button.

00:00:28 Yeah.

00:00:30 So today,

00:00:32 we are digging into the part of Bitcoin everyone pretends they understand

00:00:36 until a transaction gets stuck.

00:00:39 Have you ever experienced that, McIntosh? Not on the mainnet.

00:00:44 No? Okay. I have.

00:00:46 Yeah. So we will talk about that, about the fees, the mempool and UTXO Hygiene.

00:00:52 We will frame fees as what they really are, a live market for scarce

00:00:57 block space,

00:00:58 then break down what you're actually paying for in such per v byte,

00:01:03 how to read mempool conditions without turning it into a full time job,

00:01:08 and the two real escape hatches when things go sideways,

00:01:12 RBF and CPFP.

00:01:14 So return by fee and child pays for parent.

00:01:18 Mhmm. So, hopefully, by the end, you'll have a simple playbook you can use this week so you can spend Bitcoin like money

00:01:25 without overpaying

00:01:27 or getting trapped waiting on confirmations.

McIntosh:00:01:31 Awesome. Looking forward to it. But before we get there, Kenshin,

00:01:36 since you're not watching the Olympics,

00:01:38 I'm gonna go ahead and break that news.

00:01:41 What are you doing this week?

Kenshin:00:01:45 Well, I actually

00:01:47 did some road tripping

00:01:50 trip. Okay. Road trip. So I drove

00:01:54 five hours

00:01:56 to one city

00:01:58 and then five hours back on the 70. Oh.

McIntosh:00:02:03 And how long were you in the city?

Kenshin:00:02:07 Around three hours, I think. Wow. That's a long day.

McIntosh:00:02:11 Yeah. That was really long day. Just ten hours of driving period is a long day. Yeah.

Kenshin:00:02:17 And on the way back, you know, it's when you go, it's exciting and Right. You you begin of the day and it feels yeah. It feels good. You don't get tired and it's fun. The way back is From like home, you're ready to die.

00:02:32 Fuck. Yeah. Three

Unknown:00:02:34 hours from home, I was like, is it still three hours? Really?

00:02:38 And it's dark and you cannot see. Yeah.

McIntosh:00:02:42 Yeah. So that was Wow.

Kenshin:00:02:45 Yeah. That was a lot.

00:02:48 But we made it, me, my mother, and my dog.

00:02:52 So

00:02:53 that was good. Alright.

McIntosh:00:02:55 And your dog. You took the dog on the trip.

00:02:58 Yeah. Let's see. You have a smaller dog. Right?

00:03:02 Yeah. You you showed me to him on camera one time or her. Sorry. I don't remember which. Him. Yeah. You showed you showed them to me on camera. I remember. Yeah.

00:03:12 Yeah. Very cool.

Kenshin:00:03:14 Yeah. He was he was very well behaved. I was very proud of him. Yeah. If I ever get to the point

McIntosh:00:03:21 again,

00:03:21 I actually used to drive a lot,

00:03:24 like road, you know, travel.

00:03:27 If I ever get to that point again in my life, I I do. I want a dog to go on the road trips with me and

00:03:32 sit there. Course, it sounds great, but what that means is you have to stop every couple hours for the dog to go to the bathroom and, you know, it's

00:03:41 whatever.

00:03:42 So

Kenshin:00:03:43 Yeah. It it it was a bit stressful for this reason also. Yeah.

McIntosh:00:03:47 Not as glamorous as it sounds.

00:03:51 Oh, me and old Bo sit there and we drive along. Anyways.

00:03:55 Alright.

00:03:57 Well,

00:03:58 I will be honest.

00:04:00 I had something happen this week I wanted to share with y'all.

00:04:05 It doesn't well, it does involve AI, but not in the way that you maybe think.

00:04:10 And it does involve today's topic,

00:04:13 actually,

00:04:14 oddly enough, in a in a different in a in a way, you'll see.

00:04:18 So

00:04:19 we have a lightning note

00:04:22 for

00:04:23 these Toshi's Plebs podcast.

00:04:26 And much like

00:04:29 the shoemaker's children,

00:04:34 the

00:04:35 Who?

00:04:36 There's

00:04:38 a children's tale about the shoemaker's tilt children and, like, they don't have shoes because he's too busy making shoes for everyone else.

00:04:48 Much like that little child's tale,

00:04:51 I don't take care of our stuff as much as

00:04:55 I should

00:04:56 and it backfired on me.

00:04:58 So apparently,

00:05:00 it turns out

00:05:01 our

00:05:03 lightning node went down back in mid January,

00:05:08 like the maybe it was a little bit later, but somewhere around there. And

00:05:14 one of our nice

00:05:17 listeners

00:05:18 sent me a message on Nostr. It was bullish Bitcoiner, I believe. And if I'm wrong, I apologize.

00:05:26 But they sent me a message saying, hey, my boost didn't work.

00:05:30 I don't know if it was on my end or not, but you might wanna check on that. Well, turns out it was on our end.

00:05:36 Lightning was not working correctly.

00:05:38 I got things back up and running pretty quickly.

00:05:44 But

00:05:46 but we had a channel, so there's channels with lightning

00:05:51 and they

00:05:52 basically run from both sides. Like you open a channel with another node and that node participates in that and so on and so forth.

00:06:00 Because we were down for a couple weeks, I don't blame them,

00:06:03 honestly,

00:06:05 but the the other channel forced closed

00:06:07 the the channel.

00:06:09 Okay? Now what normally happens in that case when you have a forced close,

00:06:16 The money gets returned

00:06:18 to your Bitcoin wallet,

00:06:19 which is Right. The main net,

00:06:22 not Lightning,

00:06:24 and that's the end of it. Well, in this case, because I was offline for several weeks,

00:06:30 it couldn't do that,

00:06:33 I guess. I'm not a 100% well, because my server wasn't signaling from its side

00:06:39 that it was, you know, it was online or that it was okay or or whatever.

00:06:44 And so it essentially got hung.

00:06:47 And then my my node didn't I mean, there was information there, but it was it's very confusing.

00:06:53 This is why,

00:06:55 I don't wanna say amateurs, but if you're just dabbling in Bitcoin,

00:07:00 don't run a lightning note.

00:07:03 Okay?

00:07:04 It's not straightforward.

00:07:07 I sat down that night as soon as I figured this out and I started piecing it together. And me and chat GPT did figure it out. It took a while.

00:07:17 I had to do a lot of stuff.

00:07:20 And to be honest,

00:07:21 I would've had to have gotten online and talked to other people and it probably would've taken days, if not a week or more, to figure this out

00:07:30 if without

00:07:31 ChatGPT.

00:07:32 I'm not saying I couldn't and it was a 100,000 sats. It was a 130,000

00:07:37 sats actually

00:07:38 that was tied up.

00:07:40 I happen to know.

00:07:42 Alright? So it was like a $100. It was not a trivial amount of money and I wanted it back because it was it was my money. There's I'm not there's no cheating or anything going on here. This was the money that was used to open the channel

00:07:56 originally.

00:07:57 And now that the channel was closed, it needed to go back to us. Okay?

00:08:03 So we figured it out,

00:08:06 and I was able to fully recover it within a few hours.

00:08:10 And

00:08:11 we I actually returned it to an address that we both share, Kenshin,

00:08:17 just in the light of full disclosure. It's like pleb nation at coin o s dot com or something.

00:08:24 Now, the final step is if I want, I can now move it back to my Lightning node that it's up and running.

00:08:30 We'll have a conversation about that later. I think that's what we're gonna do, but I don't know. Whatever.

00:08:36 Okay?

00:08:37 Yeah. I learned something,

00:08:39 and it was interesting because essentially,

00:08:42 in a way, my fees were stuck. I mean, they were. They you could see the transaction on the main net. It was kind of wild because it was just sitting there.

00:08:51 Right. So now that's not specifically what we're gonna talk about

00:08:56 in terms of lightning, certainly, but I did think it was interesting that, you picked this exact topic for today. And I had not told you about this until just now. He it's not like you had prior notice of this. So No. It's news to me.

Kenshin:00:09:12 Yep. But, yeah, you made me look at my

00:09:15 personal

00:09:16 lightning node now.

00:09:18 And, thankfully, it's it's running properly.

McIntosh:00:09:21 Well So that's good. Next step is to put some monitoring in place, and and I'll discuss that with you. It's probably something you could use on you know? It'll be it's relatively straightforward because

00:09:34 the service was not it wasn't showing the proper status. I mean and I didn't run out of disk space. It wasn't

00:09:41 that wasn't the problem.

00:09:43 Right. So, anyways, it was I mean, it had been online for a long time.

00:09:48 These things just happen. But Yeah. With Lightning in particular,

00:09:53 it's pretty important that you, to avoid these type issues, that you return it to service as quickly as possible, like a

00:10:01 few hours.

00:10:02 If you don't, yeah, people are gonna start closing channels. Now, fortunately, our million sat channel that we had opened with,

00:10:09 I believe, a listener of the show or maybe a just a follower on Noster,

00:10:14 they kept it open.

00:10:16 So that was good. Yeah. Okay.

Kenshin:00:10:19 Yeah.

00:10:20 Lightning is still a bit advanced, I would say. If you're It is. Running Lightning node, you you you need to know what you're doing still. It's You know,

McIntosh:00:10:29 I used to think that Lightning was gonna be

00:10:34 running a Lightning node was gonna be, like, super simple. Simple. Like, running a Bitcoin node itself is really straightforward

00:10:40 once you get a few concepts down and you understand some things. Lightning,

00:10:46 it can be very esoteric. I don't know if that's ever gonna change. There's some

00:10:52 limitations,

00:10:53 in my opinion, because of channel the the channel architecture

00:10:58 that they built.

00:11:01 And I don't know if those can ever be overcome, to be honest. I don't I don't know. We'll see. They may stay in the realm of basically

00:11:10 super committed hobbyist, if you wanna call them that, and professionals,

00:11:14 and not just everybody runs a lightning node, you know. Hey, you've got Bitcoin, you wanna run a lightning. I'm not I would not recommend to the average person

00:11:23 or maybe even the average listener of this podcast

00:11:27 to run a lightning node. That doesn't mean that

00:11:30 there I'm sure there are some of you who could,

00:11:33 but you just need to be aware of what you're getting into because you're putting money at stake. You are.

Kenshin:00:11:39 Yeah.

00:11:40 Mean, everybody can. It just takes too long to to figure it out.

00:11:45 Yes. More than more it takes more to figure out Lightning than it does to take

00:11:50 figure out Bitcoin with a self custody

00:11:53 your wallets. Yeah. 100.

McIntosh:00:11:56 Exactly. That's a great way of putting it. Alright. Enough about that though. It was a fun experience and maybe one day we'll talk about lightning

00:12:04 in some more details or whatever, but, not today.

00:12:08 What are we talking about today?

Kenshin:00:12:11 Yeah. So

00:12:13 a face,

00:12:15 Mempool, UTXO hygiene. Right? So face What's a UTXO,

McIntosh:00:12:20 first of all?

Kenshin:00:12:21 Oh,

00:12:22 unspent

00:12:24 transaction

McIntosh:00:12:26 Output?

00:12:28 Output? That what it is? I think it is. It is unspent transaction. I believe it's output. Let me double check on that.

Kenshin:00:12:35 Yeah.

McIntosh:00:12:41100%.

00:12:42 We were both right.

Kenshin:00:12:44 Right. Okay. So so the fees in general are very important

00:12:48 Mhmm. Because

00:12:50 there are there are so many bytes in a block. Right?

00:12:54 And there's only one block per ten minutes as we know.

00:12:59 So the fees then play a crucial role there.

00:13:04 Then we need to talk about low fees

00:13:08 and why low fees are important, and they are important to get organized and prepare for the future.

00:13:16 Then we'll talk a little bit about UTXO management

00:13:19 and how to,

00:13:22 yeah, arrange your UTXOs in a good way

00:13:25 and without

00:13:27 making it worse for you in the future.

00:13:31 And and then how to not get transactions

00:13:35 stuck

00:13:36 Okay. In the mempool, basically. Like And

McIntosh:00:13:40 this is what happened to you, you said. Right? You you had a transaction that got stuck.

Kenshin:00:13:44 Yeah. It has happened when you are a bit too

00:13:48 greedy with the fees, let's say. You don't want to pay too high fees. You're thinking, it

00:13:53 shouldn't be that bad. And then

00:13:55 or something happened. I don't remember, actually. I think something happened, and then the fees just

00:14:00 quadrupled and stayed high for a while.

00:14:04 Yeah. Back in the back in the, how is it called, the inscription days.

McIntosh:00:14:10 The inscription crazy. Thanks for bringing that up. Appreciate that.

Kenshin:00:14:14 That was crazy time.

McIntosh:00:14:16 You're

00:14:17 right.

00:14:18 Alright. Very cool.

Kenshin:00:14:21 Let's jump in. Yeah. So if we talk first about the fees.

00:14:27 Right? So Okay. As we said, there are

00:14:32 we pay fees

00:14:34 SAT in SAT per v byte.

00:14:38 So when when you you create a transaction

00:14:42 Mhmm. That transaction,

00:14:43 when you do

00:14:45 one input

00:14:46 to one output, so I put, let's say,

00:14:50 an amount and I send you to a single address, that's the smallest transaction.

00:14:55 Okay. So that transaction, it has one input, one output,

00:15:00 and all this is basically in a text file. So this

00:15:04 is a certain number of characters and weighs

00:15:07 a certain amount of

00:15:10 bytes.

McIntosh:00:15:12 Is it essentially

00:15:13 the address

00:15:16 that you're sending it to converted into

00:15:18 well, that's a that's a string of characters. Right? Yeah. Yeah. And you're you that's takes up a number of bytes of space. Is that literally what In the middle part. Part is? Yeah. Yes. Exactly.

Kenshin:00:15:31 Makes sense. So and and the simple transaction,

00:15:37 yeah, it's very light because you have one input, one output from this address to this address, this amount.

00:15:43 Mhmm. If if you do a more complex transaction,

00:15:47 you can have I I can send 10

00:15:50 UTXOs,

00:15:5110 inputs, or 10 people can send,

00:15:55 yeah, can send Bitcoin

00:15:57 to 10 other

00:15:58 addresses.

00:15:59 So you have 10 inputs, 10 outputs.

00:16:02 Then that essentially, this transaction

00:16:05 is

00:16:0610 times the weight

00:16:08 in bytes,

00:16:11 which means you need to pay 10 times the fees. Right. To put it in the blockchain because you take 10 times the resolving

McIntosh:00:16:19 down to there's a number of characters involved.

00:16:22 Those characters take up a certain amount of bytes of space,

00:16:26 and that's what you're actually paying for. So when you see

00:16:30 the mempool when it says a transaction fee is 1 SAT per v byte like it typically does now

00:16:38 Mhmm. That does not mean you're paying 1 SAT

00:16:41 No. For that transaction.

Kenshin:00:16:43 No. If your transaction is 10 bytes,

00:16:4610 v bytes, then you pay 10 sat.

00:16:4910 sat. And your transaction is always

00:16:53 yeah. Maybe we can see a live one.

00:16:56 Yeah. Transaction is always, let's say, I see here

00:17:0036

00:17:01 sets.

00:17:02 Okay. Yeah.

00:17:04 The virtual size was 206

00:17:06 Vbytes.

00:17:07 I think a 150

00:17:10 to 200, that's the smallest transaction. That sounds right for some reason. Yeah. Yeah. I've seen that many times. So

McIntosh:00:17:19 So that'd be like a 150 to 200 Satoshis

00:17:22 would be the minimum

00:17:24 payment Yeah. For a one sap per v byte. Now,

00:17:27 I would mention, I don't like it as a minor saying this, but I would mention these days,

00:17:32 you have the ability to even go below 1 sap per v byte. Yeah. So a lot of times we'll see it. It's down to like point one sats per v byte. Point one. Yeah. Yes. Which is insane.

Kenshin:00:17:44 It's crazy. So I saw here a transaction with 0.17

00:17:49 per v byte.

00:17:50 One single transaction and they did it with 36

00:17:53 SATs total,

00:17:55 which equates to equals to $0.02.02.

00:18:01 So right now, we keep we kept complaining it's too expensive to send money on the Blockchain. Right. It's 2¢ of dollar. I would say that that actually

McIntosh:00:18:11 which by the way, that's cheaper than sending it across the,

00:18:15 Lightning Network. I'm almost sure.

00:18:18 But I would say that you are undervaluing

00:18:21 the Bitcoin network network at at that that point. Point. That's just me. I'm a selfish miner.

00:18:26 I do not think you should send us a transaction

00:18:29 for

00:18:30 less than a Satoshi per v byte and I still think that's a bargain. But that's again,

00:18:36 you know,

00:18:37 what it is. Yeah.

Kenshin:00:18:41 Yeah. So this is so the fees then,

00:18:44 you pay those fees. Right?

00:18:47 Mhmm. Why do you pay those fees? You pay them. You essentially do a bidding war.

00:18:53 Right. It's like eBay.

00:18:56 You you have a very I've thought about it like that. Yeah. Oh, really? No. That's the case. So you're

00:19:03 trying to bid yourself in the next block.

00:19:06 So the one who pays the most gets a space in the next block.

00:19:12 So that's why I say it's like eBay because you bid one over the other. If you see that the the

00:19:18 average

00:19:19 SAT is at two,

00:19:20 then you put three.

00:19:22 Someone sees then, okay, someone put three then they put four.

00:19:26 So then it becomes like a bidding war and then

00:19:30 the average SATs per Vb byte per transaction goes up.

00:19:34 So in that sense

00:19:37 you,

00:19:38 yeah, you you pay

00:19:41 you always try to pay the right amount

00:19:44 to get in the next block or at least in

00:19:48 in a reasonable amount of blocks forward.

McIntosh:00:19:51 Okay.

Kenshin:00:19:52 And those fees go to the miners.

00:19:56 So each block

00:19:57 has, as we know, the the block subsidy.

00:20:02 So right now it's 3.125.

00:20:06 And then the miner who

00:20:08 gets that, they also get all the fees

00:20:11 that are included in the block.

00:20:14 And

00:20:15 so the higher the fees,

00:20:18 the more a miner makes from from Right. Finding the most interested they are in the block.

McIntosh:00:20:24 Right.

00:20:27 Now

00:20:29 sorry. Let me take a very quick side. I would just point out that is why

00:20:35 the inscriptions and all that other stuff was

00:20:40 worked because the miners simply looked at it. A lot of the miners, I should say, would simply look at it as I'm making more money, and they would pay

00:20:50 to get into

00:20:51 the the transactions.

00:20:53 The arguments

00:20:54 and I'm a miner, so to me, from that perspective, yes, it's attractive, but then the counterargument

00:21:01 is, of course, you're filling up the blockchain

00:21:04 with stuff that's nonmonetary.

00:21:06 It's just not. It's not monetary at all. It's just, in my opinion, garbage and does not need to be in there. So in a nutshell, that actually is why those even worked at all. Sorry. Mhmm. Hope that helps.

Kenshin:00:21:19 Yeah.

00:21:21 Actually,

00:21:22 the miners, I don't know how this works but the miners,

00:21:26 they automatically

00:21:29 put the higher

00:21:32 fee rates

00:21:34 into the blocks.

00:21:35 So if they have two transactions and one is three SATs per V byte and the other is one set per view byte, they automatically take the three sets per view byte into the block. Right? So

00:21:45 that's that's why there is this competition

00:21:47 for us to

00:21:49 we need to put a higher

00:21:50 pay higher fees.

McIntosh:00:21:52 Mhmm. Mhmm. Just like eBay. I I really like that analogy. But yeah. Yeah.

Kenshin:00:21:57 Mhmm. So, of course, the miners make profits. They care about it. They look at the

00:22:03 fee

00:22:04 in SAT per Vb byte. They don't care about

00:22:08 which one is the largest or the smallest transaction

00:22:10 because if for all of them they look at the fee per V byte,

00:22:14 that means they maximize the the

00:22:18 the feed potential

McIntosh:00:22:20 Right. In block.

Kenshin:00:22:22 Okay.

00:22:24 So

00:22:27 what does that all mean?

00:22:32 If you

00:22:34 choose a fee that is too low, if you don't know

00:22:38 about this setup and and that you actually compete

00:22:41 for block space

00:22:43 Mhmm. And to compete you need to to increase your fees,

00:22:47 then you might put a fee that is too low

00:22:50 and essentially

00:22:52 your transaction gets bumped to the next block and then to the next block. Because everybody above you

00:22:58 have paid a higher fee, which means they are added to the block and you're left out because each block has four megabyte space

00:23:05 and each byte counts.

McIntosh:00:23:07 Mhmm. So

Kenshin:00:23:08 you're left out.

00:23:10 And you might be left out for a very, very long time if you're Right. Yeah.

00:23:16 If the mempool is constantly full and never empties, and there's always a

00:23:21 line who gets in.

McIntosh:00:23:23 And eventually, it could even get dropped. I mean, it's theoretically possible at least. It's not normal behavior.

Kenshin:00:23:30 I'll say that. Yeah. Well, yeah. Then if we go

00:23:34 a small tangent into how nodes work,

00:23:38 if the nodes get full,

00:23:44 then most of the nodes by default have 300 megabytes

00:23:48 of Right. Memory space for pending transactions.

00:23:52 If more transactions come in and

00:23:56 essentially

00:23:57 the space goes, let's say, 400, 500 megabytes,

00:24:02 the the node starts to purge

00:24:04 the lower transactions.

McIntosh:00:24:06 Right.

Kenshin:00:24:07 So in that sense, if your transaction gets purged from all the nodes around the world

00:24:13 Then it's gone? It's

McIntosh:00:24:15 gone. Yeah. You need to repeat that transaction. I I would very much say that's an edge case and

00:24:21 not something the average person needs to worry about, but just this base idea of,

00:24:26 you know, if I've got if I'm paying higher payments,

00:24:30 you know, I wanna get in quicker essentially. That's the the key to this. And where is a place that they can see that? Have we talked about that specifically?

00:24:40 Like how can you tell what

00:24:44 the the rates are right now?

Kenshin:00:24:46 Yeah. There are

00:24:48 the block

00:24:50 how are they called?

00:24:52 Now I Block explorers? Block

00:24:54 explorers. Thank you. Yes. Mhmm. Yeah. The most popular I think is the mempool.space.

00:25:01 At least that's what I use.

00:25:04 There are a couple other more that are quite popular but I usually go to mempool.space

McIntosh:00:25:09 now. I blank out And every node has one as well, but they're just not accessible typically. So

00:25:17 yeah. But mempool.space

00:25:19 is kind of the de facto block explorer for the Bitcoin ecosystem.

00:25:25 Just go to mempool.space

00:25:27 and you can see it.

Kenshin:00:25:29 Yes. With a caveat.

00:25:31 Mhmm. I don't look my

00:25:33 transactions on mempool.space

00:25:35 and I don't think you should either

00:25:38 because mempool.space

00:25:41 is a website run by

00:25:44 whoever runs that website. I don't know who. We don't know who which is funny. And

00:25:51 anything,

00:25:52 any query you put in that search bar.

00:25:55 Can certainly be logged. Yeah. Can be logged and probably is by Yeah.

McIntosh:00:26:03 With your IP address maybe. So So this is why we tell people run your own node

00:26:08 Yep. And then you can

00:26:11 connect that up to your wallet,

00:26:14 and it's like a buffer, plus you can use that node as a mempool to look at values.

00:26:20 And it's not very hard at that point to to get that sub. If you're doing like a umbral type setup, I mean, there's just a separate

00:26:28 like like an install or whatever for Mempool

00:26:32 versus your Yeah. Your Bitcoin note itself.

00:26:35 But it really is working in coordination with that. So anyways, I don't wanna get off on that but, yeah, it's a great privacy feature.

Kenshin:00:26:43 Yeah.

00:26:45 Yeah. And I and I use it a lot.

00:26:48 So it's

00:26:49 great. So there in this mempool explorer,

00:26:52 for example, mempool.space,

00:26:54 you can very easily see the transaction fees. Right now, I see live.

00:26:59 The no priority fee is at 0.2 subs per v byte, which is crazy.

00:27:04 The low priority is 0.5,

00:27:07 the medium priority is one, and the high priority is two.

00:27:10 What that means is that

00:27:13 if you select the medium priority

00:27:16 Mhmm. You create a transaction and then

00:27:19 you select manual you can select manually the Mhmm. The fee. If you put one sat per fee byte that you see now, then you can expect to be in the next

McIntosh:00:27:30 block or two. Right. Most likely the next block these days, but certainly within the next couple. Mhmm. Yeah. Now this seems like a good place to jump in and say, we're talking about mempool dot space.

00:27:44 Any

00:27:46 hardware wallet,

00:27:47 Bitcoin wallet that you're gonna be using is going to have

00:27:51 some type of estimator built into it. It'll say,

00:27:56 you know, use

00:27:57 two sats per v byte or whatever. The reality is

00:28:01 those

00:28:02 are typically not

00:28:04 very accurate.

00:28:05 You should take the time, in my opinion, to go look at mempool.

00:28:10 Space or some

00:28:12 block explorer like that in order to decide.

00:28:17 Well, right now,

00:28:18 according to this, which is a very accurate representation

00:28:22 of what's going on, I could do one sap per v byte and expect my Bitcoin transaction

00:28:28 to go out on the next

00:28:30 couple of of blocks.

00:28:33 Does that make sense? Yeah. Yeah. Personally,

Kenshin:00:28:36 I never trust

00:28:38 built in

00:28:39 estimations of the wallets. I always double check on the mempool dot space. Historically, they're very

McIntosh:00:28:46 they're they're almost always off. I believe they're doing some things to make that better,

00:28:52 but just

00:28:53 it'd be better for you just to go check on mempool Yeah. Dot space or something Yeah.

Kenshin:00:28:59 I think Sparrow Wallet

McIntosh:00:29:01 is quite smart and good, but it might be They have been making improvements on that. I was actually thinking of that when I said that, but I'm not gonna

00:29:10 I use Sparrow Wallet

00:29:11 and love it, but maybe you're not using Sparrow Wallet. I don't know. Yeah. Sure.

00:29:16 I'm sorry for you, but that's okay.

00:29:22 Yeah. So Not a paid promotional, by the way. Although, Craig, if you'd like to support this show no. I'm just kidding.

00:29:31 We should have him on. I wonder if I could get him on. He's a nice guy. He's he's

Kenshin:00:29:36 great. Yeah.

00:29:38 So,

00:29:40 yeah, we're talking about if you put a too low fee.

00:29:44 Mhmm. So if that happens,

00:29:47 there are a couple of mechanisms that we will talk

00:29:50 briefly today.

00:29:52 So one is the

00:29:55 return by fee, and the other one is child pays for parent.

00:29:59 Right.

00:30:00 And wallets

00:30:01 usually nowadays support those two, and they're

00:30:05 on by default, actually, I believe. At least the RBF, return by fee, I think it's

McIntosh:00:30:11 on by default. More common. Yes.

00:30:14 Yeah. I I don't know for sure about the other one.

00:30:19 So that would maybe vary from wallet to wallet.

Kenshin:00:30:23 Yeah.

00:30:25 Let me

00:30:26 think what else before we jump into our b f.

00:30:33 Yeah.

00:30:35 No. I think we talked about the mempool quite

00:30:38 enough.

McIntosh:00:30:40 Yes.

Kenshin:00:30:42 Yeah. So RBF,

00:30:43 what it is

00:30:46 replaced by fee.

00:30:48 So

00:30:50 when you send a normal transaction,

00:30:53 you also add, like, a tag to it or something, a flag that is it tells that this transaction

00:31:00 can be replaceable.

00:31:03 Okay. Which means that if it is stuck

00:31:07 with a very low fee and you never get into a block,

00:31:13 you can send essentially the same transaction

00:31:16 with a higher

00:31:18 fee amount.

00:31:20 Any kind of place replaces the first one. Right. Yeah.

McIntosh:00:31:25 So if I'm trying to send you that 100,000

00:31:28 for example and I put,

00:31:31 I don't know, 0.01

00:31:33 Satoshi

00:31:34 per v byte and that doesn't get through,

00:31:38 then I could bump it up to 1 sat per v byte by basically resending that transaction.

00:31:45 Mhmm. Right? With a higher fee rate.

00:31:50 Yeah.

00:31:51 Okay.

Kenshin:00:31:52 Okay. Yep. I'm a bit on now I'm confused in the two, I think. In

00:31:58 my mind, I mean, the

00:32:00 child pays for parents

00:32:02 and replaced by fee, are quite similar.

McIntosh:00:32:06 Well, the the RBF,

00:32:08 you are sending you're essentially resending the transaction. Same transaction,

00:32:13 higher fee rate is the way I read it, the way I understand it. Yes. Child pays for parent, that is not the case. It is a completely new

00:32:23 transaction.

Kenshin:00:32:25 So Yep.

McIntosh:00:32:27 You have a new transaction. The child

00:32:30 that pays a higher fee that essentially pays the fee

00:32:35 for the for the parent, which is

00:32:38 I don't know how that works. There must be a bit of magic going on there.

00:32:43 But they basically go together.

00:32:46 So the miner looks at both of them. They say, oh, this transaction

00:32:51 is a child

00:32:53 of this transaction.

00:32:55 Mhmm. So b is a a child of a.

00:32:58 But I'm going to take both of them, and I'm gonna look at it as kind of averaging out that fee.

00:33:05 So if the fee on the first one let me make this real simple. Let's make it a a high fee environment. Let's say it's

00:33:1220 sats per per vByte right now, and I sent the parent at 1 sap per vByte,

00:33:20 I may send the child I don't know if it would be 20 or maybe it have to be higher than that.

00:33:30 I'm not certain if they would average it. I we'd probably need to figure that out.

00:33:38 But you're

00:33:39 it it seems like you're actually pay you would pay more for the child. So it'd be, like, 1 and 30 or something. And then the minor goes, oh, I'll take both of those because on average, I'm getting,

00:33:52 well, 15

00:33:54 sats per v byte, I guess, in that case,

00:33:57 all things being equal. Does that make sense?

Kenshin:00:34:00 Yeah.

00:34:02 Where I'm a bit stuck is because I thought a third party could

00:34:08 do RBF for you.

McIntosh:00:34:11 RBF?

00:34:13 Probably.

Kenshin:00:34:14 Yep.

00:34:15 So because

00:34:16 you need to

00:34:19 you replace

00:34:21 the transaction with a different transaction

00:34:24 that's

00:34:25 but spends that input.

00:34:29 So that input is spent

00:34:32 of the original transaction, and you replace that with another input and a higher fee.

McIntosh:00:34:37 Mhmm.

Kenshin:00:34:39 So that that's

00:34:40 that's the RBF.

00:34:44 And then on the child pays per parent, you spend

00:34:47 the output

00:34:53 with a new transaction

00:34:54 that pays a higher fee.

00:34:59 That that that's why I got a bit stuck in this because it sounds similar, but it's one,

00:35:06 you replace the input and the other one, the output.

00:35:09 But in the transaction, it's the same thing.

00:35:14 No. But it it's well, the description is clear.

00:35:18 Child pays for parents

00:35:20 Mhmm.

00:35:21 Is a user spends an output

00:35:24 Right. From from the transaction.

00:35:27 So they spend the output. And then

00:35:30 the other the RBF,

00:35:33 the

00:35:35 transaction

00:35:37 yeah. You replace the transaction with a different transaction that spends at least one of the same inputs.

McIntosh:00:35:46 Yeah. And with a proper wallet setup,

00:35:49 I know this sounds intimidating,

00:35:51 but with a proper wallet setup,

00:35:53 this actually is not that difficult.

Kenshin:00:35:56 No. I mean, you just have it enabled and then you just

00:36:01 you just do it. You just press the the stuck transaction and you say,

00:36:05 yeah, just put a higher fee to it and send it again, basically.

McIntosh:00:36:11 Okay.

00:36:12 So where are some places

00:36:14 that

00:36:16 that

00:36:17 what are some things that could cause some pain here?

Kenshin:00:36:22 Well, some

00:36:24 if your wallet doesn't have

00:36:27 the

00:36:28 fee estimation

00:36:29 of the Satpivi

00:36:31 bytes,

00:36:32 So you might not be aware of of

00:36:35 what fee you're paying for your transaction.

00:36:38 Mhmm.

00:36:39 So you might be thinking,

00:36:41 yeah. I'm just sending a transaction, and then it might be stuck, and you don't even know why because the wallet didn't even inform you. And they did a bad job, but selecting the default

00:36:53 fee.

00:36:56 Yeah. And then wallets that don't tell you if they support RBF,

00:37:01 and they might not have it enabled, basically. So if if it gets stuck, you cannot do anything about it.

00:37:10 And then,

00:37:13 yeah, there there are exchanges

00:37:15 when you withdraw from exchanges.

00:37:19 Yeah. Usually, you don't have a choice. They they do what they want.

McIntosh:00:37:24 By the way, I would mention Spero wallet does support both of these.

00:37:29 Yet another reason to run it.

Kenshin:00:37:31 But anyways. Yeah. Spero is is full featured.

McIntosh:00:37:35 There are also payments different

00:37:37 now but that's a separate subject.

Kenshin:00:37:39 Yeah.

00:37:40 Yeah. I think we said it a few weeks or a couple months ago. Right? Yep. It's been a bit.

00:37:47 Just make sure you have those two enabled at least one of them. Yes. That's

McIntosh:00:37:52 that's it. Yeah. You can do everything. If the other one if child pays for parent scares you, you can basically do everything with RBF.

00:38:00 So make sure that's enabled for sure.

Kenshin:00:38:03 Yeah.

00:38:05 So what happens then with the UTXOs

00:38:08 and Mhmm.

00:38:09 When you have low fees,

00:38:12 a low fee environment?

00:38:16 The everybody says it's a good idea to have a good UTXO hygiene,

00:38:21 and that's actually the perfect time to console consolidate.

00:38:26 It's another expression. Consolidate your UTXOs,

00:38:30 which essentially,

00:38:33 yeah.

McIntosh:00:38:34 Can you explain

00:38:35 why

00:38:37 why do I have different UTXOs?

00:38:39 Why would I end up with a bunch of UTXOs?

Kenshin:00:38:42 Right. Right. Right. Yes.

00:38:44 So

00:38:46 so every transaction,

00:38:48 every time you

00:38:49 send yourself Bitcoin or an exchange or someone else sends you to you Bitcoin Mhmm. What you receive is a UTXO.

00:38:57 Every transaction

00:38:59 ends

00:39:00 up

00:39:01 to you as

00:39:03 one UTXO,

00:39:05 let's say one coin

00:39:07 with x value.

00:39:08 And

00:39:10 then let's say you have received 50 transactions in the past year,

00:39:15 that means you have 50 unique

00:39:17 UTXOs

00:39:18 that have their own values from those So

McIntosh:00:39:22 it's a collection

00:39:24 that in total,

00:39:25 it's kinda like having a bunch of coins. In total,

00:39:28 maybe I've got $20 worth of coins.

00:39:32 Mhmm. But I but what that means is I got a big bundle of coins instead of

00:39:36 one $20 bill.

00:39:38 Yeah. Does that make sense?

00:39:40 Yes. A bunch of little pieces.

00:39:42 But all put together,

00:39:44 it makes 20. But here's the trick. When I send those, I have to pay and it costs more.

00:39:52 Is that correct? Exactly.

Kenshin:00:39:53 Exactly. Because of what we said in the start,

00:39:56 the simplest transaction

00:39:58 is one input, one output.

00:40:01 You send one UTXO from me to you and that's the the smallest v bytes transaction.

00:40:08 If,

00:40:10 on the other hand, for me to send you 20 and I have 20 UTXOs to do that,

00:40:15 then I put 20

00:40:17 UTXOs

00:40:18 as an input

00:40:20 and I send it to you into one output, that means it's

00:40:23 almost

00:40:2420 times

00:40:25 more vivid for this transaction,

00:40:28 which multiplies the amount you need to pay in fees.

McIntosh:00:40:32 Right.

Kenshin:00:40:34 So in in many ways, you you waste a lot in fees

00:40:38 for those tiny utixels.

McIntosh:00:40:41 So

00:40:42 let's say I've been using my wallet for a long time,

00:40:46 this certain address, and I've made a lot of in well, I've well, both incoming and outgoing transactions.

00:40:54 How do I make one clean UTXO?

00:40:57 Do I, like, send it to myself?

00:40:59 Mhmm. Do I, like, consolidate everything up and how does that work?

Kenshin:00:41:05 Yeah. Exactly like that. So you

00:41:07 essentially make it a new transaction.

00:41:10 You select your 20 or 50, whatever UTXOs you have that are small and you need to group together.

00:41:17 So you send all of those

00:41:19 into your to yourself again.

McIntosh:00:41:21 To the same address? Like, I don't have to Ideally, generate

Kenshin:00:41:26 a new you should always send to a new address. Ideally, it should be new, but for Can be the same. Being practiced.

McIntosh:00:41:32 Like,

00:41:33 I'll just make this real concrete.

00:41:36 How about that? So you guys know I mine Bitcoin.

00:41:40 It's a legitimate business.

00:41:42 It's whatever.

00:41:43 So it's not like I'm trying to hide anything from anybody. Well, I don't want you to know what I'm doing, but you know what I mean? It's a legitimate business. So I have a Spero wallet set up. I have a,

00:41:59 an address that I receive Bitcoin to

00:42:03 when when I get my OceanPayout.

00:42:05 Okay?

00:42:06 And then I also send from that address to pay for my hosting because, you know, hosting is not free. It's actually the really expensive part

00:42:16 of the mining.

00:42:18 So I know I've got a bunch of UTXOs

00:42:22 built up from the last, what, two years or so that I've been using this wallet.

00:42:28 So while fees are really cheap right now, it'd probably be a good idea to consolidate those, but I can't just

00:42:36 make a new address and send everything to it because I've got to pay that I've received to this address

00:42:44 and I've got to pay I guess I could

00:42:47 I I think I just answered my own question. I guess I could send to a brand new address

00:42:52 Mhmm. That consolidates everything.

00:42:55 I continue to receive to the same address. I don't wanna have to go into Ocean and change my address. Okay?

00:43:02 No. Right? That is fine. But now I've got my

00:43:05 the one that I have to pay will now be over here

00:43:09 Mhmm.

00:43:10 Until I build up what I receive, you know, what I've received. Because the reality is it's it's there's very little margin in this business.

00:43:19 If I ship what I've made so far

00:43:22 profit in the last two years to a new address, I'm going to have to send off of that to start with at least.

00:43:29 Yeah. I

00:43:31 guess I could leave some.

00:43:33 Sure. That probably makes the most sense

00:43:36 actually. Yeah.

00:43:38 Just And as as many what I think I need to get this

00:43:42 and

00:43:44 the other is like it already is cold storage but it's super cold storage. Right? Like that's

00:43:50 the address. That's the

00:43:52 it's the treasury of the company.

00:43:55 Look at that. Wow.

00:43:56 Fancy. Right? But when it when it gets sent there now it's it's all one gigantic UTXO.

00:44:03 I hope that made sense and I hope that helps you. And kinda how you not you, I know you know this but in how you think about this stuff. Stuff.

00:44:12 Right?

00:44:14 Yeah. But but you are saying I literally could just send

00:44:18 let's say I had a tenth of a Bitcoin that's

00:44:22 a 100 transactions.

00:44:24 It doesn't matter. A 100 UTXOs.

00:44:27 I could send

00:44:28 that Bitcoin back to myself

00:44:32 Yeah. Pay the fee that it's gonna come up with, and I'm gonna end up with a single UTXO.

00:44:39 Mhmm. Whereas before it was a 100.

00:44:43 Correct.

Kenshin:00:44:44 K. Correct.

00:44:46 Yeah. And and

00:44:48 that is also the case when you do a lot of transactions yourself,

00:44:53 you also get to change back.

00:44:55 Yes. So if I need to pay you

00:44:5950 Bitcoin or whatever, 50

McIntosh:00:45:04 is the example now? 50,000. Sorry. I just 50 woke

00:45:08 Bitcoin? Wait. Yes.

00:45:10 You need to pay me that right now.

00:45:13 Let me give you an address. I'll send it in our chat.

Kenshin:00:45:18 By the way,

McIntosh:00:45:20 I don't have it and I've never had I didn't know you were an OG, man.

00:45:24 No.

00:45:25 You you don't even say bitcoins.

00:45:28 At you being all adaptive.

00:45:31 You know all the OG, they're like bitcoins.

00:45:33 They always say a lot of them. Bitcoins because

00:45:37 when you get 50 Bitcoins in a block, it's just normal to say Bitcoins, not Bitcoin.

00:45:44 What?

Kenshin:00:45:46 Yeah.

00:45:47 Okay. So so if if I would if we would agree that I need to send you 20,000 sets.

00:45:54 Yes. The smallest

00:45:56 UTXO I have, let's say,

00:45:58 or the most close UTXO I have is, let's say, 30,000 sets.

00:46:02 Right. Then I send you this 30,000 and I get back automatically 10,000.

McIntosh:00:46:08 Right.

Kenshin:00:46:09 So in this way also if you do a lot of transactions,

00:46:12 you might end up with a lot of small UTXOs due

00:46:16 to the changes, the change back. So you get changes

McIntosh:00:46:19 that way, you also get change, you know, you get a UTXO whenever somebody sends you something. You're just continually building these things up and it's something you have to account for.

Kenshin:00:46:31 Yeah.

00:46:32 Right? Yeah. And yeah. And those

00:46:34 those very small UTXOs are called dust,

00:46:39 and it can cost, for example, more to to to spend them than they than they are worth at certain

00:46:46 fee rates.

McIntosh:00:46:47 Right. So if if it's climb,

Kenshin:00:46:50 then then you end up in a problem. Mhmm. Yeah. You might have a UTXO that's a thousand sats.

00:46:56 And Right. To send a transaction might cost a thousand 500 sats. So they're basically useless.

00:47:01 And you need to combine it with other sets,

00:47:05 which also increases your fees at the same time per transaction. So it's very bad.

00:47:12 So it's good to consolidate

McIntosh:00:47:14 and group them together. Yeah. Exactly. Yeah. You wanna do that when the fees are low. So we've already seen in Bitcoin's history,

00:47:23 fees went up to a stupid amount. It was do you actually know what it got up to in terms of stats? It was like 200? No.

00:47:31 More. It was four I saw four or 500 during the inscription times. It was a lot. Four or 500 SATs per V byte whatever. It was ridiculous.

00:47:40 That is not when you need to be consolidating your UTXOs.

00:47:44 Now the good news is

00:47:49 they came back down.

00:47:51 Maybe they go back up next month. We have no idea.

00:47:55 I do believe over the long term we will slowly see fees on average go up.

00:48:01 As the network expands,

00:48:03 as more people compete for the block space on the main net,

00:48:08 the fees will go up.

00:48:10 That's the thing I'm operating under. But now when we're at one sat per v b byte or less all the time,

00:48:18 it's a great time to be doing this, which is why we're putting this episode out right now, actually.

00:48:24 Yeah. One of the reasons.

Kenshin:00:48:26 I think we need a follow-up episode to discuss a little bit about taxation

00:48:32 and things like that because, personally, I'm a bit hesitant to consolidate some some UTXOs

00:48:39 in case

00:48:41 I want to return that same UTXO to the bank, and I need to pay tax on it.

00:48:46 So consolidating

00:48:47 those UTXOs

00:48:49 might make it harder to pay

00:48:52 to figure out what you paid for those

00:48:55 and

McIntosh:00:48:56 pay tax on them, basically, be legit. I'm not, yeah, I don't know how that would work. No idea.

Kenshin:00:49:02 Sorry. Yeah. But you understand the no.

McIntosh:00:49:06 I'm just kidding. I

00:49:08 did not say that IRS.

00:49:09 I it was a joke. Okay?

00:49:11 People aren't thinking about it. Anyways.

00:49:14 Alright. Yeah. We we

00:49:16 Yep.

00:49:17 Alright.

00:49:19 Cool. What

00:49:21 about Let's

00:49:22 talk about lightning

00:49:24 for just a minute.

00:49:26 I wanna grab this one if that's okay.

00:49:29 Little practical experience here. When you do Lightning, you're opening channels, closing channels, just like what happened to me.

00:49:37 And when they forced closed that channel a few weeks ago on our node,

00:49:42 what that means is I had to pay the fees that were

00:49:46 at the time

00:49:48 like,

00:49:49 I don't know what he locked it in that. I didn't actually look it up. Most likely, was very low given the current state of things.

00:49:57 But if we would have been in a high fee environment,

00:50:00 let's say back during the inscription craze craze and

00:50:04 I had to pay for a forced close,

00:50:06 it could have been very expensive.

00:50:09 Does does that make sense? So Yes. If you're managing a lightning node, this is something you need to think about as well.

00:50:16 To some extent, you have no control. I mean,

00:50:19 a forced close or closing a channel,

00:50:23 they may decide to go do something else. Who knows? There's no telling. But,

00:50:28 ideally,

00:50:29 you would close and open

00:50:31 channels

00:50:32 when things

00:50:34 are cheap

00:50:35 on chain.

Kenshin:00:50:38 Yeah.

00:50:39 Exactly.

00:50:39 That that's that's the best time to do it, and I have done that myself also. Yeah. It's they can be quite costly, those,

McIntosh:00:50:48 lightning opening and closing chains. They can, and you gotta be careful about that. So splicing is a new way of managing channels,

00:50:56 and these notes are incorrect.

00:50:58 So,

00:51:00 it's a new way of managing channels, and it doesn't do a full open and close

00:51:05 when you splice channels.

00:51:08 It and so that does help with the fees. It's more efficient, but it doesn't completely

00:51:13 alleviate

00:51:15 the the whole problem.

00:51:18 I believe this what these type things, the very things that we're talking about right here are one of the primary drivers behind why

00:51:25 lightning is never gonna be something that everyone just does

00:51:30 unless

00:51:31 they come up with a new way of managing this stuff that I'm not I I don't have the foggiest idea how they would do that

00:51:39 because we're kinda locked into the paradigm that we are at this point.

Kenshin:00:51:45 Yeah. But everybody seems to be going more and more to custodial

00:51:49 lightning solutions.

McIntosh:00:51:50 Which is not ideal, but yes, that's that's what it's driving us to exactly.

00:51:56 These main,

00:51:57 like,

00:51:58 giant players who, you know, they maybe have multiple Bitcoin worth of channels,

00:52:04 liquidity,

00:52:06 which I, you know, I can't afford that, but that doesn't mean I can't have channels.

00:52:12 But they

00:52:13 it's a professional operation and they have someone who's not only monitoring and maintaining that server,

00:52:19 they're determining the best ways to manage that liquidity

00:52:22 and they're making money off of doing it.

00:52:25 And that's that's a very difficult thing for a pleb

00:52:29 like like like us to get involved in. Now,

00:52:33 we have ours set up and we have reasonable

00:52:36 skill set between us. We can manage it And we use it because we want it for our podcast.

00:52:44 But

00:52:45 I just don't see every household having a lightning node. I just don't think that actually

00:52:51 makes sense for most people, to be honest. And there are Maxis out there who would say, well, that's just not right and blah blah blah. I that's just being pragmatic and practical in my opinion.

Kenshin:00:53:03 It can it can be a bit stressful also to manage

McIntosh:00:53:07 lightly. It can. Like, when you have a $100 locked up and I'm glad it wasn't more if it would have been the big channel,

00:53:15 I'd I'd I would have been more stressed out. As it was, I really wasn't I was worried about it, but, I mean,

00:53:22 it's not the end of the world. But I was thinking to myself the entire time, it's a 100,000 sets, man.

00:53:29 Twenty, thirty years from now, that's gonna be a fortune, you need to get that money back. Yeah.

Kenshin:00:53:35 I personally

00:53:37 have spent more

00:53:38 than 100,000

00:53:39 such in opening and closing channels, I think.

McIntosh:00:53:43 So I actually have not. I've I've only had one case that I know of where I've lost

00:53:48 funds.

00:53:50 And I've not opened that many channels, so I I don't you know?

00:53:55 When you when you open a channel and then you close it, you're only paying the fees.

00:54:01 You you recover the liquidity. It's not gone.

Kenshin:00:54:04 Yeah. Yeah. Yeah. No. No. It's not gone. No. In fees. I meant in fees. In fees. Yeah. I just haven't opened that many channels.

00:54:11 Okay. It was experimented.

00:54:13 It's not it

00:54:15 was not necessary.

McIntosh:00:54:17 What can the plebs do this week?

Kenshin:00:54:20 Oh, that that's very interesting.

00:54:24 Look at your wallet.

00:54:25 Mhmm. Find the settings,

00:54:28 the advanced settings usually, and look for RBF.

00:54:31 It should be there.

McIntosh:00:54:32 And ladies and gentlemen, if your wallet starts with an l and ends with edger or t and ends with

Unknown:00:54:40 reser Reser. Reser.

McIntosh:00:54:43 Get a new wallet.

00:54:44 That's McIntosh's

00:54:46 advice.

00:54:47 I don't care if they support RBF or whatever.

00:54:50 Those two wallets are garbage.

00:54:52 Hot garbage.

00:54:54 Move on. Sorry. Right. Yes.

00:54:56 Make sure you've got RBF at least.

00:54:59 Make sure it's turned on.

00:55:02 Right?

00:55:03 Because if it's not turned on and you make a transaction without it,

00:55:07 you're stuck. You cannot do it without points. Yeah. Potentially. I mean. Make

00:55:14 sure that your wallet is showing fee rates and stats per v byte.

00:55:18 Don't trust

00:55:20 fast,

00:55:21 medium, slow, whatever.

00:55:23 You don't know what that means and there are times when that could mean you're spending a lot of money.

Kenshin:00:55:30 Yeah. And at the same time, familiarize yourself with the mempool.space

00:55:34 or similar Yes. Block Explorer. And then compare

00:55:38 if your wallet has a free rate,

00:55:41 compare the suggested fee rate

00:55:44 with the mempool.space.

00:55:47 Mempool.space

00:55:48 will be more accurate. It will be more accurate. That that should be your guide.

McIntosh:00:55:54 Yeah. If your wallet supports it, which I don't even know if Sparrow does support SubOne set sends.

00:56:00 But these days,

00:56:01 honestly, look, I I've already explained

00:56:04 my whole thing. I just don't think that but that doesn't mean you can't do a subset

00:56:11 send if you want. Right? Do it for point five or whatever.

00:56:15 Whatever works

00:56:17 because you're saving money. I don't blame you for that.

Kenshin:00:56:20 Yeah. Exactly. And there are decimals.

00:56:23 I always put random numbers like 1.68

00:56:28 or whatever,

00:56:29 you know, 2.6

McIntosh:00:56:31 edge out those 1.6

00:56:33 guys.

Kenshin:00:56:34 Yeah. Exactly.

McIntosh:00:56:36 That's funny. Actually,

Kenshin:00:56:37 good tip for you that it took me a while to see it on the block

00:56:42 on the mempool. Space.

00:56:44 Okay. On the block, on the top row that you have all the blocks going through.

00:56:50 Yes. The first number you see is the SATS per V byte. But for me, what I start looking more nowadays is the second row.

00:56:58 It shows you the variation

00:57:01 of fee rates. So the last block it says

00:57:04 the lowest fee rate was 0.19

00:57:08 such per view byte and the highest was 300 SAT byte. So that's what I'm looking at.

00:57:14 I look at the next block, it says the minimum

00:57:16 is 1

00:57:18 SAT per V byte and maximum is $4.60.

00:57:21 So I know that if I put 1.5,

00:57:24 I will be there.

00:57:25 Right. The suggested SAT per per V byte right now is 2, but I know if I put 1.5,

00:57:32 still

00:57:33 will be there. So for me, that's even more accurate and

00:57:36 a good tip for people if they haven't noticed that.

00:57:42 Cool.

00:57:43 Yeah. And then you can do some small tests if you if you want to familiarize yourself. Yes.

00:57:50 So that's also good.

McIntosh:00:57:52 Otherwise Yeah. You should you should be doing tests while everything's low. You should, you know, you if you have been actively using a Bitcoin wallet for a while

00:58:03 and you have a lot of UTXOs,

00:58:06 you should be able to tell in the wallet, like, if you poke around,

00:58:10 like, you can see your

00:58:14 UTXOs,

00:58:15 right?

00:58:16 Mhmm. You should have some idea of what you've got in there.

00:58:20 Maybe it's time to consolidate those like we were talking about. I'm probably I'm just gonna go ahead, look, I've got some homework for the week. Maybe the next two weeks. Give me a couple weeks. I'm gonna go

00:58:31 and

00:58:32 I'm gonna consolidate my UTXOs for my mining business. I'll let you know how it goes.

Kenshin:00:58:37 Yeah. Okay? Don't don't forget RBF.

00:58:41 Yeah. So that consolidated

00:58:43 transaction doesn't get stuck.

McIntosh:00:58:45 Yeah.

00:58:47 That would be terrible. Alright. Hey. I gotta read this closing line. In case y'all don't know, I think everybody I mean, we do use

00:58:55 chat GPT or whatever to

00:58:58 craft our show notes and whatever.

00:59:00 It's funny sometimes the stuff it comes up with. I have to read this closing line. This is awesome. Pleb rule,

00:59:07 treat your UTXOs

00:59:08 like ammo. Organize it when it's quiet, not when you're in a firefight.

00:59:13 Pretty sure chat GBT came from the South, but that's okay.

00:59:17 I

00:59:18 thought that was funny.

00:59:21 So we do have some questions of the week. We got two, I guess, actually. Right?

Kenshin:00:59:26 Alright.

00:59:27 So do you have a UTXO plan?

00:59:31 Mhmm. And

00:59:33 have you ever meaning the first question. Do you have a UTXO plan?

00:59:37 Do you consolidate?

00:59:38 Do you look when to consolidate?

00:59:41 Do you know what UTXO is?

00:59:44 Yeah. Sorry.

McIntosh:00:59:46 Yeah. And then the second part of this?

Kenshin:00:59:49 Yes. Have you ever used RBF or CPFP successfully?

00:59:53 I

00:59:55 have only used once personally RBF.

McIntosh:01:00:00 Is that how you got out of that jam?

01:00:03 Did I already ask you that?

Kenshin:01:00:04 No. I don't remember. I think it was just to open the light right. You said you didn't remember.

01:00:09 Yeah. I think that's where I spent

01:00:12 a bit more for Lightning

01:00:14 opening the channel.

01:00:16 Yeah. It was a bit stuck.

McIntosh:01:00:18 Hey. You can get

01:00:20 back to us with your answers for these questions by boosting.

01:00:24 If you got a podcasting two point o app,

01:00:27 like Fountain, for example,

01:00:30 and you can do that by Noster.

01:00:34 Either way, we would love it if you would boost us in park acid two point zero. Boost us on Noster.

01:00:41 Let us know

01:00:43 what you think. I guess we need to make a post saying, do you have

01:00:49 putting that out there so people know where to go. If you follow us where it's

01:00:55 if you search for Satoshi's plebs

01:00:57 on Nostra, you'll find us. I don't know what our pub key is obviously but

Kenshin:01:01:02 No. It's a random stream of characters.

McIntosh:01:01:05 Not random streams of characters. No. Alright. So

01:01:09 that's gonna be it. We've got news and notes for this week though.

01:01:14 I don't know if you know this but Bitcoin's down, Kenshin.

Kenshin:01:01:18 Oh, no. I

01:01:20 I noticed.

McIntosh:01:01:22 That I knew. Can I just tell you I well, no? I went and looked again on Sunday.

01:01:28 I was like,

01:01:29 did my my my automatic buy. I woke up Sunday, I looked at it and went, yes.

01:01:35 More Bitcoin.

Kenshin:01:01:37 Yeah.

McIntosh:01:01:39 The way you gotta think about it, ladies and gentlemen. Keep the long range view.

01:01:43 But we do have some,

01:01:45 we do have some articles here to talk about real quick.

Kenshin:01:01:50 Either more

01:01:51 connect to the price.

McIntosh:01:01:55 World Who is this Bernstein dude? Because man,

01:01:59 he's on some hopium,

01:02:00 I'm afraid.

01:02:03 I'm just saying. I'm gonna call that. Maybe he's right?

01:02:08 Bitcoin Magazine in my opinion tends to be a little optimistic.

01:02:12 I'll just say that. So that's where this came from. And he's saying

01:02:16150 k by 2026.

01:02:20 If

01:02:22 he did that if that happens,

01:02:24 would that

01:02:25 obviate

01:02:26 would that

01:02:27 would does that mean the four year cycle will be over? I mean, now, we're still in the four year cycle pattern.

01:02:35 Does that mean then that the next cycle would just be much much higher? Because, I mean, we we had an all time high. I even know how many days ago it was.

01:02:45 It wasn't that long ago.

01:02:48 And what he's saying is in nine months that we're gonna be

01:02:53 higher than that by a significant amount.

Kenshin:01:02:56 It it would be unusual but we we will hit the bottom of this cycle in October. In October is what you're saying according to that pattern, which so far has held true, by the way. Yeah. For the last

01:03:09 ten plus years. Yeah.

01:03:10 So if that holds

01:03:12 yeah. And then could we, from that point,

01:03:15 go to a 150?

01:03:17 I don't know. And I don't know. I I I think we already reached the lowest point of this cycle. I mean,

01:03:23 theoretically

01:03:24 speaking

McIntosh:01:03:26 you're not a 58 k person.

Kenshin:01:03:30 We hit what did we hit now? 60 It it was 64,

McIntosh:01:03:35 I think. Yeah. 63 and some change, I think, really.

01:03:39 But, yeah, 64.

01:03:41 It was 60 I mean, that's significantly

01:03:43 above

01:03:4658 k.

01:03:47 I don't know. We'll just look, at this point, I'm just gonna monitor it and respond to it. If it goes low,

01:03:55 buy more Bitcoin.

01:03:57 If it goes high,

01:03:59 buy more Bitcoin and say yay.

01:04:01 I mean, I don't

01:04:04 I

01:04:05 think

01:04:07 I did hear something this week that was interesting I wanted to bring up.

01:04:11 They said,

01:04:15 basically,

01:04:15 we haven't

01:04:17 determined at this point why

01:04:20 there's a reason why the market went from

01:04:23 a 126

01:04:24 k on October

01:04:27 down to where we're at right now so rapidly.

01:04:31 This wasn't Plebs selling off, this wasn't the HODLers selling off,

01:04:36 this wasn't the businesses like the treasury companies selling off.

01:04:41 Something else happened

01:04:44 and at this point that remains unknown.

01:04:49 So was it an FTX style event? No, probably not but something very major

Kenshin:01:04:57 happened. Oh,

01:04:58 I heard about Binance.

01:05:00 Yeah. I heard maybe Binance

McIntosh:01:05:02 a one theory.

Kenshin:01:05:03 Yes. Yeah. Binance comes up all the time in those dates. Exactly. Thank you. Yeah.

McIntosh:01:05:10 Until it's proven,

01:05:12 it's just all speculation,

01:05:14 but I do believe that the sentiment may be correct.

01:05:18 You think about how quickly it dropped, it was crazy.

01:05:22 It's just like it's just like all of a sudden a bunch got dumped on the market. Imagine that.

01:05:29 I don't know.

Kenshin:01:05:30 Okay. By by the way, the lowest we had last week was $60,001.

McIntosh:01:05:37 Oh, sorry. I was wrong. Well, if I were a 58 ker, I just claim credit and go home.

01:05:44 I I mean, that is so ridiculously

01:05:46 close. I forgot. I did not realize

01:05:49 it didn't it got that low. Was just reading this right here. Sorry. Yeah. It's true. That's

01:05:57 nuts.

01:05:58 I would actually say that's basically 58 ks. It's not. It's technically not but

Kenshin:01:06:07 Yeah. I don't know.

McIntosh:01:06:08 I I don't know. So we got people saying

01:06:11 everything's

01:06:13 hunky dory and we're going to the moon?

01:06:16 Not yet. I tell you it doesn't feel like it. I'll just say that.

01:06:20 But these things can change. We are at the lowest

01:06:24 fear and greed index, which is a measure of

01:06:27 sentiment in the market that I've ever seen. I don't know if it's been lower, but I saw it at eleven the other day. This is actually something we might wanna add to our statistics

01:06:37 for the section.

Kenshin:01:06:39 I can price right there.

McIntosh:01:06:42 It's so it's up a little bit

01:06:44 but that is extremely low. Yeah. Like, we're talking super like, that's in the ditch. Like, you're drunk on the way home and you fell in the ditch and you can't get up.

01:06:54 Okay?

01:06:55 So we need to sober up

01:06:58 and get

01:06:59 out of the ditch.

01:07:01 But until

01:07:02 that starts happening, I'm just gonna keep buying Bitcoin because I got nothing else to do.

01:07:08 Another thing,

01:07:12 what is this about Bitcoin Core? I I actually had something else about that I wanted to mention briefly.

01:07:18 I don't know. But Bitcoin Core the new release?

Kenshin:01:07:22 They're just planning for the release 31.

01:07:25 It's not not no big specifics yet, but it's scheduled for April 10 now. So

McIntosh:01:07:32 I did wanna mention along with this, one of the core maintainers stepped down. There's only like four I think there's four now. I think there was five of them. Gloria.

01:07:42 Mhmm. This is a person I've discussed in the past and I'm not making fun of her, I'm just stating facts.

01:07:49 She's not been on there very long, only a few years.

01:07:53 I do believe,

01:07:54 and this is my opinion, and it's it's just my opinion, you can take it for whatever you want.

01:08:00 She's not a good fit for the Bitcoin Core team, and I will tell you why. It's not because her technical ability. I don't even know what that is.

01:08:09 It's because she thinks that Bitcoin should be treated as whatever,

01:08:14 the Bitcoin network. I I have pulled segments.

01:08:18 She was on Peter McCormack's show, for example,

01:08:21 and for thirty seconds, she sat there and talked about how Bitcoin was for for basically anything.

01:08:28 It was not just for money and it doesn't matter.

01:08:31 And

01:08:33 frankly,

01:08:34 that's 100%

01:08:36 the

01:08:38 opposite

01:08:40 of my view of Bitcoin. And I'm not sorry to see her go. I I don't know who's gonna come along. I know she left because

01:08:49 her feelings were hurt or whatever.

01:08:52 I don't

01:08:54 this is too important to me.

01:08:56 As I've said over and over, I believe Bitcoin will one day be the global

01:09:01 network,

01:09:03 monetary network.

01:09:04 And I think that's a good thing for the world. That's it. Dead stop.

01:09:09 I also believe that it helps

01:09:12 people

01:09:14 who are less advantaged than I am

01:09:17 get out of their situations.

01:09:19 Those two things to me are far more important than having fun and playing around with the blockchain.

01:09:25 So I'm sorry.

01:09:27 I'm not gonna cry tears over it. I'll just be honest.

Kenshin:01:09:31 Yeah. And she was not the only one to have those

McIntosh:01:09:34 No. She's not. In fact, I would argue probably more than half of the core contributors

01:09:40 Yeah. Before

01:09:42 she left are like that. We will see what happens. I hope there's a shift in the narrative. I do not know. There's still a lot of fighting going on.

01:09:52 Okay.

01:09:55 There we go. Bitcoin price

01:09:58 as we record,

01:09:59 at least as we started,

01:10:01$68,907

01:10:04 US. What do we got in euros, sir?

Kenshin:01:10:07€57,800.

McIntosh:01:10:09 How are you feeling about that?

Kenshin:01:10:14 I didn't think we would see 50 k

01:10:17 range in euros

01:10:19 again.

01:10:20 So I was a bit

01:10:22 surprised,

01:10:24 but I like you said, I see my DCA,

01:10:27 my daily DCA, and

01:10:30 it looks higher than ever or higher than I think I have said this.

McIntosh:01:10:34 I don't think I didn't think we would go below 70. I thought 70 was the floor.

01:10:39 Obviously,

01:10:40 that's not true, but that's okay. Bitcoin's gonna do what Bitcoin's gonna do. And if somebody's dumping on the market, then we'll get through it just like we got through FTX or all these other things. Bitcoin market cap,

01:10:54 right now is 1,400,000,000,000.0.

01:10:56 Gold market cap, 35,000,000,000,000.

01:10:59 That means we're at 4.61

01:11:01 percent Bitcoin to gold market cap, and I think this is what

01:11:05 Syndicate Mike wants.

01:11:06 Bitcoin priced in gold,

01:11:0916.4

01:11:10 ounces of gold per Bitcoin. Is that what he was looking for?

Kenshin:01:11:14 Yeah.

01:11:15 Great. We had reached at some point 30

01:11:18 something. I think it's close to 40, the all time high.

01:11:22 How many ounces you could buy in Dirty 1

McIntosh:01:11:25 fiat dollars you got in your pocket, you can trade those in for beautiful

01:11:31 pristine

01:11:32 Satoshis,

01:11:331,451

01:11:35 of them per dollar.

01:11:37 That is a bargain.

Kenshin:01:11:39 Yeah. We were below a thousand.

McIntosh:01:11:43 Don't think about that. All time high, a $126,080.

01:11:48 That was reached on October 6,

01:11:51 a hundred and twenty seven days ago.

Kenshin:01:11:54 Oh, I want that in weeks.

McIntosh:01:11:57 What? Dude.

01:12:00 Sorry. I'm just kidding. No. I'm just kidding. It is it is

Kenshin:01:12:04 for

01:12:05 no. 127,

01:12:07 you said. Yeah. Okay. We need to find thirteen weeks because I know it's fifty two weeks of the bear market.

McIntosh:01:12:13 So that's easier to Okay. Then that's a good reason to do that. I will reprogram that.

01:12:19 That was pulled by my script, which I did with

01:12:22 by the way, I didn't even talk about that. Yeah.

01:12:26 Is our beta

01:12:28 and it did pretty good.

01:12:30 Let's skip the assets.

01:12:32 We'll run along. One sat per v byte, 29,000 unprocessed

01:12:36 transactions.

01:12:37195

01:12:38 megabytes in the transaction pool, though. And I will say this, I we did not have a yeah. That was February 19.

01:12:48 Crap. When was the last one?

01:12:50 Did we have the down

Kenshin:01:12:52 downward difficulty last week? We did. We did. We did on

McIntosh:01:12:57 yeah. We did. But it was after we recorded. Right?

01:13:0111.16%

01:13:03 down.

Kenshin:01:13:04 Yeah. Yeah. 11.16

McIntosh:01:13:06 down. We ended up going down 11.16.

01:13:08 I don't think that's a big surprise.

01:13:11 Unfortunately,

01:13:11 we're lined up for a 10.79%

01:13:14 upswing.

01:13:15 Nine days out, mind you, so maybe that will keep going down. It actually was originally, like, 13%

01:13:21 or something. But

01:13:23 that is the

01:13:25 biggest drop since the China mining ban back in 2021.

01:13:29 It's official.

01:13:30 So we have not seen that low a dip

01:13:35 in,

01:13:36 how many years? Twenty twenty one. So four years now.

01:13:39 Five years.

01:13:41 I thought that was pretty cool.

Kenshin:01:13:43 Wow. Yeah. Alright.

McIntosh:01:13:4654.31%

01:13:49 to the next cycle,

01:13:50 halving.

01:13:51 Alright. 04/12/2028,

01:13:54 two years, sixty two days away.

01:13:57 Yep. Are you ready?

Kenshin:01:14:00 Yeah. It feels very far away, but yeah.

McIntosh:01:14:03 It'll get here before you know it. It will. Mhmm.

01:14:07 Ladies and gentlemen,

01:14:09 Satoshi's Plebs is a value for value podcast supporting podcasting two point o.

01:14:14 We strive to bring you honest Bitcoin content every week. We ask, are you getting value from this show? Support it through time, talent, or treasure. Help with future projects, stream sats,

01:14:24 boost messages, even a 100 sats saying great show or you suck. We'll read it either way.

01:14:30 Oh my goodness.

01:14:32 I'm so glad I thought of this.

01:14:35 This is beta show notes, by the way. We're building a system to have it. We left off SenditMike's

01:14:41 boost.

01:14:43 Oh. We need to do a full stop right here. I apologize, SenditMike.

01:14:49 Whoever brings it up first, say it.

Kenshin:01:14:53 So SenditMike

01:14:54 send

01:14:55 us 1,069

01:14:56 SATs, he said, I do use multisig,

01:14:59 but it's through BitKey, which isn't truly self self custodial.

01:15:03 I enjoy the talk about AI stuff. Maybe someday I'll get myself motivated to do something with it.

01:15:10 And we had zero AI talk today.

McIntosh:01:15:14 Well,

01:15:16 AI screwed up my show notes.

01:15:20 No. AI helped me troubleshoot that. I could not I'm I'm serious. It would've taken me a week and instead it was a couple hours.

01:15:27 I mean, that's just a great example right there. Anyways, do appreciate that. Send it, Mike. Of course. Glad to hear from you. And I would encourage you on your AI journey, sir. It's something that we all need to learn about even if it's just here's the chat GPT interface. What can I do with it? I mean, we're doing some having it code and do all kinds of crazy stuff,

01:15:49 but not everybody wants to be a coder nor would I recommend that actually.

01:15:54 Check out the apps@podcastapps.com

01:15:57 and support Independent Bitcoin Media. If you like the content, I would love it if you write a review on Apple and tell your friends about the podcast. That is one of the best ways for us to grow. This week's music, by the way, is an awesome jam by Abel James,

01:16:15 called Voodoo Queen. I would call it

01:16:19 it's a New Orleans style music. I'll say that. I am

01:16:23 from the general area of New Orleans. It's I love

01:16:27 New Orleans jazz music, and it's kind of a funk,

01:16:32 blues,

01:16:33 not really jazz,

01:16:35 but, man, it just sounds like New Orleans.

01:16:38 I think he's a little further west. I think he's over in Austin,

01:16:42 but, man, it's some I really liked it. Really good stuff.

01:16:47 And I put one of his tracks on there for this week. Any boost or streaming of sets during that song will go straight to the artist.

Kenshin:01:16:55 So thanks for joining us this week. You'll hear from us again next Thursday morning.

01:17:00 We hope this has been helpful, and we would love to hear from you on Nostr or on Fountain.

01:17:05 You can also find all our contact info at satoshidustplayoffs.com.

01:17:09 Stay humble, DCA those sites, and have a great weekend.

McIntosh:01:17:12 We'll talk to you all soon.

Kenshin:01:17:14 Bye bye.

Unknown:01:18:04 e

01:18:07.

01:18:10.

01:18:14,

01:18:16 but

01:18:18.

01:18:24,

01:18:26,

01:18:30.

01:18:34.

01:18:37.

01:18:41.

01:18:47 escape

01:18:50.

01:18:53,

01:18:57,

01:19:00.

01:19:27.

01:19:31.

01:19:34.

01:19:38,

01:19:41 g

01:20:00 Now

01:20:15.

01:20:18.

01:20:20 I do
