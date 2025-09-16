from math import sqrt, erf
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
    def get_weighted_mean(data_set: list[tuple[int, int]]) -> float:
        """
        Weighted mean formula
            X̄ = Σ(w_i * x_i) / Σw_i
            x_i = value
            w_i = weight
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
