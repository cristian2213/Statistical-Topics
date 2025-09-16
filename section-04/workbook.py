import sys
import os
import matplotlib.pyplot as plt
import matplotlib
import statistics

matplotlib.use("Agg")

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helpers import Statistics

print(
    "# ***************************\n"
    "# MEAN, VARIANCE, AND STANDARD DEVIATION\n"
    "# ***************************"
)

# QUESTION 1
aggregation = 10  # points
data_set = range(40, 81, 2)
new_data_set = [value + aggregation for value in data_set]
data_set_mean = Statistics.get_mean(data_set)
new_data_set_mean = Statistics.get_mean(new_data_set)
data_set_std = Statistics.get_standard_deviation(data_set, True)
new_data_set_std = Statistics.get_standard_deviation(new_data_set, True)
# Conclusion: The standard deviation doesn't change when we add a constant to all data points and the mean will change by k units.


# QUESTION 2
dot_plot = [(0, 3), (1, 0), (2, 0), (3, 5), (4, 2), (5, 3), (6, 0)]
full_list = Statistics.get_full_list_from_frequency(dot_plot)


def custom_mean_cb():
    mean = Statistics.get_weighted_mean(dot_plot)
    return mean


dot_plot_variance = Statistics.get_variance(
    data_set=full_list,
    population=False,
    mean_cb=custom_mean_cb,
)
print("question 2 variance", dot_plot_variance, "\n")

# QUESTION 3
sample_set = [97, 110, 112, 121, 110, 98]
sample_mean = Statistics.get_mean(sample_set)
deviations = [value - sample_mean for value in sample_set]
deviations_squared = [deviation**2 for deviation in deviations]
print("question 3 deviation column", deviations)
print("question 3 squared column", deviations_squared, "\n")

# QUESTION 4
total_items = 25
variance = 212 / total_items
std = variance ** (1 / 2)
print("question 4 std", std, "\n")

print(
    "# ***************************\n"
    "# FREQUENCY HISTOGRAMS AND POLYGONS, AND DENSITY CURVES\n"
    "# ***************************"
)

# QUESTION 2
crayons_by_student = [1, 4, 5, 5, 9, 11, 13, 14, 15, 15, 16, 16, 16, 17, 17, 20]
crayon_intervals = [(1, 5), (6, 10), (11, 15), (16, 20)]
# crayon_intervals = [(1, 5), (5, 10), (10, 15), (15, 20)]
frequencies = Statistics.get_interval_frequencies(crayons_by_student, crayon_intervals)
print("question 2 frequencies", frequencies, "\n")

fig, ax = plt.subplots()
ax.bar(frequencies.keys(), [freq[1] for freq in frequencies.values()])
ax.set_title("Histogram of Crayons by Student")
ax.set_xlabel("Number of Crayons")
ax.set_ylabel("Relative Frequency")
ax.grid(True)
plt.savefig("section-04/output/question-2-histogram.png", bbox_inches="tight")
plt.close()

# QUESTION 3
scores_set = [
    40,
    95,
    32,
    91,
    40,
    72,
    32,
    33,
    81,
    61,
    40,
    87,
    46,
    83,
    59,
    78,
    55,
    61,
    47,
    101,
    77,
    82,
    83,
    65,
    88,
    99,
    91,
    87,
]
scores_intervals = [
    (30, 39),
    (40, 49),
    (50, 59),
    (60, 69),
    (70, 79),
    (80, 89),
    (90, 99),
    (100, 109),
]
frequencies = Statistics.get_interval_frequencies(scores_set, scores_intervals)
print("question 3 frequencies", frequencies, "\n")

# frequency polygon
fig, ax = plt.subplots()
ax.fill_between(
    frequencies.keys(), [freq[1] for freq in frequencies.values()], closed=True
)
ax.set_title("Frequency Polygon of Scores")
ax.set_xlabel("Score")
ax.set_ylabel("Relative Frequency")
ax.grid(True)
plt.savefig("section-04/output/question-3-frequency-polygon.png", bbox_inches="tight")
plt.close()

# QUESTiON 3
data_set = [6, 8, 9, 10, 10, 11, 11, 12, 12, 13, 15, 15, 18, 19, 20, 20, 21]
iqr = Statistics.get_iqr(data_set)
q1 = iqr["q1"]
q3 = iqr["q3"]
iqr = iqr["iqr"]
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
outliers = [value for value in data_set if value < lower_bound or value > upper_bound]
print(lower_bound, upper_bound, outliers, "\n")

# QUESTION 4
data_set = [
    0,
    18,
    19,
    20,
    20,
    20,
    21,
    23,
    23,
    23,
    24,
    24,
    24,
    24,
    24,
    25,
    25,
    25,
    25,
    25,
    25,
    30,
    30,
    31,
]
result = Statistics.get_outliers(data_set)
print(result, "\n")
# Central tendency: Median
# Spread : IQR

