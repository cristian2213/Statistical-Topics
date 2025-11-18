import sys
import os
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")

# Add parent directory to path to import helpers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.stats.helpers import Statistics, TemperatureConverter, Normalizer


print(
    "# ***************************\n"
    "# MEASURES OF CENTRAL TENDENCY\n"
    "# ***************************"
)

# QUESTION 3
data_set = [13, 17, 18, 21, 24, 26, 35, 35, 52, 56]
mode = Statistics.get_mode(data_set)
print("question 3 mode", mode)

# QUESTION 4
data_set = [1, 2, 8, 13, 17, 20, 30, 31]
median = Statistics.get_median(data_set)
print("question 4 median", median)

print(
    "# ***************************\n# MEASURES OF SPREAD\n# ***************************"
)

# QUESTION 1
# Sarah is visiting dairy farms as part of a research project and counting the number of red cows at each farm she visits. Here is her data:
data_set = [0, 1, 1, 1, 2, 5, 5, 7, 7, 18, 24, 24]
iqr = Statistics.get_iqr(data_set)
print("question 1 iqr", iqr, "\n")

# QUESTION 3
# (value, frequency)
data_set = [(2, 5), (5, 2), (8, 1), (12, 2), (13, 2), (15, 3), (21, 1)]
full_list = Statistics.get_full_list_from_frequency(data_set)
iqr = Statistics.get_iqr(full_list)
median = Statistics.get_median(full_list)
print("question 3 iqr", iqr, "\n")

# QUESTION 6
# (value, day of week)
data_set = [(10, 1), (6, 2), (4, 3), (6, 4), (10, 5), (8, 6), (12, 7)]
data_iqr = Statistics.get_iqr([value for value, _ in data_set])
print("question 6 iqr", data_iqr, "\n")

print(
    "# ***************************\n"
    "# CHANGING THE DATA AND OUTLIERS\n"
    "# ***************************"
)
# QUESTION 3
data_set = [24, 70, 80, 85, 85, 90, 91, 95, 99, 100]
data_mean = Statistics.get_mean(data_set)
data_median = Statistics.get_median(data_set)
print("question 3 mean", data_mean)
print("question 3 median", data_median, "\n")

# QUESTION 4
# weighted sample mean formula
# X̄ = Σ(w_i * x_i) / Σw_i
# x_i = value
# w_i = weight
# (value, weight)
data_set = [(1, 3), (2, 10), (3, 2), (4, 2)]
weighted_mean = Statistics.get_weighted_mean(data_set)
full_list = Statistics.get_full_list_from_frequency(data_set)
median = Statistics.get_median(full_list)
print("question 4 weighted mean", weighted_mean)
print("question 4 median", median, "\n")
# mean (~2.18) > median (2) -> a little imbalance in the data, but it's not too much

# QUESTION 5
# (points scored, frequency)
data_set = [
    (0, 5),
    (1, 6),
    (2, 7),
    (3, 8),
    (4, 9),
    (5, 10),
    (6, 9),
    (7, 8),
    (8, 7),
    (9, 6),
    (10, 5),
]
weighted_mean = Statistics.get_weighted_mean(data_set)
full_list = Statistics.get_full_list_from_frequency(data_set)
median = Statistics.get_median(full_list)
print("question 5 weighted mean", weighted_mean)
print("question 5 median", median, "\n")
# mean (5) = median (5) -> symmetric distribution (equal amount of area on both sides of the median)

# QUESTION 6
# data in degrees Celsius
mean = 102
median = 101
mode = 99
range = 7
iqr = 4
# Degrees Celsius -> Fahrenheit
# F = (C * 9/5) + 32
mean_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(mean)
median_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(median)
mode_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(mode)
# range and iqr don't change when each value is shifted by a constant
range_fahrenheit = range * 9 / 5
iqr_fahrenheit = iqr * 9 / 5
print("question 6 mean", mean_fahrenheit)
print("question 6 median", median_fahrenheit)
print("question 6 mode", mode_fahrenheit)
print("question 6 range", range_fahrenheit)
print("question 6 iqr", iqr_fahrenheit, "\n")

print(
    "# ***************************\n"
    "# BOX-AND-WHISKER PLOTS\n"
    "# ***************************"
)

# QUESTION 1
min_value = 216_290
max_value = 845_300
range = Statistics.get_range((min_value, max_value))
quartile_1 = 324_528
quartile_3 = 790_390
iqr = Statistics.get_iqr((quartile_1, quartile_3))
print("question 1 range", Normalizer.thousands_separator(range))
print("question 1 iqr", Normalizer.thousands_separator(iqr["iqr"]), "\n")

# QUESTION 2
# min, q1, median, q3, max
data_set = sorted([35, 10, 40, 40, 20, 10, 15, 14, 18, 35])
extremes = Statistics.get_extremes(data_set)
iqr = Statistics.get_iqr(data_set)
median = Statistics.get_median(data_set)
print("question 2 min", extremes["min"])
print("question 2 q1", iqr["q1"])
print("question 2 median", median)
print("question 2 q3", iqr["q3"])
print("question 2 max", extremes["max"])
print("question 2 iqr", iqr["iqr"], "\n")

# QUESTION 3
# Create a box plot based on the following data:
mode = 300
min_value = 100
quartile_1 = 200
median = 2_000
mean = 1_887.5
quartile_3 = 3_050
max_value = 4_800

fig, ax = plt.subplots()

# Create a horizontal box plot using the five-number summary
ax.boxplot([min_value, quartile_1, median, quartile_3, max_value], vert=False)
ax.set_xlim(0, 5000)
ax.set_ylim(0, 2)

# Add mean and mode
ax.plot(mean, 1, "ro", label="Mean")
ax.plot(mode, 1, "g^", label="Mode")

# Add legend and labels
ax.legend()
ax.set_xlabel("Values")
ax.set_title("Horizontal Box Plot with Mean and Mode")

plt.savefig("section-03/output/box-and-whisker-plots-q3.png")
plt.close()

# QUESTION 6
# stem and leaf
data_set = {1: [3, 7, 8], 2: [1, 4, 6], 3: [5, 5], 4: [], 5: [2, 6]}
full_list = Statistics.get_list_from_steam_and_leaf(data_set)

fig, ax = plt.subplots()
ax.boxplot(full_list, vert=False)

ax.set_xlim(0, 65)
ax.set_ylim(0.5, 1.5)
ax.set_title("Box Plot of Book ratings")
plt.savefig("section-03/output/box-and-whisker-plots-q6.png", bbox_inches="tight")
plt.close()
