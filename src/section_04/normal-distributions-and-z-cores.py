import statistics

# QUESTION 1
mean = 150
stdev = 28
# z = (x - mean) / stdev
# 2.28% of values fall below 94
x_1 = 94
z_score_1 = (x_1 - mean) / stdev

# cdf(x) -> cumulative distribution function returns the percentage of values below x
x1_percentile = statistics.NormalDist(mean, stdev).cdf(x_1) * 100
print(f"z_score_1 of {x_1} is {z_score_1}")

# 97.72% of values fall below 206
x_2 = 206
z_score_2 = (x_2 - mean) / stdev
x2_percentile = statistics.NormalDist(mean, stdev).cdf(x_2) * 100
print(f"z_score_2 of {x_2} is {z_score_2}")

dif_between = round(x2_percentile - x1_percentile)
print(f"difference between {x_2} and {x_1} is {dif_between}%")

# QUESTION 2
mean_q2 = 50
stdev_q2 = 3
x_q2 = 53
x_q2_percentile = round(statistics.NormalDist(mean_q2, stdev_q2).cdf(x_q2) * 100)
print(f"x_q2_percentile of {x_q2} is {x_q2_percentile}%")

# QUESTION 3
x_q3 = 12
z_score_q3 = -0.80
mean_q3 = 14
# we need to get the stdev_q3
# z = (x - mean) / stdev
# solve for stdev -> stdev = (x - mean) / z
stdev_q3 = (x_q3 - mean_q3) / z_score_q3
print(f"stdev_q3 of {x_q3} is {stdev_q3}")
