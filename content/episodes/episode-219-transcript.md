---
title: "Episode 219 Transcript"
draft: false
_build:
  list: never
  render: always
---

[00:00:00] McIntosh:

What is up, PlebNation? Today is July 26, and this is episode 219 of Satoshi's Plebs. In today's episode, I ask a simple question. Is your Bitcoin safe? Alright. As I record, we have a block height of 907,193. Once again, hopefully for the last week, I am alone. Miss Kenshin, I know you're listening when you get a chance, and I appreciate that. I appreciate everything that you've done. You've become, in a really short time, a big part of this show. So, anyways, hopefully, we'll see you back next week. Hope things are going well. Alright. For me, for this week, all about work. You don't wanna hear about it, but, hey, we hit our milestones sort of. 

And, in essence, we're kind of on the downhill, so hopefully things will calm down. Alright. Great. We are a little late this week. As you'll hear here in just a minute, I had an a great interview with Andreas from bitcoinsafe.org bitcoin-safe.org. And, I thought it was important enough that I delay things by a day, plus work was even more stupid than normal yesterday. And so there we go. So here it is. I'm getting it out as quickly as I can. Andreas and I interviewed this morning early, and I've now done that edit. And I'm gonna do this wrap up, kind of around it just so that you know what's going on and we don't jump right into the interview. 

But before we do that, I do want to, give a shout out to Send It Mike. He boosted a 1069 sats about last episode, which was which was Are You Ready for a Million Dollar Bitcoin. So I appreciate that, Send It Mike. Here's his message. He said, good episode. I personally no longer think the having will drive price cycles. That's not to say there won't be booms and busts. That's just human nature. I think it'll be driven by global liquidity and people moving in and out of risk assets. Appreciate the insight. Appreciate the opinion. And, there are a lot of people who think that. I am going to be a little more conservative, to be honest, and I'll believe that the havings are gone when I see that the havings are gone. But I do understand where you're coming from. Makes perfect sense. 

I'm just, paranoid. Alright. So is your Bitcoin safe? I as I said today, we're going to be interviewing Andreas from bitcoin-safe.org. He has written a great piece of software to work with hardware wallets to manage your Bitcoin and do it in a very effective way. In fact, this product has been on my radar for a while. And I actually said in the interview, and I wasn't just saying this, I'm probably gonna test it out before the end of the year as kind of a replacement for my current strategy. And I'll just you know, I talk about it in the interview a little bit, so that's all I need to really say about that. But, Andreas is the real deal. He's been around for a while. We talk about all of that. 

This is open source software, which is always important to me, but he's done some very innovative things. I think he's done it in a very clean manner. I think, he has a real handle on multisig wallets and and setup. So pay attention. Take a listen. This may be something that you want to incorporate for your family. So with no further ado, here is Andreas.  

[00:03:52] McIntosh:

is. Alright. So, hey, Plebs. This is McIntosh, of course, and I just today, we're gonna be doing something special for this segment. I have the creator of the bitsafe.org. I guess you call it Bitcoin say I I'm sorry. Bitcoins dash well, boy, I munched that all up, Andreas. This is Andreas, by the way, and he has created a product called Bitcoin safe. So we'll start there. 

English hard. I as I say from time to time. Sorry. But, yeah, welcome to the show, first of all, Andreas. 

[00:04:31] Andreas:

Yeah. Thanks. Thanks for the invitation. You're welcome. 

[00:04:34] McIntosh:

You are an elite part of an elite group of people. There's only been a few other people on the show that we have interviewed. So congratulations. You made the cut. You said yes. Actually, that's what it was. But, yeah, thanks for being on the show. I came across your product. It's been several months ago on Noster, and I wanna it's very interesting. I I believe you have a different, slant on this, and it's something that listeners of the show may want to, explore and hear about. So I thought I'd have you on the show. 

Go ahead. Just to start off, just tell us very briefly kind of what Bitcoin Safe is, what your vision is for it, and we'll go from there. Sure. 

[00:05:22] Andreas:

