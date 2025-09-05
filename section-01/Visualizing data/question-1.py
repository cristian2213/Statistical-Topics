# From data table to Ogive
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')  # Must be called before importing pyplot


def get_cumulative_frequencies(data: list) -> list:
    frequencies = []
    cumulative = 0
    for i in data:
        if i == data[0]:
            frequencies.append(i)
            cumulative = i
            continue

        cumulative += i
        frequencies.append(cumulative)
    return frequencies


# Upper class boundaries
upper_class_boundaries = [1, 2, 3, 4, 5, 6]

data = [350, 455, 600, 540, 1275, 1685]
cumulative_frequencies = get_cumulative_frequencies(data)
print(cumulative_frequencies)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(
    upper_class_boundaries, cumulative_frequencies,
    marker='o', linestyle='-', color='b'
)

# Labels and title
plt.title("Ogive (Sit-up program)")
plt.xlabel("Week")
plt.ylabel("Number of sit-ups completed")

# Grid
plt.grid(True)

# Show the plot
plt.savefig("Visualizing data/output/ogive_plot.png")
