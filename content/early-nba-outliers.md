Title: Early season NBA trends
Date: 2025-11-18 10:20
Category: sports betting
Tags: basketball, bajillion

[!["Round 6", by Prince Jammy](https://img.youtube.com/vi/eyF1T1gGuzU/0.jpg)](https://www.youtube.com/watch?v=eyF1T1gGuzU){:target="_blank"}

Song: ["Round 6", by Prince Jammy](https://www.youtube.com/watch?v=eyF1T1gGuzU){:target="_blank"}

A few interesting statistics from the first dozen games of the 2025-26 NBA season.

I'm generally talking about stats per 100 possessions, rather than raw stats (unless otherwise noted).

### The absurd OKC Thunder
The OKC Thunder have been a godless basketball killing machine this year. Almost every win is a blowout, despite their second best player being injured. They look like they don't even have to try all that hard, and they're winning by an average of 16 points.

To me, their secret sauce is that they make it nearly impossible to score against them. There are no easy buckets. Here are some good ways to get easy points in the NBA:

1. make lots of 3's
2. get lots of free throws (and make them)
4. take a lot of shots close to the basket
5. get points off of turnovers
6. get out on the fast break
7. get second chance points

The Thunder are middle of the pack at the first two. They're only 15th in 3 pointers made against them per game, and 12th in free throws given up.

They're ridiculously elite at everything else that makes scoring hard. The Thunder are first in the league at:

1. Defensive Rating
2. Defensive Rebounding
3. Steals
4. Fewest opponent fast break points
5. Fewest opponent points in the paint
6. Fewest opponent points scored
7. Lowest opponent effective FG%

They're second in the league at:

1. Fewest turnovers
1. Fewest opponent points off turnovers
2. Fewest opponent 2nd chance points
3. Fewest opponent assists
4. Most opponent turnovers

The most remarkable part is how they've built their team. Their 3rd and 4th leading scorers, Ajay Mitchell and Aaron Wiggins, were both 2nd round draft picks. Their 5th leading scorer, Isaiah Joe, was a 2nd round pick by the 76ers who got waived, then refurbished by the Thunder like an estate sale armoire. Their best defender, Lu Dort, went undrafted. 

The team just finds a way to bring the best out of players that any other team *could* have had. What did they see that everybody else missed, and what did they do to develop them?

As a fan of another NBA team, and someone who lived in Seattle in the 15 years after the Sonics were stolen away to OKC, I [want to get off Mr Presti's Wild Ride](https://knowyourmeme.com/memes/mr-bones-wild-ride). But statistically, it's great.

### Bucking trends
Victor Wembanyama is by far the best shot blocker in the NBA, averaging 3.6 blocks a game. But the Spurs are only 6th overall in blocks. Nikola Jokic is by far the best passer in the NBA, but the Nuggets are only 5th overall in assists. Steph Curry is the best 3 point shooter of all time. But the Warriors are only 12th in 3 point percentage. This isn't all that surprising. Just because one player is good at a particular skill, that doesn't mean the rest of the team is.

What's more surprising to me is that Giannis Antetokounmpo draws the most free throws in the league, but the Bucks are 28th in free throw attempts. Teams that get a lot of free throw attempts tend to attack the basket a lot, or be the Los Angeles Lakers. The Bucks are weird because pretty much only Giannis does anything free throw-worthy. At the time I wrote this, Center Myles Turner had not shot a single free throw in his last 63 minutes of game time. That doesn't seem like a recipe for success for the Bucks.

### Basketball is broken
And I know the guy who did it: Nikola Jokić. Advanced stats aren't everything, but right now he has a Win Shares per 48 (WS/48) of .441. Win Shares are probably a little biased towards big men who score efficiently, and affected by the pace of the game. That aside, it's a pretty good stat as far as having a single number to quantify how good somebody is at basketball. It correlates pretty strongly with actual basketball watching, I think. The top players in WS/48 are usually the top candidates for the MVP every year. And it matches who we think the best players are historically.

Last year, the top player by WS/48 was Shai Gilgeous-Alexander, at .309. The year before, it was Jokic, at .299. The year before, it was Jokic at .308. In 2014, it was Steph Curry, at .288. In 2004, when the pace of play was slower, the leaders were Nowitzki and Garnett at .248. In 1994, it was David Robinson, at .273.

Pretty much anything over .250 is an MVP caliber season. There's really no historical precedent for a WS/48 of .441. After 12 games played, Jokic could be the worst player in the league for the next 7 games, and he'd still be having an MVP-type season overall.

Before last game, it was .448. What did Jokic do last game that caused his WS/48 to go down a tiny bit? He got 36 points, 18 rebounds, and 13 assists, on good scoring efficiency and only 2 turnovers. That's a slightly below average game for him right now.

### The perils of hand-rolled metrics, pt. 137
I was trying to put together something to show how historically off the charts OKC has been defensively. I started with using a fancy technique, PCA, before realizing that just adding up the ranks of each of the statistics was better and simpler. If one team is 1st in blocks, 2nd in steals, 2nd in opponent points in thde paint, etc., just add the ranks up, lowest score is best.

I ran it on every team over the last 15 years. All of the teams that did well on my metric were good defensively, and the teams that did poorly were putrid on defense. It's not totally useless. But it's a bad way to find the best teams of all time.

Here are the top defensive teams since 2010 by this metric:

1. the 2025-26 OKC Thunder
2. The 2018-19 Milwaukee Bucks (won 60 games with peak Giannis)
3. The 2010-11 Philadelphia 76ers (last Iguodala season, young Jrue Holiday)
4. The 2019-20 Orlando Magic (Aaron Gordon and some guys)
5. The 2017-18 Utah Jazz (the "you got Jingled" meme team that beat OKC)

Ah well. That's not a terrible list. They were all very good at defense, and made it a big part of their team identity, but I don't think those are really the best defensive teams of the last 15 years. A team's rank by Defensive Rating is still a better predictor of the team's win percentage than my attempts.

There's definitely some [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart's_law) potential here. OKC are near the top of a bunch of statistical categories, because they are good at defense overall. You can't necessarily get on their level just by trying to copy specific things OKC does well, like prevent fast break points.

### We see you, Jalen Duren
More like Jalen Durian, because some of the things he's doing are just nasty. You will definitely get kicked off the bus in Singapore if you're watching Jalen Duren highlights.

### Data used
All data from https://www.nba.com/stats/

I had to screen scrape some stuff from their website, since some of the endpoints in the python `nba_api` package are broken now.  See the `early-nba-trends.ipynb` notebook for code.