# QUESTION 5
data_set = [(12, 1), (13, 0), (14, 1), (15, 3), (16, 5), (17, 7), (18, 8), (19, 5)]
full_list = Statistics.get_full_list_from_frequency(data_set)
median = Statistics.get_median(full_list)
outliers = Statistics.get_outliers(full_list)
iqr = Statistics.get_iqr(full_list)
print(median, outliers, iqr, "\n")
# Shape: Left-skewed distribution
# Central tendency: 17.0
# Spread : IQR 2
# Outliers: [12]

# QUESTION 6
data_set = [(22, 1), (23, 2), (24, 3), (25, 4), (26, 3), (27, 2), (28, 1)]
full_list = Statistics.get_full_list_from_frequency(data_set)
median = Statistics.get_median(full_list)
outliers = Statistics.get_outliers(full_list)
standard_deviation = Statistics.get_standard_deviation(full_list)
print(median, outliers, standard_deviation, "\n")
# Shape: Symmetric distribution
# Central tendency: Mean or Median 25.0
# Spread : Standard Deviation 1.632993161855452
# Outliers: None

print(
    "# ***************************\n"
    "# NORMAL DISTRIBUTIONS AND Z-SCORES\n"
    "# ***************************"
)

# QUESTION 1
mean = 62
std = 5
value = 50
z_score = (value - mean) / std
print("question 1 z-score", z_score, "\n")

# QUESTION 3 (CMs)
mean = 170
std = 8
value = 154
# returns the percentage of values less than or equal to the given value
percentage = statistics.NormalDist(mean, std).cdf(value) * 100
print("question 3 percentage", percentage, "%", "\n")

# QUESTION 4 (Inches)
mean = 18
std = 4
percentile = 0.21
# returns the value at the given percentile
value_21st_percentile = statistics.NormalDist(mean, std).inv_cdf(percentile)
print("question 4 value", value_21st_percentile, "\n")

# QUESTION 5 (68% of normal distribution)
range_68_percent = (mean - std, mean + std)
print("question 5 values", range_68_percent, "\n")

# QUESTION 6 (IQ Scores)
mean = 100
std = 16
val1 = 120
val2 = 140
z_core1 = (val1 - mean) / std
z_core2 = (val2 - mean) / std
percentage1 = Statistics.z_to_probability(z_core1)
percentage2 = Statistics.z_to_probability(z_core2)
print("question 6 percentage", percentage2 - percentage1)

print(
    "# ***************************\n"
    "# CHEBYSHEV’S THEOREM\n"
    "# ***************************"
)

# QUESTION 1
# Ans. It tells us that at least 75% of the data must be within 2 standard deviations of the mean.

# QUESTION 2 ( What percentage of the strawberries in the basket have a weight between 1.5 and 2.5 ounces?)
mean_weight = 2
std = 0.35
weights = (1.5, 2.5)
k1 = (weights[1] - mean_weight) / std
k2 = (weights[0] - mean_weight) / std
k = k1 if k1 > 0 else k2
percentage = 1 - (1 / k**2)
print("question 2 percentage", percentage, "%", "\n")
# Ans. 0.51% of the strawberries in the basket have a weight between 1.5 and 2.5 ounces.

# QUESTION 3
total_whales = 580
mean_distance = 2_000  # miles
std = 175  # miles
distance_range = (1_600, 2_400)
k1 = Statistics.get_k_deviations(distance_range[0], mean_distance, std)
k2 = Statistics.get_k_deviations(distance_range[1], mean_distance, std)
k = Statistics.get_positive_k(k1, k2)
percentage = Statistics.get_chebyshev_theorem(k) * 100
whales = Statistics.get_percentage_of(total_whales, percentage)
print(
    "question 3 amount of whales which traveled between 1,600 and 2,400 miles",
    whales,
    "\n",
)
# Ans. About 469 whales traveled between 1,600 and 2,400 miles.

# QUESTION 4 (Find the height range for the central 90% of team members.)
mean_height = 73  # inches
std = 1.8
chebyshev_percentage = 90 / 100
k = Statistics.get_k_inverse(chebyshev_percentage)
result = Statistics.get_ranges_by_k(mean_height, k, std)
print(f"question 4 height range ({result[0]} to {result[1]})", "\n")
# Ans. 90% of team members have a height between ~67.3 and ~78.7 inches.

# QUESTION 5 (Find the values that make up the middle 75% of the yearly acceptance range.)
total_students = 40_000
mean_new_students_by_year = 10_000
std = 500
chebyshev_percentage = 75 / 100
k = Statistics.get_k_inverse(chebyshev_percentage)
result = Statistics.get_ranges_by_k(mean_new_students_by_year, k, std)
print(f"question 5 yearly acceptance range ({result[0]} to {result[1]})", "\n")
# Ans. The middle 75% of the yearly acceptance range is between 9,000 and 11,000 students.

# QUESTION 6 (Find the weight range for the central 82% of the data.)
mean_weight = 100  # pounds
std = 24
chebyshev_percentage = 82 / 100
k = Statistics.get_k_inverse(chebyshev_percentage)
result = Statistics.get_ranges_by_k(mean_weight, k, std)
print(f"question 6 weight range ({result[0]} to {result[1]})", "\n")
# Ans. The central 82% of the data has a weight between ~43.4 and ~156.6 pounds.
