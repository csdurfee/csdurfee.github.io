Title: LeBron James, the Unstreaky King
Date: 2025-06-12 10:20
Category: sports analytics
Tags: basketball, the hot hand

In previous installments, I've shown that NBA players are, as a whole, less streaky than they should be. This is apparent in game-level data, and more obvious looking at multi season trends.

So far, I've only looked at the past few seasons of the NBA. I decided to gather as much data as I could, analyzing every single shot taken in the NBA from 2004 to 2024.

Data is taken from https://www.kaggle.com/datasets/mexwell/nba-shots.

## The streakiest games of the past 20 years
As I showed in the last installment, there are two ways of measuring how relatively streaky each individual game is. We can use the normal approximation from the Wald-Wolfowitz test, or we can calculate the percentile ranks from the exact probabilities.

These two metrics give different answers to what is the streakiest game of the past 20 years.  According to percentile rank, the streakiest ever was Cedi Osman, who in 2022 missed 10 shots in a row, followed by making 6 shots in a row, for an equivalent z-score of -3.6.

According to the normal approximation, the streakiest game ever was Chris Bosh in 2007, who made 15 shots in a row before missing his final 4. Bosh doesn't even make the top 5 by percentile rank. 

Other strong performances include Andre Iguodala, who had 16 straight misses followed by 3 makes in 2008, and Willie Green, who had 5 misses followed by 12 makes. The sheer length of those streaks is impressive, but to maximize the number of expected streaks, there need to be similar numbers of makes and misses. A game with 5 makes and 5 misses has a maximum of 10 streaks. A game with 15 makes and 4 misses, like Chris Bosh, has a maximum of 9 streaks.

Kobe Bryant's final game in the NBA also deserves mention. He went an extremely streaky 22 for 50, earning the highest number of expected streaks in the data I have (25.64): `11111000100110000101110000101100001100001111100000`

## The least streaky games
The least streaky was by Richard Hamilton in 2006, who had 10 makes and 13 misses, no two makes in a row: `01001010101010010101010`

Kyrie Irving, Dejounte Murray (previously covered), and Kevin Martin also had strong showings. 