Okay. So Bitcoin Safe is, open source Bitcoin wallet, and, it is focused on savings. So my my kind of slogan on the website is, a Bitcoin savings wallet for the entire family. Mhmm. And, what does Bitcoin savings mean here? That means I focus on hardware signers. So in Bitcoin safe, you have to use a hardware signer, at least on Mainnet, to be able to use it because I think that's the only way to keep real savings secure. A computer itself is not designed to hold secrets. 

So a a hardware signer, and I support all of them, is, I think, a requirement for Bitcoin savings. 

[00:06:14] McIntosh:

Okay. Great. So you'd you don't have a 

[00:06:18] Andreas:

phone wallet version of this. So what you're saying? No. I don't have a phone wallet version. Actually, that's exactly kind of the differentiation I I I make because Bitcoin safe is for desktop only. Right. And that's kind of my view how I see it. So the phone is something that you have with you all the time. It's fast. It's easy. Mhmm. It's for daily spendings. It's Yep. Perfect for lightning, for cashew, for for anything that that's fast. And if you lose it, you lose it. Yeah. It maybe hurts a little bit, but life goes on. Yeah. But if you have real savings for yourself or for family or so, then you don't want the things to be fast. You want things to be slow. Mhmm. And you want to double and triple and quadruple check everything. 

And for that, Bitcoin savers. And that's why I said very early on, I'm not gonna support seeds at all, just on testnet because it's great to play around with it. So go ahead there. But on mainnet, seeds on a computer are a really bad idea. Yes. 

[00:07:23] McIntosh:

Yes. That's terrific. I to be honest, I think you and I share a lot of similar philosophies about that kind of thing. I have said a number of times on this show talking about like, specifically talking about lightning wallets, really. You know, hey. You don't this is kinda like your carry around money. It's like your wallet. Like, you put your wallet in your back pocket, and you don't walk through, a bad neighborhood carrying a couple thousand bucks in your wallet. 

Right. That's just not smart. Right? And so but if I had 20 in there or, I guess, maybe even these days, a 100 because of inflation, you know, it's it's yeah. Is it gonna hurt? Yeah. Am I gonna think about it? Yeah. But it's really not that big a deal. But developing specifically, for this idea of, hey. We're gonna keep it safe. We're gonna keep it offline using the hardware wallet with the technologies that those provide. You know, that's that's good. Do you consider, by the way, the seed signer to be a hardware wallet? I did I haven't. Sure. Okay. So you support that one? Yep. Great. That's my favorite in case you'd I don't know if you listen to the show regularly. 



[00:08:38] Andreas:

Not regularly. Actually, since I started programming 

[00:08:42] McIntosh:

so much on on Bitcoin safe Mhmm. I reduced how much Bitcoin podcast I listen to because I don't have infinite amount of time. Alright, ladies and gentlemen. What he's saying is I didn't make the cut, but that's okay. I can handle rejection. It's alright. I love the Seed Signer. And in fact, the next guest that I'm planning on having on the show is the creator of the Seed Signer. We had him on. I looked it up. It was back in 2023, and they just put out a new version of the SeedSigner with a bigger screen, which I'm really excited about. So I wanna have him back on the show. I guess that was a preannouncement of the announcement. Sorry. 

But yeah. Awesome. Good stuff. So I wanna so how did you get involved in this, actually? 

[00:09:32] Andreas:

Yeah. So so I think it started for me with the trucker protests. The with the tracker protests, then I really noticed, okay. I mean, I could contribute something that that brings the space hopefully forward. So I started contributing to Spectre desktop wallet Okay. Under, the NIM. And and I learned a lot. It was really cool. But at some point, then I saw, okay. I if I especially because I saw how how far BDK was coming along, so Bitcoin development kit. Okay. It's a it's a Bitcoin it's a library for Bitcoin development. 

