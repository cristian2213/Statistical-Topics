import statistics


def calculate_median(data_set):
    # check if it's even or odd
    data_set_length = len(data_set)
    is_even = (data_set_length % 2) == 0
    sorted_data_set = sorted(data_set)

    if is_even:
        # M = X(n/2)+ X([n/2]+1)
        f_index = int(data_set_length / 2) - 1
        s_index = f_index + 1
        mean = (sorted_data_set[f_index] + sorted_data_set[s_index]) / 2
        median = mean
    else:
        # M = X(n+1/2)
        position = int((data_set_length + 1) / 2) - 1
        median = sorted_data_set[position]

    return median


# Test 1 Odd - expected = 7
odd_set = [13, 3, 7, 1, 10, 20, 30]
odd_res = calculate_median(odd_set)
print(odd_res)

# Test 2 Even - expected = 7
even_set = [15, 3, 9, 1, 12, 5, 20, 80]
even_res = calculate_median(even_set)
print(even_res)

print("odd res", statistics.median(odd_set))
print("even res", statistics.median(even_set))
print("mode", statistics.mode([1, 3, 2, 3, 4, 5]))

# question 1
buildings_set = [750, 850, 700, 650, 750, 900, 950]
print("question 1", round(sum(buildings_set) / len(buildings_set)), "mm")

# question 2
num_set = [2, 2, 2, 4, 4, 6, 6, 7, 8, 9, 10, 10, 10]
print("bi-modal", statistics.multimode(num_set))
print("is mean > median ?", statistics.mean(num_set) > statistics.median(num_set))
