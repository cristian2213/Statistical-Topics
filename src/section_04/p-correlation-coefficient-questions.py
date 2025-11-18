import math

# QUESTION 1
# Question: Given the sample covariance S_xy = 0.456 and the sample standard deviations S_x = 2.53 and S_y = 0.25, calculate the value of the correlation.

# r_xy = S_xy / (S_x * S_y)
r_xy = 0.456 / (2.53 * 0.25)
print(f"Q1 r_xy: {r_xy}")  # ~0.7209 (positive and strong correlation)

# QUESTION 2
# Question: Two corporations record their stock returns between 2010 and 2014. Calculate the value of the correlation coefficient and interpret the result.

# 2010, 2011, 2012, 2013, 2014
x = [2, 1, -2, 4, -1]  # %
y = [3, 0, 1, 2, 1]  # %

# calculate covariance (sample)
x_bar = sum(x) / len(x)
y_bar = sum(y) / len(y)

covariance = sum([(x_i - x_bar) * (y_i - y_bar) for x_i, y_i in zip(x, y)]) / (
    len(x) - 1
)

# calculate standard deviation of x and y
x_stdev = math.sqrt(sum([(x_i - x_bar) ** 2 for x_i in x]) / (len(x) - 1))
y_stdev = math.sqrt(sum([(y_i - y_bar) ** 2 for y_i in y]) / (len(y) - 1))

# calculate correlation coefficient
r_xy = covariance / (x_stdev * y_stdev)
print(f"Q2 r_xy: {r_xy}")  # ~0.4960 (positive and moderate correlation)

# QUESTION 3
# Question: Given the sample covariance S_xy = -0.12 of the data set, calculate the value of the correlation coefficient.

x = [12, 5, 8, 18, 6, 5, 11]
y = [0.5, 0.8, 0.3, 0.4, 0.55, 0.25, 0.67]

# calculate standard deviation of x and y
x_bar = sum(x) / len(x)
y_bar = sum(y) / len(y)

x_stdev = math.sqrt(sum([(x_i - x_bar) ** 2 for x_i in x]) / (len(x) - 1))
y_stdev = math.sqrt(sum([(y_i - y_bar) ** 2 for y_i in y]) / (len(y) - 1))

# calculate correlation coefficient
r_xy = -0.12 / (x_stdev * y_stdev)
print(f"Q3 r_xy: {r_xy}")  # ~-0.1280 (negative and very weak correlation)
