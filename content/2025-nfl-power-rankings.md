Title: Revisiting 2025 NFL preseason predictions
Date: 2026-02-01 10:20
Category: sports betting
Tags: football, worse than a coin flip


[![Kids See Ghosts, "Kids See Ghosts"](https://img.youtube.com/vi/cHFzyFMT0pw/0.jpg)](https://www.youtube.com/watch?v=cHFzyFMT0pw){:target="_blank"}

Song: [Kids See Ghosts, "Kids See Ghosts"](https://www.youtube.com/watch?v=cHFzyFMT0pw){:target="_blank"}

[Spreadsheet here](https://docs.google.com/spreadsheets/d/1omE0MMJA-KDpZ2FV8Fc0mqx9mkpyFwG73LkAKaVU0Ag/edit?usp=sharing)

Notebook: [https://github.com/csdurfee/csdurfee.github.io/blob/main/notebooks/NFL-win-totals.ipynb](https://github.com/csdurfee/csdurfee.github.io/blob/main/notebooks/NFL-win-totals.ipynb)

Some stats courtesy of [pro-football-reference.com](https://www.pro-football-reference.com/)

Before the first game of the NFL season, I captured the power rankings from 11 media sources, as well as odds on pre-season win totals from a couple of sportsbooks. I thought it would be interesting to see how the power rankers did.

## 2025 was a strange one
We've [previously seen](/nobody-wins-at-nfl-betting.html) that gamblers have done historically badly this NFL season.

The betting markets severely underestimated both teams that made the Super Bowl. The Patriots' preseason over win total was `8.5 +105`, meaning a slightly less than 50% chance of winning 9 games or more. The Patriots were expected to have the easiest strength of schedule in the NFL, so that was a pretty modest number.

The only team that exceeded their win total by more than the Patriots was the Seattle Seahawks. Their preseason over win total odds were `7.5 -139`. (The `-139` odds implies there's a `139/239 = 58%` chance of the bet winning.)

The Patriots had an average rank of 22nd in the preseason power rankings, with the highest ranking being 17th, and the lowest 27th. The Seahawks had an average rank of 19th, with the highest being 16th and the lowest 27th.

There were a lot of disappointing teams this year. Of the top 7 highest ranked teams at the beginning of the season, only one of them, the Buffalo Bills (#3 average rank) won a playoff game. The Eagles (#1 average rank) and Packers (7th) lost in the first round. The Ravens (2nd), Chiefs (4th), Lions (5th) and Commanders (6th) didn't even make the playoffs.

The teams that the Seahawks and Patriots beat to make the Super Bowl were a lot closer to preseason expectations. The Denver Broncos were ranked 10th on average, and the Los Angeles Rams were ranked 8th. 

While the 4 lowest ranked teams (Giants, Titans, Browns and Saints) were all bad, the Colts and Panthers also ranked in the bottom 6 on average, and had very good seasons. The Colts looked like one of the best teams in football for a big chunk of the season, before injuries took hold. The Panthers made the playoffs, and almost won.

## Comparing expert rankings to SRS
Pro-football-reference.com has a statistic called SRS, which is the average margin of victory, adjusted for strength of schedule. So it should be a better metric for comparing teams than their actual win-loss record, or average margin of victory. Because the NFL schedule is so short, it's important to use an adjusted metric like SRS.

Comparing preseason power rankings to SRS, the teams that defied expectations the most were the Colts, Jaguars, Seahawks, and Patriots (better than expected), and the Commanders and Bengals (worse than expected).

## Who had the most accurate preseason power rankings?
I calculated the correlation between the power rankers and regular season SRS. USA Today was the most accurate, and Inside the Lines (CBS) was the least accurate. 

|                         |   corr|
|:------------------------|------:|
| Inside the Lines (CBS)  | 0.345 |
| FOX Sports              | 0.354 |
| NFL Spin Zone           | 0.354 |
| CBS Sports              | 0.404 |
| NFL.com                 | 0.429 |
| Sharp Football Analysis | 0.431 |
| Sporting News           | 0.435 |
| ESPN                    | 0.447 |
| DirecTV                 | 0.449 |
| TeamRankings.com        | 0.488 |
| USA Today               | 0.494 |

These correlations are far lower than what we saw with [NBA power rankings](/two-ways-to-go-from-the-middle.html) a while back.

The worst power ranker, [Inside the Lines (CBS)](https://www.cbssports.com/betting/news/nfl-power-rankings-2025-model-says-packers-in-top-tier-chiefs-not-among-top-five-contenders/), used a statistical model, but it sounded like baloney, so I wasn't surprised they did poorly.  Here's how they describe their model:

> we have reverse engineered oddsmakers' models which has resulted in 85-90% of our projections being virtually identical to the oddsmaker's lines (main markets and props). When sportsbooks' lines differ from ours, we know they are likely manipulating a line to either sucker the public or minimize risk.

Their model is so good that when its predictions differ from reality, we should assume reality itself is wrong or somebody's being dishonest! Good grief. Lord grant me the confidence of a bottom tier tout.  

They claim they've gone `72-47, 60.5%, +18.5 units over the last three seasons` but I couldn't find any record of those picks. If they were taking the games at even odds, they would be up +20.3 units, so they're taking some bets that should win more than 50% of the time, which makes the winning percentage look artificially better. We previously saw [a tout known as "The Commish" over at FTN](/nobody-wins-at-nfl-betting.html) doing the same thing.

### Which 2025 NFL records are misleading?
By point differential, the Patriots were the 3rd best team in the league, but by SRS, they were 6th, behind three teams from the NFC West (Seahawks, Rams and 49ers). 

Due to being in the same division as two powerhouse teams, the Cardinals and 49ers had the biggest discrepancies between margin of victory and SRS -- they were probably better than their win-loss record. In the other direction, the Patriots, Broncos, Bills, Cowboys and Dolphins benefitted the most from playing an easy schedule.

### Are the 2025 Seahawks historically great?
There was no disagreement at the top. The Seahawks and Rams were #1 and #2 in both SRS and margin of victory. That may be underselling how good they were. [According to DVOA](https://ftnfantasy.com/nfl/final-2025-dvoa-ratings), a more sophisticated way of assessing team strength than SRS, both the Rams and Seahawks were among the top 10 teams in NFL history. 

That's pretty remarkable to me. My instinct is that DVOA isn't adjusting to changes in the football rules or strategy over time, because it's hard to believe that a team quarterbacked by Sam Darnold is one of the 10 greatest of all time. But what do I know? I'm a guy who gets most of his football news from [Tom Grossi's "If the NFL was scripted" videos](https://www.youtube.com/watch?v=2-ll2uwZMaA&list=PLpfKWYL55S9Eckl2J5py0ujqjyarU5gRP).

I'm not sure anybody knows anything about football, though. The Seahawks' average preseason rank was 19th. Is it possible a team that 11 football experts thought would be below average was actually historically great? Football is way less knowable than other sports because of the short season, the large number of players, and the outsized influence of the quarterback. 

Even with that in mind, these power rankings have not aged well. 6 out of 11 rankers (CBS Sports, USA Today, DirecTV, NFL Spin Zone, TeamRankings.com, Sharp Football Analysis) put the Arizona Cardinals ahead of the Seahawks at the beginning of the season. The Cardinals finished with a 3-14 record, the worst in the league, while the Seahawks went 14-3, the best in the league. It's hard to be wronger than that.

The Seahawks defense may have been historically great this season, but none of the power rankers seemed to have a clue that would happen. Considering the Seahawks went 10-7 and had the 11th best defense the prior season, the low rankings are puzzling.

Here's everything [NFL Spin Zone](https://nflspinzone.com/nfl-power-rankings-risers-and-fallers-after-week-1-preseason-action-in-2025/2) had to say about the Seahawks:

> Seattle might have something special on their hands with Jalen Milroe, but he is definitely a raw prospect and will absolutely need some time to turn into an NFL-caliber passer. Sam Darnold could be competent in the meantime, though.

[USA Today](https://www.usatoday.com/story/sports/nfl/columnist/nate-davis/2025/07/30/nfl-power-rankings-2025-preseason-eagles-ravens-chiefs/85429548007/) didn't remark on the defense, either: 

> Seattle Seahawks (15): As a member of the Vikings, QB Sam Darnold dealt the 2024 Seahawks a death blow last December in Lumen Field. Now the 12s can only hope he's the real deal and won't serve a self-inflicted coup de grâce in November.

[The Sporting News](https://www.sportingnews.com/us/nfl/news/nfl-power-rankings-preseason-eagles-49ers-cowboys-jets-jaguars/092235fe2a7fd870c0c95c61) at least mentioned it:

> Seattle Seahawks (18): The Seahawks are feeling overall about their offensive state in Year 2 with the changes to Sam Darnold and Klint Kubiak but to compete for a playoff spot in the NFC West, Mike Macdonald's defense needs more impactful results.

The Cardinals played in the hardest division in the NFL and their quarterback got injured after five games, so some of their futility is understandable. But after seeing the season play out, it's hard to imagine any possible scenario where the Cardinals were going to be better than the Seahawks, even if a majority of football experts thought so before the season. 

Hindsight bias is a heck of a thing. It seems obvious in retrospect that the Chiefs (the consensus 4th best team before the season) have been losing steam for a while and didn't do enough to keep up with Father Time. Of course the Bengals (11th) were going to be terrible on defense, and the Panthers (27th) were significantly more talented and better coached than the Jets (26th) or Raiders (25th).

These all would've been hot takes just a few months ago, though. It's not like there was a lot of disagreement on the preseason rankings. Most of the power rankers had a correlation of .9 or higher with each other. The conventional wisdom, or whatever these handicappers are using, was just way off this year. Everybody's bad at this.

### Another bad football handicapper
TeamRankings.com had the 2nd most accurate power rankings. They also sell picks against the spread. We've previously looked at a bunch of football touts, and they've all lost money this season. TeamRankings is the first exception to that, though just barely. 

[They went 149-130 on their "TR Picks" this season](https://www.teamrankings.com/nfl/betting-models/detailed-splits/), for a 53.4% winning percentage and +5.5 units of profit. However, they've gone 493-479 (50.7% win percentage, -30.8 units) over their past 1,000 picks. So, like the average entrants in the Super Contest, they're a little better than flipping a coin, but not good enough to beat the vig.

They also offer algorithmic picks based on their power rankings, which are notably bad. Those went 126-153 (45.2% win percentage) this season, and 454-518 (46.7% win percentage) over the last 1000 bets. Fading those picks would've made +14.4 units this season. 

Their power rankings were relatively good, but that doesn't mean they're useful for deciding which side of the line has more value. It's not enough to know which team is better than the other one -- anybody who follows the NFL could probably tell you that. A gambler has to accurately estimate how much better in order to identify positive EV bets.

TeamRankings charges $299 a year for a subscription.

### nflpickwatch: A smorgasboard of bad football handicappers
I came across another site that sells picks in the course of writing this.

[nflpickwatch.com](https://nflpickwatch.com/nfl/picks/ats/experts/2025/22?s_sB=season_profit_loss&s_sD=true&d_s_pi_e=true&d_s_pi_o_u=Over&d_s_pi_p=50&t_t_r=20&h_h_r=2024) is yet another website that sells NFL football picks, aggregated from experts across the internet, including writers for ESPN, the New York Post, and Bleacher Report.

They have 181 NFL experts on the site this year. Of those 181 experts, 84% of them lost money this season. If the experts made their picks randomly, we'd expect around 22% of them to be making money, so 16% is bad. 99 of the 181 experts (55%) had below 50% winning percentage. Once again, people who get paid to talk football for a living are significantly worse than a coin flip.

The site also has a section for fans to make their picks. 551 out of 2,682 (20.5%) fans made money this year. That's still worse than we'd get from flipping a coin, but better than the experts.

The experts have done better at times in the past. Here are the percentage of experts that made money (won over 52.4% of their bets) by year:

|  season       | profitable touts | percent |
|:--------------|------|-----:|
| 2025          | 29/181 | 16 % |
| 2024          | 77/170 | 45% |
| 2023          | 75/246 | 30% |
| 2022          | 37/226 | 16% |
| 2021          | 61/234 | 26% |
| 2020          | 23/172 | 13% |
| 2019          | 16/66  | 24% |
| 2018          | 5/45   | 11% |

The touts were better than the 22% rate we'd expect from flipping coins in 4 of the last 8 seasons, and worse in the other 4. Combining all 8 seasons together, 323/1340 tout-years were profitable, a 24% rate.

So in aggregate, they may be a tiny better than flipping coins, but even in the very best season, the majority of touts on the site would lose you money if you took their picks.

At least they're a little cheaper than TeamRankings -- only $180 a year for the chance to lose money playing somebody else's picks.

Who's paying for this stuff, and how do I get a taste? It's easier to get people to pay for bad advice than it is to get them to follow good advice given freely. If you tell people you can see the future, they will pay for your predictions even if they're worse than random, but if you show them evidence that nobody can see the future, they'll refuse to believe you, if they even bother to listen in the first place.

## The Mathletix Bajillion, final edition
I forgot to do picks last week, so I guess that's the end of the experiment. Both teams went 2-2 the prior week, meaning the Hand-Eggs finished with a record of 27-26-1, and the McAul-Stars finished at 26-24-4. The Hand-Eggs lost a tiny bit of (fake) money on the season and the McAul-Stars made a tiny bit. At *full juice*, both teams would've lost money despite having winning records. 

I was going to reveal which team was picking bets by chance, and which was using a simple algorithm, but since they ended up getting very similar results, I guess it doesn't matter which is which, right?

Although it was a small sample size, I think I showed that betting *reduced juice* can save a substantial amount of money. I don't think it's reasonable to expect to make money betting on the NFL, but betting reduced juice is at least *less irrational* than using a retail sportsbook like DraftKings that [spends over $100 Million a month on advertising](https://draftkings.gcs-web.com/static-files/63f5b560-fcf4-4117-9d2c-1cfe2400798a).

The Ringer have been slightly more respectable the past few weeks, and they now have 2 of 5 teams with winning records (but still losing money against the vig). Collectively, the Ringer have a 242-273 record, for a 47% winning percentage. The three gambling podcasts had the three worst records, with one going 47-56 (-14.6 units), and the other two at 45-58 (-18.8 units apiece).
