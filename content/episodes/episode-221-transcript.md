---
title: "Episode 221 Transcript"
draft: false
_build:
  list: never
  render: always
---

[00:00:00] McIntosh:

Welcome back to Satoshi's Plebs for episode 221, not two zero one like I have in my notes. It's gonna be one of those days, Kenshin. I'm McIntosh. 

[00:00:12] Kenshin:

And I am Kenshin. And today, we're diving into Joinster, a decentralized coin join implementation using Nostr that's tackling Bitcoin's privacy in a completely new way. 

[00:00:25] McIntosh:

After ZSnacks and Samurais got shut down this year, a lot of Bitcoiners have been asking what's next for privacy. Joinster might be an answer. 

[00:00:35] Kenshin:

Yes. So we will start with CoinJoin fundamentals, then go into the technical details. 

[00:00:41] McIntosh:

Whether you're looking for privacy options or just want to understand where Bitcoin privacy tech is heading, let's jump on in. 

Alright. First of all, we don't have a live audience. We've got some some challenges. Kenshin got a new new to his setup, I guess. Yeah. Laptop or server, whatever it is that he's got running over there. I don't actually know. But it's new, and we don't have OBS on it. So, frankly, I've been lazy and haven't set up, OBS, and there you go. Sorry. We'll try and get it up next week. But 

[00:01:20] Kenshin:

Yep. It's, yeah. You know,  in summer vacations, you do all those changes here and there, and you try new stuff. So that's what happened. I decommissioned my big desktop, that was making a lot of noise with a small, compact 

[00:01:36] McIntosh:

What? No more bumps? 



[00:01:38] Kenshin:

Nope. No big cheap in use. So, yeah, it's nice and quiet. 

[00:01:43] McIntosh:

Alright. We've got a block height as we start recording of nine zero eight eight ninety six. So 908,896 blocks. What's going on with you, Kenshin? 

[00:01:58] Kenshin:

Yeah. I mean, summer vacations are almost over, which means I need proper vacations now. 

[00:02:07] McIntosh:

You I need a vacation from my vacation. 

[00:02:11] Kenshin:

Yeah. I mean, it's it's been crazy busy, this past couple of weeks and especially this week is full steam ahead to finish my project with my wife, get it up and running on yeah, when this podcast gets out, I guess, on Friday some sometime. And then from next week, I'm back to the Fiat world, back to the Fiat job, which I'm not looking forward to. So a bit stressed this week. 



[00:02:42] McIntosh:

Well, I I'm sorry you have to go back to work. I am. I know that you would rather do other things, but Soon. This is what we have to do. Alright. So for me, I did get a lot of work done on our HUGO static website, and I actually have something that I can show you. Now this is not the official satoshisblebs.com website yet, but it will be. I'm gonna go ahead and let you know what it is. If you go to https, colon//macintosh, mcint0sh,1775.github, github,.io. There it is. Now if you poke around, you will find some rough edges for certain, but I think it will give you a general idea of where we're going. And what I would actually recommend that you do is kinda compare it to satoshis-plebs.com and take a look at the speed because it is just mind boggling to me how fast the new site is compared to the old site. Yeah. 



[00:03:55] Kenshin:

It looks really good. 

[00:03:57] McIntosh:

So we've still got some work there to do. I believe, we're gonna do a little business on the air here. But, Kinshin, you should have access now to the repo. I don't know if you've had time to get in there. 

[00:04:10] Kenshin:

Yeah. I got the invites. 

[00:04:11] McIntosh:

Have it not typed? I expect a pull request every day. 

[00:04:15] Kenshin:

No. 

[00:04:16] McIntosh:

Yes. Our merge request every day so that, you know, we get this up to date. No. I'm just kidding. But yeah. And that's actually something, frankly, a listener could help with. If you want, I could give you permissions on that site, and you could, you know, update things. So let me know if that's something that might be of interest to you. 

Second thing I've got, I did wanna take a minute. I have been meaning to talk about this for a few weeks. My miners, I am sort of still in the process of transition, And I've frankly decided to kinda unload some things on the unsuspecting audience. And if you will forgive me in advance, I'm gonna try and not say anything that will get me in trouble legally. I doubt that that would happen, but, frankly, I'm really, really fed up right now. So I moved. And if you've listened to this podcast long enough, you know I used to host at KaboomRacks. I had, a small number of servers, and, frankly, Kaboom Rack's service has gone downhill a lot over the last year. 

They've had a number of people who have left. I know that. That is on the record. And so and, frankly, one of those was my salesperson who originally got me involved, and that actually kind of really caught my attention. I noticed that they started having issues, with uptime, so I started planning my exit. I found a new host at bitcap. Let's see. Is itBiitcap or I should know this. Bitcap.co, and we moved the first batch of servers over. I don't wanna really wanna give you all numbers, to be honest, but, you know, we moved a small number of servers over. I had and it was my s 19 k Pros, and one of those came up bad when they racked it. Okay. Fine. 

