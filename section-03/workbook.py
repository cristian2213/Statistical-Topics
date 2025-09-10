import math
import sys
import os

# Add parent directory to path to import helpers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import Statistics


# ***************************
# MEASURES OF CENTRAL TENDENCY
# ***************************

# QUESTION 3
data_set = [13, 17, 18, 21, 24, 26, 35, 35, 52, 56]
mode = Statistics.get_mode(data_set)
print("question 3 mode", mode)

# QUESTION 4
data_set = [1, 2, 8, 13, 17, 20, 30, 31]
median = Statistics.get_median(data_set)
print("question 4 median", median)

# ***************************
# MEASURES OF SPREAD
# ***************************

# QUESTION 1
# Sarah is visiting dairy farms as part of a research project and counting the number of red cows at each farm she visits. Here is her data:
data_set = [0, 1, 1, 1, 2, 5, 5, 7, 7, 18, 24, 24]
iqr = Statistics.get_iqr(data_set)
print("question 1 iqr", iqr)

# QUESTION 3
# (value, frequency)
data_set = [(2, 5), (5, 2), (8, 1), (12, 2), (13, 2), (15, 3), (21, 1)]
full_list = Statistics.get_full_list_from_frequency(data_set)
iqr = Statistics.get_iqr(full_list)
median = Statistics.get_median(full_list)
print("question 3 iqr", iqr)
