import matplotlib.pyplot as plt
import matplotlib
import random

matplotlib.use("Agg")

# QUESTION 1
# Question: Calculate the covariance of the sample
x1 = [2, 3, 4, 5, 6]
y1 = [3, 5, 7, 9, 11]

# Formula for sample
# S_xy = Σ[(x_i - x̄)(y_i - ȳ)] / (n - 1)

# restrictions x and y lengths must be equal
assert len(x1) == len(y1)

n = len(x1)
x1_bar = sum(x1) / n
y1_bar = sum(y1) / n

numerator = sum([(x_i - x1_bar) * (y_i - y1_bar) for x_i, y_i in zip(x1, y1)])
denominator = n - 1

result = numerator / denominator
print(f"Q1 result: {result}")

# QUESTION 2
# Question: If x takes on the sample values 2,4,6,8,10,15, and y takes on the sample values 12,17,23,25,33,40, find the covariance of x and y.
x2 = [2, 4, 6, 8, 10, 15]
y2 = [12, 17, 23, 25, 33, 40]

# restrictions x and y lengths must be equal
assert len(x2) == len(y2)

n = len(x2)
x2_bar = sum(x2) / n
y2_bar = sum(y2) / n

numerator = sum([(x_i - x2_bar) * (y_i - y2_bar) for x_i, y_i in zip(x2, y2)])
denominator = n - 1

result = numerator / denominator
print(f"Q2 result: {result}")

# Question 3
# Question: Two corporations record their stock returns between 2010 and 2014. From the sample, calculate the covariance of their stock returns.
# y = 2010, 2011, 2012, 2013, 2014
# x = [2%,   1%,   -2%,  4%,   -1%]
# y = [3%,   0%,   1%,   2%,   1%]

# x3 = [2, 1, -2, 4, -1]
# y3 = [3, 0, 1, 2, 1]

# random values (No linear relationship between variables)
x3 = [random.randint(1, 500) for _ in range(100)]
y3 = [random.randint(1, 500) for _ in range(100)]

# restrictions x and y lengths must be equal
assert len(x3) == len(y3)

n = len(x3)
x3_bar = sum(x3) / n
y3_bar = sum(y3) / n

numerator = sum([(x_i - x3_bar) * (y_i - y3_bar) for x_i, y_i in zip(x3, y3)])
denominator = n - 1

result = numerator / denominator
print(f"Q3 result: {result}")

plt.scatter(x3, y3)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter plot of Q3")
plt.grid(True)
plt.savefig("section-04/output/covariance_q3_scatter_plot.png")
plt.close()
