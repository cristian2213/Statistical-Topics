import math
# QUESTION 1
# Question: A website asks visitors to rate their user experience on a scale from 1 to 10, with 1 being the worst experience, and 10 being the best experience. They record 50 responses. Calculate the mean satisfaction score.

# Ratings and corresponding number of users
ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_users = [2, 1, 3, 5, 7, 4, 8, 7, 12, 1]

# weighted mean = Σ(w_i * x_i) / Σw_i
# w_i = weight = number of users
# x_i = rating

satisfaction_score = sum([w_i * x_i for w_i, x_i in zip(num_users, ratings)]) / sum(
    num_users
)

print(f"Q1 satisfaction_score: {satisfaction_score}\n")


# QUESTION 2
# Question: Mark’s grade points are 3.0 for English, which corresponds to 4 credits, 4.0 for Physics, which corresponds to 6 credits, 3.5 for Chemistry, which corresponds to 5 credits, and 3.8 for History, which corresponds to 3 credits. Calculate his grade point average.
grade_points = [3.0, 4.0, 3.5, 3.8]
credits = [4, 6, 5, 3]

# w_i = weight = credits
# x_i = grade point

grade_points_avg = sum([w_i * x_i for w_i, x_i in zip(credits, grade_points)]) / sum(
    credits
)

print(f"Q2 grade_points_avg: {grade_points_avg}\n")

# QUESTION 3
# Question: Given the frequency table of grouped data, calculate the sample mean, variance, and standard deviation.

# Class intervals (as tuples representing ranges)
x = [(1, 3), (4, 6), (7, 9), (10, 12), (13, 15)]

# Frequencies for each class interval
frequency = [2, 5, 12, 4, 6]


def get_midpoint(interval: tuple):
    return (interval[0] + interval[1]) / 2


# x_bar = Σ(f_i * x_i) / Σf_i
x_bar = sum(
    [f_i * get_midpoint(interval) for interval, f_i in zip(x, frequency)]
) / sum(frequency)

# Grouped variance = Σ(f_i * (M_i - x̄)^2) / Σf_i - 1
s2 = sum(
    [f_i * (get_midpoint(interval) - x_bar) ** 2 for interval, f_i in zip(x, frequency)]
) / (sum(frequency) - 1)

s = math.sqrt(s2)

print(f"Q3 grouped mean: {x_bar}")
print(f"Q3 grouped variance: {s2}")
print(f"Q3 grouped standard deviation: {s}")