And, I saw, okay, this would be a great library to build upon. And, and I thought, okay, I could I could start my own wallet with this because, ADK would handle all of the, like, very, very complicated Bitcoin parts that, and and BTK basically just abstracts this way. And that's a great kind of, separation of concern. Right. BTK does not does not, do anything with you. The interface is also they just focus on having a very, very good API. And, that's what I can use and integrate. Yeah. Okay. And I can focus on the stuff that is is important to me. And and BDK, 

[00:11:04] McIntosh:

it's a very solid product. It's been around for I don't know how long, but it's been a a good while. 

Will they ever have a bug? Sure. I'm sure they probably will at some point or two or three maybe, but, you know, 

[00:11:18] Andreas:

they've been I mean, every software has bugs. But I mean, the the question is how serious. Right. And, I I I doubt there are any. I mean, I cannot imagine that they're serious bugs. It's it's very well vetted. So, 

[00:11:32] McIntosh:

it's it's a solid product to be building on, to use to use as a building block, right, which is really what you're talking about. So that's that's great to hear. Now while we're going down kind of the software side of things, you told me before we started, well, it's right on your website, right on the front page. This is an open source product. Does that mean that somebody can go and grab your code off of GitHub? Sure. 

Sure. It's GPO three. Okay. And so do you have a community of people that are helping you out or you're essentially the well, I know you're the primary coder, certainly, but do you have other people who are involved? Let me put it that way. I mean, there is a since since the beginning of the year, there, 

[00:12:17] Andreas:

a designer joined, and I'm super grateful for that. Okay. It's, because I I can code well, but design is not my strong suit. So, I have a lot of features in there, but it's not necessarily clear how to reach them in the user interface and so on, how how they're structured. And that's really where the designer come comes in and, and helps me really to to to make a better user interface. 

And it's also what the next version is going to be about with 1.5. I'm I'm working on that. Okay. And it's, it's gonna be a a big design environment. The UX upgrade. Okay. 

[00:12:56] McIntosh:

It's interesting how many people I talk to that they can handle the coding part, but they, you know, the UX is a challenge. And I get that. I don't know if it's, maybe a different way of thinking. I don't know. But, that's a very, very common, you know, thing. So I'm glad you got somebody involved. You clearly have other people involved who are helping you with language unless you know a lot of different languages. I mean, not not really. I mean, there there were a few contributions, but the main part is, just AI. AI is the same. Now that's interesting. That's the first time I've ever heard of that. So I just as I'm not gonna go through the list, and just say them all, but one, two, three, four. I you've got 13 languages on here, if I'm reading this correctly, if I'm counting correctly. Yeah. I I I lost track. 

Actually, that might be a good area for people who want to support you to jump in, you know, if Yeah. AI is not perfect, and I wanna talk about AI in just a second, but AI is not perfect. It certainly does make mistakes. And you've got Hindi listed on here, for example. I doubt you can look at a Hindi translation and, you know, figure out that that's a mistake. So that would be a great area for people to help support. 

[00:14:23] Andreas:

Yeah. Absolutely. And I I try to also make it really easy. So I have an integration with WebLATE, where you 

[00:14:31] Speaker 2:

have then wait. You can look up all the languages of Bitcoin safe in this interface Mhmm. 



[00:14:36] Andreas:

And directly edit it and submit it. And I basically get it as a PR. Oh, wow. It's really easy. I've never heard of that. That's interesting. That is 

[00:14:45] McIntosh:

interesting. That is really cool. Yeah. And that yeah. That would make it really easy. So there you go, plebs. There's a way that you can help out. Now my cohost my cohost speaks seven languages. He kills me. I can't even speak one. Oh, my cohost speaks seven seven different languages. So I'll just have him go through and, you know, clean out half this list. I'm just kidding. Oh, cool. Yeah. Know if he actually writes all of these, to be honest. I've not I so there's a question, Kenshin. Do you do you actually, do you write all these? But, yeah, you got Italian, French, and I don't think he speaks German, but he does I know Italian and French. 

