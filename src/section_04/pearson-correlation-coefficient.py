import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

matplotlib.use("Agg")  # For environments without GUI

# Person correlation coefficient formula for sample
# r_xy = (Σ[(x_i - x̄)(y_i - ȳ)]) / n-1) / sqrt([Σ(x_i - x̄^2]/n-1) * [Σ(y_i - ȳ^2]/n-1)]
# Sample covariance by product of standard deviation of x and y
# r_xy = S_xy / (s_x * s_y)

# Person correlation coefficient formula for population
# r_xy = (Σ[(x_i - x̄)(y_i - ȳ)]) / sqrt([Σ(x_i - x̄^2]/n) * [Σ(y_i - ȳ^2]/n)]
# Population covariance by product of standard deviation of x and y
# r_xy = σ_xy / (σ_x * σ_y)

# x=ages and y=net worths (in thousands of dollars)
x = [20, 30, 40, 45, 50, 55, 60, 65, 75, 85]
y = [20000, 150000, 250000, 300000, 200000, 250000, 500000, 800000, 1200000, 900000]

# calculate x-bar and y-bar (means)
x_bar = sum(x) / len(x)
y_bar = sum(y) / len(y)

# calculate covariance (sample)
covariance = sum([(x_i - x_bar) * (y_i - y_bar) for x_i, y_i in zip(x, y)]) / (
    len(x) - 1
)

# calculate standard deviation of x and y
x_stdev = math.sqrt(sum([(x_i - x_bar) ** 2 for x_i in x]) / (len(x) - 1))
y_stdev = math.sqrt(sum([(y_i - y_bar) ** 2 for y_i in y]) / (len(y) - 1))

# calculate person correlation coefficient (sample)
person_correlation_coefficient = covariance / (x_stdev * y_stdev)
print(
    f"person_correlation_coefficient: {person_correlation_coefficient}"
)  # approx 0.882 (a strong positive linear relationship between the variables)

# scatter plot of x and y with linear regression line
plt.figure(figsize=(10, 5))
plt.scatter(x, y)

# linear regression line
z = np.polyfit(x, y, 1)  # [slope, intercept]
p = np.poly1d(z)  # polynomial function
plt.plot(x, p(x), "r-")  # plot the linear regression line in red

plt.xlabel("Age")
plt.ylabel("Net Worth")
plt.title("Scatter plot of Age vs Net Worth")
plt.grid(True)
plt.savefig("section-04/output/pearson_correlation_coefficient_scatter_plot.png")
plt.close()
