import math

data = sorted([10, 11, 12, 18, 28, 28, 28, 32,
              36, 38, 39, 44, 44, 44, 52, 56, 60])
# print("sorted", data)

max_value = data[-1]
min_value = data[0]
data_range = max_value - min_value
# print("data_range", data_range)

class_num = 6
bin_size = data_range / class_num

bin_width = math.ceil(bin_size)
# print("bin_width", bin_width)


def generate_bin_intervals(min_value, bin_width, class_num):
    intervals = []
    # interval [10-19], [20-29], [30-39], [40-49], [50-59], [60-69]
    min_interval = min_value
    for i in range(class_num):
        upper_bound = min_interval + bin_width
        intervals.append((min_interval, upper_bound))
        min_interval = upper_bound + 1
    return intervals


intervals = generate_bin_intervals(min_value, bin_width, class_num)
# print("intervals", intervals)


def count_frequencies(data, intervals):
    frequencies = {}
    for i, (lower, upper) in enumerate(intervals):
        frequencies[f"{lower}-{upper}"] = 0

        for value in data:
            if (lower <= value <= upper):
                frequencies[f"{lower}-{upper}"] += 1
    return frequencies


frequencies = count_frequencies(data, intervals)
print("frequencies", frequencies)
