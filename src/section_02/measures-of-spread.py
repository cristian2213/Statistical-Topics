# range
shoes_set = [
    ("a", 10),
    ("b", 6),
    ("c", 5),
    ("d", 6),
    ("e", 9),
    ("f", 6),
    ("g", 12),
    ("h", 4),
    ("i", 8),
    ("j", 4),
    ("k", 6),
]
sorted_set = sorted(shoes_set, key=lambda x: x[1])
data_range = sorted_set[-1][1] - sorted_set[0][1]
print("data_range", data_range)

# interquartile range
q1 = sorted_set[int(len(sorted_set) * 0.25)][1]
q2 = sorted_set[int(len(sorted_set) * 0.5)][1]
q3 = sorted_set[int(len(sorted_set) * 0.75)][1]
interquartile_range = q3 - q1
print("q2", q2)
print("interquartile_range", interquartile_range)
