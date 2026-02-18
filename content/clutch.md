Title: NBA clutch statistics
Date: 2026-02-17 10:20
Category: basketball
Tags: basketball

[![iiO – Rapture (Deep Dish Space Remix)](https://img.youtube.com/vi/RJmsNX9emKs/0.jpg)](https://www.youtube.com/watch?v=RJmsNX9emKs){:target="_blank"}

Song: [iiO – Rapture (Deep Dish Space Remix)](https://www.youtube.com/watch?v=RJmsNX9emKs){:target="_blank"}

Notebook: [https://github.com/csdurfee/csdurfee.github.io/blob/main/notebooks/nba-clutch-stats.ipynb](https://github.com/csdurfee/csdurfee.github.io/blob/main/notebooks/nba-clutch-stats.ipynb)

This week, I'm discussing [team clutch statistics from nba.com](https://www.nba.com/stats/teams/clutch-traditional?Season=2010-11).

A basketball player who tends to make good plays in high-pressure situations is known as being "clutch". When the game is on the line, who do you want taking the last shot, or guarding the other team's best player?

Like a lot of other psychological phenomena, I think "clutchness" is mostly somethine we notice in retrospect.It's easy to remember when our favorite players "came up clutch". It's harder to remember times when they didn't, and perhaps impossible to accurately calculate whether a player is clutcher than average or not without using statistics. Our brains just don't tally raw statistics very well.

With the *hot hand* phenomenon, we notice a player "can't miss" after they've already made a few shots in a row, and then they make another one. Although I've shown that the opposite of the hot hand exists in the NBA, I can't argue against the feeling that a player is *on fire*, or *can get hot*. Like *clutchness*, some players just seem to have it, and some don't. It's an artifact of how we remember things.

This is perhaps reflected in the NBA's [Clutch Player of the Year award](https://en.wikipedia.org/wiki/NBA_Clutch_Player_of_the_Year). Last year, it was won by Jalen Brunson, who is a player I think NBA fans would consider pretty clutch (at least on the offensive end, where he is a one man band, not so much on defense, where he is a one man turnstile).  But [statistically](https://www.nba.com/stats/players/clutch-traditional?PerMode=Per100Possessions&Season=2024-25&dir=A&sort=AST), Brunson wasn't one of the best players in clutch time last season. His team, the Knicks, only went 17-11 (60.7%) in clutch games, which was almost exactly the same winning percentage as they went overall, 50-32 (61%). But Brunson feels like a *clutch guy*. It's an award based on *vibes*, rather than objective facts.

This week, I'm going to start looking at NBA clutch statistics at the team level. The NBA defines *clutch time* as the last 5 minutes of a game, when the score is within 5 points. Would a species with 4 fingers on each hand have gone with the last 4 minutes, when the game is within 4 points?

## Our old frenemy, conditional probability
The math behind statistics isn't that hard, compared to other types of math (lookin' at you, partial differential equations). The real difficulty is the process of thinking statistically. It's easy to find statistical correlations that seem important or profound, but are actually meaningless once the mess of conditional probabilities are untangled, like a box of old Christmas lights, and the right baseline is established.

An example would be bets on NFL point totals, where one can wager on whether the total number of points by both teams is higher or lower than a certain number. Let's say an NFL game is a blowout -- one team wins by more than 20 points. 55% of the time, when a game is a blowout, the bet on the over wins. Is this an interesting correlation? 

Perhaps we might take it as evidence of the *rubber band effect*, where teams that are ahead by a large margin tend to play with less intensity on defense, allowing the other team to score *garbage time points* -- scores that don't affect the outcome of the game, but make the final score look more competitive than the game actually was. It looks like the *rubber band effect* makes the point total over more likely to win, right?

Wrong! In order for one team to win by at least 20 points, at least one team has to score 20 points first. In the set of games where one team scored at least 20, the over wins 60% of the time. So the game being a blowout lowers the probability of the over winning. A 20-0 blowout probably should happen more often than a 40-20 blowout. That makes sense. But so does "teams leading by a lot get lazy on defense, leading to more points than expected". And that's wrong.

## Clutch time is mediocrity time
In order for an NBA game to go into clutch time, it has to be a close game in the first place. Really good teams and really bad teams will be involved in fewer *clutch* games than mediocre teams, because they're usually either winning or losing by a large margin at the end of the game. 

Clutch games are pretty common, around half of all NBA games. Here's a plot of the winning percentage versus percentage of games played in the clutch:

![/img/clutch-density.png](/img/clutch-density.png)

## Do clutch teams exist?

We should start with the assumption that teams win clutch games at the same rate that they win games in general. A team that wins 60% of its games overall should probably win 60% or so of its clutch games. And if they win 70%, or 50%, of their clutch games, that very well could be just small sample size.  Here's a plot of win percentage in clutch vs. non-clutch games.

![/img/clutch-non-clutch.png](/img/clutch-non-clutch.png)

There's a clear positive trend -- teams that are bad tend to lose in both clutch and non-clutch games. Teams that are good tend to be good in both. Most teams are mediocre at both.

### Offense and Defense in the clutch
Offensive and Defensive ratings are a measure of the average number of points scored/given up per 100 possessions.

There is a clear effect on these numbers in clutch time. Offensive and defensive ratings are about 2.5 points lower when the game is in the clutch. Either offenses are worse, or defenses are better, or a bit of both. But it's a little bit harder to score.


What would constitute evidence that a team is actually doing something special to win games in the clutch, versus just doing what they always do? I'm interested in teams that are better on both offense and defense in the clutch. Do teams like that tend to win more games during the regular season and the playoffs?