It's actually still out for repair. These things happen. But then I had just a handful left of s 20 one's, which are they're only a year old. Like, they literally my year ended July. So I asked them now first of all, even right before that, one of those magically went down dead. Okay. Fine. Ship it off. And then another one went down. Well, that's weird. This this has been up and running for a year. Then they shipped them. They got the one back from repair, shipped the so I'll just go ahead and tell you I have four of these. Otherwise, none of this is gonna make any sense. 

Yeah. They ship three of them off. So one's still in repair. Three gets shipped to the new facility. They unpack these at the new facility at Bitcap, and they sent me a message that said, hey. All three of these are dead. And they listed the reasons and their various issues, and not a single one of those they they were perfect supposedly, they were perfectly functioning machines when they left the building. Now the serial numbers match what they should. I don't know what's going on. But to be honest, I'm really not happy with Kaboomracks night right now. And frankly, I put them in the same category as compass mining, which if you've ever been in the mining business of hosting where somebody hosts your mines, you know that that's bad news. Do not host with compass. 

If you have miners with kaboom racks and you have not had issues with Kaboomracks, you probably need to start planning how you can get out. And, unfortunately, you can't just leave. They always have a contract, and you have to make sure that you line it up with whenever that ends and whatever before you renew your new one. So I hope that wasn't too harsh, but frankly, right now, I don't really care because I have thousands of dollars in damage on minors. I have minors that have not been online for weeks now, and I don't even understand. And and all I get from them is and I can read it word for word. 

I'll read it. We we have noticed that a large majority of kpros and s21 miners have had to go to repair or warranty repair. Bitmain may have had some bad batches with these. I had not had a single issue with those Kaypros until it got shipped out. I've not had a single issue with any of these S21s until they knew I was leaving. And I'm gonna leave it at that. 

[00:09:09] Kenshin:

Wow. 

[00:09:11] McIntosh:

Yeah. It sucks. 

[00:09:12] Kenshin:

Let me get this straight then. Then you mean when they removed them, they were working, and when they removed them from from the rock and shipped them? 

[00:09:22] McIntosh:

I don't know, but one's got a completely blown power supply, Kenshin. I don't know how a server runs without a power supply. I probably need to turn myself down because I can see I'm peaking red on the meter. 

So sorry if I'm yelling in your ear, Kenshin. I do apologize. I am not this is why I wanna mine on my own. And the problem is that requires a large upfront investment that I just don't have. You know? I mean, you know kind of some of the things I wanna do. That stuff requires money, and it's money that I don't have. So I'm kinda stuck. I hope bit sorry, guys. I it's Bitcap. Right? Yes. They're they're not a new company. They've actually been around for a long time. And so far, I think I've well, so far, I've had a a great experience with them aside from the fact that they open up boxes and find dead servers, but that's not their fault. 

Alright. I do have one other thing. I have not opened these three miners yet, but I took my oldest three miners offline. Did not want to run them because of efficiency reasons. They'd rather have newer servers there, which I get. I thought they were still worth it, but I'm not gonna argue with them about it. So I got them for sale. I need to unbox them and make sure they look, like they're running before I start sending them off. I'm kinda scared at this point, frankly, of what I'm gonna find. I'm asking $300 for them for a well, actually, $3 a Terahash, and they're all around a 100 Terahash. It's not that's not exact. I think one of them is 95. 

One of them is right over 100, and maybe one of them is like 120, but I I'm not certain about that. So it would depend on the actual Terahash, and so it'd be $3. I'll pay the shipping as long as in as it's in The United States. These would make great home mining experimental type machines, frankly. Right. Or if you got cheap power, then go for it. Put it on your system and I mean, these are hashing machines. There's like 300 total terahash between the three of them. So I don't know. Sorry. I've been wanting to get that off my chest for a bit, and they just kinda sent me over the edge the last couple of days with four dead servers. And then, oh, I think we got a bad batch. 

[00:11:57] Kenshin:

Yeah. I remember you were you were close to saying something 

[00:12:01] McIntosh:

couple of months ago. It's been going on for a while in various ways. The the uptime has been terrible lately for months. 

There's always an excuse. I mean, I've been told it's crazy. Like, they literally said told me one time, they shut a data center down because of a storm. Give me a freaking break. A snowstorm. It's a data center. Right. I've never heard such foolishness. Not because of so these are, like so these are what do they call it? Where they can shut them down when they need the power. That's not what was going on, just to be clear. Right. This just they I don't know. I have no idea. I don't know. But, yeah, stay away from Kaboomracks. I would not buy servers from them. I would not buy hosting from them. I wouldn't touch them with a 10 foot pole right now. 

I hope they get their act together, but I'm I honestly, my suspicion is they're gonna go bankrupt because they cannot run a business like this. It makes no sense. I'm done. That's today's episode, ladies and gentlemen. We'll see you all next week. No. I'm just kidding. That went longer than I really wanted, frankly. I and I apologize. But, yeah, I I'm done with it, so it's it's over. I just had to pay the money now and get the servers fixed and get them back online. Whew. Let's talk about CoinJoin. Let's talk about Joinster. So I came across this a few months ago, and I thought this would be I've been keeping an eye on it. It's fairly new. 

