import sys
import os
import matplotlib.pyplot as plt
import matplotlib

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
