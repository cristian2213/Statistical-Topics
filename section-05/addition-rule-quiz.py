def check_divisibility(
    combinations: list[tuple[int, int]], divisors: int | list[int]
) -> list[tuple[int, int]]:
    """Returns a list of tuples that are divisible by the given divisor after being added"""
    result = []
    is_list = isinstance(divisors, list)
    for combination in combinations:
        for val_1, val_2 in combination:
            sum = val_1 + val_2
            if is_list:
                if sum % divisors[0] == 0 and sum % divisors[1] == 0:
                    result.append((val_1, val_2))
            else:
                if sum % divisors == 0:
                    result.append((val_1, val_2))
    return result


def get_combinations(die_1: list[int], die_2: list[int]) -> list[tuple[int, int]]:
    combinations = []
    for val_1 in die_1:
        row = []
        for val_2 in die_2:
            row.append((val_1, val_2))
        combinations.append(row)
    return combinations


def get_sums(
    combinations: list[tuple[int, int]], criteria: list[int]
) -> list[tuple[int, int, int]]:
    sums = []
    for combination in combinations:
        for val_1, val_2 in combination:
            sum = val_1 + val_2
            for c in criteria:
                if sum == c:
                    sums.append((val_1, val_2))
    return sums


# QUESTION 1
die_1 = list(range(1, 7))
die_2 = list(range(1, 7))

combinations = get_combinations(die_1, die_2)
# [
#     [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],
#     [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)],
#     [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)],
#     [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)],
#     [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)],
#     [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)],
# ]

divisible_by_2 = check_divisibility(combinations, 2)
# [
#     (1, 1),
#     (1, 3),
#     (1, 5),
#     (2, 2),
#     (2, 4),
#     (2, 6),
#     (3, 1),
#     (3, 3),
#     (3, 5),
#     (4, 2),
#     (4, 4),
#     (4, 6),
#     (5, 1),
#     (5, 3),
#     (5, 5),
#     (6, 2),
#     (6, 4),
#     (6, 6),
# ]

divisible_by_5 = check_divisibility(combinations, 5)
# [(1, 4), (2, 3), (3, 2), (4, 1), (4, 6), (5, 5), (6, 4)]

divisible_by_2_and_5 = check_divisibility(combinations, [2, 5])
# [(4, 6), (5, 5), (6, 4)]

intersection = len(divisible_by_2_and_5)
divisible_by_2 = len(divisible_by_2) - intersection
divisible_by_5 = len(divisible_by_5) - intersection


# QUESTION 2
sums_8 = get_sums(combinations, [8])
sums_10 = get_sums(combinations, [10])