The Joinster in that two. Right? I should say. What's that? It's from 2022, I think. At least the first proof of concept. Yeah. It's actually older than I thought it was, but it's still fairly new, especially with this type thing that it takes a while to get traction. So before we dive into Joinstar itself, I wanna give you a brief overview of CoinJoin. It was something we have talked about on here, but, you know, it's good stuff to know, especially when we're talking about privacy of your Bitcoin. Again, I know I've said this before, but Bitcoin, it's an open network. It's an open ledger, and so it's not private by default, if that makes sense. 

In fact, well, that's really what CoinJoin was kind of built for to kind of help solve that problem. So that well, yeah. Every transaction that you make is always it's going to be recorded on the block blockchain. So you can see how funds move between different addresses, and your name is not explicitly tied to it. But through chain analysis, what they call chain analysis, they can figure things out and, you know, kinda point back at you. 

[00:15:10] Kenshin:

Yeah. If they find one address belongs to you, then it's easy to trace all your movements. And I need to bring you up so I can actually see you. I'm sorry, Kenshin. 

[00:15:20] McIntosh:

There we go. 

Right. Exactly. So before we even dive into, you know, CoinJoin itself, one good thing to note is you should not be reusing addresses unless you have a real reason to. My mining wallet, for example, which all of that is open, you know, they've already got my information. The the hosting company does. I use the same address because otherwise, it just gets to be a challenge. But in general, that's not something that you would want to do. Alright? 

[00:15:53] Kenshin:

But every time you send money to one of your other addresses, you always use a new address. Yes. Right. Mhmm. 

[00:16:00] McIntosh:

Yep. I never send money anywhere except to the host. 

That money is locked up. It's in a business, and it will stay there for the foreseeable future. But, yes, that's true. Alright. So let's talk about CoinJoin itself. This is actually new to me. I did not realize this. I knew who Greg Maxwell was. He's pretty famous on Twitter. You know who he is. Right? 

[00:16:26] Speaker 2:

No. For the kids? You don't know who Greg Maxwell is? 

[00:16:30] McIntosh:

No. Oh my goodness. Well, there you go. Go follow Greg Maxwell. From what I can tell, and I don't well, seems like a pretty good guy. I'll just say that. I'm not gonna I don't know. That's what I know. But it was first proposed by Greg back in 2013, so it's been a long time. 

CoinJoin, this is the base implementation as a method to break this transaction linkability. The core principle is simple. We're just gonna combine multiple user transactions into a single transaction where inputs and outputs cannot be linked because that's the basis of chain analysis. I've got this input. I've got this output. They're all you know, we do the analysis, and we can figure things out. But what they're doing is they're mixing everything up. If you wanna think about it real simple, I don't have this in the notes, Kenshin, so bear with me. But if you had a bunch of money and I had a bunch of money and five of our friends had a bunch of money, we could stand around a washing machine and they were all the same bills. Let's just make this real simple. Everybody's got $100 worth of $5 bills. I know, American money. 

I'm sorry. $5 bills. We throw them all into the washing machine, and we run the washing machine or the dryer. It doesn't matter. Let's do the try and make it a little little cleaner. Right? And then we pull them back out, and everybody gets their number of $5 bills. Right? So if everybody had a $100 worth, that's $25 bills each, and there's seven of us. There's, 20 that's $145 bills, and we just hand them all back out randomly after they've been through the dryer and they've spun all around and they've mixed all up. What do you have? 

It's the same it it literally is the same kind of idea. Everything gets mixed up. You get the same amount going out as you came in. You get your $100 worth, but it's not the same bills. It's almost statistically insignificant, the chances of you getting the same bill. Does that make sense? 

[00:18:54] Kenshin:

Yeah. And if someone is striking that in the the one that you initially put in the dryer Mhmm. They track it back and then it goes somewhere else instead of Exactly. 

[00:19:05] McIntosh:

It breaks the chain of traceability. 

[00:19:08] Kenshin:

Yeah. It's funny that you take that example with the dryers or washing machine. Why is that? 

Yeah. Because it's like You've never heard that before? I've heard that used for coin joint before. Yeah. Yeah. Yeah. That's that's the example that came to mind also, but I am thinking yeah. That's just such a cliche type of thing. You wash money. 

[00:19:31] McIntosh:

Oh, I didn't think about it. Yeah. By the way, ladies and gentlemen, so I don't get in trouble with anyone. Yeah. This is not for money laundering. I'm just this is to keep your money private. Okay. Wow. Thanks for bringing that out, Kenshin. Great. I don't wanna worry about that for the rest of the episode. 

[00:19:54] Kenshin:

Well, if one person thinks about it, then others will. So Alright. 



[00:19:59] McIntosh:

So here are the requirements for a coin join. All the outputs have to be identical. In our example, we all put in I made it easy. I it's not true that you have to put in the same amount, but the outputs have to be equal point one BTC, for example, a Bitcoin, a tenth of a Bitcoin to create that ambiguity. If we got if if I put in $5 and got out $5, well, then most likely, that was me on both ends. Right? It doesn't mean it is, but most likely, it would be. You see and and chain analysis, it operates off probability. So they would look at that and say, oh, well, that's the same person. But if we all put in a $100 or if we all put in $5 and got out $5. If we all got out the same amount, that creates the ambiguity. 



