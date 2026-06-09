Title: Harmonics
Date: 2025-07-31 10:20
Category: math
Tags: some educational value

[![Donna Summer and Giorgio Moroder, "I Feel Love" (Patrick Cowley Remix)](https://img.youtube.com/vi/5Ocq8UlLuuw/0.jpg)](https://www.youtube.com/watch?v=5Ocq8UlLuuw){:target="_blank"}

Song: [Donna Summer and Giorgio Moroder, "I Feel Love" (Patrick Cowley Remix)](https://www.youtube.com/watch?v=5Ocq8UlLuuw){:target="_blank"}

Notebook: [https://github.com/csdurfee/csdurfee.github.io/blob/main/harmonics.ipynb](https://github.com/csdurfee/csdurfee.github.io/blob/main/harmonics.ipynb)

I was gonna do random walks this week, but the thing about random walks is you don't know where you're gonna end up, and I ended up back at last week's topic again. 

Last time, we saw that the sine wave, sawtooth wave and square wave produced very different distributions.

All three waveforms are used in electronic music, and they all have different acoustic properties. A sine wave sounds like a "boop" -- think of the sound they play to censor someone who says a swear word on the TV.  That's a sine wave with a frequency of 1000Hz. Sawtooth waves are extremely buzzy. A square wave has, ironically, kind of a round sound, at least as far as how it gets used in electronic music.  A good example is the bass line to this week's song. 

It's not a pure square wave, and it's rare to ever hear pure sawtooth or square waves because they're harsh on the ears. Usually multiple waveforms are combined together and then passed through various filters and effects -- in other words, synthesized. 

Pretty much every sound you've ever heard is a mix of different frequencies. Only sine waves are truly pure, just a single frequency. I tried looking for an actual musical instrument that produces pure sine waves, and the closest thing (according to the internet, at least) is a tuning fork. 

Any other musical instrument, or human voice, or backfiring car, will produce overtones. There's one note that is perceived as the *fundamental frequency*, but every sound is kind of like a little chord when the overtones are included. 

For musical instruments, the loudest overtones are generally at frequencies that are a multiple of the original frequency. These overtones are called *harmonics*.

For instance, if I play a note at 400 Hz on a guitar, it will also produce harmonics at 800 Hz (2x the fundamental frequency), 1200 Hz (3x), 1600 Hz (4x), 2000 Hz (5x), and so on. This corresponds to the [harmonic series in mathematics](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)). It's the sum of the ratios of the wavelengths of the harmonics to the fundamental frequency: 1 + 1/2 + 1/3 + 1/4 + 1/5 + ...

### The clarinet is the squarest instrument
I played the clarinet in grade school and I am the biggest dork on the planet, so it's certainly metaphorically true. But it's also literally true.

There's a lot that goes into exactly which overtones get produced by a physical instrument, but most instruments put out the whole series of harmonics. [The clarinet is different](https://newt.phys.unsw.edu.au/jw/clarinetacoustics.html#harmonics). Because of a clarinet's physical shape, it pretty much only produces odd harmonics. So, in our example, 400 Hz, 1200 Hz, 2000 Hz, etc.

The square wave is like an idealized version of a clarinet -- it also only puts out odd harmonics. This is a result of how a square wave is constructed. In the real world, they're formed out of a combination of sine waves. Which sine waves? You guessed it -- the ones that correspond to the odd harmonic frequencies.

Here's the fundamental frequency combined with the 3rd harmonic:

![/img/square3.png](/img/square3.png)

It already looks a bit square-wavey. Additional harmonics make the square parts a bit more square.  Here's what it looks like going up to the 19th harmonic:

![/img/square21.png](/img/square21.png)

In the real world, we can only add a finite number of harmonics, but if we could combine an infinite number of them, we would get the ideal square wave. This is called the [Fourier series](https://en.wikipedia.org/wiki/Fourier_series) of the square wave.

Here's an illustration to help show how the square wave gets built up:

![/img/square-buildup.png](/img/square-buildup.png)

The red wave is the fundamental frequency. The orange square-ish wave is the result of combining the other colored waves with the red wave.

The sum normally would be scaled up a bit (multiplied by 4/pi), but it's easier without the scaling to see how the other waves sort of hammer the fundamental frequency into the shape of the square wave. At some points they are pushing it up, and other points pulling it down.

Perhaps this graph makes it clearer. The red is the fundamental, the yellow is the sum of all the other harmonics, and the orange is the combination of the two:

![/img/combine-harmonics-square.png](/img/combine-harmonics-square.png)

Where the yellow is above the X axis, it's pulling the fundamental frequency up, and where it's below, it's pulling the fundamental down.

### The sawtooth
A sawtooth wave is what you get when you combine all the harmonics, odd and even. Like the square wave, it starts to take its basic shape right away. Here's the fundamental plus the second harmonic:

![/img/sawtooth2.png](/img/sawtooth2.png)

And here it is going all the way up to the 10th harmonic:

![/img/sawtooth10.png](/img/sawtooth10.png)

Red fundamental plus yellow harmonics produce the orange sawtooth wave:

![/img/combine-harmonics-saw.png](/img/combine-harmonics-saw.png)

Last time, I talked about the sawtooth wave producing a uniform distribution of amplitudes -- the butter gets spread evenly over the toast. The graph above isn't a very smooth stroke of butter. It's not steadily decreasing, particularly at the ends. Here's what the distribution looks like at this point:

![/img/sawtooth10-amps.png](/img/sawtooth10-amps.png)

With an infinite series of harmonics, that graph will even out to a uniform distribution


### Getting even
What about only the even harmonics? Is that a thing? Not in the natural world as far as I know, but there's nothing stopping me from making one. (It wouldn't be the worst musical crime I've ever committed.)

Here's what a combo of just the even harmonics looks like:

![/img/even-harmonics.png](/img/even-harmonics.png)

Thanks to a little code from the pygame project, it's easy to turn that waveform into a sound file. It sounds like an angry computer beep, with a little flutter mixed in.

[Here's an audio sample](/audio/evens_clean.wav){:target="_blank"}

### In my prime
The [harmonic series of primes](https://mathworld.wolfram.com/HarmonicSeriesofPrimes.html) is what it sounds like: the harmonic series, but just the prime numbers: 1 + 1/2 + 1/3 + 1/5 + 1/7 + 1/11 + 1/13 + ....

Although it's important in mathematics, I don't have a good musical reason to do this. But if you can throw the prime numbers into something, you gotta do it.

As a sound, I kinda like it. It's nice and throaty. [Here's what it sounds like.](/audio/primes.wav){:target="_blank"}

It doesn't really sound like a sawtooth wave or a square wave to me. Here's the waveform:

![/img/prime-waveform.png](/img/prime-waveform.png)

Here's what the distribution of amplitudes looks like:

![/img/prime-amp.png](/img/prime-amp.png)

### Dissonance
Some of the overtones of the harmonic series don't correspond with the 12 notes of the modern western musical scale (called 12 tone equal temprament, or 12TET). The first 4 harmonics of the series are nice and clean, but after that they get weird. Each harmonic in the series is smaller in amplitude than the previous one, so it has less of an effect on the shape of the final wave. So the dissonance is there, but it's way in the background.

The prime number bloop I made above should be extra *weird*. The 2nd and 3rd harmonics are included, so those will sound nice, but after that they are at least a little off the standard western scale.

Say we're playing the *prime bloop* at A4 (the standard pitch used for tuning).  Here's how the harmonics work out. A cent is 1% of a semitone. So a note that is off by 50 cents is right between two notes on the 12 tone scale.

|harmonic # | frequency | pitch | error |
|-----------|-----------|-------|-------|
|  1        | 440 Hz    | A4    | 0     |
|  2        | 880 Hz    | A5    | 0     |
|  3        | 1320      | E6    | +2 cents  |
|  5        | 2200      | C#7   | -14 cents |
|  7        | 3080      | G7    | +31 cents |
| 11        | 4840      | D#8   | -49 cents |
| 13        | 5720      | F8    | +41 cents |
| 17        | 7480      | A#8    | +5 cents |

(Note the 3rd harmonic, E6, is a little *off* in 12TET, despite being a *perfect fifth* -- an exact 3:2 ratio with the A5.)

### Harmonics aren't everything
While it's true that any audio can be decomposed into a bunch of sine waves, the fundamental frequency and the harmonics aren't really what gives an instrument its unique timbre. It's hundreds or thousands of tiny overtones that don't line up with the harmonics.

Here are the spectra of two different piano sounds playing at 220 Hz. One is a somewhat fake piano sound (Fruity DX10), the other a natural, rich sounding one (LABS Soft Piano, which you might've heard before if you listen to those "Lofi Hip Hop Beats to Doomscroll/Not Study To" playlists). Can you guess which is which?

![/img/real-piano.png](/img/real-piano.png)

![/img/fake-piano.png](/img/fake-piano.png)

The answer may surprise you. I mean, it can't be that surprising since there are only 2 options. But I'd probably get it wrong, if I didn't already know which is which.

### Sources/Notes
[This website from UNSW was invaluable](https://www.phys.unsw.edu.au/music/), particularly [https://newt.phys.unsw.edu.au/jw/harmonics.html](https://newt.phys.unsw.edu.au/jw/harmonics.html)

Code used to generate the audio: [https://stackoverflow.com/questions/56592522/python-simple-audio-tone-generator](https://stackoverflow.com/questions/56592522/python-simple-audio-tone-generator)
     
"The internet" claiming the sound of a tuning fork is a sine wave here (no citation given): [https://en.wikipedia.org/wiki/Tuning_fork#Description](https://en.wikipedia.org/wiki/Tuning_fork#Description).

There are many good videos on Youtube about 12TET and Just Intonation, by people who know more about music than me. Here's one from David Bennett: [https://www.youtube.com/watch?v=7JhVcGtT8z4](https://www.youtube.com/watch?v=7JhVcGtT8z4)