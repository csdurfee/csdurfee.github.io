Title: Riding the waves
Date: 2025-07-26 10:20
Category: statistics
Tags: some educational value

[![Roy of the Ravers, "Emotinium"](https://img.youtube.com/vi/ko8cJucsbBU/0.jpg)](https://www.youtube.com/watch?v=ko8cJucsbBU){:target="_blank"}

After spending several weeks in the degenerate world of sports gambling, I figured we should go get some fresh air in the land of pure statistics.

## The Abnormal Distribution
Everybody knows what the normal distribution looks like, even if they don't know it as such. You know, the bell curve? The one from the memes?

In traditional statistics, the One Big Thing you need to know is called the Central Limit Theorem. It says, if you collect some data and take the average of it, that average (the sample mean) will behave in nice, predictable ways. It's the basis of basically all experimental anything.  If you take a bunch of random samples and calculate the sample mean over and over again, those sample means will look like a normal distribution, if the sample sizes are big enough. That makes it possible to draw big conclusions from relatively small amounts of data.

How big is "big enough"? Well, it partly depends on the shape of the data being sampled from. If the data itself is distributed like a normal distribution, it makes sense that the sample means would also be normally shaped. It takes a smaller sample size to get the sampling distributions looking like a normal distribution.

While a lot of things in life are normally distributed, some of them aren't. The uniform distribution is when every possible outcome is equally likely. Rolling a single die, for instance. 1-6 are all equally likely. Imagine we're trying to estimate the mean value for rolling a standard 6 sided die. 

A clever way would be to team up sets of sides - 6 goes with 1, 5 goes with 2, 4 goes with 3. Clearly the mean value has to be 3.5, right?

A less clever way would be to roll a 6 sided die a bunch of times and take the average. We could repeat that process, and track all of these averages. Those averages will make a nice bell curve, with the center at 3.5.

The uniform distribution is sort of obnoxious if you want to calculate the sample mean. The normal distribution, and a lot of other distributions, have a big peak in the middle and tail off towards the edges. If you pick randomly from one of these distributions, it's far more likely to be close to the middle than it is to be far from the middle. With the uniform distribution, every outcome is equally likely:

![/img/uniform.png](/img/uniform.png)

Couldn't we do even worse than the uniform distribution, though? What if the tails/outliers were even higher than the center? When I first learned about the Central Limit Theorem, I remember thinking about that - how could you define a distribution to be the most obnoxious one possible? The normal distribution is like a frowny face. The Uniform distribution is like a "not impressed" face. Couldn't we have a smiley face distribution to be the anti-normal distribution?

## Waveforms and probabilities.
All synthesizers in electronic music use a mix of different types of simple waveforms. The sublime [TB-303](https://en.wikipedia.org/wiki/Roland_TB-303) synth line in the song at the top is very simple. The TB-303 a monophonic synth -- a single sawtooth wave (or square wave) with a bunch of filters on top that, in the right hands, turn it from buzzy electronic noise to an emotionally expressive instrument, almost like a digitial violin or human voice.

This got me thinking about what probability distributions based on different types of waveforms would look like. How likely is the waveform to be at each amplitude?

Here's the sawtooth waveform:

![/img/sawtooth.png](/img/sawtooth.png)

If we randomly sample from this wave (following a uniform distribution -- all numbers on the x axis are equally likely) and record the y value, then plot the values as a histogram, what would it look like? Think of it like we put a piece of toast on the Y axis of the graph, the X axis is time. How will the butter be distributed? 

It should be a flat line, like the Uniform distribution, since each stroke of butter is at a constant rate. We're alternating between a very fast wipe and a slower one, but in both cases, it doesn't spend any more time on one section of bread than another because it's a straight line.

![/img/sawtooth-distro.png](/img/sawtooth-distro.png)

## Advanced breakfast techniques
A square wave spends almost no time in the middle of the bread, so nearly all the butter will be at the edges. That's not a very interesting graph. What about a sine wave?

The sawtooth wave always has a constant slope, so the butter is evenly applied. With the sine wave, the slope changes over time. Because of that, the butter knife ends up spending more time at the extreme ends of the bread, where the slope is shallow, compared to the middle of the bread. The more vertical the slope, the faster the knife passes over that bit of bread, and the less butter it gets.

If we sample a bunch of values from the sine wave and plot their Y values as a histogram, we'll get something that looks like a smiley face -- lots of butter near the edges, less butter near the center of the toast. Or perhaps, in tribute to Ozzy, the index and pinky fingers of someone throwing the devil horns.

![/img/arcsine-from-sine.png](/img/arcsine-from-sine.png)

That's a perfectly valid buttering strategy in my book. The crust near the edges tends to be drier, and so can soak up more butter. You actually want to go a bit thinner in the middle, to maintain the structural integrity of the toast.

This distribution of butter forms a probability distribution called the arcsine distribution. It's an anti-normal distribution -- fat in the tails, skinny in the middle. A "why so serious?" distribution the Joker might appreciate. The mean is the least likely value, rather than the most likely value. And yet, the Central Limit Theorem still holds. The mean of even a fairly small number of values will behave like a Normal distribution.

Here are 1,000 iterations of an average of two samples from the arcsine distribution:

![/img/arcsin-approx-2.png](/img/arcsin-approx-2.png)

And averages of 5 samples:

![/img/arcsin-approx-5.png](/img/arcsin-approx-5.png)

And 30 samples at a time. Notice how the x range has shrunk down.

![/img/arcsin-approx-30.png](/img/arcsin-approx-30.png)

There are a lot of distributions that produce that U-type shape. They're known as [bathtub curves](https://en.wikipedia.org/wiki/Bathtub_curve). They come up when plotting the failure rates of devices (or people). For a lot of things, there's an elevated risk of failure near the beginning and the end, with lower risk in the middle. The curve is showing conditional probability -- for an iPhone to fail on day 500, it has to have not failed on the first 499 days.

![/img/Bathtub_curve.svg](/img/Bathtub_curve.svg)

(source: Wikipedia/Public Domain, [https://commons.wikimedia.org/w/index.php?curid=7458336](https://commons.wikimedia.org/w/index.php?curid=7458336))


## Particle man vs triangle man

The Uniform distribution isn't really that ab-Normal. It's flat, but it's very malleable. It turns into the normal distribution almost instantly. The symmetry helps.

If we take a single sample from a Uniform distribution over and over again, and plot a histogram, it's going to look flat, because every outcome is equally likely.

If we take the sum (or average) of two Uniform random variables, what would that look like? We're going to randomly select two numbers between 0 and 1 and sum them up. The result will be between 0 and 2. But some outcomes will be more likely than others.  The extremes (0 and 2) should be extremely unlikely, right? Both the random numbers would have to be close to 0 for the sum to be, and vice versa. There are a lot of ways to get a sum of .5, though. It could be .9 and .1, or .8 and .2, and so on.

If you look online, you can find many explanations of how to get the PDF of the sum of two Uniform distributions using calculus. ([Here's a good one](https://courses.cs.washington.edu/courses/cse312/20su/files/student_drive/5.5.pdf)). While formal proofs are important, it's not very intuitive. So, here's another way to think of it.

Let's say we're taking the sum of two dice instead of two Uniform random variables.  We're gonna start with two 4 sided dice. It will be obvious that we can scale the number of faces up, and the pattern will hold.

What are the possible combinations of dice? The dice are independent, so each combination is equally likely. Let's write them out by columns according to their totals:

|        |       |       |       |       |      |       |        
|--------|-------|-------|-------|-------|------|-------|
|(1, 1)  | (1,2) | (1,3) | (1,4) |  -    |  -   |   -   |
|   -    | (2,1) | (2,2) | (2,3) | (2,4) |  -   |  -    |
|   -    |  -    | (3,1) | (3,2) | (3,3) | (3,4)|  -    |
|   -    |  -    |   -   | (4,1) | (4,2) | (4,3)| (4,4) |

If we write all the possibilities out like this, it's gonna look like a trapezoid, whether there are 4 faces on the dice, or 4 bajillion. Each row will have one more column that's blank than the one before, and one column that's on its own off to the right. 

If we consolidate the elements, we're gonna get a big triangle, right? Each column up to the mean will have one more combo, and each column after will have one less.

|        |       |       |       |       |      |       |        
|--------|-------|-------|-------|-------|------|-------|
|(1, 1)  | (1,2) | (1,3) | (1,4) | (2,4) |(3,4) |(4,4)  |
|   -    | (2,1) | (2,2) | (2,3) | (3,3) |(4,3) |  -    |
|   -    |  -    | (3,1) | (3,2) | (4,2) | -    |  -    |
|   -    |  -    |   -   | (4,1) |  -    | -    | -     |


With a slight re-arrangement of values, it's clear the triangle builds up with each extra face we add to the dice.

|        |       |       |       |       |      |       |        
|--------|-------|-------|-------|-------|------|-------|
| (1, 1) | (1,2) | (2,2) | (2,3) | (3,3) |(3,4) |(4,4)  |
|   -    | (2,1) | (1,3) | (3,2) | (2,4) |(4,3) |  -    |
|   -    |  -    | (3,1) | (1,4) | (4,2) | -    |  -    |
|   -    |  -    |   -   | (4,1) |  -    | -    | -     |

The results for two 2 sided dice are embedded in the left 3 columns of table, then the results for two 3 sided dice on top of them, then two 4 sided dice. Each additional face will add 2 columns to the right. I'm not gonna formally prove anything, but hopefully it's obvious that it will always make a triangle.

That's the [triangular distribution](https://en.wikipedia.org/wiki/Triangular_distribution#Distribution_of_the_mean_of_two_standard_uniform_variables).

Here's a simulation, calculating the sum of two random uniform variables over and over, and counting their frequencies:

![/img/shaggy-triangle.png](/img/shaggy-triangle.png)

# 3 is the magic number

The sum (or average) of 3 Uniform random variables looks a whole lot like the normal distribution. The sides of the triangle round out, and we get something more like a bell curve. It's more than a parabola because the slope is changing on the sides. Here's what it looks like in simulation:

![/img/shaggy-parabola.png](/img/shaggy-parabola.png)

Here are three 5 sided dice. It's no longer going up and down by one step per column. The slope is changing as we go up and down the sides.

| 3         | 4         | 5         | 6         | 7         | 8         | 9         | 10        | 11        | 12        |
|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|
| (1, 1, 1) | (2, 1, 1) | (2, 2, 1) | (2, 2, 2) | (3, 3, 1) | (3, 3, 2) | (3, 3, 3) | (4, 4, 2) | (4, 4, 3) | (4, 4, 4) |
| -         | (1, 2, 1) | (2, 1, 2) | (3, 2, 1) | (3, 2, 2) | (3, 2, 3) | (4, 4, 1) | (4, 3, 3) | (4, 3, 4) | -         |
| -         | (1, 1, 2) | (1, 2, 2) | (3, 1, 2) | (3, 1, 3) | (2, 3, 3) | (4, 3, 2) | (4, 2, 4) | (3, 4, 4) | -         |
| -         | -         | (3, 1, 1) | (2, 3, 1) | (2, 3, 2) | (4, 3, 1) | (4, 2, 3) | (3, 4, 3) | -         | -         |
| -         | -         | (1, 3, 1) | (2, 1, 3) | (2, 2, 3) | (4, 2, 2) | (4, 1, 4) | (3, 3, 4) | -         | -         |
| -         | -         | (1, 1, 3) | (1, 3, 2) | (1, 3, 3) | (4, 1, 3) | (3, 4, 2) | (2, 4, 4) | -         | -         |
| -         | -         | -         | (1, 2, 3) | (4, 2, 1) | (3, 4, 1) | (3, 2, 4) | -         | -         | -         |
| -         | -         | -         | (4, 1, 1) | (4, 1, 2) | (3, 1, 4) | (2, 4, 3) | -         | -         | -         |
| -         | -         | -         | (1, 4, 1) | (2, 4, 1) | (2, 4, 2) | (2, 3, 4) | -         | -         | -         |
| -         | -         | -         | (1, 1, 4) | (2, 1, 4) | (2, 2, 4) | (1, 4, 4) | -         | -         | -         |
| -         | -         | -         | -         | (1, 4, 2) | (1, 4, 3) | -         | -         | -         | -         |
| -         | -         | -         | -         | (1, 2, 4) | (1, 3, 4) | -         | -         | -         | -         |

The notebook has a function to print it for any number of faces and dice. Go crazy if you like, but it quickly becomes illegible.

Here's the results of three 12 sided dice:

![/img/three-twelves.png](/img/three-twelves.png)

This isn't a Normal distribution, but it sure looks close to one.   

## Toast triangles

What if we feed the triangular distribution through the `sin()` function? To keep the toast analogy going, I guess we're spreading the butter with a sine wave pattern, but changing how hard we're pressing down on the knife to match the triangular distribution -- slow at first, then ramping up, then ramping down.

Turns out, if we take the sine of the sum of two uniform random variables (defined from the range of -pi to +pi), we'll get the arcsin distribution again! I don't know if that's surprising or not, but there you go.

## Knowing your limits
There's a problem with the toast analogy. (Well, at least one. There may be more, but I ate the evidence.)

The probability density function of the arcsine distribution looks like this:

It goes up to infinity at the edges!

![/img/arcsine-pdf.png](/img/arcsine-pdf.png)

The derivative of the `arcsin` function is `1/sqrt(1-x**2)` which goes to infinity as x approaches 0 or 1. That's what gives the arcsine distribution its shape. That also sort of breaks the toast analogy. Are we putting an infinite amount of butter on the bread for an infinetesimal amount of time at the ends of the bread? You can break your brain thinking about that, but you should feel confident that we put a finite amount of butter on the toast between any two intervals of time. We're always concerned with the defined amount of area underneath the PDF, not the value at a singular point.

Here's a histogram of the actual arcsine distribution -- 100,000 sample points put into 1,000 bins:

![/img/arcsine-hist.png](/img/arcsine-hist.png)

About 9% of the total probability is in the leftmost and rightmost 0.5% of the distribution, so the bins at the edges get really, really tall, but they're also really, really skinny. there's a bound on how big they can be.

The CDF (area under the curve of the PDF) of the arcsine distribution is well behaved, but its slope goes to infinity at the very edges.

![/img/arcsine-cdf.png](/img/arcsine-cdf.png)

## One for the road
The `sinc()` function is defined as `sin(x)/x`. It doesn't lead to a well-known distribution as far as I know, but it looks cool, like the logo of some aerospace company from the 1970's, so here you go:

![/img/sinc.png](/img/sinc.png)

Would I buy a Camaro with that painted on the hood? Yeah, probably.

## An arcsine of things to come
The arcsine distribution is extremely important in the field of random walks. Say you flip a coin to decide whether to turn north or south every block. How far north or south of where you started will you end up? How many times will you cross the street you started on?

I showed with the hot hand research that our intuitions about randomness are bad. When it comes to random walks, I think we do even worse. Certain *sensible* things almost never happen, while *weird* things happen all the time, and the arcsine distribution explains a lot of that.


### References/further reading
* [https://www.johndcook.com/blog/2009/02/12/sums-of-uniform-random-values/](https://www.johndcook.com/blog/2009/02/12/sums-of-uniform-random-values/)
* [https://www.jstor.org/stable/2287407](https://www.jstor.org/stable/2287407)
* [https://archive.org/details/dli.ernet.5666/](https://archive.org/details/dli.ernet.5666/)