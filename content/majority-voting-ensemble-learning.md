Title: Majority Voting in Ensemble Learning
Date: 2025-05-22 10:20
Category: machine learning
(notebook is available at [github.com/csdurfee/ensemble_learning](github.com/csdurfee/ensemble_learning).

## Ensemble Learning
AI and machine learning systems are often used for classification. Is this email spam or not? Is this person a good credit risk or not? Is this a photo of a cat or not?

There are a lot of ways to build classifiers, and they all potentially have different strengths and weaknesses. It's natural to try combining multiple models together to produce better and more robust results than the individual models would. 

Model A might be bad at classifying black cats but good at orange ones, model B might be bad at classifying orange cats but good at black ones, model C is OK at both. So if we average together the results of the three classifiers, or go with the majority opinion between them, the results might be better than the individual classifiers.

This is called an ensemble. Random forests and gradient boosting are two tried and true machine learning techniques that use ensembles of *weak learners* -- a large number of deliberately simple models that are all trained on different subsets of the data. This strategy can lead to systems that are more powerful than their individual components. While each little tree in a random forest is weak and prone to overfitting, the forest as a whole can be robust and give high quality predictions.

## Majority Voting
We can also create ensembles of *strong learners* -- combining multiple powerful AI or machine learning models together. Each individual model is powerful enough to do the entire classification on its own, but we hope to achieve higher accuracy by combining their results.  The most common way to do that is with voting. Query several classifiers, and have the ensemble return the majority pick, or otherwise combine the results.

There are some characteristics of ensembles that seem pretty common-sense [Bonab 2017]. The classifiers in the ensemble need to be *diverse*: as different as possible in the mistakes they make. If they all make the same mistakes, then there's no way for the ensemble to correct for that. 

The more classification categories, the more classifiers are needed in the ensemble. However, in real world settings, there's usually a point where adding more classifiers doesn't improve the ensemble. 

## <a name="model"></a>The Model
I like building really simple models. They can illustrate fundamental characteristics, and show what happens at the extremes. 

So I created an extremely simple model of majority voting (see [notebook](github.com/csdurfee/ensemble_learning)). I'm generating a random list of 0's and 1's, indicating the ground truth of some binary classification problem. Then I make several copies of the ground truth and randomly flip `x%` of the bits. Each of those copies represent the responses from an individual classifier within the ensemble. Each fake classifier will have `100-x%` accuracy. There's no correlation between the wrong answers that each classifier gives, because the changes were totally random. 

For the fake classifiers with 60% accuracy, they will both be right `60% * 60% = 36%` of the time, and both wrong `40% * 40% = 16%`. So they will agree `36% + 16% = 52%` of the time at minimum.

That's different from the real world. Machine learning algorithms trained on the same data will make a lot of the same mistakes. If there are outliers in the data, any classifier can overfit on them. And they're all going to find the same basic trends in the data. 

Bootstrapping (training each component on different slices of the data) can help a bit with overfitting, but there's no way to overcome fundamental deficiencies in the training data. If there aren't a lot of good walrus pictures in the training data, every model is probably going to be bad at recognizing walruses. There's no way to make up for what isn't there.

## Theory vs Reality

In the real world, there seem to be limits on how much an ensemble can improve classification. On paper, and in the simulation, there are none.

What is the probability of the ensemble being wrong about a particular classification?

That's the probability that the majority of the classifiers predict 0, given that the true value is 1 (and vice versa). If each classifier is more likely to be right than wrong, as the number of classifiers goes to infinity, the probability of the majority of predictions being wrong goes to 0.

If each binary classifier has a probability > .5 of being right, we can make the ensemble arbitrarily precise if we add enough classifiers to the ensemble (assuming their errors are independent). We could use the normal approximation to the binomial distribution to get the exact number, if necessary.

Let's say each classifier is only right 50.5% of the time. We might have to add 100,000 of them to the ensemble, but we can make the error rate arbitrarily small.

## Correlated models ruin ensembles

The big difference between my experiment and reality is that the errors the fake classifiers make are totally uncorrelated with each other. I don't think that would ever happen in the real world.

The more the classifiers' wrong answers are correlated with each other, the less useful the ensemble becomes. If they are 100% correlated with each other, the ensemble will give the exact same results as the individual classifiers, right? An ensemble doesn't *have to* improve results.

To put it in human terms, the "wisdom of the crowd" comes from people in the crowd having wrong beliefs about uncorrelated things. If most people are wrong in the same way, there's no way to overcome that with volume. 

My experience has been that different models tend to make the same mistakes, even if they're using very different AI/machine learning algorithms, and a lot of that is driven by weaknesses in the training data used.

For a more realistic simulation, I created models with correlated answers, so that the models agree with the ground truth 60% of the time, and with each other 82% of the time instead of the theoretical minimum 52% of the time. (In general we'd want to use the [kappa statistic](https://en.wikipedia.org/wiki/Cohen%27s_kappa) as a measure of correlation, not just the percentage overlap.)

The simulation shows that if the classifiers' responses are correlated with each other, there's a hard limit to how much the ensemble can improve things. 

Even with 99 classifiers in the ensemble, the simulation only achieves an f1 score of .62. That's just a slight bump from the .60 achieved individually. There is no marginal value to adding more than 5 classifiers to the ensemble at this level of correlation.

## Ensembles: The Rich Get Richer
I've seen voting ensembles suggested for especially tricky classification problems, where the accuracy for even the  best models is pretty low. I haven't found that to be true, though, and the simulation backs that up. Ensembles are only going to give a significant boost if the individual classifiers are significantly better than 50% accuracy.

The more accurate the individual classifiers, the bigger the boost from the ensemble. These numbers are for an ensemble of 3 classifiers (with no correlation between their responses):

| Classifier Accuracy | Ensemble Accuracy |
|----|----|
| 55% | 57% |
| 60% | 65% |
| 70% | 78% |
| 80% | 90% |


## Hard vs. soft voting

There are two different ways of doing majority voting, hard and soft. This choice can have an impact on how well an ensemble works, but I haven't seen a lot of guidance on when to use each. 

*Hard voting* is where we convert the outputs of each binary classifier into a boolean yes/no, and go with the majority opinion. If there are an odd number of components and it's a binary classification, there's always going to be a clear winner. That's what I've been simulating so far.

*Soft voting* is where we combine the raw outputs of all the components, and then round the combined result to make the prediction. [sklearn's documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier) advises to use soft voting "for an ensemble of well-calibrated classifiers" without really specifying what that means.

In the real world, binary classifiers don't return a nice, neat 0 or 1 value. They return some value between 0 or 1 indicating a relative level of confidence in the prediction, and we round that value to 0 or 1. Classifiers won't ever return an exact 0 or 1 if they are based on probability distributions with infinite range -- to such models, nothing is impossible, just extremely unlikely.

If a classifier returns `.2`, we can think of it as the model giving a `20%` chance that the answer is `1` and an `80%` chance it's `0`. That's not really true of most machine learning models, but the big idea is that there's potentially additional context that we're throwing away by rounding the individual results.

For instance, say the raw results are `[.3,.4,.9]`. With hard voting, these would get rounded to `[0,0,1]`, so it would return `0`. With soft voting, it would take the average of `[.3,.4,.9]`, which is `.53`, which rounds to `1`. So the two methods can return different answers.

To emulate the soft voting case, I flipped a percentage of the bits, as before. Then I replaced every 0 with a number chosen randomly from the uniform distribution from `[0,.5]` and every `1` with a sample from `[.5,1]`. The values will still round to what they did before, but there's additional noise on top. 

In this experiment (3 classifiers in the ensemble), the soft voting ensemble gives less of a boost than the hard voting ensemble -- about half the benefits. As with hard voting, the more accurate the individual classifiers are, the bigger the boost the ensemble gives us. 

| Classifier Accuracy | Ensemble Accuracy |
|----|----|
| 55% | 56% |
| 60% | 62% |
| 70% | 74% |
| 80% | 85% |


## Discussion
Let's say a classifier returns `.21573` and I round that down to 0. How much of the `.21573` that got lost was noise, and how much was signal? If a classification task is truly binary, it could be all noise. Let's say we're classifying numbers as odd or even. Those are unambiguous categories, so a perfect classifier should always return exactly 0 or 1. It shouldn't say that three is odd, with 90% confidence. In that case, it clearly means the classifier is 10% wrong. There's no good reason for uncertainty.

On the other hand, say we're classifying whether photos contain a cat or not. What if a cat is wearing a walrus costume in one of the photos? Shouldn't the classifier return a value greater than 0 for the possibility of it not being a cat, even if there really is a cat in the photo? Isn't it somehow less cat-like than another photo where it's not wearing a walrus costume? In this case, the `.21573` at least partially represents signal, doesn't it? It's saying "this is pretty cat-like, but not as cat-like as another photo that scored `.0001`".

When I'm adding noise to emulate the soft voting case, is that *fair*? A different way of fuzzing the numbers (selecting the noise from a non-uniform distribution, for instance) might reduce the gap in performance between hard and soft voting ensembles, and it would probably be more realistic. But the point of a model like this is to show the extremes -- and it's possible that hard voting will give better results than soft voting.


## Big Takeaways
1. Ensembles aren't magic; they can only improve things significantly if the underlying classifiers are diverse and fairly accurate.
2. Hard and soft voting aren't interchangeable. If there's a lot of random noise in the responses, hard voting is probably a better option, otherwise soft voting is probably better. It's definitely worth testing both options when building an ensemble.
4. Anyone thinking of using an ensemble should look at the amount of correlation between the responses from different classifiers. If the classifiers are all making basically the same mistakes, an ensemble won't help regardless of hard vs. soft voting. If models with very different architectures are making the same mistakes, that probably reflects a weakness in the training data that can't be fixed by an ensemble.

### Citations
[Bonab 2017] Bonab, Hamed; Can, Fazli (2017). "Less is More: A Comprehensive Framework for the Number of Components of Ensemble Classifiers". arXiv:1709.02925

Tsymbal, A., Pechenizkiy, M., & Cunningham, P. (2005). Diversity in search strategies for ensemble feature selection. Information Fusion, 6(1), 83–98. doi:10.1016/j.inffus.2004.04.003 