# The un-streaky king
The 4th most un-streaky game of the past 20 years belongs to LeBron James.  [LeBron scored 31 points in an easy win over the SuperSonics in 2005](https://www.basketball-reference.com/boxscores/200511090CLE.html). Aside from 2 makes in a row at the start of the game, he perfectly alternated makes and misses the rest of the game: `110101010101010101`

In the 20 years of shot data I analyzed, LeBron stands out as by far the most un-streaky player. Here are the career z scores of every player from 2004-2024:

![career-z-scores](/img/career-z-scores.png)

LeBron can't even be seen on this chart. He is in a world of his own, with a career z score of 5.9. We have to go to the Jon Bois style scatterplot with one extreme outlier in the corner:

![career-z-scatter](/img/career-z-scatter.png)

If this were a Youtube video, imagine me zooming in on the solitary dot in the upper right while the saxophone hook from [Baker Street](https://youtu.be/BO1qcWa6blQ?t=22) kicks in.

Which is to say, it's really, really unlikely. The odds are around 1 in 550 million. That puts him in the 99.9999998th percentile.

If all 8.2 Billion people on the planet had LeBron's NBA career, taking over 29,000 shots like he has, at the same FG% he did, we'd expect 15 people to be that unstreaky or more. That's elite company. Not only is LeBron James the LeBron James of basketball, he's also the LeBron James of being unstreaky at basketball.

As both the most unstreaky player of all time, and the most prolific scorer of all time, LeBron James makes a perfect test subject for understanding unstreakiness.

He's had 15,159 shooting streaks in his career so far, which is 504 more streaks than expected.  Say LeBron takes a low percentage shot because he feels like he has the hot hand. It might be lower, but it's probably not dramatically worse than his regular shot. So for him to have 500 more streaks than expected, that's potentially thousands of choices LeBron has made over his career that increased the likelihood of streaks getting broken.

## Streak lengths
I simulated LeBron's career 1000 times and compared the frequency of streak lengths to his actual career. Here are his actual streaks compared to the expected frequencies:

![lebron-make-streaks](/img/lebron-make-streaks.png)

![lebron-miss-streaks](/img/lebron-miss-streaks.png)

He has slightly more 1 and 2 shot make/miss streaks than expected, and fewer streaks of 5-6 or more.

Previously I discussed that players could cause unstreakiness because they "go get a bucket" when the "shot isn't falling" -- in other words, they take higher percentage shots when they're on a cold streak. They might try to draw contact from a defender, and if they do get fouled, it only counts as a shot attempt if the shot goes in. On the other hand, they might take risky "heat check" shots when they are performing relatively well because they feel like they can't miss.

To capture "hot" versus "cold", I decided to track the FG% over the previous 5 shots in the game. So, it's undefined for the player's first 5 shots of the game, then defined from the 6th on. Because LeBron is such a high volume scorer and has been for so many years, that's still a lot of data to look at. 

here are the number of shot attempts by LeBron by each "last 5" shooting percentage.

```
NaN    7460
0.6    7222
0.4    6906
0.8    3518
0.2    3090
1.0     612
0.0     503
```

I have defined *cold* as making 0 or 1 of the last 5 shots, and *hot* as making 4 or 5 of the last 5. This was a semi-arbitrary choice based on make/miss streaks longer than 5 happening less frequently than chance would dictate. It also matches how my simulated un-streaky player works.

There's a clear trend. LeBron's FG% is 10% higher when he's missed his last 5 shots than when he's made his last 5.

![lebron-last-5](/img/lebron-last-5.png)

That's a pretty big swing.

## LeBron is un-streaky due to shot selection
What's behind this trend?

LeBron takes a lot more high percentage shots when he's *cold* versus when he's *hot*.

```
Change in shot rates (cold minus hot):

Above the Break 3       -0.119694
Backcourt               -0.001659
In The Paint (Non-RA)    0.023637
Left Corner 3            0.000429
Mid-Range               -0.056841
Restricted Area          0.159098
```

When he's *hot*, he takes 29% of his shots in the restricted area (right near the basket, which is his highest percentage shot). When LeBron's *cold*, that jumps up to 45% of his shots. When he's hot, 29% of his shots are above the break 3's, but he only takes that shot 17% of the time when he's *cold*.

LeBron's FG% at each type of shot doesn't change much between times when he's *hot* and *cold* and *in between*. He's a tiny biy better at corner 3's when he's cold vs. hot, but that's on very small volume. LeBron is usually attacking the middle of the court, not standing in the corner. 

He's actually slightly worse at his three most common shot types (above the break 3, mid-range, restricted area) when he's on a cold streak. He's not un-streaky because he suddenly becomes a better shooter. He chooses to "go get a bucket" and seek out a higher percentage shot.


```
Change in FG% (cold minus hot):

Above the Break 3       -0.036856
In The Paint (Non-RA)    0.001647
Left Corner 3            0.026525
Mid-Range               -0.023709
Restricted Area         -0.013754
Right Corner 3           0.157949
```

It looks like it cuts both ways. LeBron takes lower percentage shots when he's shooting well, and higher percentage shots when he's shooting poorly over the past 5 shots, compared to the average performance.

TODO: Visualization here

## Shot order trends

LeBron's FG% appears to trend downward with the more shots that he takes in a game. The white line is his career average:

![seq-vs-fg](/img/seq-vs-fg.png)

I haven't looked into it yet, but I suspect this is partially due to LeBron often taking the last shot of the game. Final shots of the game should be harder than average if it's a close game. Everybody knows the ball's going to LeBron for the final shot, so the defense is keying in on him. I'll save that for another installment, though.

## Other unstreaky guys
Kyle Kuzma, Julius Randle, Elton Brand, and Anthony Edwards are all in the 4+ z score club, with Luka Doncic, Giannis, John Henson, Goran Dragic, and Jordan Poole also in the top 10.

## League-wide trends
I went back and did the same analysis for every non-LeBron shot over the last 20 years. The league as a whole doesn't show the same trends that LeBron does. FG% isn't correlated with number of makes of the last 5. Here are the shooting percentages, graphed on the same scale as the one I used for LeBron:

![league-last-5](/img/league-last-5.png)

There's a very slight uptick when a player has made all 5 of their last 5 shots in the game, but otherwise it's remarkably flat.

Looking at the order of of shots taken, the NBA as a whole shows the same rough trend as LeBron's, though less dramatically. Lower FG% on the first shot of the game, and FG% slowly going down as the number of attempts goes up. (Again, I've locked the Y axis to match the scale of LeBron's.)

![league-shot-seq](/img/league-shot-seq.png)

Not a lot there in aggregate. I also looked at just higher volume shooters, but there wasn't a trend I could see there.

Finally, I looked at players with a z-score over 2 (aside from LeBron). Now, by artificially selecting players with a high z-score, I need to be careful with my analysis to avoid self-fulfilling prophecy. 

By definition, they're going to seem more unstreaky. But it's notable they're unstreaky in the same way as LeBron -- higher shooting percentage when they're *cold* and lower when they're *hot*. It's not a strong trend, but it's there. They shoot 47% when they've missed their last 5 in a row, and 44.8% when they've made their last 5 in a row. If the high Z scores were solely due to chance, I wouldn't expect to see such a clear pattern in the last 5 data.

![high-z-last5](/img/high-z-last5.png)


## Streaky guys
There's only one super streaky guy in the last 20 years, Ivica Zubac, with a Z score of -3.98. That's pretty crazy, but still plausibly within the realm of chance, around 1 in 30,000.

The other guys with extremely streaky behavior on high volume are Dwight Powell, Nemanja Bjelica, Erick Dampier, Aaron Nesmith and Rudy Gobert, with z scores around -3. Most of those guys are big men who aren't primarily scorers. I wonder if it has something to do with rebounding their own shot. Sometimes a big man who isn't good at shooting will do what I call the Moses Malone -- miss a shot, get their own rebound, miss that, get their own rebound again, shoot again, etc, which might produce longer streaks of misses than makes.

However, I don't think there's a need to deeply analyze the streaky players at this point, because it could be due to chance alone. 

## Goofy Nonsense
Zydrunas Ilgauskas was a longtime player for the Cleveland Cavaliers who was nicknamed "The Big Z". However, his career z score was only 1.49, so I don't think it's a statistics based nickname. Which is too bad, because the game could use some of those. "Small Z" for Ivica Zubac's -3.98 score might be confusin to people, unfortunately.

## Final thoughts
If I were LeBron's coach, I'd try to talk him out of believing he has the hot hand, because as we've seen, acting like it exists has caused him to be the most *lukewarm handed* player of the past 20 years.

Shot selection shouldn't change for the worse just because a player is shooting well. LeBron on a hot streak has roughly the same shooting percentages for each type of shot as when he's not on a hot streak, or when he's on a cold streak. 

His innate shooting skill doesn't change, he just takes lower percentage shots, perhaps believing they're not really lower percentage shots when he's *feeling it*. It's feel vs. real, as it often is in sports, and life in general. Regardless of feel, they're still worse shots than he would normally take.

Going the other way, it's like the old joke about an airplane's black box -- if black boxes are indestructible, why don't they just build the whole airplane out of that material? If LeBron has a higher shooting percentage when he's *cold* and decides to "go get a bucket", and that works, why doesn't he just do that on every play?

I don't have a statistical answer to that question, but I do have a common sense one. In sports, part of the game is making the other team have to handle as many possibilities at a time. A quarterback in football shouldn't throw deep passes every play, because that's easy to defend. A baseball pitcher shouldn't just throw their best pitch every time, because that's easy for the hitter to anticipate. 

Likewise, LeBron probably shouldn't just put his head down and "get a bucket" every possession, because that's easy to plan against. LeBron wouldn't be an all time great if he only shot in the restricted area. While 3 pointers and midrange shots may have a lower expected value versus driving to the hoop, they force the defender to worry about LeBron no matter where he is on the court. But I think both as a hoops fan and a data nerd, trying to create a high percentage shot isn't a bad thing to do when a player is struggling in a game. That's especially true if a player can become less engaged in other aspects of the game when they are shooting poorly.