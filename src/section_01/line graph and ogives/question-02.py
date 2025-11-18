# From data table to Ogive
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')  # Must be called before importing pyplot


# Upper class boundaries
upper_class_boundaries = [2011, 2012, 2013, 2014, 2015, 2016]

data = [1000, 500, 1500, 2000, 2500, 1500]
cumulative_frequencies = data
print(cumulative_frequencies)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(
    upper_class_boundaries, cumulative_frequencies,
    marker='o', linestyle='-', color='b'
)

# Labels and title
plt.title("Line graph (Passengers)")
plt.xlabel("Year")
plt.ylabel("Nunber of Passengers")

# Grid
plt.grid(True)

# Show the plot
plt.savefig("line graph and ogives/output/question-2.png")
