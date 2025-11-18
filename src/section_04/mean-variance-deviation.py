import statistics
import math

# Sample mean
sample_set = [29, 33, 35, 38, 40, 43, 46, 49, 56, 63]
sample_mean = statistics.mean(sample_set)
# print("sample_mean", sample_mean)

# Sample variance
sample_variance = statistics.variance(sample_set)
# print("sample_variance", sample_variance)

# Sample standard deviation
sample_std = statistics.stdev(sample_set)
# print("sample_std", sample_std)


def calculate_mean(data_set):
    return sum(data_set) / len(data_set)


def calculate_variance(data_set, mean, is_sample=False):
    total = 0
    for item in data_set:
        total += (item - mean) ** 2
    return total / (len(data_set) - (1 if is_sample else 0))


def calculate_std(variance):
    return math.sqrt(variance)


# QUESTION 1
q1_set = [6, 3, 3, 2, 2]
q1_mean = calculate_mean(q1_set)
q1_variance = calculate_variance(q1_set, q1_mean, is_sample=False)
q1_std = calculate_std(q1_variance)
# ANSWER = A
print("q1_mean", q1_mean, "q1_std", q1_std, "\n")

# QUESTION 2
q2_set = [2, 4, 7, 9, 10]
q2_mean = calculate_mean(q2_set)
q2_variance = calculate_variance(q2_set, q2_mean, is_sample=True)
q2_std = calculate_std(q2_variance)
# ANSWER = B
print("q2_mean", q2_mean, "q2_std", q2_std, "\n")

# QUESTION 3
q3_set = [1, 2, 1]
q3_mean = calculate_mean(q3_set)
q3_variance = calculate_variance(q3_set, q3_mean, is_sample=False)
q3_std = calculate_std(q3_variance)
print("q3_std", q3_std)

q3_mutated_set = [item + 4 for item in q3_set]
q3_mutated_mean = calculate_mean(q3_mutated_set)
q3_mutated_variance = calculate_variance(
    q3_mutated_set, q3_mutated_mean, is_sample=False
)
q3_mutated_std = calculate_std(q3_mutated_variance)
print("q3_mutated_std", q3_mutated_std)