I'm not sure about the Portuguese, the Spanish. So, yeah, all the, what is it called? Romance based language? The the Latin based languages, I think. Anyways, enough about that. That's funny. Sorry. I I I humor myself. It's because nobody else laughs. I don't know. Alright. Terrific. Now how are you managing to do this? How do you do you do this full time? Are you do you have support? This kind of thing. 

[00:16:00] Andreas:

Yeah. I I do that, in my free time, basically, and, I have now support from open sets Okay. Which is really cool. That's terrific. Yeah. And I also got a few donations now. It's it's really great. It's support, especially financial support, is is super important for, 

[00:16:17] McIntosh:

all the time. As someone who runs a podcast who depends on support, yes, it is really important. 

No. It it is. And that's terrific. I OpenSats is a great organization. I frankly, we could use more of, I guess, nonprofits like that. I don't know how else to describe them. But they if there's projects who are doing Bitcoin work essentially or Nostra work, and I I wanna talk about Nostra as well. Don't let me forget that. But, yeah, they, there's a high chance that they'll support it, which is I mean, they support a large number of projects. It's really good stuff. Very cool. Before we kinda go into the future cases for this, one thing I wanna talk to you about, I saw, and I guess I should say in case you people don't know at this point, yes, I have not used Bitcoin safe. 

I'm actually very interested in it. I may set it up and and actually experiment with it. And this is the reason why what we're about to talk about here. Bitcoin safe supports multisig, which we've talked about on the show before, certainly. Meaning, in order for the funds to be released, multiple people kind of have to be involved and provide the Bitcoin, their key. So, obviously, you support this. Can you talk about that for just a minute? 

[00:17:50] Andreas:

Absolutely. So, I mean, for for me, there have been actually two reasons two big reasons why to bid quite safe. And the first one is actually multisig. 



[00:18:01] McIntosh:

Okay. 

[00:18:02] Andreas:

I think for for for for significant savings, multisig is the way to go. It's it's simple enough that you can understand it, but it's robust and good enough to secure large amount of funds. And, so I I think of it that this way that if you have a two of three multisig, it allows you to make a really big mistake and don't lose your money. It gives you robustness against one really big mistake. So if you get fished once or if you lose your seed, it is robust against that. You can recover with all of your funds. And this is this is a superpower. This is a So a typical 

[00:18:45] McIntosh:

multi stake setup would either be well, like, would be two of three. Right? 

Yeah. So can you kind of walk through an ex a quick example of how that would work? 

[00:18:57] Andreas:

Yeah. Sure. One of the one of the things with, Bitcoin safe I I did is I created a step by step setup guide to help you set up a multisig in a secure way. Because multisig multisig is still complex or complicated. And, for for someone who is new, they they don't know which step to do at which time and when they're finished. Is is it now secure or not? And so I made this kind of wizard or step by step guide to help you set it up. So you click through you click through, you say next step, and once you're done, you're done. And it is it is really set up and it is secure. 

And part of that is, of course, setting up all the signers. Then I give you a PDF or three PDF sheets, where the descriptors on. And that is and these descriptors for MultiSync are really important. They're important parts of the security. So that's why I I give them my people have to print them during the setup process. And, then the next step is to register the MultiSync setup on the signers so the hardware signers know about the MultiSignature Wallet and can verify some things. And, of course, then it's also about testing. You have to test the Multisignature if everything works. So for that, you have to receive a small amount of Bitcoin onto this Multisignature Wallet and then you have to test all the signers. So for two or three multisignature, that means you have to make one transaction and sign with the signer one and signer two, and you have to make a second transaction and sign with signer two and signer three. 

And then you have to and then you have tested all recovery paths, all paths, and you can be absolutely sure that the hardware signers work as expected because they could produce valid signatures. 

[00:20:51] McIntosh:

And then you're basically done. This is very cool. So I have looked at a number of different product where, you know, maybe they support multi a lot of them don't, but let's say they do. I've never seen anything like this. So you not only you've got your seed words here, but you create a, are you creating a QR code as part of this for the seed sing is it like with seed signer where you show the QR code? What is this for? I support all I mean, to communicate with the hardware signer, I support all methods. QR code, USB, and with SD card. And that for all signers. But yeah. But this combined with the step by step directions which you have, this is this is fabulous. This alone would be a a a great reason to use this. So 

