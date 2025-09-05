# From data table to Ogive
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')  # Must be called before importing pyplot


# Upper class boundaries
upper_class_boundaries = range(-10, 25, 5)

data = [0, 20, 10, 30, 30, 10, 30]
cumulative_frequencies = data
print(cumulative_frequencies)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(
    upper_class_boundaries, cumulative_frequencies,
    marker='o', linestyle='-', color='b'
)

# Labels and title
plt.title("Line graph ()")
plt.xlabel("")
plt.ylabel("")

# Grid
plt.grid(True)

# Show the plot
plt.savefig("line graph and ogives/output/question-5.png")