[00:20:57] Kenshin:

Yeah. Yeah. The input can be different. The output must be the same. Right. Is the output that is the untraceable one Mhmm. Or the broken chain one. Mhmm. Mhmm. The input can be different. It must be higher than the output, equal or higher. Equal or higher. Right. You could put in a bigger input 

[00:21:15] McIntosh:

and then Yeah. Get out multiple outputs. 

[00:21:19] Kenshin:

Yeah. Because then you get the change. Exactly. The change is traceable, 

[00:21:25] McIntosh:

but the equal output is Right. Broken chain. Maybe I put in 1 Bitcoin, and I get out 10.1 Bitcoins. So that's 1 Bitcoin in total. Okay? Oh, that's the other hand, you only put in 0.1 Bitcoins and you get out point one. If your pool is big enough, and we'll talk about that in just a minute, then it it creates enough cover essentially for that. Mhmm. 



[00:21:54] Kenshin:

Yeah. But another another one I've seen, it's with join market. You can put, let's say, you said 0.1. If you would put 0.15, you would get change 0.05. 

[00:22:10] McIntosh:

Right. So that's still traceable. There has to be some planning on the input part. Yes. Yeah. Sorry. That is absolutely correct. Obviously, the well, the output has to be equal. You have to have multiple people doing this. If you mix it yourself and give it to yourself, then it's still you, and that's easily figured out. You have to have someone to coordinate this, and we'll talk about that because that's kind of what Joinster solves, if you wanna call it that. 

And then you also use different fresh new addresses for all the out outputs. You don't reuse those addresses. Alright? So let's talk about coordination for just a second because that's a key to a lot of this. The challenge of any traditional CoinJoin implementation is gonna be how do you coordinate all these people who don't know each other necessarily and hopefully, most likely without creating a trusted third party. So just creating a new lack of trust, a place to fail. Right? And I'll just give you an example. We saw this with Wasabi, with the Wasabi Wallet with k Snacks, which is the company that was behind them. 

They were pressured by the government, and they subsequently stopped. Were they evil? No. Probably not. I don't particularly care for the person behind that project, frankly, but, you know, I don't think that they're evil. Does that make sense? Yeah. But they were a party that had to be trusted in all this, and the government stepped in and, you know, they they stopped. They shut down in 2024. 

[00:24:06] Kenshin:

And it was a centralized, 

[00:24:09] McIntosh:

solution as well? Yeah. It was at the time. So Yeah. They, they can be compromised. That's certainly possible. They could be coerced like z k snacks was, but it is a single point of failure. The the other side is it's really easy to do. 

It's an easy system to implement, and it provides for reliable coordination, but you are putting your trust in them. Now a peer to peer solution like JoinMarket that you mentioned earlier is more decentralized, and they basically just use a market based fee structure. But it is more complex. And depending on who it is, liquidity can be a problem. I don't know what joint market is like these days. I think it's got a reasonable amount of liquidity, but these systems tend to be less used. 

[00:25:08] Kenshin:

My favorite so far has been a solution on top of joint markets called Jam, j a m. We have briefly talked about Jam before in the past. 

So for me, that was super easy to use, and, the only issue for me was too high fees. 

[00:25:27] McIntosh:

Right. 

[00:25:29] Kenshin:

Which join stir solves also. 

[00:25:32] McIntosh:

Alright. So, if we have this decentralized system, we have some challenges. How do you prevent participants from signing conflicting transactions? So this kinda goes back to, what's called the double spend problem. Alright? And another issue is if someone provides invalid inputs, how do you identify them and how do you exclude them without compromising privacy? A third issue, is a denial of service just plain and simple? How do you prevent people, for whatever reason, from disrupting those rounds? 

And then finally, you have what's called a sybil attack, which is when you have one entity that controls multiple inputs. Alright? So those are all different challenges that you can have with these decentralized solutions. I don't wanna get too in-depth on that, but 

[00:26:32] Kenshin:

it sounds maybe like if you have one person with multiple inputs that's, it's easier if you figure out that person with multiple inputs, then it's easier to figure out the rest of them as well. Right. So it That makes a lot of sense. Compromise everybody's privacy. If you've only got five people in the round 

[00:26:50] McIntosh:

and one person has three of those inputs, then that narrows things down a lot. 

Right. Right? Okay. Yeah. That makes a lot of sense. So join a STR is actually what we're specifically gonna be talking about. And it is a coin joint implementation that uses nostr in the background. It doesn't really mean you have to be, like a nostr guru or whatever, that was launched as a proof of concept in August 2022. Okay? So it's been a couple of years. Probably time to take a real look at this. And, Joynster, unlike, say, Wasabi, they're set up, z k snacks. It does operate in a decentralized manner, which is going to eliminate the need for centralized coordinators, which is a huge, part of these problems. 