[00:21:47] Andreas:

Oh, it took me a long time to develop this setup guide because it's it's it's nontrivial 

[00:21:52] McIntosh:

No. To make this secure. Yeah. This is terrific. You you are to be commended seriously. 

And, this is highly worth looking at if you are interested in multisig, which you should be if you're if you have a significant amount of Bitcoin. And remember, a significant amount of a Bitcoin is 10 times at least its value as it is right now because after the next bull run, maybe that's what it'll be at. So alright. Exactly. Very, very good. Alright. What do you have future is 

[00:22:26] Andreas:

did what yeah. What do you have for future plans for for this? Yeah. So, I I mean, there were two reasons to create Bitcoin safe. First is to make multisig easier, right? Self sovereign multisig, I have that. The second one is to include compact block filters. Okay. 

Right now, most, almost all Bitcoin wallets use Electrum servers. Also, also Bitcoin safe right now uses Electrum servers to get the blockchain information. Okay. Why? Well, it is it is fast. It is like really fast because you're asking a server for the information. Mhmm. And this is, however, it it basically, you have to trust the server. And, I'm using Blockstream. I mean, I I trust Blockstream, but still this is not a great long term thing to be able to to have to trust the server. Okay. And there is a technology out there called Compact Block Filters. Mhmm. And that works the following way. 

You connect directly to Bitcoin core notes out there, just like a Bitcoin note. And the Bitcoin core notes will send you a summary of the blocks. For each block, you get, like, a summary and that's called a compact block filter. Mhmm. And the summary is very small, but it has enough information to tell you if there's a transaction in the block that you might be interested in. And if you're interested in the block, then you will request the entire block from the Bitcoin quarter. And then, yeah, then you'll get all of the information that is necessary because you download the entire block. But since there are lots of transaction blocks, something like 2,000, you have a good anonymity set. Okay. Okay. So 

[00:24:17] McIntosh:

to a tiny extent, you're kind of compromising your anonymity, but it's a lot better than if you're just looking at the full blocks. Is that correct? 



[00:24:27] Andreas:

No. You are looking at the full blocks. Okay. Then I'm not understanding. 

[00:24:31] McIntosh:

Sorry. 

[00:24:33] Andreas:

Okay. Okay. So maybe, maybe we back up a second and how does Electrum servers work? Right. So, basically, the the wallets tells the Electrum server, these are my addresses. Please give me all transactions for these addresses. Okay. And that is not good for privacy because you are basically telling the server what your wallet is, right? All wallets do that because it's fast. And because certain servers are trustworthy. That's also the reason, right? You shouldn't connect to like random servers out there. That's not a good idea. Right. 

But even if you trust the server, it's not a good long term decentralization point. Okay. And compact block filters is a way to get the necessary data from all the Bitcoin core nodes out there. So, you don't need a server, you just connect to the Bitcoin core nodes just like a Bitcoin folder. Right. Right? And to make it fast, you're not downloading all the blocks. You're first downloading a summary of all the blocks and that's that's a compact box filter. And this summary then tells you if there's something interesting in a block. And if there's something interesting for your wallet in the block, you download the entire block. And that way, you get very good anonymity and all the information necessary. 

And it's I mean, it's not as fast as Electrum Servers, of course, but it is much, much faster than, syncing your own full node. Okay. And, this was or is being developed and was developed by a developer, with BDK. So this is now out there, and I will integrate this as soon as I can. Okay. Very cool. 

[00:26:32] McIntosh:

Alright. I to be honest, I think I'm following about 90% of that. So, that makes a lot of sense. So we're talking it's not a brand new technology. It's been around since 2018. But Right. Yep. Now integrated. It it's got core support, and this can be utilized. It's just not widely utilized at this point, it looks like. Correct. And I want to change that. Yeah. Well, good. Good. That's terrific. And so that'll be coming down the road. 

