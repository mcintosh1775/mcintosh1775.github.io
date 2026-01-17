---
title: "Episode 138 Transcript"
draft: false
_build:
  list: never
  render: always
---
```text
WEBVTT

NOTE
Transcription provided by Podhome.fm
Created: 1/16/2024 5:40:40 AM
Duration: 3205.904
Channels: 1

1
00:00:00.399 --> 00:00:04.340
McIntosh: Hey, Sat Stackers. Today is October 19th, and this is episode 138

2
00:00:04.720 --> 00:00:06.020
of generation Bitcoin.

3
00:00:06.399 --> 00:00:09.620
I'm your host, Macintosh. And today's episode is

4
00:00:09.925 --> 00:00:12.025
about the lightning network usage.

5
00:00:42.140 --> 00:00:42.640
Alright.

6
00:00:43.500 --> 00:00:45.120
Let's get right into it.

7
00:00:47.425 --> 00:00:50.645
Yeah. We'll be talking about the Lightning Network today. Of course,

8
00:00:51.025 --> 00:00:53.205
shortly after I did episode 134,

9
00:00:54.465 --> 00:00:55.125
on lightning,

10
00:00:56.770 --> 00:00:59.990
River Financial posted a a a review,

11
00:01:00.450 --> 00:01:01.510
which they've done

12
00:01:01.890 --> 00:01:03.990
at least they did it a year ago as well,

13
00:01:04.625 --> 00:01:08.805
on lightning network usage. They're one of the largest nodes in the lightning network,

14
00:01:09.345 --> 00:01:11.450
and they're one of the people who have the best

15
00:01:11.930 --> 00:01:17.149
ability to kind of see what's going on. Now understand before we even dive into this report

16
00:01:17.850 --> 00:01:19.469
and some additional information

17
00:01:19.929 --> 00:01:20.429
about

18
00:01:21.424 --> 00:01:23.284
podcasting 2.0 stats

19
00:01:23.744 --> 00:01:27.924
in kind of the network that we use to support shows like mine.

20
00:01:29.650 --> 00:01:34.470
A lot of the Lightning Network is private, private nodes running behind Tor,

21
00:01:34.850 --> 00:01:38.310
so on and so forth. And it's very difficult to

22
00:01:39.025 --> 00:01:41.365
really understand it all what's going on.

23
00:01:42.385 --> 00:01:46.405
So you'll see in this report that they talk about kind of lower bounds,

24
00:01:46.930 --> 00:01:52.869
And so what they're saying is it can't be any less than this, but it's certainly more. You can read that into it because

25
00:01:53.570 --> 00:01:55.750
there is an unknown number of

26
00:01:56.215 --> 00:01:57.115
nodes and

27
00:01:57.655 --> 00:01:59.515
and such out there that

28
00:01:59.975 --> 00:02:02.395
that are not being accounted for in this report.

29
00:02:03.310 --> 00:02:08.530
So. Anyways, we'll get all get to all that in a minute. We've had some good feedback.

30
00:02:10.270 --> 00:02:11.650
Bitcoin is pumping.

31
00:02:13.254 --> 00:02:19.515
We'll talk about that for a minute. Our block height at time of recording, let's just go ahead and throw this out there, is 8129

32
00:02:20.614 --> 00:02:21.114
fiver

33
00:02:21.620 --> 00:02:22.120
3812

34
00:02:22.580 --> 00:02:23.080
953.

35
00:02:24.580 --> 00:02:28.120
We probably need to talk about that for just a little bit.

36
00:02:28.795 --> 00:02:31.135
Why don't we just jump on into our market update?

37
00:02:32.075 --> 00:02:36.495
Man, McIntosh, if you only had a script right in front of your eyes that you could

38
00:02:36.795 --> 00:02:37.295
actually

39
00:02:37.950 --> 00:02:38.450
used

40
00:02:38.910 --> 00:02:56.080
to keep on track. I have I have to work really hard to to keep on track even when I do have a script, and I don't have a script. I don't have a word for word script, but I have notes in front of me. By the way, I use Trillium for that on my umbral node. I found it fairly useful. I'm slowly transferring over

41
00:02:56.460 --> 00:02:57.200
my notes

42
00:02:57.820 --> 00:02:59.600
from Evernote to Trillium.

43
00:03:00.140 --> 00:03:01.280
So, anyways,

44
00:03:02.144 --> 00:03:04.784
market. Right now, as I record, we're at 8

45
00:03:05.185 --> 00:03:05.685
28,759.

46
00:03:08.144 --> 00:03:09.525
That will be the official

47
00:03:10.144 --> 00:03:11.730
price for today.

48
00:03:12.110 --> 00:03:13.090
As I record

49
00:03:13.390 --> 00:03:15.810
here on Thursday afternoon, unfortunately,

50
00:03:16.590 --> 00:03:22.985
I was tied up last night with some work stuff, so I'm having to record later than normal. Sometimes duty calls,

51
00:03:23.845 --> 00:03:27.225
I was actually not I was not on call this week, but,

52
00:03:28.370 --> 00:03:34.069
I got pulled into an HBI after having to work late already on some other issues.

53
00:03:35.305 --> 00:03:36.045
And so,

54
00:03:36.505 --> 00:03:43.325
you know, it wrecked my whole night, to be honest. But because of that, I was able to get off a little bit early. So here I am recording,

55
00:03:43.720 --> 00:03:46.060
and I'll punch this out as quickly as I can.

56
00:03:46.680 --> 00:03:51.100
I do apologize for the delay during the week. Sometimes these things are just unavoidable.

57
00:03:51.675 --> 00:03:52.895
Anyways, 28,759,

58
00:03:54.315 --> 00:03:57.055
and we're actually continuing to pump up from there.

59
00:03:57.435 --> 00:03:58.815
If I open up

60
00:03:59.840 --> 00:04:00.739
trading view.

61
00:04:03.280 --> 00:04:04.260
I think overall,

62
00:04:05.760 --> 00:04:06.260
well,

63
00:04:07.255 --> 00:04:12.715
what we've seen is that things were not so well. We were kind of heading down.

64
00:04:13.015 --> 00:04:23.180
And then, basically, I think CoinTelegraph. It was either CoinTelegraph or CoinDesk, and I do not remember which. It should be in my news, but 1 or the other of them posted

65
00:04:24.385 --> 00:04:24.885
inherently

66
00:04:25.505 --> 00:04:26.005
that,

67
00:04:28.065 --> 00:04:35.510
BlackRock had been approved for a spot ETF approval, and it provided in an instant, you know, less than an hour $1,000 pump.

68
00:04:36.690 --> 00:04:37.190
And,

69
00:04:37.650 --> 00:04:45.565
of course, they retracted that. It's not true. Nothing in terms of bought ETFs has been approved, but the levels have stayed up.

70
00:04:46.265 --> 00:04:54.570
So, you know, we're we're moving back towards the top side of this box, if you wanna call it that. As we've discussed, we've got this box going on between

71
00:04:54.950 --> 00:04:55.450
25,031,000

72
00:04:56.550 --> 00:04:58.650
that's going back for months now.

73
00:05:00.294 --> 00:05:13.170
I do believe that when a spot ETF gets approved, we will break out of this box personally late if we're not alright. And that's my personal opinion. It's not financial advice, and I'm certainly not giving you trading advice, by the way.

74
00:05:15.125 --> 00:05:15.625
But

75
00:05:16.165 --> 00:05:20.025
I think there's a chance after that happens that it stays above 31,000.

76
00:05:21.150 --> 00:05:32.075
I'm not a believer that, you know, spot ETFs are gonna save Bitcoin. I don't even care whether they get approved or not. But the reality is is that they bring in Wall Street money.

77
00:05:32.695 --> 00:05:39.740
They bring in people who don't want to invest in Bitcoin in any other way, but they want to invest in Bitcoin. I get all that.

78
00:05:40.120 --> 00:05:42.380
It will continue Bitcoin's dominance

79
00:05:43.560 --> 00:05:45.979
march to dominance, I I should say,

80
00:05:46.794 --> 00:05:49.854
as a global reserve currency at some point.

81
00:05:51.275 --> 00:05:52.335
So it's necessary,

82
00:05:52.955 --> 00:05:54.870
but I don't really care about them.

83
00:05:55.750 --> 00:06:01.449
I would not recommend that you buy in a spot ETF. I would recommend that you own your own Bitcoin

84
00:06:01.750 --> 00:06:03.449
and you put it in your own

85
00:06:04.275 --> 00:06:04.775
hardware

86
00:06:05.155 --> 00:06:11.735
wallet. Seed signer seems to be the best thing going on right now. I am going to be building one of those in the next few months.

87
00:06:12.340 --> 00:06:14.520
I'll be reporting on that as I do it.

88
00:06:14.900 --> 00:06:21.755
And one other brief note, by the way, let's see. That clearly happened on October 16th, 16th, Monday,

89
00:06:22.215 --> 00:06:24.875
and it pumped all the way up to $30,000,

90
00:06:25.895 --> 00:06:27.514
kissed it 29,

91
00:06:27.815 --> 00:06:29.514
probably 29 99,

92
00:06:31.259 --> 00:06:42.445
and fell right back down, but it fell at a higher level. So, I mean, you very clearly can see that we've consolidated. We're building actually a flag formation, a nice flag formation.

93
00:06:43.705 --> 00:06:48.430
The Bollinger Bands are pinching down. We may be pressing back up towards that

94
00:06:48.810 --> 00:06:49.469
30,000, 31,000

95
00:06:49.849 --> 00:06:50.349
mark

96
00:06:50.889 --> 00:06:52.590
before the weekend. We'll see.

97
00:06:53.129 --> 00:06:56.095
That's certainly not financial advice, and I'm just

98
00:06:56.655 --> 00:06:59.395
rambling as I look at a trading view chart.

99
00:07:02.015 --> 00:07:07.770
What do we say here here at Generation Bitcoin Stack Sats. Buy every day. Use the strike app

100
00:07:08.469 --> 00:07:09.289
McIntosh: if you must.

101
00:07:10.150 --> 00:07:11.530
However you do that,

102
00:07:12.375 --> 00:07:16.155
McIntosh: just do it. Just do it daily. Don't worry about the price. Don't worry about,

103
00:07:16.935 --> 00:07:17.995
at worst case,

104
00:07:18.455 --> 00:07:18.955
weekly.

105
00:07:19.409 --> 00:07:23.110
I would not recommend monthly. You may get left behind at some point,

106
00:07:23.650 --> 00:07:25.349
and that would be a terrible thing.

107
00:07:27.545 --> 00:07:29.645
So just keep stacking those sats.

108
00:07:30.185 --> 00:07:38.620
Strike is an easy way to do that. There are other options certainly at this point. Oh, by the way, to close-up the market stuff, I did wanna mention,

109
00:07:40.200 --> 00:07:44.025
on 16th, so just a few days ago, we had an adjustment, estimate 6.47%

110
00:07:45.125 --> 00:07:48.745
up in the difficulty. So things are getting harder. And, unfortunately,

111
00:07:49.205 --> 00:07:49.865
right now,

112
00:07:50.780 --> 00:07:59.199
the next one will be on the 29th, so ten days from now, and it's looking like it's going to be another 5% or so up. Now I'm hoping that comes down

113
00:07:59.575 --> 00:08:01.595
because, frankly, I could use some more

114
00:08:01.895 --> 00:08:03.755
sats in my mining setup.

115
00:08:04.295 --> 00:08:13.710
It does look like we will have another upward adjustment. So what does this mean? Well, what it means is that more hash rate is coming online. As more and more hash rate comes online,

116
00:08:14.810 --> 00:08:23.605
there's more people competing. The blocks are getting mined faster. And, of course, as I've explained before, the difficulty adjustment essentially is designed to

117
00:08:24.465 --> 00:08:30.700
keep that block mining happening around every 10 minutes. Well, right now, it's not. It's happening faster than that.

118
00:08:32.415 --> 00:08:37.935
Our fees are still fairly high. They look like they've actually been kind of going up. Oh, well, look at their

119
00:08:40.149 --> 00:08:43.850
a minute ago, they were 15. Now they're 6 and 4,

120
00:08:44.630 --> 00:08:47.529
so priority is 6 sets per v byte.

121
00:08:48.185 --> 00:08:50.285
We're still over on the mempool,

122
00:08:51.065 --> 00:08:51.565
451

123
00:08:52.105 --> 00:08:53.245
megabytes. So,

124
00:08:54.505 --> 00:08:55.405
I don't know.

125
00:08:56.040 --> 00:08:56.860
No idea.

126
00:08:58.199 --> 00:09:02.459
But, yeah, it certainly looks like more hash is being added to the network.

127
00:09:02.855 --> 00:09:06.555
I think what is happening as Bitcoin goes up in price,

128
00:09:07.334 --> 00:09:07.834
miners

129
00:09:08.214 --> 00:09:09.515
that have been inactive

130
00:09:09.895 --> 00:09:12.235
because they can't afford to run the miners

131
00:09:13.290 --> 00:09:14.910
we're starting to bring those online.

132
00:09:15.690 --> 00:09:16.750
So there you go.

133
00:09:17.290 --> 00:09:20.030
I think that covers that. So we will move on

134
00:09:20.650 --> 00:09:21.710
to our topic.

135
00:09:23.155 --> 00:09:26.375
So this report, it's a it's a 20

136
00:09:27.395 --> 00:09:29.575
no. 45 page report.

137
00:09:32.290 --> 00:09:33.670
McIntosh: I've read through it.

138
00:09:34.690 --> 00:09:36.790
I'm going to summarize it in part.

139
00:09:37.805 --> 00:09:40.145
There's a lot of interesting things in here.

140
00:09:41.165 --> 00:09:41.665
McIntosh: Basically,

141
00:09:42.205 --> 00:09:43.105
in summary,

142
00:09:43.805 --> 00:09:44.305
despite

143
00:09:45.560 --> 00:09:46.699
a drop in Bitcoin.

144
00:09:47.399 --> 00:09:48.220
And despite

145
00:09:49.240 --> 00:09:51.339
McIntosh: a decrease in search interest,

146
00:09:52.199 --> 00:09:53.500
there have been more

147
00:09:53.879 --> 00:09:54.379
payments

148
00:09:55.625 --> 00:09:56.445
McIntosh: in the last

149
00:09:57.145 --> 00:10:00.525
2 years, 2 years, 2 months since August 2021.

150
00:10:01.385 --> 00:10:03.405
So in the last 2 years

151
00:10:04 --> 00:10:04.820
or so,

152
00:10:05.520 --> 00:10:06.420
there's been

153
00:10:07.200 --> 00:10:13.540
an increase in lightning payments. That's the way to say it. Even though 44% price drop,

154
00:10:13.955 --> 00:10:14.455
45%

155
00:10:14.915 --> 00:10:18.855
decrease in search interest, which by the way directly relates to the price,

156
00:10:19.475 --> 00:10:19.975
1212%.

157
00:10:21.555 --> 00:10:23.255
Now that's not a number.

158
00:10:23.959 --> 00:10:31.019
And in fact, what we see is that at least for the last year or so, the amount of Bitcoin tied up in

159
00:10:31.399 --> 00:10:31.899
lightning,

160
00:10:32.965 --> 00:10:39.545
certainly on the visible network, if you wanna call it that. I'm gonna kind of differentiate between visible and invisible,

161
00:10:40.085 --> 00:10:41.065
Tor based.

162
00:10:41.910 --> 00:10:44.490
That really hasn't changed a huge amount,

163
00:10:45.110 --> 00:10:52.445
not like this, but the number of payments is. And I that makes me very bullish. Show people are using the lightning network.

164
00:10:54.185 --> 00:10:55.245
That's the equivalent

165
00:10:55.625 --> 00:10:57.725
right now of 2.5 transactions

166
00:10:58.185 --> 00:10:58.925
per second.

167
00:10:59.560 --> 00:11:01.420
Bitcoin on chain is 4.4.

168
00:11:02.440 --> 00:11:03.579
So there you go.

169
00:11:04.040 --> 00:11:04.779
So we're

170
00:11:05.160 --> 00:11:05.660
basically

171
00:11:06.199 --> 00:11:06.699
halfway,

172
00:11:07.825 --> 00:11:08.885
no more than halfway

173
00:11:09.505 --> 00:11:13.205
to the amount of transactions that are occurring on the Bitcoin main chain.

174
00:11:13.585 --> 00:11:18.670
Now what would our fees be like if all this traffic we're on the main chain. I don't wanna think about it.

175
00:11:19.850 --> 00:11:23.310
Now the primary use case, and I'm gonna pick a bone here

176
00:11:24.175 --> 00:11:31.235
with this report. The primary use case driving transaction growth that we identified are, and we being River,

177
00:11:31.959 --> 00:11:32.459
gaming,

178
00:11:32.920 --> 00:11:35.500
social media tipping, and streaming.

179
00:11:36.120 --> 00:11:39.500
Now I don't know what they mean by streaming. Maybe they mean

180
00:11:40.075 --> 00:11:41.455
Podcast 2.0,

181
00:11:41.995 --> 00:11:47.855
streaming of sats while people listen. I assume they could mean things like streaming while watching

182
00:11:48.320 --> 00:11:51.459
a TV show. I don't know because I've never actually heard of

183
00:11:51.839 --> 00:11:53.860
I've only heard of streaming outside

184
00:11:54.800 --> 00:12:05.045
or in the context of podcast 2 point o. Now the interesting thing is is in this report, as far as I can tell, not once do they mention podcast podcast 2 point o,

185
00:12:05.425 --> 00:12:08.390
who, by the way, started, what, 3 years ago.

186
00:12:09.250 --> 00:12:09.750
Mhmm.

187
00:12:10.450 --> 00:12:13.270
And we do know from the stats that,

188
00:12:15.145 --> 00:12:19.965
the guys over at podcast 2 point o keep that the number of sats

189
00:12:21.145 --> 00:12:22.285
is fairly significant

190
00:12:22.879 --> 00:12:30.899
going across this podcast 2 point o network. Now I don't know. Again, I think from what I understand, these are kind of lower bounds.

191
00:12:32.265 --> 00:12:34.605
But over the last 90 days, $30,000

192
00:12:35.625 --> 00:12:36.845
over a 100,000,000

193
00:12:37.545 --> 00:12:38.045
sats,

194
00:12:38.585 --> 00:12:39.405
1 Bitcoin

195
00:12:40.480 --> 00:12:41.540
has been transacted

196
00:12:42.400 --> 00:12:42.900
across

197
00:12:43.760 --> 00:12:46.340
value for value podcast 2.0

198
00:12:46.720 --> 00:12:47.220
lightning

199
00:12:47.680 --> 00:12:48.180
payments.

200
00:12:49.154 --> 00:12:49.654
McIntosh: Almost

201
00:12:52.595 --> 00:12:53.814
McIntosh: 1,000,000 transactions

202
00:12:54.834 --> 00:12:55.735
doing that.

203
00:12:56.970 --> 00:12:58.910
And the number of unique senders,

204
00:13:01.130 --> 00:13:02.829
if I'm reading this correctly,

205
00:13:04.295 --> 00:13:05.195
McIntosh: must be

206
00:13:06.774 --> 00:13:09.595
well, they don't have a number for unique senders, so I'm

207
00:13:10.055 --> 00:13:12.690
I oh, there it is. So it's like 295.

208
00:13:13.149 --> 00:13:15.889
McIntosh: It looks like 3 so the lower boundary,

209
00:13:16.190 --> 00:13:18.209
like, 260. There's the lowest.

210
00:13:19.445 --> 00:13:21.625
So let me see if I can figure this out,

211
00:13:22.084 --> 00:13:22.584
169.

212
00:13:22.885 --> 00:13:24.345
The highest is

213
00:13:25.765 --> 00:13:30.730
380, and that's, I think, on a daily basis. So between 160

214
00:13:31.270 --> 00:13:34.570
and almost 400 unique senders per day.

215
00:13:37.015 --> 00:13:37.515
So

216
00:13:38.375 --> 00:13:40.235
high volume, high transactions,

217
00:13:40.935 --> 00:13:43.355
honestly, low number of unique senders.

218
00:13:43.880 --> 00:13:44.380
Now,

219
00:13:45 --> 00:13:49.240
do they have groupings there? I don't know. Is, like, all the,

220
00:13:50.200 --> 00:13:54.435
Albi wallets, do they show up as one sender? I do not know.

221
00:13:54.975 --> 00:13:59.020
I would love to see that unique senders go up personally, but the point is

222
00:13:59.500 --> 00:14:01.520
there is a decent quantity

223
00:14:02.060 --> 00:14:06
of traffic that if you go back far enough, we know is growing.

224
00:14:07.375 --> 00:14:18.030
It's not in this chart, but if you go back in time, and they've talked about that on the podcast 2.0 show. How over the last few years, of course, this has gone up, and it will only continue

225
00:14:18.570 --> 00:14:20.110
to do so as more

226
00:14:20.650 --> 00:14:22.990
value for value podcast 2.0,

227
00:14:23.595 --> 00:14:27.855
shows come out or shows come on board. People promoting,

228
00:14:28.475 --> 00:14:36.990
hey. You can support this podcast as I will at the end of this show by doing what? By streaming sats, by sending boost,

229
00:14:37.850 --> 00:14:39.790
by becoming a part of this ecosystem

230
00:14:40.125 --> 00:14:48.065
still man, providing value for value instead of sitting like a dumb sheep and listening to a bunch of ads. And I'm sorry if you find that offensive.

231
00:14:49.600 --> 00:14:55.380
I I really am, but I I mean it. I mean, I hate listening to ads. Let's be honest.

232
00:14:55.975 --> 00:14:58.235
McIntosh: I fast forward through them whenever possible,

233
00:14:58.935 --> 00:15:00.155
and I find it

234
00:15:00.935 --> 00:15:04.890
McIntosh: look. I'm I'll tell you about a podcast I was listening to this week, and it was

235
00:15:05.770 --> 00:15:06.670
McIntosh: it was almost

236
00:15:07.130 --> 00:15:10.270
McIntosh: unlistenable, and I'm not gonna mention the name of the podcast.

237
00:15:10.890 --> 00:15:13.630
But it's a mining industry podcast

238
00:15:15.385 --> 00:15:17.245
that sponsored by a miner,

239
00:15:17.705 --> 00:15:20.925
one of the public miners or public hosting companies,

240
00:15:21.785 --> 00:15:23.085
and they had on

241
00:15:24.620 --> 00:15:28.880
the guy who's behind drive chain and one of his pals.

242
00:15:29.260 --> 00:15:30.880
And they were trying to explain

243
00:15:31.964 --> 00:15:33.024
to us plebs,

244
00:15:35.245 --> 00:15:37.024
how drive chains are awesome.

245
00:15:37.725 --> 00:15:42.120
It's the same song and dance they've been listen they've been saying for months.

246
00:15:42.660 --> 00:15:44.120
And I've listened to it,

247
00:15:44.420 --> 00:15:47.880
and I've read it, and I've dissected it. And as a miner

248
00:15:48.635 --> 00:15:52.975
and as a pleb, I completely reject it. I say, I do not need this.

249
00:15:53.675 --> 00:15:55.615
They say, well, this is going to increase

250
00:15:56.315 --> 00:15:57.215
miner profitability

251
00:15:58.100 --> 00:16:05.160
on the one hand, and on the other hand, they say things like literally in this podcast, they said one of the guys who was a miner,

252
00:16:05.595 --> 00:16:08.335
it wasn't Paul. Like, Jamie was his name.

253
00:16:08.795 --> 00:16:09.615
He said,

254
00:16:10.715 --> 00:16:17.840
well, you know, you gotta be running 50 megawatts to be profitable. I mean, that's almost word for word what he said.

255
00:16:18.300 --> 00:16:19.680
And, Jamie, respectfully,

256
00:16:20.140 --> 00:16:23.680
with any respect that's due, I would say, that's garbage.

257
00:16:25.215 --> 00:16:31.315
Now, if I have one miner, I have a higher chance of failure because maybe I have a hardware failure of that miner

258
00:16:31.680 --> 00:16:34.259
that I can't cover out of the operating cost.

259
00:16:35.199 --> 00:16:36.500
But let me tell you,

260
00:16:37.040 --> 00:16:45.445
if you're mining with one unit and you're upside down in that miner, in other words, you're mining less Bitcoin than it costs you to run that miner,

261
00:16:46.385 --> 00:17:01.695
then you're unprofitable. And I can be unprofitable at 50 megawatts. And at the same time, I can be profitable at one unit or ten units or a 100 units or a 1000 units. By the way, a megawatt at today's units. That's roughly 300 units.

262
00:17:02.154 --> 00:17:05.855
So if I'm doing that math right, what he said was,

263
00:17:07.710 --> 00:17:09.090
you can't be profitable

264
00:17:09.470 --> 00:17:10.770
at roughly 300

265
00:17:12.750 --> 00:17:15.490
times 50. How's that make you feel, plebs?

266
00:17:16.245 --> 00:17:18.665
Oh, and by the way, he also talked about having,

267
00:17:19.365 --> 00:17:22.985
not him, Paul. I I well, actually, I don't remember which.

268
00:17:23.570 --> 00:17:32.470
They were talking about yeah. We need to have, like, a behind closed doors meetings and not have literally said not have the plebs. Now I don't know who he meant by that,

269
00:17:33.345 --> 00:17:37.284
but I get very offended with crap like that gets said. Okay?

270
00:17:38.065 --> 00:17:39.284
It's not okay.

271
00:17:39.585 --> 00:17:41.044
This is an open network,

272
00:17:42.700 --> 00:17:46.240
and miners have to participate that in and and and

273
00:17:46.700 --> 00:17:55.425
and I don't mean miners. I mean public miners because that's who these people are starting they're trying to represent. And I think it's interesting

274
00:17:55.885 --> 00:17:56.705
that the

275
00:17:58.800 --> 00:18:00.020
CTO CEO.

276
00:18:00.320 --> 00:18:08.180
I'm not sure. Somebody very high up in Riot, if I'm not mistaken, who is the largest miner public miner in the world

277
00:18:09.684 --> 00:18:12.105
McIntosh: has come out and said this is not a good idea.

278
00:18:12.565 --> 00:18:14.105
So who's left, Paul?

279
00:18:14.965 --> 00:18:17.465
Because now you've ticked off to Plebs

280
00:18:18.740 --> 00:18:21.240
because, you know, we don't know what we're talking about.

281
00:18:23.860 --> 00:18:27.845
McIntosh: The public miners apparently aren't getting on board, so there's nobody left.

282
00:18:28.405 --> 00:18:29.945
So go pound sand.

283
00:18:30.485 --> 00:18:31.705
Go over to Litecoin

284
00:18:32.005 --> 00:18:33.385
and set up your drivetrain

285
00:18:33.765 --> 00:18:38.470
and show us how it works because we're too stupid to understand it

286
00:18:39.330 --> 00:18:41.110
after you've called 14,000

287
00:18:41.650 --> 00:18:43.990
people ugly names on Twitter.

288
00:18:45.575 --> 00:18:46.075
McIntosh: Ridiculous.

289
00:18:47.654 --> 00:18:49.355
Give people the time of day.

290
00:18:54.110 --> 00:18:54.610
Sorry.

291
00:18:55.950 --> 00:19:01.404
McIntosh: I didn't even mean to talk about that this week. I tell you, sometimes I think the best things I say are scripted.

292
00:19:01.945 --> 00:19:09.030
That may just be my opinion. I may have blown out half the audience right there, and that's okay because I'm allowed to have my opinion, and I have this microphone.

293
00:19:09.650 --> 00:19:11.430
You can fast forward. That's okay.

294
00:19:13.650 --> 00:19:18.434
I wouldn't even want Paul to come on the show. I can't have an honest debate with him at this point.

295
00:19:18.894 --> 00:19:20.914
For one thing, he's very good at talking.

296
00:19:22.255 --> 00:19:29.220
Maybe not very good at writing on Twitter, but he's very good at talking. He'll talk circles around you, but that doesn't mean that he's right.

297
00:19:29.840 --> 00:19:32.340
And I'm not gonna debate somebody like that

298
00:19:33.654 --> 00:19:35.274
McIntosh: because I'll look like an idiot,

299
00:19:37.975 --> 00:19:40.794
McIntosh: but I have taken the time to do the work.

300
00:19:41.139 --> 00:19:44.120
And I do have invested interest in what's going on.

301
00:19:44.899 --> 00:19:47
McIntosh: And I'm not some stupid idiot.

302
00:19:48.315 --> 00:19:50.174
I'm actually reasonably smart.

303
00:19:51.914 --> 00:19:52.414
So

304
00:19:53.034 --> 00:19:53.534
whatever.

305
00:19:54.554 --> 00:19:56.335
Moving right on. Sorry.

306
00:19:56.850 --> 00:19:57.750
McIntosh: I do apologize

307
00:19:58.050 --> 00:19:58.550
again,

308
00:19:59.090 --> 00:20:06.390
going back to lightning, which is what we're here to talk about. I do not know how I got off on that. So the point to this thing,

309
00:20:07.145 --> 00:20:08.445
the point to this report

310
00:20:09.225 --> 00:20:13.325
because I don't wanna make this week's episode too long. The point to this report,

311
00:20:13.945 --> 00:20:15.485
from what they can see,

312
00:20:16.350 --> 00:20:17.090
even though

313
00:20:17.550 --> 00:20:23.010
in some ways the network is not growing, even though Bitcoin price is down, even though

314
00:20:23.365 --> 00:20:26.585
Bitcoin searches are down, which are a direct indicator of interest.

315
00:20:27.125 --> 00:20:29.625
Lightning itself seems to be growing.

316
00:20:30.005 --> 00:20:33.560
Certainly, the number of transactions across lightning are growing.

317
00:20:33.940 --> 00:20:37.400
In the podcast 2 point o industry, we see this.

318
00:20:37.780 --> 00:20:39.640
There was 7 6,600,000

319
00:20:41.575 --> 00:20:43.995
transactions involving more than 2 nodes

320
00:20:44.455 --> 00:20:45.195
in public

321
00:20:45.575 --> 00:20:47.755
that showed up in August of 2022.

322
00:20:49.320 --> 00:20:59.144
If you have direct transactions, if my node opens up a transaction to your node, that often doesn't show up. If you have 2 private nodes over private channels, that certainly

323
00:20:59.524 --> 00:21:01.065
won't show up. So we know

324
00:21:01.524 --> 00:21:02.024
that,

325
00:21:02.325 --> 00:21:04.264
basically, 6a half 1000000

326
00:21:05.284 --> 00:21:07.144
were logged in August 20

327
00:21:07.470 --> 00:21:12.130
23. We don't know. I would actually estimate at least 25%

328
00:21:12.510 --> 00:21:13.410
more than that.

329
00:21:14.805 --> 00:21:18.265
And I'm not gonna do that math, but it's, what, 8,000,000 or so

330
00:21:19.765 --> 00:21:21.145
are actually occurring.

331
00:21:22.220 --> 00:21:22.720
So

332
00:21:23.100 --> 00:21:32.085
despite claims by Paul that the lightning network is dead, actually, that's, I believe, one of the things he said. Hard to keep up with all the stuff that comes

333
00:21:32.385 --> 00:21:33.205
from him.

334
00:21:33.745 --> 00:21:38.165
It is alive and growing. By the way, back in August of 2021, there was 503,000

335
00:21:40.290 --> 00:21:45.750
transactions during that month. That's actually oh, it's exactly 2 years. They're going from August to August.

336
00:21:46.530 --> 00:21:48.654
So that's where they get the 1212%

337
00:21:50.475 --> 00:21:52.735
growth. That doesn't mean that,

338
00:21:53.674 --> 00:21:54.820
there's 1212%

339
00:21:55.440 --> 00:22:00.340
more Bitcoin locked up into those notes. And by the way, there's things

340
00:22:00.880 --> 00:22:05.845
that I'm not really happy about lightning. I think it still got a ways to go.

341
00:22:07.825 --> 00:22:09.605
McIntosh: We do see a clear divergence.

342
00:22:10.065 --> 00:22:11.365
There's a chart here

343
00:22:11.730 --> 00:22:12.230
between

344
00:22:12.769 --> 00:22:19.830
the on daily lightning transactions on and daily on chain transactions. So if you compare the transactions

345
00:22:20.395 --> 00:22:22.255
they're occurring on the main net.

346
00:22:23.755 --> 00:22:24.415
It is,

347
00:22:26.715 --> 00:22:30.360
roughly, I said that 4.4 per transactions per second.

348
00:22:30.740 --> 00:22:32.200
Lightning is now 2.5,

349
00:22:32.740 --> 00:22:35.240
but the lightning is growing at a faster rate.

350
00:22:36.075 --> 00:22:39.135
McIntosh: I would argue that within the next two years that it will

351
00:22:39.835 --> 00:22:40.735
exceed that.

352
00:22:43.250 --> 00:22:46.470
So probably during the height of the next bull run,

353
00:22:47.090 --> 00:22:50.390
let's say August, not August, Q4 2025,

354
00:22:52.335 --> 00:23:03.980
when Bitcoin's going to be at an all time high, as I've said, and I'll still stand by that until proven otherwise. That's what the data has shown historically. It doesn't mean it can be different. It can be, but

355
00:23:04.440 --> 00:23:06.940
until proven otherwise, that's what I'm going by.

356
00:23:08.475 --> 00:23:11.295
I I will say that lightning will probably exceed

357
00:23:12.235 --> 00:23:19.830
the main chain transactions. We'll have more transactions per second occurring over lightning, and that is the way that it should be.

358
00:23:21.250 --> 00:23:23.909
Now we know that, for exam,

359
00:23:24.785 --> 00:23:30.405
Coinbase, for example, hasn't even gone lightning yet. They've announced that they're going to.

360
00:23:30.865 --> 00:23:32.245
That'll be a big thing.

361
00:23:33.720 --> 00:23:38.120
They talked about how gaming has grown a lot. They've talked about

362
00:23:39.160 --> 00:23:40.060
all of these

363
00:23:40.855 --> 00:23:45.115
use cases have been growing, and and they will continue to grow, in my opinion,

364
00:23:45.495 --> 00:23:46.475
for quite a while.

365
00:23:46.935 --> 00:23:50.180
By the way, the volume the actual volume in in Bitcoin.

366
00:23:50.720 --> 00:23:53.140
In other words, the total, like, amount

367
00:23:53.520 --> 00:23:54.020
worth

368
00:23:54.320 --> 00:23:55.780
has grown as well.

369
00:23:57.335 --> 00:23:58.875
I'm trying to figure this out.

370
00:23:59.255 --> 00:24:03.915
The volume in US dollars, volume okay. So it grew from 303

371
00:24:04.375 --> 00:24:04.875
Bitcoin

372
00:24:05.335 --> 00:24:06.155
back in

373
00:24:06.790 --> 00:24:08.170
August of 2021

374
00:24:08.550 --> 00:24:10.490
to right now in August of 2023,

375
00:24:11.350 --> 00:24:12.490
almost 30,02950.

376
00:24:14.304 --> 00:24:15.205
So that's an

377
00:24:16.145 --> 00:24:16.645
874%

378
00:24:17.345 --> 00:24:19.205
growth. So not as big as

379
00:24:19.664 --> 00:24:20.164
1200%,

380
00:24:21.424 --> 00:24:22.965
right, but still

381
00:24:23.389 --> 00:24:24.210
quite significant,

382
00:24:26.509 --> 00:24:30.610
quite, quite significant. And, again, this doesn't include all the private payments.

383
00:24:31.515 --> 00:24:33.375
The payment size has grown.

384
00:24:34.394 --> 00:24:34.894
25%

385
00:24:35.355 --> 00:24:41.720
is 1 to 10 sets, so that's kind of the gaming and streaming stuff, podcasting 2 point o. Another 25%

386
00:24:42.340 --> 00:24:44.200
between 10 and 1,000

387
00:24:44.740 --> 00:24:45.240
sats.

388
00:24:45.620 --> 00:24:46.679
Maybe a tip?

389
00:24:48.395 --> 00:24:51.855
Probably a tip. A 1,000 sets is only, what?

390
00:24:53.195 --> 00:24:55.500
Well, it's less than a dollar. It's like, 30¢,

391
00:24:55.800 --> 00:25:00.620
so not many purchases would be at that range. From 10,000 and upward,

392
00:25:03.295 --> 00:25:06.835
a lot of commerce remittance and node rebalancing, actually.

393
00:25:08.655 --> 00:25:09.155
So

394
00:25:10.180 --> 00:25:15.160
lightning is definitely solving a need. I think we can certainly draw that. Right?

395
00:25:16.260 --> 00:25:17.960
So they got some data here.

396
00:25:18.715 --> 00:25:19.455
The US

397
00:25:19.755 --> 00:25:21.855
is actually leading lightning usage,

398
00:25:23.355 --> 00:25:24.975
followed by my Myanmar.

399
00:25:25.275 --> 00:25:26.414
Interesting. Burma,

400
00:25:28.520 --> 00:25:33.179
Southeast Asia, the UK, Italy, Germany, France, Nigeria, Canada,

401
00:25:35.054 --> 00:25:38.915
Iran. So so far, I see 1 African country, Nigeria.

402
00:25:39.375 --> 00:25:42.675
I would have actually thought that in places

403
00:25:46.980 --> 00:25:49.080
interesting. I woulda thought that

404
00:25:49.540 --> 00:25:51.480
in places like Nigeria, Kenya,

405
00:25:52.035 --> 00:25:54.535
you know, these African countries, South America,

406
00:25:55.075 --> 00:25:58.455
these places that the lightning usage would have been a lot higher.

407
00:26:00.270 --> 00:26:02.210
That is very interesting. Alright.

408
00:26:02.990 --> 00:26:04.290
The number of nodes

409
00:26:04.910 --> 00:26:05.730
has grown

410
00:26:06.190 --> 00:26:06.690
from

411
00:26:07.085 --> 00:26:07.585
roughly

412
00:26:08.285 --> 00:26:08.785
7,000

413
00:26:09.325 --> 00:26:10.065
up to,

414
00:26:10.925 --> 00:26:12.065
right now, about

415
00:26:12.685 --> 00:26:13.185
17,000.

416
00:26:13.805 --> 00:26:14.305
However,

417
00:26:15.880 --> 00:26:19.980
I'm sure they well, they do point this out. It very much reached a plateau.

418
00:26:20.679 --> 00:26:22.779
In fact, it peaked in 2022,

419
00:26:23.080 --> 00:26:24.220
and it's now dropped.

420
00:26:25.275 --> 00:26:27.855
This is a little concerning to me. Okay?

421
00:26:28.875 --> 00:26:39.760
I would love to see more lightning notes, not less. I would love to see more plebs running lightning notes, not less. And the number of channels has followed that same course. It peaked back in 2022.

422
00:26:40.940 --> 00:26:42.160
McIntosh: It's gone down

423
00:26:42.934 --> 00:26:49.755
McIntosh: about 11%, it said. The capacity has followed route as well, actually, the total Bitcoin capacity.

424
00:26:50.830 --> 00:26:56.770
So it does look like for now, we've basically reached a plateau, and I think that very much would

425
00:26:57.470 --> 00:26:59.810
pattern along with the bear market.

426
00:27:00.325 --> 00:27:01.304
We will see

427
00:27:02.085 --> 00:27:06.025
as the market starts taking off, this will go up more.

428
00:27:08.860 --> 00:27:09.360
Alright.

429
00:27:09.900 --> 00:27:13.679
I think that's pretty much it. It's a lot of good stuff.

430
00:27:14.495 --> 00:27:17.075
Even though they don't give a lot of

431
00:27:17.935 --> 00:27:20.675
emphasis to the podcasting 2.0,

432
00:27:21.535 --> 00:27:22.035
stuff,

433
00:27:22.630 --> 00:27:25.530
I see this as a very valuable part of the ecosystem,

434
00:27:25.990 --> 00:27:31.130
especially as music starts to come along, as we can stream music to,

435
00:27:32.485 --> 00:27:41.385
value for value music creators as we can boost in this kind of thing. So I think you'll see a lot of growth there over the next few years

436
00:27:41.779 --> 00:27:42.440
as well.

437
00:27:42.899 --> 00:27:46.679
I'll add my own notes here. I I do believe that lightning

438
00:27:46.980 --> 00:27:47.720
in general

439
00:27:49.835 --> 00:27:52.095
McIntosh: for a custodial a noncustodial

440
00:27:52.475 --> 00:27:52.975
setup

441
00:27:53.835 --> 00:27:54.895
needs to improve.

442
00:27:56.390 --> 00:27:58.170
McIntosh: Being able to run your own node

443
00:27:58.550 --> 00:28:00.090
or being able to somehow,

444
00:28:02.070 --> 00:28:05.610
manage your own hot wallet, that kind of thing. That's

445
00:28:06.165 --> 00:28:06.665
noncustodial.

446
00:28:08.885 --> 00:28:09.865
It's very important.

447
00:28:10.325 --> 00:28:14.745
The experience is not there yet. It is still difficult to run a note. It has improved,

448
00:28:15.820 --> 00:28:20.720
keeping channels. A lot of I talked about splicing recently, keeping channels open,

449
00:28:21.900 --> 00:28:24.400
balancing those channels, that type of thing.

450
00:28:24.735 --> 00:28:29.875
There needs to be more improvement, and there will be. We're so young. I think it's only been 5 years,

451
00:28:31.934 --> 00:28:44.260
that lightning has been around, and we're so young. We're so new to this. I don't wanna be too hard. A lot of people are there. Like, oh, we're not there yet. Blah blah blah. Lightning is dead. I'm like, yeah. You don't know what you're talking about.

452
00:28:45.745 --> 00:28:46.245
Sorry,

453
00:28:46.705 --> 00:28:47.525
not true.

454
00:28:48.065 --> 00:28:55.380
We we've plateaued as I just talked about, but we are in the middle of a bear market. And the plateau is a very high

455
00:28:55.680 --> 00:28:57.780
McIntosh: amount over the two years ago.

456
00:28:58.240 --> 00:28:59.380
So there you go.

457
00:29:00.825 --> 00:29:01.325
Alright.

458
00:29:03.784 --> 00:29:13.320
McIntosh: Let's talk about our supporters. Let's move on so that we can wrap this hop a up before it gets too late. I've been going on for 30 minutes. Thanks to my

459
00:29:14.020 --> 00:29:15.240
McIntosh: rant about Paul.

460
00:29:16.075 --> 00:29:18.575
Sorry. I just I had to get that off my chest.

461
00:29:19.515 --> 00:29:24.175
McIntosh: He'll never listen to this podcast. I don't care. I'm not gonna debate him. Its just

462
00:29:24.890 --> 00:29:26.090
stuff like that just,

463
00:29:26.570 --> 00:29:28.590
it just rubs me the wrong way.

464
00:29:30.090 --> 00:29:30.590
McIntosh: Really?

465
00:29:32.225 --> 00:29:36.725
Yep, we did get some support this week. As always, I appreciate that.

466
00:29:38.799 --> 00:29:42.260
McIntosh: Just to kinda run through the stats. I'm looking for 25,000

467
00:29:43.039 --> 00:29:45.299
sats per episode as a target.

468
00:29:45.855 --> 00:29:52.595
And the way that that works out is it comes out to about $50 a month, which is roughly what it costs to host and,

469
00:29:54.220 --> 00:29:56.960
you know, manage the infrastructure, so to speak,

470
00:29:57.340 --> 00:29:58.880
for what I'm trying to do.

471
00:29:59.580 --> 00:30:00.080
And

472
00:30:00.835 --> 00:30:05.015
put aside a little bit for, frankly, things like I need to upgrade my computer.

473
00:30:06.275 --> 00:30:06.775
And

474
00:30:07.235 --> 00:30:08.295
you'll find out

475
00:30:08.755 --> 00:30:11.490
as we as we talk about this, of course,

476
00:30:12.110 --> 00:30:17.490
that's not really the case at this point. So we're not there yet, but that's where we're heading,

477
00:30:20.335 --> 00:30:20.815
and,

478
00:30:21.295 --> 00:30:25.555
and we'll get there. And I do appreciate the people who support the show directly

479
00:30:25.960 --> 00:30:29.420
through streams, through boost as we'll talk about here in just a second.

480
00:30:30.440 --> 00:30:37.085
There are certainly other ways that you can support the show, and we'll talk about those at the end, but I've always got things

481
00:30:38.105 --> 00:30:39.544
that can help out.

482
00:30:40.799 --> 00:30:47.620
While I bring this up really, really quickly, I actually I have 2 podcasts that I deal with, one that I used to edit.

483
00:30:48.455 --> 00:30:49.595
The podcast is

484
00:30:49.895 --> 00:30:54.554
in hiatus. I don't think it'll ever come back out of hiatus, but we still host it.

485
00:30:55.360 --> 00:31:00.419
At Captivate along with the Generation Bitcoin podcast. I'm moving to a Castapod

486
00:31:00.880 --> 00:31:01.380
setup,

487
00:31:01.919 --> 00:31:07.335
and I actually moved that show because it made the most sense move it first earlier this week,

488
00:31:07.875 --> 00:31:14.215
and it went really smoothly. So I may actually before the next episode comes out, Monday,

489
00:31:15.679 --> 00:31:18.100
maybe, like, Sunday night. I may

490
00:31:18.720 --> 00:31:19.700
I may actually

491
00:31:21.760 --> 00:31:22.820
make that move,

492
00:31:23.125 --> 00:31:29.145
and will be on cast a pot, and that will open up essentially all the tags from my understanding.

493
00:31:30.630 --> 00:31:34.890
Alright. So we go back to 16th. We had some streaming.

494
00:31:35.190 --> 00:31:37.210
This was the conversation with Diego.

495
00:31:38.935 --> 00:31:40.795
Appreciate that, some good streaming.

496
00:31:41.175 --> 00:31:42.875
I do appreciate that a lot.

497
00:31:44.535 --> 00:31:45.275
And then

498
00:31:45.735 --> 00:31:48.075
with our Eric Hersman of gridless

499
00:31:48.890 --> 00:31:49.390
episode,

500
00:31:50.730 --> 00:31:54.029
Kyrin boosted a row of ducks. He said fantastic

501
00:31:54.409 --> 00:32:00.885
episode with Eric. More like this, please, thank you, sir. I do appreciate that, and that is one of my goals.

502
00:32:01.345 --> 00:32:04.645
I am trying to figure out just to be completely candid

503
00:32:05.130 --> 00:32:10.350
kinda how I do this. I love doing these interviews. I think the one with Diego went very well as well.

504
00:32:11.049 --> 00:32:16.794
It was a great conversation about somebody who's really on the front lines of what I would call hyperinflation.

505
00:32:17.174 --> 00:32:19.355
I guess, technically, it's not, but

506
00:32:19.975 --> 00:32:20.955
they're at a 138%

507
00:32:21.654 --> 00:32:23.560
or something inflation year over year.

508
00:32:24.280 --> 00:32:25.420
That's just nuts,

509
00:32:25.960 --> 00:32:29.820
and they are doing things to cope with that. I thought that was a a very good interview.

510
00:32:30.894 --> 00:32:37.554
I would love to get more of those, and I work on that as I can. I'm trying to do them every week. I'm not, as you can tell,

511
00:32:38.174 --> 00:32:40.274
but, maybe we can get there.

512
00:32:41.210 --> 00:32:43.630
So, I've got the technical stuff.

513
00:32:44.650 --> 00:32:52.785
I've got the macro stuff, and I've got the mining stuff. So I've got all these different and that does even talk about the things that I really wanna talk about,

514
00:32:53.725 --> 00:33:01.779
helping people who are unbanked. I mean, that's a whole different category, and I don't really talk about it a whole lot anymore.

515
00:33:02.480 --> 00:33:05.380
McIntosh: What about the people in Argentina who are out in the

516
00:33:05.705 --> 00:33:06.685
in the sticks.

517
00:33:07.385 --> 00:33:08.745
And there's actually a,

518
00:33:10.025 --> 00:33:15.110
there's a topic well, it goes along with, we'll talk about it in the news. I apologize,

519
00:33:15.730 --> 00:33:16.950
McIntosh: it's lightning related,

520
00:33:17.410 --> 00:33:18.150
and it

521
00:33:18.690 --> 00:33:23.670
relates to this very idea that I just put out, this banking the unbanked.

522
00:33:24.045 --> 00:33:24.365
So,

523
00:33:24.925 --> 00:33:26.465
Kyron did boost there.

524
00:33:26.925 --> 00:33:31.265
I think that might have been our only boost. We got some good streaming.

525
00:33:32.510 --> 00:33:34.289
So his was a row of ducks

526
00:33:34.590 --> 00:33:35.330
and then

527
00:33:38.110 --> 00:33:38.610
5,126.

528
00:33:40.190 --> 00:33:46.275
So that is, of course, after the Satoshi tax, the Satoshi stream tax. So we're probably looking at,

529
00:33:46.735 --> 00:33:47.795
I don't know, 52.50

530
00:33:48.174 --> 00:33:49.155
or so total.

531
00:33:49.870 --> 00:33:51.810
And that's for this episode between

532
00:33:52.670 --> 00:33:55.970
the last one that I put out on Sunday and now.

533
00:33:56.885 --> 00:33:58.245
So I do appreciate that.

534
00:33:58.804 --> 00:34:01.945
I always appreciate the support we get at whatever amount.

535
00:34:03.580 --> 00:34:06.080
Let's jump on into the news.

536
00:34:07.659 --> 00:34:11.040
There's there was a bit of news, and this one thing in particular

537
00:34:11.585 --> 00:34:16.405
I wanted to talk about I post my news on Twitter. You can follow me at Macintosh Fintech

538
00:34:17.105 --> 00:34:19.765
on Twitter, and you'll kinda get it in real time.

539
00:34:21.920 --> 00:34:22.420
So

540
00:34:23.119 --> 00:34:25.619
I think this came up after the last

541
00:34:26 --> 00:34:27.220
episode, ironically.

542
00:34:30.444 --> 00:34:32.224
The current government in Argentina

543
00:34:32.684 --> 00:34:39.180
has abolished the income tax a week before the presidential elections. Their elections are, like, late this week

544
00:34:40.200 --> 00:34:42.540
or very early next week. I'm hoping Monday.

545
00:34:42.895 --> 00:34:46.915
We have some news about that, and I'll be honest. I mean, this is just dirty.

546
00:34:47.775 --> 00:34:48.895
McIntosh: These full these

547
00:34:49.615 --> 00:34:50.115
sorry.

548
00:34:50.910 --> 00:34:52.610
These people think that

549
00:34:54.270 --> 00:35:00.210
McIntosh: well, they're just trying to buy votes. I mean, it's very obvious. They could just turn right around and reinstate that right after the election.

550
00:35:01.095 --> 00:35:08.075
Now from the very latest data that I've seen today, it looks like this is not having any effect on people,

551
00:35:08.410 --> 00:35:09.630
McIntosh: and I hope it doesn't.

552
00:35:10.410 --> 00:35:13.630
McIntosh: And I don't know if he's the answer, Javier Millet.

553
00:35:15.290 --> 00:35:18.110
But I do know that the people who are in power there,

554
00:35:18.525 --> 00:35:19.425
it's a joke.

555
00:35:19.725 --> 00:35:20.945
The it's a wreck.

556
00:35:21.245 --> 00:35:23.185
The country's a wreck. Let's be honest.

557
00:35:23.725 --> 00:35:25.745
And they need something new. So

558
00:35:26.090 --> 00:35:29.550
maybe he's it. I don't know, and I've made that very clear.

559
00:35:30.250 --> 00:35:32.270
And I'm not I don't live in Argentina,

560
00:35:32.730 --> 00:35:35.710
so I have no dog in this hunt as they would say.

561
00:35:36.195 --> 00:35:38.295
So, anyways, on October 16th,

562
00:35:38.675 --> 00:35:41.015
I think that was Monday, that's when we got

563
00:35:41.635 --> 00:35:48.770
this report about Bitcoin, about BlackRock, about their spot ETF, and, like, you got this giant candle,

564
00:35:49.150 --> 00:35:54.610
and it's just straight up to 30,000, turn around, go right back down. But as I've said,

565
00:35:55.055 --> 00:35:55.555
the

566
00:35:56.015 --> 00:35:58.275
so it went back down to 27,000,

567
00:35:58.815 --> 00:36:00.115
less than 28,000,

568
00:36:00.494 --> 00:36:01.875
and now we're at 28,000,

569
00:36:02.415 --> 00:36:03.395
almost 800.

570
00:36:05.930 --> 00:36:09.950
New Bitcoin hash rate. Again, that's why we're seeing the increase in

571
00:36:10.810 --> 00:36:11.310
difficulty,

572
00:36:12.295 --> 00:36:12.795
440,000

573
00:36:14.135 --> 00:36:16.395
or not a 1,000. It's it's 440

574
00:36:17.575 --> 00:36:18.954
McIntosh: Exashash, I guess.

575
00:36:21.109 --> 00:36:31.444
McIntosh: By the way, a few weeks ago, I mentioned, oh, so I saw this crazy number and I reported it. It had to have been a glitch in the software. It very clearly said it was, like, 500 and something

576
00:36:31.744 --> 00:36:34.325
or 600 and something. There's no way,

577
00:36:35.960 --> 00:36:50.285
that was actually realistic. So I apologize. I try not to do things like that, but I did make a mistake. And I think even when I said it, I said this doesn't make sense, but I was just that's literally what I was seeing as I was recording. So right now, we're at roughly 440

578
00:36:50.984 --> 00:36:51.724
Exashash.

579
00:36:52.560 --> 00:36:53.460
The US

580
00:36:53.760 --> 00:36:57.780
secretary treasurer. I could not resist posting this. Janet Yellen.

581
00:36:58.800 --> 00:37:02.265
I she's our treasury secretary, so she's in charge of the money.

582
00:37:03.125 --> 00:37:09.540
America can absolutely fund afford to fund another war. Now I'm not gonna get into the politics of this, but, of course,

583
00:37:09.840 --> 00:37:14.020
we're sending money to the Ukraine. We're sending money to Israel.

584
00:37:15.245 --> 00:37:29.520
They're trying to approve another 100,000,000,000. Actually, I guess they approved it. Whatever. I don't it doesn't even matter anymore. They just print the money and send it. And she's saying, yeah, we can we can do another war. Hey. What if we open up a third one? Why don't we go ahead and open up maybe three, four?

585
00:37:32.075 --> 00:37:33.174
I'll just stop.

586
00:37:36.194 --> 00:37:39.015
Peter McCormick has posted a film

587
00:37:40.829 --> 00:37:42.049
actually about Argentina,

588
00:37:42.589 --> 00:37:44.049
45 minutes long.

589
00:37:45.150 --> 00:37:47.410
To be honest, I haven't watched it yet.

590
00:37:47.875 --> 00:37:51.575
It looks very interesting. I have not had the time. It's been a crazy week,

591
00:37:51.875 --> 00:37:55.335
but it's about the very things we were talking about on

592
00:37:56.160 --> 00:37:56.660
the

593
00:37:57.520 --> 00:37:58.900
podcast last week.

594
00:38:01.520 --> 00:38:04.725
Junk bonds now exceed top rated triple 8,

595
00:38:05.125 --> 00:38:05.945
triple a,

596
00:38:06.245 --> 00:38:07.145
excuse me,

597
00:38:07.445 --> 00:38:09.385
debt for the first time in history.

598
00:38:10.245 --> 00:38:12.025
So that goes back to the eighties.

599
00:38:13.830 --> 00:38:15.450
Spiral made a great video.

600
00:38:16.390 --> 00:38:20.090
The whole thing about the pigeons in this video is kinda stupid, but

601
00:38:20.494 --> 00:38:22.835
who is Bitcoin? It gives a great

602
00:38:23.295 --> 00:38:24.434
10 minute overview.

603
00:38:25.454 --> 00:38:33.450
It covers so many things that people think about Bitcoin that are wrong and whatever. It's a great little introduction. You should take a look at that.

604
00:38:37.245 --> 00:38:44.385
Their 1st prototype of their mining ASIC circuit board. I don't have a whole lot of hope for this, but to be honest, any competition,

605
00:38:44.990 --> 00:38:52.450
anything new in the mining space is good. We need more than, you know, a couple of Japanese companies that make cheaper stuff

606
00:38:53.465 --> 00:38:54.845
not Japanese, Chinese,

607
00:38:55.145 --> 00:38:55.805
and then

608
00:38:56.185 --> 00:39:00.205
basically overpriced American stuff. I mean, that's kinda what it is.

609
00:39:00.820 --> 00:39:04.600
Right. You got Bitmain. You've got the Whatsminer people,

610
00:39:05.140 --> 00:39:07.400
which I can never remember their actual name.

611
00:39:08.075 --> 00:39:10.255
Those are the Chinese companies and then

612
00:39:11.035 --> 00:39:15.855
and and Bitmain's the cheapest, and Bitmain's making the best equipment right now. It's inarguable

613
00:39:16.315 --> 00:39:19.150
unless they're just not reliable. We'll see.

614
00:39:20.170 --> 00:39:20.490
It's

615
00:39:21.049 --> 00:39:22.349
we need more competition.

616
00:39:24.010 --> 00:39:25.309
We need more competition,

617
00:39:26.015 --> 00:39:27.955
and we need things that

618
00:39:28.494 --> 00:39:31.795
end users can run at home, and I think that's very important.

619
00:39:33.670 --> 00:39:37.210
I don't need a machine that runs on 2 20 volt

620
00:39:37.829 --> 00:39:41.450
and sounds like a jet engine when you plug it in in my home

621
00:39:42.275 --> 00:39:45.175
and provides enough heat to heat my house because

622
00:39:45.555 --> 00:39:55.420
not that that's a terrible thing, but it's also extremely difficult to get rid of unless you, like, plummet into your heating unit, and that becomes a a really big thing.

623
00:39:56.280 --> 00:39:58.705
By the way, Janet Yellen, in an interview.

624
00:39:59.165 --> 00:40:00.945
This is the secretary treasurer.

625
00:40:01.325 --> 00:40:02.865
She literally said,

626
00:40:04.285 --> 00:40:05.905
I don't know where the 122%

627
00:40:06.765 --> 00:40:11.640
number comes from the US federal debt to GDP ratio is about 98%

628
00:40:12.660 --> 00:40:13.400
right now.

629
00:40:13.940 --> 00:40:14.839
It literally

630
00:40:15.375 --> 00:40:17.075
came from the Saint Louis Fed,

631
00:40:18.974 --> 00:40:19.474
and

632
00:40:19.855 --> 00:40:21.315
it is a 122%,

633
00:40:21.775 --> 00:40:23.395
and that's our debt to GDP.

634
00:40:26.990 --> 00:40:30.610
I'll just leave that there. I really wish they'd find somebody else.

635
00:40:34.085 --> 00:40:34.984
Bank of America

636
00:40:35.605 --> 00:40:36.105
reported

637
00:40:36.645 --> 00:40:37.145
131,000,000,000

638
00:40:39.045 --> 00:40:39.945
with a b,

639
00:40:40.450 --> 00:40:43.190
dollars of unrealized loss on securities

640
00:40:43.890 --> 00:40:47.750
in q three. So this is like t bills, treasury notes.

641
00:40:49.165 --> 00:40:50.385
McIntosh: In Q3

642
00:40:51.085 --> 00:40:51.825
they have

643
00:40:52.365 --> 00:40:57.425
unrealized. Meaning, if they sold them right now, this is how much they would be down,

644
00:40:58.260 --> 00:40:59
a $131,000,000,000.

645
00:41:01.540 --> 00:41:02.040
McIntosh: Alright.

646
00:41:02.420 --> 00:41:09.075
The bank industry in the United States at least is not on stable ground. And let's see.

647
00:41:10.015 --> 00:41:12.755
It is really starting to look like these

648
00:41:13.780 --> 00:41:22.119
spot ETFs are going to be approved. I think they have run out of steam. January 10th at this point would be the last day of approval,

649
00:41:23.775 --> 00:41:25.395
or outright refusal.

650
00:41:28.095 --> 00:41:33.300
So I will note that we will continue to monitor. I do believe, in my opinion,

651
00:41:34.880 --> 00:41:35.940
like I said earlier,

652
00:41:37.040 --> 00:41:41.780
especially if BlackRock gets approved, we're gonna immediately spike above 31,000,

653
00:41:42.464 --> 00:41:44.645
and then we'll see if it stays above that,

654
00:41:45.505 --> 00:41:52.260
Chinese property giant, Country Garden. So this is the second biggest one in China, I believe.

655
00:41:53.280 --> 00:41:59.059
It's Evergrande and then Country Garden. They've missed a final deadline to pay interest on a dollar bond.

656
00:41:59.905 --> 00:42:03.685
So they are going to end up going into bankruptcy, I would assume.

657
00:42:04.065 --> 00:42:07.820
There's a Wall Street Journal article about that. I'll have that in the show note.

658
00:42:08.700 --> 00:42:10.080
McIntosh: Last thing I wanted to mention.

659
00:42:11.260 --> 00:42:11.760
Yesterday,

660
00:42:12.140 --> 00:42:13.200
Lightning Labs,

661
00:42:14.940 --> 00:42:16.240
announced Taproot

662
00:42:16.540 --> 00:42:17.040
asset,

663
00:42:18.325 --> 00:42:19.145
which is

664
00:42:22.005 --> 00:42:25.385
McIntosh: they call it a protocol for assets on Bitcoin and lightning.

665
00:42:25.800 --> 00:42:32.540
So then they released it and said you can put it on the main net on the not the test net.

666
00:42:34.635 --> 00:42:35.694
McIntosh: What this allows

667
00:42:36.555 --> 00:42:38.414
is essentially stable coins

668
00:42:38.795 --> 00:42:39.615
on Bitcoin.

669
00:42:40.530 --> 00:42:44.550
And I actually think this could potentially prove to be very important.

670
00:42:44.930 --> 00:42:49.845
There's a lot of Bitcoin maximalists who say things like, you should only be working in Bitcoin.

671
00:42:51.665 --> 00:42:53.845
McIntosh: I understand where that comes from. However,

672
00:42:54.705 --> 00:42:56.245
McIntosh: I would argue, respectfully,

673
00:42:57.630 --> 00:43:00.530
these people have not been to places like

674
00:43:01.150 --> 00:43:02.210
parts of Africa

675
00:43:02.590 --> 00:43:04.210
or parts of South America

676
00:43:05.795 --> 00:43:10.615
McIntosh: where people live on less than $2 a day, US, if you convert it to US dollars,

677
00:43:11.850 --> 00:43:14.190
and or Lebanon. Any

678
00:43:14.490 --> 00:43:15.630
a lot of these places.

679
00:43:16.410 --> 00:43:17.150
They cannot

680
00:43:17.530 --> 00:43:18.030
handle

681
00:43:18.570 --> 00:43:19.310
the volatility

682
00:43:20.435 --> 00:43:21.255
of Bitcoin.

683
00:43:22.115 --> 00:43:26.935
Well, Bitcoin is going to go up. Well, yes. I agree with that.

684
00:43:27.930 --> 00:43:29.550
But if it drops 20%

685
00:43:29.930 --> 00:43:36.430
and that person can't buy the milk that they need to get through the week because of it, is that a good thing?

686
00:43:37.405 --> 00:43:37.905
McIntosh: No

687
00:43:39.005 --> 00:43:39.505
lightning

688
00:43:40.445 --> 00:43:42.225
taproot assets allows

689
00:43:43.165 --> 00:43:44.145
you to issue

690
00:43:45.430 --> 00:43:49.130
McIntosh: stable coins essentially on Bitcoin, on lightning specifically.

691
00:43:50.390 --> 00:43:53.369
So people can transact in US dollars,

692
00:43:54.225 --> 00:43:57.045
and that US dollar will be the same regardless

693
00:43:57.585 --> 00:44:03.605
of whether Bitcoin goes up or down. Is the US dollar depreciating? Is it becoming worthless?

694
00:44:04.609 --> 00:44:05.109
Absolutely,

695
00:44:05.890 --> 00:44:08.310
but at a much slower rate than, say,

696
00:44:09.250 --> 00:44:11.030
respectfully, the Argentine peso,

697
00:44:12.484 --> 00:44:14.744
which is one one of the reasons why Javier

698
00:44:15.045 --> 00:44:17.944
says that they want to switch to the US dollar.

699
00:44:20.620 --> 00:44:23.840
And as Diego pointed out, it's not pegging it to the dollar.

700
00:44:24.140 --> 00:44:24.960
If I understood

701
00:44:25.580 --> 00:44:29.495
him and recall correctly, it's actually using the US dollars. So

702
00:44:31.315 --> 00:44:32.215
that's why.

703
00:44:33.075 --> 00:44:33.575
And

704
00:44:34.570 --> 00:44:40.270
I'm not in their position, and I'm not going to tell somebody, look. You've got to you save in Bitcoin.

705
00:44:41.130 --> 00:44:44.875
You've got to keep everything in Bitcoin. You can't keep a US dollar.

706
00:44:45.335 --> 00:44:48.315
You shouldn't do that bad. Bad bit you know?

707
00:44:49.015 --> 00:44:54.950
No. If you need to keep it in Bitcoin, if you need to keep some savings in Bitcoin and some in

708
00:44:55.490 --> 00:45:00.550
some version of the US dollar, then do that. And let me provide you the tools to do that

709
00:45:00.914 --> 00:45:05.575
over the Bitcoin lightning network so that we can do things like send money instantaneously

710
00:45:06.355 --> 00:45:10.134
McIntosh: from the state of the United States to your country or vice versa

711
00:45:10.970 --> 00:45:12.750
for virtually nothing.

712
00:45:13.930 --> 00:45:17.549
McIntosh: So these things, I think, are gonna become very important. People don't realize

713
00:45:18.424 --> 00:45:19.005
how much

714
00:45:19.785 --> 00:45:22.125
of the market, for example, USDT,

715
00:45:22.664 --> 00:45:23.805
the Tether token,

716
00:45:24.265 --> 00:45:26.204
takes up. That's based on

717
00:45:26.770 --> 00:45:27.270
Ethereum.

718
00:45:27.650 --> 00:45:31.750
Why would I be pushing somebody to Ethereum if we can have that on Bitcoin?

719
00:45:32.930 --> 00:45:37.125
So I wanna point that out. It's a very important release. It's something that

720
00:45:37.505 --> 00:45:38.484
from a bankless

721
00:45:38.785 --> 00:45:43.845
perspective, again, going back to what I was talking about earlier, this is something that's very interesting to me.

722
00:45:44.670 --> 00:45:49.410
I don't understand, to be honest, exactly how that works. How do I issue

723
00:45:49.950 --> 00:45:51.570
a a dollar,

724
00:45:52.605 --> 00:45:55.745
but we know that the underlying Bitcoin can fluctuate.

725
00:45:56.605 --> 00:46:03.330
I'm looking into that. I have somewhat of an understanding, but I don't completely understand it. So maybe we talk about that

726
00:46:03.790 --> 00:46:04.690
down the road.

727
00:46:04.990 --> 00:46:05.490
Alright.

728
00:46:07.550 --> 00:46:09.410
I think that covers it. So

729
00:46:09.835 --> 00:46:14.255
we've already talked about this a little bit, so I won't harp on this too much, but Generation Bitcoin

730
00:46:15.115 --> 00:46:20.100
is a podcasting 2.0 podcast. We're a value for value podcast.

731
00:46:20.400 --> 00:46:24.980
There will never be a sponsor. Oh my goodness. I didn't even I got so sidetracked.

732
00:46:26.255 --> 00:46:27.075
That whole

733
00:46:28.175 --> 00:46:33.875
mining podcast I was listening to. They literally had to say at the front, oh, by the way,

734
00:46:34.660 --> 00:46:37.079
the people behind driving drive chain,

735
00:46:37.859 --> 00:46:39.319
the very people they were interviewing,

736
00:46:39.940 --> 00:46:40.920
paid us money,

737
00:46:44.395 --> 00:46:46.335
McIntosh: So that didn't change your viewpoint.

738
00:46:47.995 --> 00:46:49.375
I'll never have a sponsor.

739
00:46:49.910 --> 00:46:53.370
McIntosh: Paul could come to me and say, I will give you a $100,000, and I'll say

740
00:46:54.470 --> 00:46:54.970
McIntosh: no.

741
00:46:55.830 --> 00:46:57.610
It will be extremely hard,

742
00:46:57.934 --> 00:46:59.234
but I will say no.

743
00:47:00.335 --> 00:47:07.474
McIntosh: We have no advertising. You can support the podcast in 3 different ways, time, talent, and treasure. If you wanna support the podcast, it has a time or talent.

744
00:47:07.920 --> 00:47:10.660
There's stuff. There's stuff. Just send me a message. Okay?

745
00:47:11.200 --> 00:47:12.980
Treasure, we've already talked about.

746
00:47:13.360 --> 00:47:19.285
I appreciate immensely the people, those people who sit in those 5,000 sats this week. By the way,

747
00:47:19.585 --> 00:47:22.005
I meant to do this during support. If

748
00:47:22.465 --> 00:47:28.170
I continue to do this clips program, people are not taking me up on this. Please let me give you sats.

749
00:47:28.710 --> 00:47:35.530
If you make a clip of the 1st episode, hey. Go back and clip what I was talking about on that podcast.

750
00:47:36.615 --> 00:47:40.795
Do it, and I will post 500 sats to you, sir or ma'am.

751
00:47:42.055 --> 00:47:43.195
On an older episode,

752
00:47:43.660 --> 00:47:48.880
McIntosh: three hundred, and I'll do it right there. It'll go right into your lightning wallet. That's it. Done.

753
00:47:49.580 --> 00:47:51.280
I'll talk about that another time.

754
00:47:52.204 --> 00:48:04.210
McIntosh: If you like the content, I would love it if you tell your friends about Generation Bitcoin podcast. It is the best way to grow this podcast. Thanks for being here. I do hope this has been helpful. I know sometimes I get a little nuts,

755
00:48:04.590 --> 00:48:06.370
but it's because it's so important.

756
00:48:07.905 --> 00:48:12.005
I'm on Twitter at McIntosh Fintech. I'm on Mastodon at McIntosh podcast

757
00:48:12.625 --> 00:48:19.490
index dot social. That's it. I'm not even going through the rest. Stay humble friends. I'll talk to y'all next Monday.
```
