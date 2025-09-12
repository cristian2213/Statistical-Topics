from typing import List, Tuple, Dict, Union


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


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9


class Normalizer:
    @staticmethod
    def thousands_separator(num: int) -> str:
        return f"{num:,}"
