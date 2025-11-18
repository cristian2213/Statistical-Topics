import math

# QUESTION 1
data_set = [
    8,
    8,
    9,
    10,
    11,
    12,
    20,
    25,
    28,
    29,
    30,
    31,
    45,
    51,
    55,
    65,
    67,
    68,
    68,
    70,
    72,
    78,
    86,
    90,
    91,
    100,
]

sorted_set = sorted(data_set)
min_value = min(sorted_set)
max_value = max(sorted_set)

data_range = max_value - min_value
bin_size = 10
bin_width = math.ceil(data_range / bin_size)
print("bin_width", bin_width)
