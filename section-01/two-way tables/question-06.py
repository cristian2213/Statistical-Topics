import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.use('Agg')  # For environments without GUI

# Data from the table
months = ["January", "February", "March",
          "April", "May", "June", "July", "August"]

data_2015 = [3.62, 2.96, 2.53, 5.56, 16.96, 3.95, 0.92, 0.46]
data_2016 = [1.04, 2.20, 2.67, 4.60, 6.25, 3.60, 3.89, 4.42]
data_2017 = [4.39, 2.33, 1.06, 3.38, 0.70, 8.44, 4.12, 4.24]

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(months, data_2015, marker='o', label="2015", color="skyblue")
plt.plot(months, data_2016, marker='o', label="2016", color="orange")
plt.plot(months, data_2017, marker='o', label="2017", color="green")

# Labels and title
plt.title("Comparison Line Graph (2015–2017)")
plt.xlabel("Month")
plt.ylabel("Value")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# save file
current_directory = os.getcwd()
plt.savefig(f"{current_directory}/output/question-6.png")
