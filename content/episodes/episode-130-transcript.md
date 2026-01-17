---
title: "Episode 130 Transcript"
draft: false
_build:
  list: never
  render: always
---
```text
McIntosh:00:00:00Hey, Sats Stackers. Today is September 18th, and this is episode 130 of generation Bitcoin. I'm your host McIntosh. And today's episode is another Bitcoin basics nodes on the network.

00:00:41Alright. Let's get into it.

00:00:44Got a lot to cover, and I wanna make it as short as possible for your listening pleasure.

00:00:51We'll cover the market. We had a Bitcoin

00:00:55weekly close. Well, let's see. What do we got? 2 and a half hours ago at time of recording. That was at 26,500

00:01:04and 63.

00:01:06We had a block type at time of recording, as in right now,

00:01:12of

00:01:14808,219.

00:01:19Alright. We have an estimated difficulty adjustment of plus 5.17%

00:01:24happening on September 20th. So that's just a couple days from now. Unfortunately,

00:01:29it looks like things have been progressing along a little too fast,

00:01:34like, 9 and a half

00:01:36minutes on average since the last difficulty adjustment, hence

00:01:40the pretty steep increase.

00:01:43But interestingly,

00:01:46recently,

00:01:46it actually seems to have slowed down. I saw earlier man, there was one that took almost an, like, an hour.

00:01:53It's really weird.

00:01:54Right now, we got an average transaction

00:01:58fee of, 20 sats per a v byte, which is a little high, a little high. Of course, mempool is up to

00:02:061.25

00:02:06gigabytes. Man, it's getting

00:02:08getting big with 565,000

00:02:11unconfirmed

00:02:12transactions.

00:02:13So

00:02:14things are stacked and racked and ready to be packed up into those blocks.

00:02:19We're actually gonna be discussing that a little bit tonight, kind of the flow of that as part of our discussion. So maybe you'll have a little better understanding of that if you don't know what I mean

00:02:29when I'm talking about that.

00:02:34Alright. I'm not really gonna go over market update. Hey. It's the same.

00:02:38Like I said, well,

00:02:40we're actually up a little bit, 26.7

00:02:42right now,

00:02:44even since our close. So

00:02:46we did close the week, of course, over that 26,300

00:02:50to 300 level.

00:02:52So

00:02:53I don't know. We'll see. Again,

00:02:56I'm not convinced until we break well above 30,000,

00:03:00on consistent basis,

00:03:03you know, for multiple days slash really weeks.

00:03:06We're in a we're in a crab market. We're we're going sideways. I wouldn't say we're in a bear market because we're not continuing to go down. We keep going down and

00:03:16pulling right back up.

00:03:18And since, what, early early this year,

00:03:22we've not been down below,

00:03:25just a few $1,000

00:03:26below where we're at right now. So I would call it a crab market.

00:03:30That's what we got. So, of course, what's our strategy?

00:03:34Every week we talk about this. I don't care what the price is. You should be DCA ing. Right? I was having a discussion with a friend of mine

00:03:42who is frankly showing some interest in Bitcoin,

00:03:46and I don't think he realized

00:03:48how involved I was. So

Unknown:00:03:50we were we were driving somewhere. We were actually having a discussion about

McIntosh:00:03:55just kind of the world in general.

00:03:57And he does know I'm involved in Bitcoin, but he turns to me and he's like, well, you should run some miners. And I'm like, well, I already do.

00:04:06But, anyways, we had a great discussion

Unknown:00:04:10a great discussion, but, you know, you don't have to guess at this. You don't have to worry about if it's up, if it's down.

McIntosh:00:04:16Just like I told him, just DCA.

00:04:19Get the strike app. I think cash app does the same thing. Whatever.

00:04:24Buy Bitcoin on a daily basis. When you get any kind of amount,

00:04:29you know, a couple $100,

00:04:31move it off to cold storage.

00:04:33That should be your next step. What do I do? Why buy Bitcoin? What do I do next? I set up cold storage seed signer or ledger,

00:04:42I guess, or something like that. A hardware wallet

00:04:46and then,

00:04:48start saving. That's what you do. Right? We don't trade. We don't do any of that. Just just save.

00:04:56Save and come back to me in 8 years, 10 years.

00:04:59That'd be 2 complete cycles.

00:05:02You will be happy you did. Let's jump on into our topic.

00:05:06We're gonna cover

00:05:08a good bit of ground today, but it all ties in together and I think it's all very important.

00:05:13It's actually in the end, I was actually just going to talk about Bitcoin nodes,

00:05:19the kind that

00:05:21are not miners that just run the Bitcoin software.

00:05:25And I actually ended up tying in the whole thing together because it really makes sense. So we are going to talk about Bitcoin nodes

00:05:32in general,

00:05:33and there are multiple different kinds. We'll talk about that. It will give you a good understanding, I think, of how the Bitcoin network itself

00:05:42actually works.

00:05:44So that you,

00:05:46have some understanding

00:05:47of how

00:05:49transactions work, how, you know, your

00:05:52Bitcoin gets to someone else or how

00:05:55transactions are verified, all of this kind of stuff. So we'll we'll jump right in there

00:06:00and we'll cover all that.

00:06:02So Bitcoin nodes in general are the underlying infrastructure of the Bitcoin

00:06:06network. They secure it.

00:06:08They maintain it.

00:06:10It is because of Bitcoin nodes

00:06:13that the network is even possible. Without them, there would be no Bitcoin network.

00:06:19Unfortunately,

00:06:21a lot of people don't really understand

00:06:23what they are and how they work.

00:06:26So we're going to talk about that. Before we do, I want to cover some topics.

00:06:31There's 3 different ways of looking at bitcoin. There's 3 different

00:06:34things that Bitcoin can refer to. Bitcoin is a network. It's a collection of these nodes. We're gonna talk about the nodes more specifically

00:06:42very shortly. But it's a collection

00:06:44of computers

00:06:45that are tied together essentially communicating

00:06:48with each other,

00:06:50sharing information back and forth. That is the Bitcoin network.

00:06:53Bitcoin is a protocol.

00:06:55Bitcoin is a set of rules. That's what the protocol means. That's what it defines.

00:07:01A set of rules for how that information

00:07:04can be shared back and forth.

Unknown:00:07:07Those rules

McIntosh:00:07:09keep things from like double spending occurring for example. Bitcoin is also,

00:07:15some software. It's a program. You'll often hear Bitcoin Core, which is one of the most common versions of this Bitcoin software. It's a program that understands these protocol rules. It's been programmed

00:07:28to understand these protocol rules. It's run by computers on the network,

00:07:33and

00:07:34it drives that network really. The Bitcoin nodes, they're computers that they run that software, that Bitcoin software and there are different versions of that. I don't wanna get hung up on that but it's not just

00:07:46the core Bitcoin software. Although that is certainly the most common,

00:07:51and they're connected by

00:07:53this Bitcoin network. They validate. They broadcast.

00:07:57They process and they store Bitcoin transactions.

00:08:01Alice wants to send Bob

00:08:031 bitcoin.

00:08:05I don't know. For whatever reason,

00:08:07that's a transaction.

00:08:10They're batched up. They're stored in a group. This is for an efficiency

00:08:15thing, right? That group, that's actually a block. So when somebody says, here's a block

00:08:21of Bitcoin.

00:08:22What they mean is, this is a block

00:08:25of transactions, of Bitcoin transactions.

00:08:28And actually,

00:08:29this is actually where blockchain comes from. When when this term

00:08:35was created,

00:08:36it was referring to Bitcoin and it was talking about these blocks

00:08:43of transactions.

00:08:44And part of those blocks is basically information

00:08:49that points

00:08:50back to the block.

00:08:53Previous block, if I'm not mistaken. It gives a historical context into it. It creates that chain.

00:09:01It gives the Bitcoin

Unknown:00:09:03core pro and I'm gonna again, I don't wanna get bogged down on this. It's not just a Bitcoin core software, but it's just habit. So it gives us Bitcoin core,

00:09:13the ability to traverse that

00:09:16chain of transactions.

00:09:18So

00:09:19before a new block gets added to that blockchain,

00:09:22those

McIntosh:00:09:24transactions have to be verified as valid. So that is the function

00:09:29of some of these Bitcoin nodes.

00:09:31These nodes on the network. Not all of them, and we're gonna break that down in a few minutes. But when somebody says,

00:09:37I

00:09:38run a Bitcoin node, this is what they mean. This is a node that runs the Bitcoin core software or some other version of that software,

00:09:47of the Bitcoin protocol

00:09:50software.

00:09:51And

00:09:52that's what it does. It sits there and it verifies transactions. So these are a very important part of the network.

00:10:00What are they verifying? They're doing things like checking to see that

00:10:05the double spending issue that I was talking about, whether you

00:10:08have spent that Bitcoin twice or whether a sender

00:10:12actually has the Bitcoin that's being sent. All of these different rules that have been created over the last, what, 14 years in order to ensure

00:10:22the correctness of the blockchain.

00:10:26They're programmed into Bitcoin core

00:10:28And therefore, they're running on those Bitcoin nodes

00:10:31and they're verifying

00:10:34the

00:10:35transactions

Unknown:00:10:36that are flowing through it. When you have a bunch of servers, a bunch of bitcoin nodes that agree on a transaction, they are reaching what's called consensus. Consensus meaning they agree on it. They they say, yes. This is good. Nobody's saying it's a bad block.

00:10:55Okay?

00:10:56So that's what they do. 247.

00:10:59Every

00:11:00minute of the day.

00:11:03Nodes do not

McIntosh:00:11:06assume that a block is valid. Nodes do the work.

00:11:12We love in Bitcoin to say proof of work. This is proof of work.

00:11:16We

Unknown:00:11:17do the work

00:11:19to verify that those transactions are valid.

00:11:23To to do this,

00:11:26the Bitcoin nodes,

00:11:28they have to be able to run,

McIntosh:00:11:31they have to be able to have access to a full copy of the Bitcoin blockchain.

00:11:37So when you bring up a new node, and I've done this, I have 2 nodes running right now.

00:11:43And when you do this, the first thing it does, you set up the Bitcoin software, you connect it to the network. So if you establish connectivity to other nodes

00:11:52peers,

00:11:56then it

00:11:57downloads

00:11:58literally

00:11:59like the original data, the Genesis block, and it starts building

00:12:04the blockchain

00:12:05from there. And it runs through

00:12:07the whole thing. And you can watch it in the log file. It's amazing. It starts from

00:12:13gracious alive. Whenever it was that it came online.

00:12:17January of 2,009,

00:12:19if I'm not mistaken,

00:12:21all the way up to the present time.

00:12:24It literally does the work to verify that entire thing.

00:12:30When it's done, it has a copy of the Bitcoin

00:12:34blockchain.

00:12:35That takes up a fair amount of space. I believe it's around 600 gigs right now.

00:12:40So that has become a little bit problematic. We're gonna set that aside for now, but we're actually gonna come back to that because

00:12:47600 gigs is a is a

00:12:49pretty good amount,

00:12:50and

00:12:51that can be,

00:12:53there's ways around that. So we'll talk about that in a few minutes. But right now, I just wanna kinda set that aside.

00:12:59Each node though has a full blockchain

00:13:02or they've run through all that work. Let's just say it that way,

Unknown:00:13:06To crit to authenticate that blockchain.

McIntosh:00:13:10Alright. Now, when a new block gets sent out, each node has to decide whether they're going to add a copy of that block to their blockchain.

00:13:19They are not

00:13:20trusting this is why we say trustless. They are not trusting

00:13:25anyone. They are verifying

00:13:27everything. And this is very important. It is part of the

00:13:32foundational principles of Bitcoin.

00:13:35So do not gloss over that.

00:13:37We do not trust. We verify.

00:13:39Right? Let's break this down a little bit.

00:13:42So what I have been describing is what is called a full node.

00:13:46Now I glossed over some details in there and we're gonna come back to that in a minute. But before we do,

00:13:54we're going to talk about miners because miners are nodes. The miners that I have

00:14:00sit there, they are nodes on the Bitcoin network. They are essentially separate

00:14:04from a core,

00:14:06Bitcoin

00:14:07node. They don't run the same software, in fact, that they used to,

00:14:12actually.

00:14:13From my understanding in the very early days, that's what they did. But as mining has gotten more sophisticated,

00:14:21they have evolved. They run

00:14:23different software

00:14:26that it implements the same protocol.

00:14:29Remember, we got Bitcoin protocol,

00:14:32but they do not use the same software because

00:14:35they do different things.

00:14:37Going back to your full node, transaction is valid.

00:14:41Once it authenticates that a transaction is valid,

00:14:44that actually gets sent out to the the peers and those that are connected to it. Those nodes also verify

00:14:51it once

00:14:53a,

00:14:54sufficient number of nodes have verified, and I don't know what that number is, but once a sufficient number of nodes have agreed that this transaction is valid, it's then added to a pool of other valid transactions. And that's kind of where the miners pick up,

00:15:11just to wrap that up. Now, mining nodes, they pick up those transactions.

00:15:15They package them actually into blocks.

00:15:19Miners run

00:15:21a

Unknown:00:15:23set of rules

00:15:25protocol, if you wanna call it that,

00:15:27for creating and proposing

00:15:29blocks to the Bitcoin network.

00:15:32So miners can create and propose blocks.

McIntosh:00:15:36These core Bitcoin nodes on the other hand, they verify blocks.

00:15:40There's

00:15:41they they balance each other.

00:15:44See, a miner can create a block, they can inject things in it and it may break the rules of Bitcoin. See, they can

00:15:52compromise the system if you wanna think of it that way, which is kind of what is that's actually a valid way of looking at it.

Unknown:00:15:59But

McIntosh:00:16:01core nodes, these Bitcoin nodes, people call them Bitcoin nodes. There's probably a better way of saying it. These bitcoin nodes on the other hand, they validate

00:16:10the transaction. So if they catch a miner

Unknown:00:16:13creating an illegal

00:16:14transaction,

McIntosh:00:16:16they throw out the transaction.

00:16:18They won't

00:16:19verify it. So they balance each other and I think that's very important.

00:16:24No one in Bitcoin should trust anyone else. Again, trustless.

00:16:29I may know you, you may know me, but we don't really know each other, do we? You're listening to me on a podcast ramble on for a 130 episodes now. You may think you know a lot about me,

00:16:42but you really don't.

00:16:44And it's always best

00:16:46to verify

00:16:48what you can, especially when it comes to something that's this important.

00:16:53So

00:16:54miners,

00:16:56like I said, they have a set of rules for creating and proposing blocks.

00:17:01The type thing we're talking about is how big those blocks can be.

00:17:05Alright. I'll have the block,

00:17:07block size wars that happened, what, in 2017.

00:17:10How you can format a transaction

00:17:13and how to sign a block. How to put your stamp on it and say, yep, this block is good.

00:17:19Miners are also competing

00:17:21against each other in a race to create the next block.

00:17:25Once a miner thinks it created a valid block, it's going to broadcast

00:17:31that valid proposed block, I should say,

00:17:34out to other nodes on the network for them

00:17:37to put their stamp on it and say, yes, this is a good block.

00:17:41So

00:17:42that block

00:17:43is broadcast out to those Bitcoin nodes, those full nodes,

00:17:48and they're gonna validate

00:17:50the block. So they validate transactions

00:17:53and they validate the block itself.

00:17:55If a full node considers that block to be valid, it then adds the block to its copy of the blockchain.

00:18:02It broadcasts it to

00:18:04other full nodes and they go through that same verification

00:18:08process.

00:18:10Once you have a sufficient number of those, and again, I don't know what that number is, but it's just like the transactions.

00:18:18Consensus is considered to be reached

00:18:20and the transactions

00:18:22are processed.

00:18:24There,

00:18:25the nodes verify and store the updated versions

Unknown:00:18:28and,

00:18:30of the blockchain.

McIntosh:00:18:31And the miners, you know, of course have moved on to creating that next block.

00:18:36Again, I wanna draw attention, which I already did, but I wanna draw attention to the fact that essentially

00:18:42miners and full nodes, they're not competing with each other. I wouldn't call it that, but they do have different jobs. Miners

00:18:50are trying to create valid blocks

00:18:52as fast as possible. That's how they get their money.

00:18:56This block reward

00:18:59is the Bitcoin that is pre programmed, so right now 6.25

00:19:04Bitcoin per block, plus the transaction fees on top of that.

00:19:08So they are incentivized

00:19:10to work as fast as they can.

00:19:13That is why you see things like miners who tune their software

00:19:17to

00:19:18over,

00:19:19overclock their ASICs

00:19:22for example.

00:19:23So the miners are proposing

00:19:26blocks to the Bitcoin network.

00:19:28Full nodes are not proposing blocks. They cannot do that, obviously. If they did, then they could earn those rewards.

00:19:34Miners can receive block rewards,

00:19:37of course

00:19:39for doing that, full notes cannot.

00:19:42There is a difference. Essentially,

00:19:47maybe this sounds bad but there's well, it's the truth. There's no direct financial incentive

00:19:53for running a full node. However, full nodes are required to run the Bitcoin network. So why would people run those? Why do I run 2 of those? That's probably costing me 10, $20 a month

00:20:06to do that in terms of computing resources.

00:20:10Well, because it helps power the Bitcoin network. Because I think that the Bitcoin network is important enough to throw my hat in the ring,

00:20:19and it's reasonable

00:20:20what these things take, but it's still a computing cost.

00:20:24And so I do that as to help support that network. That's why people do it. There's other reasons on top of that. You can use that to verify the chain data.

00:20:34I don't know. There's probably more reasons than that,

00:20:38but that's certainly a good place to start.

00:20:41I I wanna break down a full node because there's actually 2 kinds of full nodes.

00:20:46And it's a

00:20:47semi important distinction to make before we go on because there's some other stuff too that will other types of notes. But I this is probably a good place

00:20:56to,

00:20:58to talk about. There's 2 types of full nodes. There's called archive nodes.

00:21:03Archive nodes,

00:21:06they have a full and complete copy of the Blockchain. Every transaction, they can verify

00:21:11everything.

00:21:12So

00:21:13aside from the archive nodes, there's another type of full node. They're called,

00:21:18ironically I think, pruned nodes. So full

00:21:22is like the opposite of pruned to me. So pruned nodes

00:21:27don't actually store the full blockchain.

00:21:31They store a subset of it.

00:21:33So let's say you let's say that the current

00:21:36transaction space takes up like 600 gigs. It's something like that.

00:21:41Maybe I only have a 100 gigs that I can spare for that. Maybe I only have 50 gigs. Maybe I only have 5 gigs. I think one of my nodes is actually running on 5. I think the other one, I think I do like probably 50 or something.

00:21:54But both of mine are actually pruned. It does start from the start. It does

00:21:59verify everything

00:22:01all the way up to current day. But essentially,

00:22:04going out the tail, so to speak, it's dropping off blocks.

00:22:08So it doesn't keep that data after it verifies it within that window. So if I've got a 100 gigs, that's probably more than a year's worth of data at this point still.

00:22:21So maybe that goes back to

00:22:23July or June of 2022.

00:22:27If I've only got 5 gig, that may only be a month or so.

00:22:30But I've got all the current data for that month plus I've

00:22:35verified everything up to that point. So it still goes through that proof of work to verify everything and that but it just kinda discards what it it it doesn't keep

00:22:45because of space issues. Okay. So why they're called

00:22:50full nodes, I I don't know. They are considered the equivalent in terms of running

00:22:55the Bitcoin network, however.

00:22:57The Earl Grey, it was extremely hot when I started. It's already cooling off. Of course, I'm 20 minutes into this, so I would ex I'm 27.

00:23:06Good gracious, alive, Macintosh.

Unknown:00:23:09But I am approaching the end, so we're gonna wrap this up.

McIntosh:00:23:12Again, 2 types of full nodes. I'm not gonna get super in detail on that.

00:23:18They are considered equivalent in terms of running nodes on the network.

00:23:22Now, other times types of nodes. Actually, when you run a miner nodes

00:23:27and you participate in a mining pool, which I've talked about. Most people do participate in mining pools simply because they don't have enough power.

00:23:34They would be like solo mining is what they call it, and the chances of them actually mining a block would be very, very little

00:23:41simply because the network has essentially gotten so big at this point.

00:23:45I would say the vast majority of people out there are using mining pools. Mining pools,

00:23:51actually

00:23:52use a

00:23:57a mining pool. They call it a mining pool node or I think I've called it I heard a couple of different things. That orchestrates

00:24:03the group of miners in that pool and they probably can have multiple because pools can have thousands of servers. People used to say, well, all mining nodes were full nodes. That's not really true anymore.

00:24:15The miner nodes have become so specialized.

00:24:17But the pool node, I believe, either has a full

00:24:21set or it has access

00:24:24to a full node that has that blockchain for verification.

00:24:28But they're used to kind of coordinate that mining pool. So they're a semi specialized type of node in the network, but they're a node. They're a Bitcoin node and it's important to know about them. So anyways,

00:24:40there are a couple more here.

00:24:43We'll go back. There's a light node

00:24:46which isn't a full node. So it's it's a very lightweight version of the blockchain.

00:24:51Essentially, you would see something on it like this for maybe a mobile wallet, this kind of thing, where they only keep the headers of the blocks,

00:24:58and they don't keep the full blocks.

00:25:01But it means that you can do it on a very very small kind of lightweight machine.

00:25:06And then you you can send or receive bitcoin

00:25:10like, from your phone.

00:25:12And you're technically running a node on the network and you are. But you cannot use that node, it's important to note this,

00:25:19to validate transactions.

00:25:21So it depends on those full nodes to do that. So again, we go back to those full nodes which are either archival or

00:25:29the pruned nodes, in order to,

00:25:34to validate those transactions. Alright. Lightning nodes. Lightning nodes are part of the lightning network,

00:25:40but they do interact

00:25:43with the Bitcoin main net. The this this layer, these all these other nodes that we're talking about. So,

00:25:50they speak the same protocol,

00:25:52they, you know, they can interface and they provide that way

00:25:57that the lightning nodes, you know, can

00:26:01provide this

00:26:03basically instantaneous

00:26:05transactions across the internet.

00:26:08So those are actually a type of bitcoin node.

00:26:10And I think that's it. That is actually it. Okay. So there we go.

00:26:15I'm not sure that liquid has nodes. I do not know if they do or not. They may have something similar to lightning. So I'll go ahead and add them to the list, not even knowing that, which is a huge mistake.

00:26:27But liquid is not something we've really talked about a whole lot, but it's somewhat similar to lightning. So I hope that helps you understand

00:26:35how transactions

00:26:37flow through the system. I'll try and come up with a diagram

00:26:40and maybe post it on Twitter,

00:26:42that would might be helpful. Because

Unknown:00:26:45this whole transaction thing, I mean, it is a little complicated but I do think it's worth

00:26:51understanding.

00:26:52Alright. So for our supporters this week

McIntosh:00:26:56actually, before I jump into that, let me do this.

00:27:00I did have a clip made.

00:27:03I was hoping for more. I'll be perfectly honest. So Kyron over at Mare Mortals

00:27:08did make a clip

00:27:11of me actually talking about this clip program.

00:27:14And I

00:27:16replied to that or boosted that. It's not really a boost, but I replied to that. Gave him 500 sats. I tried to send a message, but frankly,

00:27:24fountain did not allow me to do that. I'm not sure why. But

00:27:28the message simply was, thanks. I appreciate that. And he should have gotten that 500 sets. Kyron, if you did not, please let me know.

00:27:36I'm quite sure that you did, but since this is the first time we've really done this, I would like to not trust but verify.

00:27:44Little joke there.

00:27:46And,

00:27:47and we'll, you know, I'll make sure that that's taken care of. So again, I would encourage you.

00:27:53For those of you who didn't hear last week,

00:27:56if you go out and make a clip of any part of the current episode,

Unknown:00:28:00500 sats,

McIntosh:00:28:01I reply to your thing or

00:28:04well, yeah. I reply to it, and I boost you essentially 500

00:28:09If you do that for an older show so

00:28:11this would be for episode 130. If you went back to 129 or 128 or 127

00:28:17or that great

00:28:19126 seed signer episode,

00:28:21there's lots of stuff I think in there that could be

00:28:24clipped up

00:28:25and make a clip. I'll give you 300 and you can do multiple. I'm trying to spend money here to spread the word

00:28:32about

00:28:33generation bitcoin,

00:28:34because we've got lots of good things going on here. I'm fixing to tell you about a couple of more interviews we got coming up that I'm super pumped about.

00:28:42We'll go ahead and do that news and notes section

00:28:44after our supporters. We did have support this week. Of course, this is kind of the short half of the week, so to speak.

00:28:51Typically, not as much, and our total support this week was a 1,000,

00:28:55for this section of the week was a 1,081

00:28:58sats. So probably right at 1100 sats. There was some streaming going on,

00:29:03which I certainly appreciate. We had Berno who sent in a boost.

00:29:08Our friend, Berno, we hear from him

00:29:10a a good bit. Thank you, Berno, your faithful supporter of this show.

00:29:14And he or she, I do not know, but I don't wanna presume. Always a pleasure to be in your company.

00:29:20Thank you very much.

00:29:22That's awesome. So I appreciate that, and I appreciate the sats.

00:29:27So from there, let's dive on into our news and

00:29:31wrap this puppy up because I do not wanna keep this long.

00:29:36We will have longer shows, it looks like, with our interviews. I've got 2 more of those lined up at this point. I think it's confident I'm safe to say this. I do have someone who lives in El Salvador. They're a I believe they're a software engineer down there, a professional,

00:29:52probably lives in Buenos Aires from what I'm I think I'm seeing,

00:29:57and I'm hoping we're gonna have a good discussion. Their hyperinflation

00:30:01is off the chain. I saw a figure

00:30:03125%

00:30:05today.

00:30:06Of course, they've got the election coming up in October,

00:30:09which I've discussed off and on a good bit. I wanna talk to them about that. I wanna talk to them about how they are coping with these

00:30:19hyperinflation

00:30:20well, I consider it hyperinflation.

00:30:22Extreme inflation,

00:30:24hyperinflation

00:30:25is what? It's 50 no. It's I guess it's really not hyperinflation.

00:30:29I don't wanna be spreading rumors so careful what you're saying, Macintosh.

00:30:33This extreme inflation,

00:30:35you know, how are they dealing with that? And, of course, they're involved with Bitcoin as well, so we'll talk about that.

00:30:41Earlier today, I got some news. I got a message back.

00:30:46I have asked,

00:30:48Eric at Gridless

00:30:50over in Africa

00:30:52to come on the show, And he has graciously agreed to that. Now I'm gonna hold him to that. So, Eric,

00:30:57if

00:30:58don't back out on me.

00:31:01But

00:31:02I this is one of the people I've been wanting to talk to.

Unknown:00:31:05And I'm very appreciative that he is

McIntosh:00:31:08going to make the time to do that.

00:31:10Next week, he is actually going to be at the African Bitcoin Mining Conference. So there'll be a link to that in the show notes.

00:31:17It's basically a get together of of African Bitcoin miners

00:31:21and their circumstances, which are different frankly than the circumstances here in the United States.

00:31:28Probably, we'll do the Argentinian

00:31:30episode,

00:31:32next Sunday, So one week or next Monday. And then Eric's the following Monday.

00:31:38And that's kind of the schedule I wanna keep. I may not do an interview. Obviously, we're not doing an this week, but we'll do those interviews on Monday. We'll do my kind of weekly wrap up on Thursdays.

00:31:52Late Thursdays really is what it's turning into, to be honest, but Thursdays anyways.

00:31:57And

00:31:59and, yeah, that's kind of I think that's gonna work out real well. So,

00:32:03let's jump into the news. There was not, again, a whole lot.

00:32:07You can follow me on Twitter at Macintosh Fintech. I always post stuff on there. And I by the way,

00:32:13I I don't know that I've made this clear.

00:32:16I post a lot more than just what we talk about on here. So, you know, some of it's not really news. Some of it may be not noteworthy enough, but

00:32:25yeah. So I already mentioned Africa Bitcoin,

00:32:30mining summit that's being put on by the Green African Mining Alliance.

00:32:36So

00:32:37I wished I could go. I mean, honestly, maybe next year I can. I doubt it, to be honest, but maybe.

00:32:44That is a part of the world I would like to look at. I would like to see. I've never been there. And I believe that what these people are doing is very important, and I I don't know, maybe I can support them somehow.

00:32:56So I did wanna point that out. Congo,

00:32:59also in Africa, of course, is having a coup, it appears.

00:33:03I tried to look this up.

00:33:05They have a border with the Central African Republic, but I'm almost certain at this point

00:33:11that they are not part of the French,

00:33:14currency,

00:33:16scam, I would call it, the CFA.

00:33:19And, I think it's the Democratic Republic of Congo

00:33:22that was. So

00:33:25I'm gonna step out on a limb. I probably shouldn't say this. I do not think Congo and the Democratic Republic of Congo, like, split apart.

00:33:32So I don't think Congo has ever been part of that. I may be mistaken,

00:33:37But again, we see this FOMET, this,

Unknown:00:33:42Africa is, you know, for

McIntosh:00:33:44I don't know. There's stuff going on there. They've got a lot of issues. A lot of the countries have severe inflation.

00:33:51Things are just not good.

00:33:54And so we're seeing this kind of stuff happen. It was the military again.

00:33:58Actually, apparently, it was the presidential

00:34:00guard,

00:34:01interestingly enough. So that's all the details I know. I did think it was worth mentioning though.

00:34:07I hope in the long run that's a good thing. I'll try and bring you some more information about that maybe next week or maybe we can talk to Eric about that. I would think he might know something about that. Maybe he doesn't. I don't know. It's the entire other side of the continent. So

00:34:23he works, over in East Africa from what I from what I understand.

00:34:27Looks like some Bitcoin things are going on in Cuba, which I think is very interesting. So it's some good stuff there. Not a whole lot, but there was just a tweet about it.

00:34:37And,

00:34:38actually,

00:34:39as an add on to this note stuff, there's a very good article that I posted too.

00:34:45We may actually have some stuff so that we can essentially instantaneously

00:34:51have what amounts to a full note.

00:34:54So they're using what are called zero knowledge proofs. This is something I know about from my dirty

00:34:59altcoin past.

00:35:01So this was one of the some of the stuff that has been done on different altcoins. So I am a little familiar with this. I'm maybe even more than a little familiar with it.

00:35:12I'm not going to go into depth

00:35:14on this show about 0,

00:35:17knowledge proofs. I I just don't know that it's really appropriate.

00:35:22However,

00:35:23basically it's a way to do all the verification

00:35:26upfront

00:35:27and then

00:35:28you can prove

00:35:30that that verification

00:35:31was done and then you can kinda get rid of all that data and then just say, hey, we verified everything up through, you know, 2020

00:35:40and then start your

00:35:41bitcoin node there. So

00:35:45this article is a pretty good there's some people who are working on that and eventually,

00:35:49it may become kind of the standard way of doing this. So rather than a pruned node,

00:35:54you could run a 0 sync node,

00:35:57and

Unknown:00:35:58effectively have an instant on node

00:36:00that would come up immediately.

McIntosh:00:36:03I don't have any information about this, but I did see,

00:36:08Justin Trudeau

00:36:10up in Canada, our neighbors to the north. And let me tell you something. The Canadian people

00:36:15I don't know if I've said this before,

00:36:17but we spent some time up there this summer.

00:36:21Years ago, I spent some time in Ottawa in the capital. 6 weeks actually there

00:36:26with some work stuff.

00:36:28So

00:36:30my reflection

00:36:31on Canada in general is that the people are extremely polite.

00:36:37Now,

00:36:38your politicians

00:36:39who run your country, ladies and gentlemen,

00:36:42they're a hot mess. They're maybe worse than the United States which is

00:36:47saying a lot. And, of course, I live in the United States, so I can denigrate my own politicians all I want. And in fact, I did so this week on Twitter, if you wanna follow me there.

00:36:58Justin Trudeau basically got up and said and this I mean, I'm not making this up. It sounds like a joke.

00:37:04In this speech, he says,

00:37:07basically, we've got

00:37:09issues

00:37:10with high inflation

00:37:12for groceries, for food.

00:37:15So

00:37:16you, whatever the big grocery chains are up there, and I do not know that, but he was specifically

00:37:22talking about these large grocery chains.

00:37:26You are either gonna have to figure this out or we're going to tax you.

00:37:30The way that this works

00:37:32is

00:37:34the grocery I mean, this this is like 5th grade stuff, I would think.

Unknown:00:37:39Grocery stores buy the food stuff

00:37:41from their vendors

00:37:43who source it wherever they source it from.

00:37:46And

McIntosh:00:37:47then they mark it up a little bit and then they sell it to the public.

00:37:51That's what they do.

00:37:54And,

00:37:55traditionally,

00:37:56the margin in grocery business has been

00:37:59pretty thin.

00:38:02So what Justin Trudeau is saying, hey, you can figure out how to cut your cost,

00:38:07which they can't do because they're fixed cost, and what are you gonna do?

00:38:12Or we're gonna tax you.

00:38:15Because, you know, capital controls. Yeah. That always works out well.

00:38:20I don't you know, as these systems grind down to a halt,

00:38:27Keynesian economics

00:38:28fails,

00:38:30this stuff will become more and more prevalent.

00:38:34And the idiocy,

Unknown:00:38:37frankly,

00:38:38that it represents

00:38:40will become more and more obvious.

00:38:42So

00:38:44don't buy into this crap.

00:38:47That is someone who is either doesn't understand economics at all

00:38:52and how grocery stores work,

00:38:55or

00:38:56they're just being

McIntosh:00:38:58a power mad

00:38:59politician who thinks that that's gonna get them more votes. I will leave it up to the Canadian people to decide which one of those 2 are. As far as I can tell, they I think they're thinking he's a power mad

00:39:11politician, but

Unknown:00:39:13okay.

00:39:14So that, ladies and gentlemen, is the news and notes for this week.

00:39:19I'll have a couple of links there in the,

00:39:23show notes,

McIntosh:00:39:25But that's gonna wrap it up for this week. Now, generation bitcoin, we support podcasting 2.0.

00:39:31We are a value for value podcast. What does that mean? I have not said a single thing about that tonight.

Unknown:00:39:38We have no sponsors. We have no advertising.

00:39:41I will never take advertising,

McIntosh:00:39:43Not

00:39:44ever. And maybe it's time I actually do an episode about that, so you understand

00:39:49why I don't ever take advertisers or sponsors. There's good reasons. It's not because I don't want to become rich.

Unknown:00:39:55Sorry.

McIntosh:00:39:57It's because I believe what is that is what is right. At least for me. And I can only speak for that.

Unknown:00:40:03But, you can support this podcast in 3 ways. Time, talent, treasure.

McIntosh:00:40:09If you wanna support the podcast and have some time or talent,

00:40:12there's stuff you can do. Just reach out to me.

Unknown:00:40:15Transcripts,

00:40:16other things,

McIntosh:00:40:18website work. There's look. I have a 1,000,000 ideas in my head. I just don't have time to do them all. That's the truth.

00:40:24Treasure? Well, maybe not a million, but a lot.

Unknown:00:40:28Treasure is just what it sounds like. If you find the content valuable, you can support this podcast by streaming sat or boosting like Bruno did earlier

00:40:37or

00:40:38going out and clipping

00:40:40shows,

McIntosh:00:40:43and I will

00:40:44see that and I will reply to it. And if I ever don't see it, just please reach out to me. There's a number of ways I'll I'll go through that list in just a second.

Unknown:00:40:53But,

00:40:54if you find the content valuable,

McIntosh:00:40:56you can stream the stats, you can boost from podcast 2.0 app. There's a bunch of them at podcastapps.com.

00:41:04If you like the content, I would love it if you would tell your friends about the Generation Bitcoin podcast.

00:41:09As I say quite frequently,

00:41:11That is the single

00:41:13most important way that this podcast can spread. Thanks for being here. I hope this has been helpful. I hope you've learned something from it. I would love

00:41:21to hear from you. I'm on Twitter at Macintosh Fintech.

00:41:24I'm on mastodon@macintosh@podcastindex.social,

00:41:27and you can reach me by email at macintosh@gendashbtc.com.

Unknown:00:41:33Matrix, Macintosh

00:41:341775

00:41:36colon matrix.org.

00:41:38Stay humble, friends. Go out. Make it a great week. I will talk to y'all

00:41:43Thursday.
```
