import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Data
upper_class_boundaries = ['Walk', 'School bus', 'Day care V', 'Carpool']

dataset1 = [1, 10, 20, 26]
dataset2 = [5, 12, 14, 19]
dataset3 = [10, 22, 5, 15]
dataset4 = [8, 33, 3, 10]

# Convert to numpy arrays for easy math
x = np.arange(len(upper_class_boundaries))
bar_width = 0.2  # Smaller bar width for 4 groups

# Create plot
plt.figure(figsize=(8, 5))

plt.bar(x - 1.5*bar_width, dataset1, bar_width,
        label="Pre-school", color="skyblue")
plt.bar(x - 0.5*bar_width, dataset2, bar_width, label="First", color="orange")
plt.bar(x + 0.5*bar_width, dataset3, bar_width, label="Second", color="pink")
plt.bar(x + 1.5*bar_width, dataset4, bar_width,
        label="Third", color="lightgreen")

# Labels & title
plt.title("Modes of Transport to School")
plt.xlabel("Mode of Transport")
plt.ylabel("Number of Students")
plt.xticks(x, upper_class_boundaries)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save the plot
plt.savefig("two-way tables/output/question-4.png")