What are some of the advantages of using Nostr for that coordination? I think there's a few. It's censorship resistant. It's very difficult to kind of shut down. I don't think it's possible at this point, certainly, to shut down the Nasr network because it's composed of all of these different components which are controlled by different people. Have you ever run a relay, Kenshin? I think you have. Yeah. Yes. I I did for a while. I mean, it's easy to spin up a relay. It's relatively easy. It's a very simple protocol. It's not very difficult, so it's easy to implement. You can use multiple relays to avoid trusting one relay, just the whole relay thing I just mentioned. 

And you can use different key pairs for each round. And your key pair is like your your Nostra key. This is your identity on the Nostra network. Like, if you go to primal and search for Macintosh and you find my account, that account is kind of backed by my key pair. Well, in this case, every time that there's a round of this, you generate new keys because it's super easy to do that. So it it's, again, it's it's kinda scrambling everything up. Does that make Mhmm. Yeah. Sense? Okay. So hold on with me for just a minute. We're gonna we're gonna roll through this. This is kind of the heart of things. So, instead of a lot of complexity involving multiple rounds, not a joinster uses something called the all pipe anyone can pay. 

Okay? It's a flag that allows a transaction to have a fixed output or fixed outputs while keeping the input list open. Now we are talking about a Bitcoin transaction. Alright? You can add your input with your signature to the transaction without invalidating all of the other signatures. Each participant is going to sign their input with a commitment to specific outputs. Anyone can combine these signed inputs into a final transaction, and that's it. There's no complex coordination that's needed. Participants can't double spin, so this completely eliminates the double spin issue because their signature commits to the output that they will receive. 

Does that make sense to you, Kenshin? Yeah. I wanna pause on that for just a second. I know it's kind of I threw out of this crazy all anyone can pay flag. Just don't get fixated on that. It's simply a flag in the transaction that you can set. And it means that you're gonna have fixed outputs or a single fixed output. And it also means that your input list is is wide open. You can have as many as you want. Alright? Yeah. One of the things that this means is that Joinster does not require participants to lock up Fidelity mods. You don't have to commit, I don't know, a quarter of a Bitcoin to throw a quarter of a Bitcoin into the coordinator. 

Does that does that make sense? 

[00:31:09] Kenshin:

Yeah. Was it is that the case for other implementations? I I think join market was, was not mandatory to to to have those type of locks in place. 

[00:31:24] McIntosh:

I'm not sure. I have heard of this type thing. So I I to be honest, I couldn't tell you specifically. Maybe they've moved past that at this point, but there have been implementations that use that. I have heard of this. You you have to use a, essentially, a bond to guarantee that you're Mhmm. Credible. You're credible. You're a legitimate person. Exactly. And the founder of this project is anonymous. So, they are maintaining a commitment to anonymity, which I think is a good thing. 

The relay is gonna share a random secret with the clients for one round, and that is going to be present in the output registration request. It does not actually get published. The relay would not be able to link inputs and outputs as the number is the same, and they get registered at different times with different keys and IP addresses. Again, I mentioned, you know, you can use multiple relays and that's gonna help, with the trust issue. 

[00:32:36] Kenshin:

I think I read in the documentation you can use your own Bitcoin node as well. 

[00:32:42] McIntosh:

Your I would not doubt that. I would not doubt that at all. 



[00:32:46] Kenshin:

So you don't even have to worry about 

[00:32:48] McIntosh:

leaking your IP address to other releases and stuff like that. Correct. The latest version actually does include a VPN implementation. So Uh-huh. All the different pool members are gonna use the same IP address provided by that VPN. So that's pretty cool. Again, plausible deniability, you know, you're kind of spreading things around. It works with Electrum, which is a wallet. They do have a new join strap for Android. I don't run Android, so I haven't been able to look at that or haven't tested that, whatever. But, that has both Testnet and Mainnet support. I would highly recommend, if you're thinking about doing this, use the Testnet to start with before you start committing real money to it. Yeah. Okay? 

Oh, yeah. The fees. We definitely should talk about this. The only fees involved are the minor fees and the Nostra server if you're not if it's not free, which a lot of them are. That's it. There's no coordinator. So you're not paying the coordinator to to do that. And in fact go ahead. 

[00:33:56] Kenshin:

And the the transaction fee, the mining fee that, of course, it's yeah. That you mentioned is the minor fee there. Right. It's shared. It's shared equally between all the participants, which is very different. 

[00:34:11] McIntosh:

If you had a dozen people involved in that transaction, then it's basically divided by 12. 

And as far as that may be the only way they do it. I don't know that they put any weight to it. They just divide it by 12, and then you pay a twelfth of it. And that's fair. Right? You're you all are sharing in that transaction. And so even if the main net fees are high, you're getting a discount. Yeah. Which is huge. Exactly. 

[00:34:41] Kenshin:

Yeah. And that's the big difference with the gem that I mentioned, the joint market implementation, where the one who starts the the coin join Right. Pays all the fees. Yes. And I did that the first time without really understanding what I was doing. When was this? I you've at least told me about this. I don't know when this I I don't know. That was a couple of years ago. I remember this. I literally I literally paid 50,000 

[00:35:07] McIntosh:

sats of fees. 

That was your kid's college fund. What did you 

[00:35:15] Kenshin:

Yeah. A lot of sats. Yeah. So many sats have been lost here and there. We have to learn. This is how we learn. Yeah. Alright. 

