import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Data
upper_class_boundaries = ['Fish', 'Cat', 'Dog', 'Other']  # x-axis categories
dataset1 = [8, 15, 7, 9]
dataset2 = [13, 10, 12, 5]  # Example comparison dataset

# Convert to numpy arrays for easy math
x = np.arange(len(upper_class_boundaries))
bar_width = 0.35  # width of each bar
print(x)

# Create plot
plt.figure(figsize=(8, 5))

plt.bar(x - bar_width/2, dataset1, bar_width,
        label="1st grade", color="skyblue")

plt.bar(x + bar_width/2, dataset2, bar_width,
        label="2nd grade", color="orange")

# Labels & title
plt.title("Favorite Pets by Grade")
plt.xlabel("Pet Type")
plt.ylabel("Number of Students")
plt.xticks(x, upper_class_boundaries)  # Set category labels
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save the plot
plt.savefig("two-way tables/output/question-1.png")
