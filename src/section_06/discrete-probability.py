from stats import Dice, Statistics

die_1 = list(range(1, 7))
die_2 = list(range(1, 7))

dice_combinations = Dice.get_combinations(die_1, die_2)
dice_sums = Dice.get_dice_sums(dice_combinations)
print("Dice sums", dice_sums)

# (score, probability)
scores = [(1, 0.136), (2, 0.159), (3, 0.248), (4, 0.202), (5, 0.255)]


scores_variance = Statistics.get_discrete_variance(scores)
scores_std = Statistics.get_discrete_std(scores_variance[0])

print("Scores mean", scores_variance[1])
print("Scores standard deviation", scores_std)


# Probability of getting at least one heads in 5 trials
# P(X >= 1) = P(X = 1)+P(X = 2)+P(X = 3)+P(X = 4)+P(X = 5)
probability = 1 / 2
binomial_probability = sum(
    [Statistics.get_binomial_probability(5, i, probability) for i in range(1, 6)]
)
print(binomial_probability)

# P(X<= 5) = P(X = 0)+P(X = 1)+P(X = 2)+P(X = 3)+P(X = 4)+P(X = 5)
probability = 0.30
binomial_probability = sum(
    [Statistics.get_binomial_probability(10, i, probability) for i in range(0, 6)]
)
print(binomial_probability)

# P(11<=X<=15)
probability = 0.45
binomial_probability = sum(
    [Statistics.get_binomial_probability(15, i, probability) for i in range(11, 16)]
)
print(binomial_probability, 1 - binomial_probability)

# P(10<=X<=20)
probability = 0.32
binomial_probability = sum(
    [Statistics.get_binomial_probability(20, i, probability) for i in range(10, 21)]
)
print(binomial_probability)

# P(X=3)
probability = 0.655
print(Statistics.get_binomial_probability(3, 3, probability))