[00:35:23] McIntosh:

No. I I think you've told me that story, though. Even if it would be I'm sure it wasn't since you've been on, but, yeah, I think you've told me that. I anyways. Yes. So big savings there. That that's kind of it in a nutshell. And with all things that are going on in the world, I think that these type tools are very important. I think they should be continued to be developed. You may need to start taking advantage of them. I think that there are people who probably, would would would be good, would be good with that. So I got a list of some kind of future developments. 

I don't know. We don't need to go into that. Alright. So to kinda wrap this up, though, in my opinion, your mileage may vary, I guess, But I think that this is frankly a very significant upgrade in the coin joint realm, so to speak. I like what they've done. I like how they've implemented Nostra into all this, and the fees, aspect of this is certainly pretty cool. I would love to see more of this, frankly. What do you think, Kinsha? 

[00:36:43] Kenshin:

Yeah. I I think it's great. I can't wait to experiment more more with it. I I just read some documentation Mhmm. Still. Did you not heard of this before now? I don't think so. Really? 

It sounds familiar, the name, but I I never really understood it was with Gnostr, 

[00:37:01] McIntosh:

CoinJoin with Gnostr. With that name like Joinster, and you didn't think it was on Gnostr? 

[00:37:07] Kenshin:

No. I thought it was like a chat app or something. I don't know. 

[00:37:11] McIntosh:

It's j o I n s t r, by the way, in case you can't understand my English, which I understand. 

[00:37:19] Kenshin:

But Yeah. But for me yeah. But for me, it sounds good. I mean, it sounds even better than Jam, which I really liked. And, I I like that it has the Nostra implementation in the back end. It's because it's it's good use for it. Mhmm. Because Nostra is not only for Twitter clones. It's not only for notes, people. It's other stuff. Protocol. 

Yeah. Exactly. Alright. Very cool. It's a good protocol. 

[00:37:46] McIntosh:

So for news and notes this week, I did I wanna do something different. So I sprung this on Kenshin right before we started. So you guys know Jack Mallers is my boy. I listen to his podcast every week, and I heard the it wasn't on his podcast. He would never do self promotion like this. He'll promote his own company, but not himself. I don't know if you ever listened to that podcast, Genshin. He's always talking about his companies. He was on Bloomberg, which is, like a business news, network, and it was pretty big thing. So I listened to this interview. It was like ten minutes long or something. 

And, of course, he's talking about what is it? '21, his new 

[00:38:33] Kenshin:

SPAC thing, whatever. And and and all that, 

[00:38:36] McIntosh:

which is which is great. But he threw in, I thought, a couple of kind of bombs. You know? I really thought these they ask him questions, and he gave, I think, some very good answers. And I just wanna I wanna listen to this. It's only a couple of minutes. So So we're gonna listen to these, and then we're gonna talk about them. So let's go ahead. 

[00:38:58] Speaker 2:

Do you envision a future where Bitcoin treasury companies such as Strategy, Mara, and you guys end up buying so much Bitcoin that there really isn't actually much left out there on the open market for people to trade. After all, it is a fixed number of Bitcoins, so 

[00:39:16] Speaker 4:

no more will be created once it reaches that number. Right. You know what's fascinating about the asset, and it's not intuitive because it's so rare, is that to your point, it is definitively scarce. 

So if everyone in the world wanted an iPhone, Apple could make more. If everyone in the world wanted a McDonald's cheeseburger, McDonald's could make more. The fact that Bitcoin cannot increase its supply means the new supply comes from the market. If you want more Bitcoin, you don't go to the Bitcoin factory to get one. You have to go up in price. Is there enough Bitcoin for me at a 120,000? No. Okay. A 130, 140, 150. So I tell you what, there's always Bitcoin available. Just depends on what you're willing to pay for it. And so what I think will happen is this price will continue to discover higher because Bitcoin is the scarcest thing. It's inelastic to the amount of demand that searches for it. So the amount of buying power that we're seeing from the capital markets, from the ETFs, and potentially from nation states like The United States, I think they'll find the supply they're looking for. They're just gonna have to go get it at a higher price. 

[00:40:18] McIntosh:

Okay. 

Very cool. Yeah. First of all, I do wanna apologize. The audio on that, not the best. I don't think it was me. I think it was actually their audio to start with. I noticed it when I was first listening to it. But it's audible. It's you can hear it. And I just I really first of all, what do you think, Kenshin? I don't wanna 

[00:40:42] Kenshin:

I think it's a great point that we always forget. Yes. Because what means, fixed supply doesn't mean, it's not gonna be available to to buy. Right. Everybody has a price. Yes. Right? It's a typical saying. Mhmm. So yeah, I know I've said before, if you look at the gold reserves, it's even less than 20 if if you look at tonnage tons, metric tonnage is 200 something thousand. 

So that's not much either. And still people trades gold around. So Right. Yep. That's a great point. I think Mhmm. Yeah. But you got some good examples. Yes. Good logic. Yes. I, you know, 

[00:41:26] McIntosh:

