Title: What are the most important events at the NFL Combine?
Date: 2025-05-23 10:20
Category: sports analytics
(the code used is available at [https://github.com/csdurfee/nfl_combine_data/](https://github.com/csdurfee/nfl_combine_data/)).

## Intro
Every year, the National Football League hosts an event called the Combine, where teams can evaluate the top prospects before the upcoming draft.

Athletes are put through a series of physical and mental tests over the course of four days. There is a lot of talk of hand size, arm length, and whether a guy looks athletic enough when he's running with his shirt off. It's basically the world's most invasive job interview. 

NFL teams have historically put a lot of stock in the results of the combine. A good showing at the combine can improve a player's career prospects, and a bad showing can significantly hurt them. For that reason, some players will opt out of attending the combine, but that can backfire as well.

I was curious about which events in the combine correlate most strongly with draft position. There are millions of dollars at stake. The first pick in the NFL draft gets a $43 Million dollar contract, the 33rd pick gets $9.6 Million, and the 97th pick gets $4.6 Million.

The main events of the combine are the 40 yard dash, vertical leap, bench press, broad jump, 3 cone drill and shuttle drill. The shuttle drill and the 3 cone drill are pretty similar -- a guy running between some cones as fast as possible. The other drills are what they sound like.

I'm taking the data from Pro Football Reference. Example page: [https://www.pro-football-reference.com/draft/2010-combine.htm](https://www.pro-football-reference.com/draft/2010-combine.htm). I'm only looking at players who got drafted.

## Position Profiles

It makes no sense to compare a cornerback's bench press numbers to a defensive lineman's. There are vast differences in the job requirements. A player in the combine is competing against other players at the same position. 

The graph shows a position's performance on each exercise relative to all players. The color indicates how the position as a whole compares to the league as a whole. You can change the selected position with the dropdown.

<iframe src="/img/position_view_2025.html" width="550" height="450" frameborder="0"></iframe>

Cornerbacks are exceptional on the 40 yard dash and shuttle drills compared to NFL athletes as a whole, whereas defensive linemen are outliers when it comes high bench press numbers, and below average at every other event. Tight Ends and Linebackers are near the middle in every single event, which makes sense because both positions need to be strong enough to deal with the strong guys, and fast enough to deal with the fast guys.

## Importance of Events by Position

I analyzed how a player's performance relative to others at their position correlates with draft rank. Pro-Football-Reference has combine data going back to 2000.  I have split the data up into 2000-2014 and 2015-2025 to look at how things have changed. 

For each position, the exercises are ranked from most to least important. The tooltip gives the exact r^2 value.

Here are the results up to 2014:

<iframe src="/img/before_2015.html" width="800" height="700" frameborder="0"></iframe>

Here are the last 10 years:

<iframe src="/img/after_2015.html" width="800" height="700" frameborder="0"></iframe>

Some things I notice:

The main combine events matter that much either way for offensive and defensive linemen. That's held true for 25 years.

The shuttle and 3 cone drill have gone up significantly in importance for tight ends.

Broad jump and 40 yard dash are important for just about every position. However, the importance of the 40 yard dash time has gone down quite a bit for running backs. 

As a fan, it used to be a huge deal when a running back posted an exceptional 40 yard time. It seemed Chris Johnson's legendary 4.24 40 yard time was referenced every year. But I remember there being lot of guys who got drafted in the 2000's primarily based on speed who turned out to not be very good. 

The bench press is probably the least important exercise across the board. There's almost no correlation between performance and draft order, for every position. Offensive and defensive linemen basically bench press each other for 60 minutes straight; for everybody else, that sort of strength is less relevant.  Here's one of the greatest guys at throwing the football in human history, Tom Brady:

![behold](/img/Tom-Brady-Combine.png)

Compared to all quarterbacks who have been drafted since 2000, Brady's shuttle time was in the top 25%, his 3 cone time was in the top 50%, and his broad jump, vertical leap and 40 yard dash were all in the bottom 25%.

## Changes in combine performance over time
Athlete performance has changed over time. 

I've plotted average performance by year for each of the events. For the 40 yard dash, shuttle, and 3 cone drills, lower is better, and for the other events, higher is better.

![change over time](/img/combine-trends.png)

40 yard dash times and broad jump distances have clearly improved, whereas shuttle times and bench press reps have gotten slightly worse.

There's a cliche in sports that "you can't coach speed".  While some people are innately faster than others, the 40 yard dash is partly a skill exercise -- learning to get off the block as quickly as possible without faulting, for starters. The high priority given to the 40 yard dash should lead to prospects practicing it more, and thus getting better numbers.

The bench press should be going down or staying level, since it's not very important to draft position.

There's been a significant improvement in the broad jump - about 7.5% over 25 years. As with the 40 yard dash, I'd guess it's better coaching and preparation. Perhaps it's easier to improve than some of the other events. I don't think there's more broad jumping in an NFL game than there was 25 years ago.

Shuttle times getting slightly worse is a little surprising. It's very similar to the 3 Cone drill, which has slightly improved. But as we saw, neither one is particularly important as far as draft position, and it's not a strong trend.

## Caveats
Some of the best athletes skip the combine entirely, because their draft position is already secure. And some athletes will only choose to do the exercises they think they will do well at, and skip their weak events. This is known as [MNAR data](https://www.ncbi.nlm.nih.gov/books/NBK493614/) (missing, not at random). All analysis of MNAR data is potentially biased.

I'm assuming a linear relationship between draft position and performance. It's possible that a good performance helps more than a bad performance hurts, or vice versa.

I didn't calculate statistical significance for anything. Some correlations will occur even in random data. This isn't meant to be rigorous.