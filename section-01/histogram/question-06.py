import math

data = sorted([4, 3, 5, 1, 0, 12, 11, 6, 4, 2, 13, 3, 7,
              12, 9, 8, 10, 22, 13, 4, 5, 20, 1, 0, 7])
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
    # interval [0-4], [4,8], [8,12], [12,16]
    min_interval = min_value
    for i in range(class_num):
        upper_bound = min_interval + bin_width
        intervals.append((min_interval, upper_bound))
        min_interval = upper_bound
    return intervals


intervals = generate_bin_intervals(min_value, bin_width, class_num)
# print("intervals", intervals)


def count_frequencies(data, intervals):
    frequencies = {}
    for i, (lower, upper) in enumerate(intervals):
        frequencies[f"{lower}-{upper}"] = 0
        is_last_interval = (i == len(intervals) - 1)
        for value in data:
            if not is_last_interval and (lower <= value < upper):
                frequencies[f"{lower}-{upper}"] += 1

            if is_last_interval and (lower <= value <= upper):
                frequencies[f"{lower}-{upper}"] += 1
    return frequencies


frequencies = count_frequencies(data, intervals)
# print("data", data)
print("frequencies", frequencies)