I wanted to bring this out for one thing. I heard this other podcast. Well, it's let's see. It was Danny Danny's podcast, what Bitcoin did, the what Bitcoin did podcast. He had on, Troy and a woman that, frankly, her name escapes me. It starts with an e, but they were talking about these, surveys that they had done across The United States, across the world in her case. And it was shocking to me, shocking how many people did not realize that and I'm dead serious that that people didn't realize that Bitcoin had a fixed supply. 

They did not know Kinshan. It was less than 5% in total. Had any idea that Bitcoin was 21,000,000 and that was it. People who held Bitcoin, go ahead and guess how many people knew about a fixed supply of Bitcoin. 

[00:42:27] Kenshin:

Oh, I would guess 25%. 

[00:42:29] McIntosh:

It was actually higher than that. Thank you. Oh. No. It it was, but it's still I mean, to me, this is, like, literally in the top three of the reasons why I Bitcoin. Okay? It Yeah. Yeah. If it's anything else, it doesn't matter. It's irrelevant. And it was less than half of the people who own Bitcoin, who literally said, I own Bitcoin. 

I do not know that Bitcoin has a fixed supply. I'm sorry. You fail. Now you don't understand what you're talking about. Right? So ladies and gentlemen, 21,000,000 Bitcoin forever. That's it. End of story. Yes, sir. 

[00:43:10] Kenshin:

And and I bet you those the majority of those people who don't know, they don't even own Bitcoin because it's they don't have the keys. So it's not really their Bitcoin. I don't wanna dive all into that. It was an interesting 

[00:43:23] McIntosh:

survey, and frankly, I don't promote other podcasts. I try not to, but you might wanna grab that one and listen to it. It is interesting. 

What Bitcoin did, it was the latest episode, I think. It was Troy, who's used to have his own podcast. I don't think he does anymore. And a woman I mean, it's like Elizabeth or I'm sorry. I'm so sorry. She's actually just she's like a student at Cornell. Kind of interesting, but, yeah, you you should listen to it. That survey results look. We're getting there, but we're not there. 

[00:44:03] Kenshin:

We're so early. We're so early. 

[00:44:06] McIntosh:

So early. 21,000,000 Bitcoin people. Just get a tattoo. 21 over infinity. I don't know. Minus all the ones from Satoshi and a bunch of other little girls. It doesn't even matter. You're right. But Yeah. Yeah. Alright. Let's do the second one. I gotta get ready. 

Say, oh, I'm sorry. Where's Reaper? It's gonna be so much cleaner once we get this set up. Alright. Here we go. 

[00:44:38] Speaker 2:

Would you expand to other digital coins? For instance, become a treasury company for Ether or Solana or something 

[00:44:44] Speaker 4:

else? Absolutely not. And I'll tell you guys why. I've made you laugh. Yeah. Because you guys are all maxis. Like, you talk to somebody who has a big an ether treasury company, and they'd say the same thing about Bitcoin. Yeah. So You can't mix the two ever? Well, little little history lesson. The term maxi was actually invented by Vitalik Buterin. It was a diss. It was slander. You know, I now take it as a compliment, but, to be clear, I don't self prescribe that. Little background on my opinion. K? 

Us humans own a little over $900,000,000,000,000 worth of stuff. Currencies, sovereign debt, real estate, precious metals, fine art, all of the things that we collectively own as a species. About half of that, so call it 400 to $500,000,000,000,000 worth of it, we're using to save money. Right? You own the $10,000,000 art painting not to put on your wall so your toddler can throw spaghetti at it and ruin it. You own it because you wanna sell it for $11,000,000 in the future. You own the real estate not to consume it because you're living in it, but because you're trying to save and build a real estate portfolio. So that the amount of wealth humans have created that they wanna bring with them tomorrow and save into the future is about 4 to $500,000,000,000,000. To me, that's what Bitcoin's going after. After. It's that pristine store value. It's that pure money. Right? What is Ethereum? What is Dogecoin? What is Solana? 

To me, I don't know. At best, a technology, are these things going after Apple, Amazon? If they are, let's go out and give Ethereum credit that I don't think it deserves and say it's going to achieve what Amazon has achieved. Okay. 2,000,000,000,000, $3,000,000,000,000 worth of value to society. Reasonable, nice, a new cool tech stock and that's if they go on to achieve that. If Bitcoin goes on to achieve a small fraction of the 4 to $500,000,000,000,000 that humans are looking to bring with them tomorrow, we're talking about tens of trillions of dollars of appreciation. So it's an orders of magnitude larger problem Bitcoin's going after. It's an orders of magnitude sounder bedrock to build a treasury. I do not wanna build a treasury on potentially the next Amazon. I wanna build a treasury on the new gold, on the new sovereign debt, on the new currency, on the new dollar. So Mhmm. That for me, our shareholders should know I will never own another asset outside the 

[00:46:51] McIntosh:

Cool. I kinda cut that last little bit off, but the everything's there. Like, that's it. So, real quick, thoughts on that. Of course, he is a Bitcoin maxi. 

