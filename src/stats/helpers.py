from math import sqrt, erf, exp, factorial
from typing import List, Tuple, Dict, Union, Callable


class Statistics:
    def __init__(self, data_set: list[int]):
        self.data_set = data_set

    @staticmethod
    def get_mode(data_set: list[int]) -> int:
        frequency_dict = {}
        for num in data_set:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        return int(max(frequency_dict, key=frequency_dict.get))

    @staticmethod
    def get_median(data_set: list[int]) -> float:
        sorted_data_set = sorted(data_set)
        data_set_length = len(sorted_data_set)
        is_even = (data_set_length % 2) == 0
        if is_even:
            f_index = int(data_set_length / 2) - 1
            s_index = f_index + 1
            return (sorted_data_set[f_index] + sorted_data_set[s_index]) / 2
        else:
            position = int((data_set_length + 1) / 2) - 1
            return sorted_data_set[position]

    @staticmethod
    def get_range(data_set: list[int] | tuple[int, int]) -> int | float:
        if isinstance(data_set, tuple):
            return data_set[1] - data_set[0]

        sorted_set = sorted(data_set)
        return sorted_set[-1] - sorted_set[0]

    @staticmethod
    def get_iqr(data_set: Union[List[int], Tuple[float, float]]) -> Dict[str, float]:
        """
        Interquartile range (IQR) using the median of halves method.
        IQR = Q3 - Q1
        Q1 = 1st Quartile (median of lower half)
        Q3 = 3rd Quartile (median of upper half)

        If data_set is a tuple, it assumes (Q1, Q3) and returns IQR directly.
        """
        if isinstance(data_set, tuple):
            return {
                "q1": data_set[0],
                "q3": data_set[1],
                "iqr": data_set[1] - data_set[0],
            }

        sorted_set = sorted(data_set)
        n = len(sorted_set)

        # def median(data: List[int]) -> float:
        #     n_med = len(data)
        #     if n_med % 2 == 1:
        #         return data[n_med // 2]
        #     else:
        #         return (data[n_med // 2 - 1] + data[n_med // 2]) / 2.0

        # Split data into lower and upper halves
        mid = n // 2
        if n % 2 == 0:
            lower_half = sorted_set[:mid]
            upper_half = sorted_set[mid:]
        else:
            lower_half = sorted_set[:mid]
            upper_half = sorted_set[mid + 1 :]

        q1 = Statistics.get_median(lower_half)
        q3 = Statistics.get_median(upper_half)
        iqr = q3 - q1

        return {"q1": q1, "q3": q3, "iqr": iqr}

    @staticmethod
    def get_full_list_from_frequency(data_set: list[tuple[int, int]]) -> list[int]:
        """Get the full list of numbers from a list of tuples (value, frequency)"""
        full_list = []
        for value, frequency in data_set:
            if frequency > 0:
                full_list += [value] * frequency
        return full_list

    @staticmethod
    def get_mean(data_set: list[int]) -> float:
        return sum(data_set) / len(data_set)

    @staticmethod
    def get_extremes(data_set: list[int]) -> dict[str, int]:
        """
        Get the minimum and maximum values from a list
        """
        return {
            "min": min(data_set),
            "max": max(data_set),
        }

    @staticmethod
    def get_weighted_mean(data_set: list[tuple[int | float, int]]) -> float:
        """
        Weighted mean formula
            X̄ = Σ(w_i * x_i) / Σw_i
            x_i = value
            w_i = weight

        tuple format: (value, weight)
        """
        return sum([w_i * x_i for x_i, w_i in data_set]) / sum(
            [w_i for _, w_i in data_set]
        )

    @staticmethod
    def get_list_from_steam_and_leaf(
        data_set: dict[int, list[int | float]],
    ) -> list[int | float]:
        full_list = []
        for steam, leaves in data_set.items():
            for leaf in leaves:
                full_list.append(
                    float(f"{steam}{leaf}")
                    if isinstance(leaf, float)
                    else int(f"{steam}{leaf}")
                )
        return full_list

    @staticmethod
    def get_variance(
        data_set: list[int],
        population: bool = False,
        mean_cb: Callable[[], float] | None = None,
    ) -> float:
        """
        Population variance formula:
            σ^2 = Σ(x_i - μ)^2 / N
        Sample variance formula:
            s^2 = Σ(x_i - x̄)^2 / (n - 1)
        """
        mean = mean_cb() if mean_cb is not None else Statistics.get_mean(data_set)
        divisor = len(data_set) if population else len(data_set) - 1
        return sum((x - mean) ** 2 for x in data_set) / divisor

    @staticmethod
    def get_standard_deviation(
        data_set: list[int],
        population: bool = False,
        mean_cb: Callable[[list[int]], float] | None = None,
    ) -> float:
        """
        Population standard deviation formula:
            σ = √(Σ(x_i - μ)^2 / N)
        Sample standard deviation formula:
            s = √(Σ(x_i - x̄)^2 / (n - 1))
        """
        return sqrt(Statistics.get_variance(data_set, population, mean_cb))

    @staticmethod
    def generate_bin_intervals(min_value: int, bin_width: int, class_num: int):
        """
        Generate bin intervals for a data set.
        Interval format: [(min_value, max_value), ...]
        """
        intervals = []
        min_interval = min_value
        for i in range(class_num):
            upper_bound = min_interval + bin_width
            intervals.append((min_interval, upper_bound))
            min_interval = upper_bound + 1
        return intervals

    @staticmethod
    def get_interval_frequencies(
        data_set: list[int], intervals: list[tuple[int, int]]
    ) -> dict[str, tuple[int, float]]:
        """
        Get the frequency of each interval in the data set.

        Returns a dictionary with the interval as key and a tuple of (frequency, relative frequency) as value.
        """
        frequencies = {}
        total = len(data_set)

        for interval in intervals:
            first = interval[0]
            second = interval[1]
            current_interval_index = intervals.index(interval)
            next_interval = (
                intervals[current_interval_index + 1]
                if current_interval_index + 1 < len(intervals)
                else None
            )
            next_first = next_interval[0] if next_interval is not None else None
            if second == next_first:
                amount = len([value for value in data_set if first <= value < second])
            else:
                amount = len([value for value in data_set if first <= value <= second])
            frequencies[f"{first}-{second}"] = (amount, amount / total)
        return frequencies

    @staticmethod
    def get_outliers(data_set: list[int]) -> dict[str, list[int]]:
        iqr = Statistics.get_iqr(data_set)
        lower_bound = iqr["q1"] - (1.5 * iqr["iqr"])
        upper_bound = iqr["q3"] + (1.5 * iqr["iqr"])
        outliers = [
            value for value in data_set if value < lower_bound or value > upper_bound
        ]
        return {
            "outliers": outliers,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
        }

    @staticmethod
    def get_k_deviations(value: float, mean: float, std: float) -> dict[str, list[int]]:
        """
        Get the k deviations of a data set.
        """
        k = (value - mean) / std
        return k

    @staticmethod
    def get_positive_k(k1: float, k2: float) -> float:
        """
        Get the positive k value from two k values.
        """
        return k1 if k1 > 0 else k2

    @staticmethod
    def get_chebyshev_theorem(k: float) -> float:
        """
        Get the chebyshev theorem value from a k value.
        """
        decimal_percentage = 1 - (1 / k**2)
        return decimal_percentage

    @staticmethod
    def get_k_inverse(chebyshev_percentage: float) -> float:
        """
        Get the k value from a chebyshev percentage.
        Formula:
            C = 1 - (1 / k^2) => k = sqrt(1 / (1 - C))
        Where:
            C = Chebyshev percentage
            k = K value
        """
        return sqrt(1 / (1 - chebyshev_percentage))

    @staticmethod
    def get_ranges_by_k(mean: float, k: float, std: float) -> tuple[float, float]:
        """
        Get the ranges by k value.
        Formula:
            lower = mean - (k * std)
            upper = mean + (k * std)
        """
        lower = mean - (k * std)
        upper = mean + (k * std)
        return (lower, upper)

    @staticmethod
    def get_percentage_of(total_amount: int, percentage: int) -> float:
        """
        Get the percentage of a total amount.
        """
        decimal_percentage = percentage / 100
        return round(total_amount * decimal_percentage)

    @staticmethod
    def get_z_score(data_set: list[int], value: int) -> float:
        """
        Get the z score of a data set.
        """
        mean = Statistics.get_mean(data_set)
        std = Statistics.get_standard_deviation(data_set)
        return (value - mean) / std

    @staticmethod
    def z_to_probability(z: float) -> float:
        """
        Calculate cumulative probability for a z-score using error function
        """
        return 0.5 * (1 + erf(z / sqrt(2)))

    @staticmethod
    def get_covariance(
        variable_x: list[int], variable_y: list[int], population: bool = False
    ) -> float:
        """
        Get the covariance of a data set.

        Population covariance formula:
            cov(x, y) = Σ[(x_i - μ_x)(y_i - μ_y)] / N
        Sample covariance formula:
            cov(x, y) = Σ[(x_i - x̄)(y_i - ȳ)] / (n - 1)
        """
        assert len(variable_x) == len(variable_y)

        n = len(variable_x)
        mean_x = Statistics.get_mean(variable_x)
        mean_y = Statistics.get_mean(variable_y)

        if population:
            return (
                sum((x - mean_x) * (y - mean_y) for x, y in zip(variable_x, variable_y))
                / n
            )
        else:
            return sum(
                (x - mean_x) * (y - mean_y) for x, y in zip(variable_x, variable_y)
            ) / (n - 1)

    @staticmethod
    def get_correlation_coefficient(
        variable_x: list[int], variable_y: list[int], population: bool = False
    ) -> float:
        """
        Get the correlation coefficient of a data set.

        Population correlation coefficient formula:
            r_xy = (Σ[(x_i - μ_x)(y_i - μ_y)] / N) / (σ_x * σ_y)
        Sample correlation coefficient formula:
            r_xy = (Σ[(x_i - x̄)(y_i - ȳ)] / (n - 1)) / (s_x * s_y)
        """
        assert len(variable_x) == len(variable_y)

        covariance = Statistics.get_covariance(variable_x, variable_y, population)
        std_x = Statistics.get_standard_deviation(variable_x, population)
        std_y = Statistics.get_standard_deviation(variable_y, population)
        return covariance / (std_x * std_y)

    @staticmethod
    def get_grouped_data_variance(
        data_set: dict[str, tuple[int, float]], population: bool = False
    ) -> dict[str, float]:
        """
        Get the grouped data variance.
        Formula for population:
            σ^2 = Σ[(f_i * (m_i - μ)^2) / Σf_i]
        Formula for sample:
            s^2 = Σ[(f_i * (m_i - x̄)^2) / (Σf_i) - 1]
        """
        data_set = [
            ((int(value.split("-")[0]) + int(value.split("-")[1])) / 2, weight[0])
            for value, weight in data_set.items()
        ]
        mean = Statistics.get_weighted_mean(data_set)
        numerator = sum((m_i - mean) ** 2 * f_i for m_i, f_i in data_set)
        denominator = sum(f_i for _, f_i in data_set)
        if population:
            return {"mean": mean, "variance": numerator / denominator}
        return {"mean": mean, "variance": numerator / (denominator - 1)}

    @staticmethod
    def get_discrete_mean(scores: list[tuple[int, float]]) -> float:
        """
        Calculate the expected value (mean) of a discrete distribution.
        Formula: E(X) = Σ(X_i * P(X_i))

        Input format: [(value, probability), ...]
        Returns the mean (expected value) of the discrete distribution
        """
        return sum(map(lambda x: x[0] * x[1], scores))

    @staticmethod
    def get_discrete_variance(scores: list[tuple[int, float]]) -> tuple[float, float]:
        """
        Input format: [(score, probability)]
        Returns the variance of a discrete distribution
        returns tuple(variance, mean)
        """
        mean = sum(map(lambda x: x[0] * x[1], scores))
        variance = sum(map(lambda x: (x[0] - mean) ** 2 * x[1], scores))
        return (variance, mean)

    @staticmethod
    def get_discrete_std(variance: float | int) -> float | int:
        """
        Return the standard deviation of a discrete distribution
        """
        return sqrt(variance)

    @staticmethod
    def get_poisson_probability(x: int, mean: float):
        """
        Calculate the probability of x occurrences using the Poisson distribution.
        Formula: P(X=x) = (e^-mean * mean^x) / x!

        Args:
        x: number of occurrences
        mean: average number of occurrences (lambda)

        Returns:
        Probability of exactly x occurrences
        """
        if x < 0:
            return 0

        e_to_negative_mean = exp(-mean)
        mean_to_power_x = mean**x
        factorial_x = factorial(x)

        probability = (e_to_negative_mean * mean_to_power_x) / factorial_x
        return probability

    @staticmethod
    def get_binomial_probability(n: int, k: int, p: float) -> float:
        """
        Calculate the probability of exactly k successes in n trials using the Binomial distribution.
        Formula: P(X=k) = C(n,k) * p^k * (1-p)^(n-k)
        Where C(n,k) = n! / (k! * (n-k)!)

        Args:
            n: number of trials
            k: number of successes
            p: probability of success in each trial

        Returns:
            Probability of exactly k successes in n trials
        """
        if k < 0 or k > n or p < 0 or p > 1:
            return 0

        # Calculate binomial coefficient C(n, k)
        binomial_coefficient = factorial(n) / (factorial(k) * factorial(n - k))

        # Calculate probability
        probability = binomial_coefficient * (p**k) * ((1 - p) ** (n - k))
        return probability


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Convert celsius to fahrenheit.
        """
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """
        Convert fahrenheit to celsius.
        """
        return (fahrenheit - 32) * 5 / 9


class Normalizer:
    @staticmethod
    def thousands_separator(num: int) -> str:
        """
        Add thousands separator to a number.
        """
        return f"{num:,}"


class Dice:
    """
    Helper functions for dice rolling
    """

    @staticmethod
    def check_divisibility(
        combinations: list[tuple[int, int]], divisors: int | list[int]
    ) -> list[tuple[int, int]]:
        """
        Returns a list of tuples that are divisible by the given divisor after being added
        """
        result = []
        is_list = isinstance(divisors, list)
        for combination in combinations:
            for val_1, val_2 in combination:
                sum = val_1 + val_2
                if is_list:
                    # FIXME - THIS IS A LIST, SO IT MUST BE ITERATED
                    if sum % divisors[0] == 0 and sum % divisors[1] == 0:
                        result.append((val_1, val_2))
                else:
                    if sum % divisors == 0:
                        result.append((val_1, val_2))
        return result

    @staticmethod
    def get_combinations(die_1: list[int], die_2: list[int]) -> list[tuple[int, int]]:
        """
        Returns a list of tuples
        """
        combinations = []
        for val_1 in die_1:
            row = []
            for val_2 in die_2:
                row.append((val_1, val_2))
            combinations.append(row)
        return combinations

    @staticmethod
    def get_sums(
        combinations: list[tuple[int, int]], criteria: list[int]
    ) -> list[tuple[int, int, int]]:
        """
        Returns a list of tuples that have a sum equal to the given criteria
        """
        sums = []
        for combination in combinations:
            for val_1, val_2 in combination:
                sum = val_1 + val_2
                for c in criteria:
                    if sum == c:
                        sums.append((val_1, val_2))
        return sums

    @staticmethod
    def get_even_or_odd_sums(
        combinations: list[tuple[int, int]], is_odd: bool = False
    ) -> list[tuple[int, int, int]]:
        """
        Returns a list of tuples that have an even or odd sum
        """
        sums = []
        for combination in combinations:
            for val_1, val_2 in combination:
                sum = val_1 + val_2
                if is_odd:
                    if sum % 2 == 1:
                        sums.append((val_1, val_2))
                else:
                    if sum % 2 == 0:
                        sums.append((val_1, val_2))
        return sums

    @staticmethod
    def get_dice_sums(combinations: list[tuple[int, int]]) -> dict[int, int]:
        """
        Returns a dictionary of tuples that have a sum equal to the given criteria
        """
        sums = {
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
        }

        for combination in combinations:
            for val_1, val_2 in combination:
                amount = val_1 + val_2
                sums[amount] += 1

        return sums
