Title: Nobody wins at NFL betting.
Date: 2025-12-18 10:20
Category: football
Tags: football, sports betting, bajillion

[![Light-Space Modulator, "These Things"](https://img.youtube.com/vi/dcGAbRISnr4/0.jpg)](https://www.youtube.com/watch?v=dcGAbRISnr4){:target="_blank"}

Song: [Light-Space Modulator, "These Things"](https://www.youtube.com/watch?v=dcGAbRISnr4){:target="_blank"}

Notebook: [https://github.com/csdurfee/csdurfee.github.io/blob/main/notebooks/super-contest.ipynb](https://github.com/csdurfee/csdurfee.github.io/blob/main/notebooks/super-contest.ipynb)

# Even the experts can't do it
As I've been chronicling in the ["Bajillion"](/tag/bajillion.html) segment, experts are really bad at betting on NFL football, or at least the ones at the Ringer are.

That inspired me to make my first YouTube video, about sports gambling and why it's not really a game of skill. I'm still working on it, but I promised I'd do a thing a week on here. This is that thing.

The Ringer's football/gambling experts doing worse than a coin flip on the NFL could just be coincidence, bad luck, or as gamblers say, a *bad beat*. I figured I should make more of an effort to find real-world betting records on the NFL by people who have might skill as gamblers, rather than people who talk about sports for a living.

[The Westgate Resorts (TM) Las Vegas Super Contest (R)](https://www.westgateresorts.com/hotels/nevada/las-vegas/westgate-las-vegas-resort-casino/casino/2025-supercontest-standings/) seemed like the perfect testing ground. It's exactly like the Ringer 107, except there's cash on the line. With a buy-in of $1500 and around 1,000 teams a year, that's a pretty nice top prize. (There are fewer contestants this year than normal, maybe because the buy-in increased from $1,000.)

While the people at the Ringer are using their picks to generate interesting football content, these contestants have lot of financial incentive to do well and nobody they have to explain their picks to. The Ringer writers might have a bias against taking the uglier/harder to justify side of a bet, because their job is really to tell a story that people want to listen to. But these folks should be eating W's like crab legs and not caring how messy it looks.

That $1500 buy in is 207 hours of wages, pre-tax, for someone making the federal minimum wage. For regular folks, $1500 is most of a mortgage payment, or a few months of groceries. Anyone risking that much money should have rational reasons to believe they're good at betting on football, right?

This isn't a non-gambling football writer forced to make picks for the sake of content. The contestants consider themselves sharp enough to beat 1,000 other competitors in a pretty famous betting contest, for a Million dollar payout and the chance to get their photo taken with a bunch of showgirls while holding a giant novelty check. 

This is the *kumite* of football betting, [the ultimate contest of warriors](https://www.youtube.com/watch?v=YNZ1ElwD_JA), and I assume you're only going to enter the *kumite* if you've won a few fights before.  

Mind you, there are around 15 NFL games every week and the teams only have to pick 5 of them for the Super Contest. Maybe most lines are so fair nobody can make money betting them, but the contestants only need to take one game in three. If there are any lines that are beatable, these contestants should be finding them. Their win rate should be an overly optimistic estimate of how beatable the *average* NFL line is, because they're not taking every game, or random games.

My assumption before running the numbers was that this was a contest for people who should have a decent chance of at least breaking even (over 52.4% winning percentage.)

## The terrible, horrible, no good, very bad year
That assumption hasn't been even close to true this season. Data as of week 16 taken from [the Westgate Resorts website](https://www.westgateresorts.com/hotels/nevada/las-vegas/westgate-las-vegas-resort-casino/casino/2025-supercontest-standings/).

There are 751 entrants in the 2025 contest. 59% of them (444/751) have a losing record. 76% of them would be losing money, if they were taking their picks at -110 odds.

Collectively, the teams have won 48.6% of their bets. It might not sound terrible, but there are 700+ teams who have taken 70 bets apiece, so it's a big sample size overall -- over 54,000 bets in total. Statistically, they're much worse than flipping a coin. If you flipped a coin 54,000 times and it came up heads 48.6% of the time, you'd be safe concluding it wasn't actually a fair coin.

Here's one way to visualize the suckitude. I simulated each team making picks by flipping a fair coin, and compared them to the actual results.

![/img/super-contest.png](/img/super-contest.png)

The white areas are where there were fewer real competitors than we'd expect by random chance, the dark blue parts are where there are more real competitors than expected, and the light blue is the overlap. 

The white vertical line is the minimum winning percent to break even at standard -110 odds. Most of the white area, where there are fewer competitors than expected, is to the right of the line, and all of the dark blue area is at less than 50% winning percentage.

## Anti Skill and Uncle Juice
The best entry in the contest is sitting at 53-21, the amusingly named `BIFFS ALMANAC`. That record would be an outlier if we were selecting bets by chance, so even though it's a small sample size, kudos to them, and their mostly accurate sports almanac.

The worst record belongs to the also amusingly named `THISSHOULDBEEASY`, with a record of 24-49. If that team had just taken the opposite of their bets, they'd be in 2nd place!

Most of the teams would be doing better if they wrote down their best picks, then took the opposite of them. Knowing stuff sure seems to be a disadvantage when betting on football. 

In aggregate, whatever strategies or football knowledge or divination rites (\*) the contestants are using makes them worse at picking winners -- they possibly have *anti-skill*. This is sort of what the efficient market hypothesis predicts -- picking stocks randomly (or index funds, which invest in every stock on the market) will generally outperform mutual funds that have professional fund managers making the picks.

(\*) I'm a big tyromancy guy myself. RIP to the recently departed [Claude Lecouteux](https://en.wikipedia.org/wiki/Claude_Lecouteux), a legendary historian of spooky medieval stuff. If you ever need to write a heavy metal concept album on short notice, his books are a goldmine.

## Previous years
After a bunch of wasted work to screen-scrape results from previous years off 3rd party sites, I discovered [another website](https://fantasysupercontest.com/supercontest-standings-2020-week-18) that has the complete records going back to 2013 in CSV format. Score!

This season has been particularly difficult on Super Contest gamblers, which probably explains the Ringer's poor record. Previous seasons have looked more like what I expected -- the average Super Contest entrant is a little better than flipping a coin, but not good enough to actually make money gambling. 

Here are the Expected Values by year:

![/img/return-rate.png](/img/return-rate.png)

The dotted line is at -4.5%, the Expected Value (EV) of taking a bet at -110 with a 50% chance of winning. There have been 5 seasons where the average competitor has done about the same as flipping a coin, or worse, and 2 seasons where they came close to breaking even.

Over all seasons and all contestants, the average EV is -2.5%, about the same as betting 'reduced juice' (-105 odds instead of -110) with a 50% chance of winning. Overall, the EV has been better than what we'd expect by chance, but not good enough to be profitable. 

Since the contestants only have to pick 5 games every week, this data should represent the best case scenario -- the most beatable lines possible, being taken by more experienced than average gamblers -- and they're still losing money 11/13 years, and breaking even the other two.

While the 75th percentile has a decent rate of return (up until this season), that's true of flipping a coin as well. With fewer than 100 bets in a Super Contest season, it's very possible to have a winning record by chance alone.

The win rate of competitors has been going down for 3 years in a row. It may be due to weaker competition in the Super Contest, or just random variation, but I would guess it's at least partially due to better lines. More money than ever is being gambled, and there's more information than ever, so the lines should get tighter. I would have to pull a lot more data to answer that question, though.

## Looking for other experts
OK, maybe that's still not enough proof -- what about people who make a living selling their supposed gambling expertise? I've looked at a ton of sites that sell picks for money, so I have an idea how this will go. But I came across a new one that's run by some pretty smart folks, so let's give it a crack, and I'll try to act suprised at the results.

The site in question is called [FTN Fantasy](https://ftnfantasy.com/bets/nfl/bet-tracker). It's affiliated with Aaron Schatz, who I'm pretty sure basically invented modern football analytics with his site Football Outsiders.

*DVOA, ever heard of it?*

If football betting is a game of skill, a game of *ball-knowing* (at least the stats version of ball-knowing), he should have that skill. Here's Aaron's record:

![/img/just-aaron.png](/img/just-aaron.png)

Oh no! He's got a losing record overall, a -11% EV on his bets (vs. -4.5% for picking which mascot would win in a fight). Who could have seen that coming?

Here's the whole site's record:

![/img/ftn-fantasy.png](/img/ftn-fantasy.png)

While they have a winning record overall, they have a losing record against the spread (the bets labeled `Sides`). 

### Giving them props
Prop bets are, well, propping their record up. Since the site is primarily about fantasy football, it makes sense they would be strong on prop bets, since fantasy is all about individual player predictions. That makes them a cut above most tout sites, who aren't good at anything.

It's quite possible that prop bets are beatable in a way spread bets aren't, though as discussed in the video, the big sportsbooks no longer allow taking the unders on prop bets, which I'm sure makes it harder to find value. 

My caveat about tips on prop bets is that the lines tend to move very rapidly, and in large amounts. A line could very quickly go from positive to negative Expected Value before someone could get a bet down. So the tips might be legit, but not be *usable* to the gambler paying for them -- they have a very short shelf life. 

### Touts and their tricks
The only tout with a good record against the spread is esteemed actor Michael Chiklis apparently doing a little moonlighting:

![/img/the-commish.png](/img/the-commish.png)

The Commish is doing something I've seen a lot of touts do, which is taking some games at higher than -110 odds in order to make the win-loss record appear better (for example, buying a couple of points and taking -150 odds, which should win significantly more than 50% of the time). The equivalent record at -110 odds would be 41-35, only a 54% winning percentage. That's better than nothin', but it ain't much.

I'm inclined to be distrustful of any tout pulling that trick, since buying points is a negative Expected Value play. (We don't need math for this one: the sportsbooks wouldn't offer the option of buying points if it was positive EV for the gambler. They're counting on the gambler making an emotional decision to buy the points, because they've done the math and know it's a bad deal.) Buying points might make the record look better, but it will hurt profits/increase losses over the long run.

## Bajillion, Week bajillion
One mathletix team picks bets randomly, the other algorithmically.

The Ringer had another losing week, going 12-13 overall, despite one team going 5-0.  Mathletix went 6-3 on the week, despite a couple of *bad beats* (bets that just barely lost).

*Lines taken on Tuesday morning.*

### The Neil McAul-Stars
last week: 4-1, +295    
Overall: 20-15, +454    
line shopping: +104    

* WAS +7 -104 (lowvig)
* MIN +7 +103 (prophetx)
* GB -2.5 -112 (lowvig)
* TEN +2.5 +102 (prophetx)
* JAX -6.5 -106 (prophetx)


### The Vincent Hand-Eggs
last week: 2-2-1, -6    
Overall: 13-20-2, -787       
line shopping: +113       

* PIT -3.5 +103 (prophetx)
* HOU +2.5 -108 (prophetx)
* WAS +7 -104 (lowvig)
* ARI +7 -101 (prophetx)
* BAL +2.5 +101 (lowvig)