I think that's I I that's kinda what we are at this point. Right? Yeah. Sure. I the the term is is almost slanderous. It certainly was to start with, but, but it means something. You know? There's a reason why Bitcoin is number one. There's a reason why all these other tokens and whatever, they end up going to zero. I saw Melania's coin or NFT or God knows whatever it was, the president's wife that they you know, it's down 99% since they issued it. So, you know, I mean, it's it's just look. It's just a a money grab. I mean, let's be honest. Yeah. 

[00:47:48] Kenshin:

I I don't know. He was very he was very kind because he didn't talk about all the negative, how do we say? 

The objectively negative aspects of those coins. Yes. That they have no fixed supply, they have a free mind, and the and the rest of it. So he went after a good narrative also that is a store of value. That's my boy. Surreal. Start claiming me. Maybe maybe 

[00:48:13] McIntosh:

I don't know. Does that get me any benefit? I don't think it does. Oh, well. Alright. Hey. I got a question for the week. I did. And it completely oh, no. I've got a question. Good lord. I'm getting old, Kinshan. I've got a question for the week, Kinshan, and here it is. That's the first time we've ever done anything like this. Clipped and, you know, sees news items or whatever. 

Let us know if you like that. If you do, if you don't, whatever. I'm always open for input. I kind of like this. It is something that does take more work, and I'm gonna tell you, we will not be doing this every week even if you all say it's the best thing since peanut butter. But I'm open to doing it more. So let us know. I like it. Well, that's one vote, and I do like it. I I it's a way for us to kind of inject something different. Alright. Awesome. I think it's about time to bring this thing on home. Okay. We do have a lot of resources for Joinster, and I'm gonna include those in the show notes up on that shiny new website we've got there, by the way. 

[00:49:37] Kenshin:

I thought I saw on their website that they also have an iOS app. 



[00:49:41] McIntosh:

I if they do, I am not aware of it. I'm sorry. Okay. I would not, be shocked. Okay. Our Bitcoin price as we record, 115,550, which is down from last week, but up for the last couple of days. And how are we doing over in Euro Land? Below 

[00:50:05] Kenshin:

100 k. So we're 99,100. 

[00:50:08] McIntosh:

So you're down a little bit too because you were just above 100 last week. Right? Yeah. But the good news is, apparently, a year ago, the price dropped in the last week. Last August 6, I could not believe this. It was down at $56,048. So we are actually up 106% in the last year. 



[00:50:32] Speaker 2:

Just let that sink in. 

[00:50:35] Kenshin:

I had to double check the math. I'm like, what what number is that? A 106%, 

[00:50:40] McIntosh:

sir. That is crazy. Okay? So this is why we DCA. This you stop worrying about the price. The price will go up. And there will be time periods, by the way, where it is conceivable that a year later, you're down. It's okay. Keep stacking SATs. SATs are cheaper when the price is down. 

[00:51:05] Kenshin:

Yeah. Bitcoin market cap is at 2,300,000,000,000.0, USD. Okay. Gold market cap, 23,400,000,000,000.0 Uh-huh. Which bring Bitcoin versus gold market cap at 9.8 

[00:51:19] McIntosh:

That's disappointing. Low 10. 

Not not above 10% again. 2 SAS per vbyte and a 177 megabytes of unprocessed transactions. It's actually over a 100,000 unprocessed transact. It seems to me that it is starting to build up again. Now I'm Yeah. It's busy. 

[00:51:42] Kenshin:

Yeah. 

[00:51:44] McIntosh:

Good. Busy busy. Good. Make sure you get those live channels set up, ladies and gentlemen. Because one day you'll wake up and it'll be 10 per v bite or 20 or a 100. And those sats will be more precious 

[00:51:59] Kenshin:

than they are now. Not those days again. Yeah. 

[00:52:03] McIntosh:

This is what happens. Alright. We're gonna wrap this puppy up. I hope this has been enjoyable. Been a little bit different today, maybe. 

But Satoshi Splebs is a value for value podcast supporting podcasting two point o. No ads, no sponsorships, just honest Bitcoin content. I deliberately avoid sponsors because even if I love a company, taking their money is going to influence my opinion. What if something goes wrong with that company? I would hesitate to warn you, frankly. Instead, I ask simply, are you getting value from this show? Support it through time, talent, or treasure. Help with chapters, transcripts, our new website, future projects, whatever. Stream sets, boost with messages. A 100 sets saying great show or you suck. We'll read it either way. By the way, we kinda skipped over the supporters because, let's be honest, there weren't any. I don't know if it's the summer. I don't know if you guys are not listening or if we're just hitting a really bad stretch. I have no idea. 

But we do appreciate you listening. Check out the apps at podcastapps.com. Support independent Bitcoin media. If you like the content, I would love it if you would tell your friends about the podcast. That is the best way for us to grow. This week's music is not Ainsley. It is Electrobador, Cypherpunk's Not Dead. It'll probably be there last week. Probably switch that out. Any boosting or streaming of sets during that song will go straight to the audio. Sorry. Straight to the artist. 

[00:53:40] Kenshin:

Nice. So thanks for being here. We hope this has been helpful, and we would love to hear from you. Find all our contact into satoshi stats plebs dot com. Stay humble. This year those ads, and have a great weekend. We'll talk to you all soon. 

Bye bye. 