And then do do do. Oh, the multisig. Going back to the multisig for just a second. I know you said and I'm not trying to pin you down. Please. Don't. But with multisig, one idea with multisig is you might have a signer that's mobile. Now understanding that you could that could be compromised, etcetera, etcetera. Is that something that you're thinking about? Are you gonna stick to the desktop type? 

[00:27:40] Andreas:

I'm going to stick, to desktop with Bitcoin safe. But I think, as you said, like, having one signer on a mobile phone makes a lot of sense, I think. But the signer on the mobile phone can be any Bitcoin. Oh, okay. It does not have to be. That's true. Sure. 

Just like it would the mobile phone would act like a signer, like any any hardware signer out there. And, yeah. So this is this is really good. One one other thing I, have already in Bitcoin safe is synchronization. So if you have multiple computers and if you want to keep your labels synchronized between the computers, I support synchronization via Nostr, in Bitcoin safe. Okay. 

[00:28:28] McIntosh:

That's interesting. Well, I no. I I'm serious. It is interesting. I'd let's I wanna go down that that trail for just a minute. Yeah. Sure. I think most of our user our listeners will be familiar with Nostra, at least to the extent that they know what we mean by that, but that is not a normal way of doing this. 

So, you know, let's expand on that for just a second. 

[00:28:55] Andreas:

Right. I mean, most know maybe, Nostra is like a like a Twitter alternative, but decentralized. Mhmm. But Nostra also supports encrypted messages. And, you can use these encrypted messages to to send anything you want, if the size is not too large. And, I wrote so I have a, like, a protocol. I wrote a protocol on how to exchange Bitcoin related data over over encrypted messages on Master. And with that, you can send labels, but you can also send PSBTs. So between 

[00:29:39] Speaker 2:

two or or multiple instances of Bitcoin safe, 

[00:29:43] Andreas:

you can synchronize the labels 

[00:29:46] McIntosh:

and send PSBTs around. Okay. Can you explain briefly what a p a PSBT is? Sure. 



[00:29:53] Andreas:

Sure. So, a Bitcoin transaction, when you create it, you first create something that's called a PSBT. It has, at first, no signatures. And then you take this PSBT. Typically, it's, you can see the QR code. You're welcome. Or you send this PSBT via USB cable to your hardware signer. And then your hardware signer takes that, looks at it and puts its signature in certain places in this PSPT. And if it's a single SICK, then you're done already and you have your transaction afterwards that you can broadcast to the Bitcoin network. But if it's a multisig, you need more than one more than one signature and you then need to take this PSBT structure again to another hardware signer, sign it until you have enough signatures collected. 



[00:30:43] McIntosh:

Okay. Right. And that depends on how many you have in your multisig setup. So very cool. Alright. That's a great explanation. Thank you. Alright. Now where were we? So that's what you're sending over the, the network, essentially. 

[00:31:02] Andreas:

Right. I mean right. No. The first thing the one thing is is labels, but I can also send PSP team over Nasr. And then, maybe you see where I'm going with that. You if you have the same wallets, a multisignature wallet on different computers, the the hardware wallet could be with the first computer. You give the first signature, then you send the PSPT via Noster to the second computer. And on the second computer, there's the second hardware signer. You give a second signature. 

And what you have done now is sign a Bitcoin a multisig Bitcoin transaction Right. Distributively or remotely. So and and that is, something where for for multi party, multi sick, 

[00:31:44] McIntosh:

this is very interesting. Yes. That is that is very interesting. So since we're already talking about Noster, Noster is actually how I know about you. Are you a Noster only person? Are you are you on Twitter or something? No. Not not Nostra only, but, I I prefer Nostra. Okay. And so if you guys are on Nostra, you can certainly follow him there. And and Nostra doesn't have a great way to, like, distribute your name. How can they find you on Nostra? Just look for, BitcoinSafe. 

All. Okay. I think I've I'm almost sure I follow you, so they can certainly look, you up through me as well. Yeah. But yeah. Are you on Twitter as well? We we we don't ban the t word around here. It's okay. Do you have a Twitter handle? You wanna go ahead and 

