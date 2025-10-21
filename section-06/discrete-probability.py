import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helpers import Dice, Statistics

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
