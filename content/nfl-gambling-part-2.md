Title: NFL point totals and money lines
Date: 2026-01-07 10:21
Category: sports betting
Tags: football, your parlay sucks


[![Sam and Dave, "Hold On, I'm Coming"](https://img.youtube.com/vi/Fowldx4hRtI/0.jpg)](https://www.youtube.com/watch?v=Fowldx4hRtI){:target="_blank"}

Song: [Sam and Dave, "Hold On, I'm Coming"](https://www.youtube.com/watch?v=Fowldx4hRtI){:target="_blank"}

Code: [https://github.com/csdurfee/scrape_yahoo_odds/blob/main/explore_football.ipynb](https://github.com/csdurfee/scrape_yahoo_odds/blob/main/explore_football.ipynb)

This week, more insights into NFL betting from BetMGM gambling data (harvested from Yahoo). I'm looking at the last 5 seasons of regular season NFL games. There are 1,359 games total, around 140 of which are missing betting percentage data, so have been excluded from parts of this analysis.

# Point totals
Gamblers can wager on whether the total number of points scored in an NFL game will be over or under a certain number. These bets are sometimes called "over/unders".

The over point total has won in 48.4% of games (658/1359), so the under has been a slightly better value. Point totals almost never push (hit the number exactly, meaning neither side wins). That's only happened in 12 of 1358 games.

The win rate for overs has changed over the past 5 seasons The over won about 46% of the time from 2021-23, and 53% of the time from 2024-25. That possibly mirrors what we saw [last time](/nfl-spread-betting-statistics-more-folly-of-crowds.html) -- it was wildly profitable to fade the public on spread bets from 2021-23, and slightly unprofitable to do so the last two seasons.

Taking the under is usually equivalent to fading the public, because [as with the NBA](/overs-money-lines-and-pigeonholes.html), the betting public greatly prefers the over on point totals, taking them 86.8% (1056/1217) of the time.

When the public takes the over, they win the bet 48.1% of the time. On the rare occasions where they take the under, they win 46.6% of the time. So, this is yet another example of where gamblers as a whole do worse than a coin flip.

50% of point total spreads are between 41.5 and 47.5, with the median being 44.5. 

A naive betting strategy would be to assume that low point totals are too low (always take the over if the total is less than 44.5), and high point totals are too high (take the under if the total is greater than or equal to 44.5). This strategy would've gone 700-658 (51.6%). It's not much, but there might be a slight advantage to betting on *boring* point total outcomes.

Here are what the errors against the point total look like. Positive values are games that went over the total, negative are games that went under.

![/img/nfl-over-under.png](/img/nfl-over-under.png)

There should be a longer tail to the positive side than the negative, and there is. It's impossible to score fewer than 0 points, which limits how far under a bet can go, but there's theoretically no limit to how many points the teams could score in the over direction. 

As with other NFL data, there are spikes because some point totals are more likely than others.  Point totals are off by an average of 10.5 points. Here are the most common errors:

```
|   total_error |   count |
|--------------:|--------:|
|          -6.5 |      30 |
|         -11.5 |      29 |
|          -3.5 |      29 |
|           3.5 |      28 |
|          -7.5 |      27 |
|           6.5 |      25 |
|          -2   |      25 |
|          -1.5 |      24 |
|          -4.5 |      23 |
|           2.5 |      23 |
|           1.5 |      23 |
|           7.5 |      22 |
|          -0.5 |      22 |
|           0.5 |      22 |
|          -8.5 |      22 |
```

59% of point totals are on the half point (for instance, 6.5 instead of 6). That means 59% of the errors will be, too. I don't have a good reason why almost all of the top errors are on the half point, though.

## Point totals, shootouts and folk beliefs
There is a slightly negative correlation between points scored by the home team and points scored by the away team. That makes sense logically. If the home team scores more points than average, it probably has possession the ball for more time than usual, meaning the away team has less time than usual on offense to score. 

But as a fan, the negative correlation goes against my naive beliefs about football a bit. I think I'm prone to remember games where both teams scored a lot. We're more likely to remember exciting games rather than boring ones. Even if we want to think rationally about sports, our brains tend to overweight the outliers because that's mostly what we remember. We just forget the boring games and remember the high-scoring shootouts.

While home and away points aren't positively correlated, I can think of a couple plausible reasons why they could be. If one team is scoring a lot, the other team may take more risks or play at a faster pace than usual to try and keep up. That could lead to more points for both the offense and the other team's defense (due to turnovers). Another plausible reason is called rubber-banding. In sports, teams with a big lead tend to relax their efforts (*let their foot off the gas*), allowing the other team to score *garbage time points* that might not affect who wins the game, but make it seem closer than it was. 

In this dataset, the over has won 55% of the time (126/229) when one team wins by at least 20 points, which could be taken as evidence of rubber-banding. But we need to be careful with conditional probabilities. For one team to win by at least 20 points, at least one team has to score 20 points first. If we look at games where at least one team scored 20, the over hits 61% of the time.

While these theories are plausible, they're not true, or at least don't override the game clock factor. It's easy to invent plausible reasons that are wrong, or just don't matter. Good thing we have statistics! 

# NFL money lines and the favorite-longshot bias
Money line bets are a wager on who will win the game outright. A bet on the underdog will pay more than one on the favorite, because it's less likely to happen.

Money line data is always going to be very high variance -- one +400 bet winning or not can wildly change the Expected Value. That was a problem with the NBA, which has 5x the games of the NFL, so it's definitely going to be a problem here.

The public would be much better off taking their money line picks than their spread picks. They're getting an EV of -3.1% on money line bets, which is a step up from the -6.7% they're doing on the spread. That mirrors the NBA, where the public does significantly better on the money line.

It's also a slightly better Expected Value than taking money line bets randomly. The public are saved by their love of favorites, which they took in 1181/1228 (96%) of games, and are a relatively good deal on the money line.

Underdog money lines on NFL football are a bad bet in general (-7.27% EV), but huge underdogs are especially bad (-29.67% EV). This is evidence of the [favorite-longshot bias](/lessons-from-four-years-of-betmgm-nba-gambling-stats.html) in NFL betting. A -30% EV puts longshot underdog money lines in the same league as the biggest sucker bets that sportsbooks offer -- Same Game Parlays, 4+ leg parlays, and teasers.

"EV %" is the expected value of taking every bet in each category. Overall, money line bets have a -5.5% EV.

|    label      |  start  | end | num games | EV % |
|:--------------|---------|-----|-----------|----------|
| all favorites | -9999 | -1 | 1271 | -3.9% |
| mild favorites | -200 | -1 | 662 | -2.8% |
| heavy favorites | -400 | -200 | 406 | -7.5% |
| huge favorites | -9999 | -400 | 203 | -0.2% |
|----------------| ----  | ---- | ---- | ------ |
| all dogs | 1 | 9999 | 1185 | -7.3% |
| mild dogs | 1 | 200 | 663 | -5.4% |
| heavy dogs | 200 | 400 | 399 | -3.4% |
| huge dogs | 400 | 9999 | 123 | -29.7% |
|----------------| ----  | ---- | ---- | ------ |
| everythang | -9999 | 9999 | 2456 | -5.5% |

That -29.67% for huge dogs is hiding a big discrepancy. Huge home dogs `(>= +400)` have actually made money, winning 8/31 games. Huge away dogs have only won 6/92 games, for an absurd -63% Expected Value. The average odds for these bets is +600 (1 in 7 chance of winning), so we'd expect 13 of 92 bets to win, not 6.

Like I said at the top, money line dogs are going to be extremely variable, and the +400 number is an arbitrary cutoff. But even if huge away dogs had won twice as often, they'd still be unprofitable. Woof!

Money line favorites turn out to be a slightly better value than spread bets. But the estimated EVs are very sensitive to changes. I've been working on this project for a couple of weeks now, and noticed the numbers changing pretty significantly over the last 2 weeks of the NFL season.

### Bootstrapping money lines
Since the outcomes are chunky, they're not going to follow some nice, polite distribution. In order to estimate the variance in outcomes, we can use bootstrapping, [a popular technique in these parts](/one-in-e.html). 

I'm using the [scikits-bootstrap](https://scikits-bootstrap.readthedocs.io/en/stable/) library to generate a 90% confidence interval for the Expected Values. It creates random subsets of the bets in each category and calculates the EV of each subset. Then it returns the 5th and 95th percentile outcomes. This gives us a plausible range of values for the EV.


|    label      |  start  | end | num games | 5th %ile     | EV | 95th %ile |
|:--------------|---------|-----|-----------|----------|----------|----------|
| all favorites | -9999 | -1 | 1271  | -7.2% | -3.9% | -0.6%
| mild favorites | -200 | -1 | 662  | -8.3% | -2.8% | 2.4%
| heavy favorites | -400 | -200 | 406  | -13.0% | -7.5% | -2.6%
| huge favorites | -9999 | -400 | 203  | -5.3% | -0.2% | 4.0%
|----------------| ----  | ---- | ---- | ------ | --- | ----- |
| all dogs | 1 | 9999 | 1185  | -14.0% | -7.3% | -0.2%
| mild dogs | 1 | 200 | 663  | -12.6% | -5.4% | 2.3%
| heavy dogs | 200 | 400 | 399  | -16.5% | -3.4% | 10.5%
| huge dogs | 400 | 9999 | 123  | -55.3% | -29.7% | 4.7%
|----------------| ----  | ---- | ---- | ------ | --- | ----- |
| everythang | -9999 | 9999 | 2456  | -9.1% | -5.5% | -1.7%

Those are some pretty wide confidence intervals! Even with the -29.7% EV for huge dogs, we can't rule out some small hope that somebody could make money taking them. But as always, if there's randomness involved, we don't get to pick whether we get the 5th percentile result, the average result, or the 95th percentile result in life.

# For the algorithm: an unusual pandas thing
I ran into a weird issue with [pandas](https://pandas.pydata.org/), the main library I used to do analysis. I couldn't find anything on stackoverflow or search engines about it easily. So I'm commenting here in case it helps some future searcher.

The short version is that negation (`~`) of a pandas series with all boolean values will behave strangely if it has a non-boolean type, such as `object` or `int`.  This is because of [how the Python language handles negation](https://stackoverflow.com/questions/75618364/why-does-true-2-in-python). Although pandas overrides the `~` operation, it doesn't change that python behavior.  For example:

```
In [1]: import pandas as pd

In [2]: x = pd.Series([True, False, True]).astype(object)

In [3]: x[x==True]
Out[3]:
0    True
2    True
dtype: object

In [4]: sum(x==True) # this works as expected
Out[4]: 2

In [5]: sum(~x) # should be 1 since there is 1 false value
Out[5]: -5

In [7]: sum(~x == True) # should also be 1
Out[7]: 0

In [8]: ~x
Out[8]:
0    -2
1    -1
2    -2
dtype: object

In [9]: pd.__version__
Out[9]: '2.2.3'

# typecasting with True
In [10]: int(True)
Out[10]: 1

In [11]: int(False)
Out[11]: 0

In [12]: int(~True) # turns out it's a weird (but intentional) python behavior when negating an int
Out[12]: -2

In [13]: int(~False)
Out[13]: -1

```

I'm not clear why the series got inferred to be type `object` when all values were `boolean` -- there were no `na` or other weird values in the column. I created the DataFrame directly from python arrays, so that part's still a mystery.

So if you're seeing weird results when applying the `~` to a boolean Series (or column of booleans in a DataFrame), check the `dtype` isn't `object` or `int`.