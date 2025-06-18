Title: The hot hand doesn't exist in the NBA, but its opposite does
Date: 2025-05-16 10:20
Category: sports analytics
Tags: basketball, the hot hand

(The code used, and ipython notebooks with a fuller investigation of the data is available at [https://github.com/csdurfee/hot_hand](https://github.com/csdurfee/hot_hand).)

# Streaks
When I'm watching a basketball game, sometimes it seems like a certain player just can't miss. Every shot looks like it's going to go in. Other times, it seems like they've gone cold. They can't get a shot to go in no matter what they do. 

This phenomenon is known as the "hot hand" and whether it exists or not has been debated for decades, even as it's taken for granted in the common language around sports. We're used to commentators saying that a player is  "heating up", or, "that was a heat check".

As a fan of the game, it certainly seems like the hot hand exists. If you follow basketball, some names probably come to mind. JR Smith, Danny Green, Dion Waiters, Jamal Crawford. When they're on, they just can't miss. It doesn't matter how crazy the shot is, it's going in. And when they're cold, they're *cold*.

It's a thing we collectively believe in, but it turns out that there isn't clear statistical evidence to support it.

We have to be careful with our feelings about the hot hand. It certainly feels real, but that doesn't mean that it is. Within the drama of a basketball game, we're inclined to notice and assign stories to runs of makes or misses. Just because we notice them, that doesn't mean they're significant. This is sometimes called "the law of small numbers" -- our brains have a tendency to reach spurious conclusions from a very small amount of data.

[Pareidolia](https://en.wikipedia.org/wiki/Pareidolia) is the human tendency to see human faces in inanimate objects -- clouds, the bark of a tree, a tortilla. While the faces might seem real, they are just a product of our brain's natural inclination to identify patterns. It's possible the "hot hand" is a similar phenomenon -- a product of the way human brains are wired to see patterns, rather than an objective truth.

## Defining Streakiness

Streaks of 1's and 0's in randomly generated binary data follow regular mathematical laws, ones our brains can't realy replicate. Writer [Joseph Buchdal](https://www.football-data.co.uk/blog/Wald_Wolfowitz.php) found that he couldn't create a random-looking sequence by hand that would fool a statistical test called the Wald-Wolfowitz test, even though he knew exactly how the statistical test worked.

I think at some level, we're physically incapable of generating truly random data, so it makes sense to me that our intuitions about randomness are a little off. Our brains are wired to notice the streaks, but we seem to have no such circuitry for noticing when something is a little bit too un-streaky. Our brains are too quick to see meaningless patterns in small amounts of data, and not clever enough to see subtle, meaningful patterns in large amounts of data. Good thing we have statistics to help us escape those biases!

For the sake of this discussion, a streak starts whenever a sequence of outcomes changes from wins (W) to losses (L), or vice-versa. (I'm talking about makes and misses, but those start with the same letter, so I'll use "W" and "L".)

The sequence `WLWLWL` has 6 streaks: `W, L, W, L, W, L`        
The sequence `WWLLLW` has 3 streaks: `WW, LLL, W`

Imagine I asked someone to produce a random-looking string of 3 W's and 3 L's. If they were making the results up, I think the average person would be more likely to write the first string. It just looks "more random", right? 

If they flipped a coin, it would be more likely to produce something with longer streaks, like the second example. With a fair coin, both of those *exact* sequences are equally likely to occur. But the second sequence has a more probable number of streaks, according to the [Wald-Wolfowitz Runs Test](https://en.wikipedia.org/wiki/Wald%E2%80%93Wolfowitz_runs_test). The expected number in 3 wins and 3 losses is (2 * (3 * 3) / (3+3)) + 1 = 4.

The expected number of streaks is the [harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean) of the number of wins and the number of losses, plus one. Neat, right?

Around 500 players attempted a shot in the NBA this season. Let's say we create a custom coin for each player. It comes up heads with the same percentage as the player's shooting percentage on the season. If we took those coins and simulated every shot in the NBA this season, some of the coins would inevitably appear to be "streakier" than others.

Players never intend to miss shots, yet most players shoot around 50%, so there has to be some element of chance as far as which shots go in or not. Otherwise, why wouldn't players just choose to make all of them?

So makes versus misses are at least somewhat random, which means if we look at the shooting records of 500 players in an NBA season, some will seem more or less consistent due to the laws of probability. That means a player with longer or shorter streaks than expected could just be due to chance, not due to the player actively doing something that makes them more streaky.

## The Lukewarm Hand
We might call players who have fewer streaks than expected by chance *consistent*. Maybe they go exactly 5 for 10 every single game, never being especially good or especially bad. Or maybe they go 1 for 3 every game, always being pretty bad.

But that feels like the wrong word, and I don't think our brains aren't really wired to notice a player that has fewer streaks than average. As we already saw, the "right" number of streaks is counterintuitive. 

I might notice a player is unusually consistent after the fact when looking at their basketball-reference page, but the feeling of a player having the *hot hand* is visceral, experienced in the moment. Even without consulting the box score, sometimes players look like they just can't miss, or can't make, a shot. They seem more confident, or their shot seems more natural, than usual. Both the shooter and the spectator seem to have a higher expectation that the shot will go in than usual. The hot hand is a social phenomenon.

![there's always an xkcd](/img/xkcd-sports.png)    
(from [https://xkcd.com/904/](https://xkcd.com/904/))

If we look at the makes and misses of every player in the league, do they look like the results of flipping a coin (weighted to match their shooting percentage), or is there a tendency for players to be more or less streaky than expected by chance? 

We don't really have a formal word for players who are less streaky than they should be, so I'm going to call the opposite of the *hot hand* the *lukewarm hand*. While the *lukewarm hand* isn't a thing we would viscerally notice the way we do the *hot hand*, it's certainly possible to exist. And it's just as surprising, from the perspective of treating basketball players like weighted coins. 

Some people I've seen analyze the hot hand treat the question as *streaky* versus *non-streaky*. But it's not a binary thing. There are two possible extremes, and a region in between. It's *unusually streaky* versus *normal amount of streaky* versus *unusually non-streaky*.

The Wald-Wolfowitz test says that the number of streaks in randomly-generated data will be normally distributed, and gives a formula for the variance of the number of streaks. The normal distribution is symmetrical, so there should be as many *hot hand* players as *lukewarm hand* ones. Players have varying numbers of shots taken over the course of the season so we can't compare them directly, but we can calculate the z score for each player's expected vs. actual number of streaks. The z score represents how "weird" the player is. If we look at all the z-scores together, we can see whether NBA players as a whole are streakier or less streaky than chance alone would predict. We can also see if the outliers correspond to the popular notions of who the streaky shooters in the NBA are.


## Simplifying Assumptions
We should start with the assumption that athletes really are weighted random number generators. A coin might have "good days" and "bad days" based on the results, but it's not because the coin is "in the zone" one day, or a little injured the next day. At least some of the variance in a player's streakiness is due to randomness, so we have to be looking for effects that can't be explained by randomness alone.

So I am analyzing all shots a player took, across all games. This could cause problems, which I will discuss later on, but splitting the results up game-by-game or week-by-week leads to other problems. Looking at shooting percentages by game or by week means smaller sample sizes, and thus more sampling error. It also means that comparisions between high volume shooters and low volume shooters can be misinterpreted. The high volume shooters may appear more "consistent" simply because it's a larger sample size.

I think I need to prove that *streakiness* exists before making assumptions about how it works. Let's say the "hot hand" does exist. If a player makes a bunch of shots in a row, how long might they stay hot? Does it last through halftime? Does it carry over to the next game? How many makes in a row before they "heat up"? How much does a player's field goal percentage go up? Does a player have cold streaks and hot streaks, or are they only streaky in one direction?

There are an infinite number of ways to model how it could work, which means it's ripe for overfitting. So I wanted to start with the simplest, most easily justifiable model. The [original paper about the hot hand](https://www.sciencedirect.com/science/article/abs/pii/0010028585900106?via%3Dihub) was co-written by Amos Tversky, who went on to win a Nobel Prize for helping to invent behavioral economics. I figure any time you can crib off of a Nobel Prize winner's homework, you probably should!

## Results
I started off by getting data on every shot taken in the 2024-25 NBA regular season. I calculated the expected number of streaks and actual number, then a z-score for every player.

Players with a z-score of 0 are just like what we'd expect from flipping a coin. A positive z-score indicates there were more streaks than expected. More streaks than expected means the streaks were shorter than expected, which means less streaky than expected. 

A negative z-score indicates the opposite. Those players had fewer streaks than expected, which means the streaks were longer.  When people talk about the "hot hand" or "streaky shooters", they are talking about players who should have a negative z-score by this test.

![all players, 2024-5](/img/all-players-2024.png)

The curve over the top is the distribution of z-scores we'd expect if the players worked like weighted coin flips. 

Just eyeballing it, it's pretty close. It's definitely a bell curve, centered pretty close to zero. If there is a skew, it's actually to the positive, un-streaky side, though.  The mean z-score is .21, when we'd expect it to be zero.

```
count    554.000000
mean       0.212491
std        1.075563
min       -3.081194
25%       -0.546340
50%        0.236554
75%        0.951653
max        3.054836
```

The Wilk-Shapiro test is way to decide whether a set of data plausibly came from a normal distribution. It passed. There is no conclusive evidence that players in general are streakier or less streaky than predicted by chance. This data very well could've come from flipping a bunch of coins.

But it's still sorta skewed. There were 320 players with a positive z-score (un-streaky) versus 232 with a negative z-score (streaky). That's suspicious.


## Outliers
A whole lot of those 554 players didn't make very many shots.  

![numer of makes, 2024-5](/img/makes-2024.png)

I decided to split up players with over 100 makes versus under 100 makes. Unlike high volume shooters, the low volume shooters had no bias towards unstreakiness. They look like totally random data.

Here are just the high volume shooters (323 players in total). Notice how none of them have a z-score less than about -2. It should be symmetrical.

![over 100 makes, 2024-5](/img/over-100-makes.png)

```
count    323.000000
mean       0.347452
std        1.068341
min       -2.082528
25%       -0.454794
50%        0.363949
75%        1.091244
max        3.054836
```

There were 20 players with a z-score less than -2 versus only 2 players with a score greater than 2.

## The Eye Test
I looked at which players had exceptionally high or low z scores. The names don't really make sense to me as an NBA fan. There were players like Jordan Poole and Jalen Green, who I think fans would consider streaky, but they had exceptionally un-streaky z-scores. I don't think the average NBA fan would say Jalen Green is less streaky than 97.5% of the players in the league, but he is (by this test).

On the other hand, two streakiest players in the NBA this year were Goga Bitadze and Thomas Bryant, two players who don't fit the profile of the stereotypical streaky shooter by any means.

## Makes vs. Streakiness

The more shots a player made this season, the less streaky they tended to be. Here's a plot of makes on the 2024-25 season versus the z-score.

![makes vs z-score](/img/makes-vs-zscore.png)

That's pretty odd, isn't it?

## Getting more data: 2021-present

I figured a bigger sample size would be better. Maybe this season was just weird. So got the last 4 seasons of data (2021-22,2022-2023, 2023-2024, 2024-2025) for players who made a shot in the NBA this season and combined them.

The four year data is even more skewed towards the *lukewarm hand*, or un-streaky side, than the single year data.

![all players, 2021-2025](/img/all-players-four-year.png)

```
count    562.000000
mean       0.443496
std        1.157664
min       -4.031970
25%       -0.312044
50%        0.449647
75%        1.184918
max        4.184025
```

The correlation between number of makes and z-score is quite strong in the 4 year data:

![2021-2025 z score vs makes](/img/four-year-makes-vs-zscore.png)

There were 48 players with a z-score > 2, versus only 9 with a score <-2. That's like flipping a coin and getting 48 heads and 9 tails. There's around a 2 in 10 million chance of that happening with a fair coin.

## High Volume Shooters, Redux

The bias towards the lukewarm hand is even stronger among high volume shooters. Here are players with more than 500 makes over the past 4 years.

![over 500 makes](/img/over-500-makes.png)

The z-scores are normally distributed according to the Wilk-Shapiro test, but they're no longer even close to being centered at zero. They're also overdispersed (the std is bigger than the expected 1.) It's not plausible that the true mean is 0, given the sample mean is .680.

```
count    265.000000
mean       0.680097
std        1.217946
min       -2.392061
25%       -0.149211
50%        0.776917
75%        1.485595
max        4.184025
```
![high volume hist](/img/high-volume-hist.png)

## Streak Lengths

I looked at the length of make/miss streaks for the actual NBA players versus simulating the results. The results were simulated by taking the exact number of makes and misses for each NBA player, and then shuffling those results randomly. What I found confirmed the "lukewarm hand" -- overall, NBA players have slightly more 1 and 2 shot streaks than expected, and fewer long streaks than expected.

![streaks](/img/streaks.png)

## Obvious objections, and what about free throws?

I'm treating every field goal attempt like it has the same chance of going in. Clearly that's not the case. Players, especially high volume scorers, can choose which shots they take. It's easy to imagine a player that has missed several shots in a row and is feeling "cold" would concentrate on only taking higher percentage shots. There's also the fact that I'm combining games together. That could potentially lead to players looking less streaky than they are within the course of a single game. But it should also make truly unstreaky players look less *unstreaky*. Streaks getting "reset" by the end of the game should make players act more like a purely random process -- not too streaky or unstreaky. It shouldn't increase the standard deviation of the z-scores like we're seeing, or cause a shift towards unstreakiness. 

I may do a simulation to illustrate that, but in the meantime, the most controlled shot data we have is free throw data. Every free throw should have exactly the same level of difficulty for the player. 

I got the data for the 200,000+ free throws in the NBA regular season over the past four years (October 2021 through April 2025).

Here are the z-scores for all players. There's a big chunk taken out of the middle of the bell curve, but it's normal-ish other than that.

![free throws](/img/free-throws.png)

240 players have made over 200 free throws in the past 4 years. When I restrict to just those players, there's a slight skew towards the "hot hand", or being more streaky than expected. There are no exceptionally *lukewarm hands* when it comes to free throws. It's sort of the mirror image of what we saw with high volume field goal shooters.

![free throws, over 200 makes](/img/over-200-ft.png)

```
count    240.000000
mean      -0.144277
std        1.021330
min       -2.686543
25%       -0.854723
50%       -0.174146
75%        0.660302
max        1.845302
```

## Conclusions, for now
I feel comfortable concluding that the hot hand doesn't exist when it comes to field goals. I can't say why there's a tendency towards *unstreakiness* yet, but I suspect it is due to shot selection. Players who have made a bunch of shots may take more difficult shots than average, and players who have missed a bunch of shots will go for an easier shot than average. While players can't choose when to "heat up" or "go cold", they can certainly change shot selection based on their emotions or the momentum of the game.

There may be a slight tendency towards the hot hand when it comes to free throws. It's worth investigating further, I think. But the effect there doesn't appear to be nearly as strong as the *lukewarm hand* tendency for field goals.