[00:32:38] Andreas:

I have a Twitter handle. It's it's bitcoinsafeorg 

[00:32:42] McIntosh:

altogether without Without any dots or anything. Okay. So so bitcoinsafeorg on Twitter. Find him on Noster. The website is bitcoin-safe.org. I would highly encourage you to go take a look at this. You have a a great website here. And I'm serious. The multisig tutorial, whatever you wanna call it, that you have that walks you through that and then your export sheets, your PDF sheets that you have at the end. That is that is terrific work. 

That is really world class stuff that I've not seen anywhere else. So you are to be commended for that. I appreciate that. And do you have anything else you wanna leave with the listeners? 

[00:33:28] Andreas:

Learn about Bitcoin. Learn about self custody. And as you said, like, think of it as, like, 10 times worth more than it is now. Because you will wake up very soon one day, ladies and gentlemen, and it will be. So 

[00:33:41] McIntosh:

that is something that you do need to think about. Alright. I really appreciate you coming on the show, Andreas. It's been terrific. 

I hope this has given you all a good overview of Bitcoin safe. I would highly encourage you to take a look at it. If you can support it with languages, with code, whatever, just word-of-mouth. I'm sure Andreas would appreciate that. And, thanks for coming on the show. 

[00:34:11] Andreas:

Yeah. Thank you so much for having me. 

[00:34:14] McIntosh:

Alright. Thanks again, Andreas. That was a great, great interview. We're gonna wrap things up. I wanna give a brief overview. We don't have any software updates as we record tonight at the block height that I said earlier, which I don't know offhand. It was $9.09, 907,193. 

We do have a Bitcoin price of 117,600 US dollars and then €100,127. Compared to last July 25, it was $67,912 last, July, and we are up 73.1%. So, still a nice healthy increase. Of course, it's down a little bit from last week, and that's okay because the Bitcoin price is holding strong. And that right now is what matters. So, we'll move on. Out of the global market cap, Bitcoin, 2,300,000,000,000.0, gold to 23,200,000,000,000.0. And that actually means we're up this week 10.1%. Last week, it was 9.2%. So we're up there in terms of gold. And then the mempool looking nice and healthy, one sat per vbyte transaction fees, A 119 megabytes of unprocessed transactions in mempool dot space, which is roughly 64,000 transactions. 

Alright. Satoshi's Plebs podcast is a value for value podcast supporting podcast in two point o. No ads, no sponsorships, just honest Bitcoin content. I deliberately avoid sponsors because even if I love a company, taking their money would influence my opinion. What if something goes wrong with that company? I would hesitate to warn you. Instead, I ask, are you getting value from this show? Support it through time, talent, or treasure, help with the chapters transcripts or future projects like our chat room, stream sats, boost with messages, even a 100 sats saying great show or you suck. I read it either way. By the way, this week, I started working on moving our website, which we actually get a fair amount of traffic on, from a WordPress system, to, really what's a static website called Hugo. 

And, so that is moving along. But if somebody's just looking for a way to help out, there's gonna be a lot of content. I mean, we have hundreds of pages because of all the episodes that we've put out, and it would be great if somebody would volunteer to go through some of that and kind of fix things up. I could help you with that. And, actually, all of our content will be put up into a GitHub. And so, basically, you can look at it online and then make a merge request, and we get it merged in, and that fixes it up. It'd be terrific. Check out the apps at podcastapps.com and support independent Bitcoin media. If you like the content, I would love it. If you would tell your friends about the podcast, that is the best way to help us grow. Again, this week, probably for the last time, we've got Cherry on Top by Ainsley Costello. 

Any boost or streaming us sats during that song will go straight to the artist. Thanks for being here. We hope this has been helpful, and we would love to hear from you. Find all of our contact info at satoshis dash plebs dot com slash episode dash two one nine. Stay humble. DCA those sats. Have a great weekend, and we'll talk to you all soon. 
