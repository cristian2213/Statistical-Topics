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
    def get_range(data_set: list[int]) -> int:
        sorted_set = sorted(data_set)
        return sorted_set[-1] - sorted_set[0]

    @staticmethod
    def get_iqr(data_set: list[int]) -> float:
        """
        Interquartile range (IQR)
            IQR = Q3 - Q1
            Q1 = 1st Quartile (25th percentile)
            Q3 = 3rd Quartile (75th percentile)

        int() -> rounds down to nearest integer e.g. int(4.99) = 4, int(4.01) = 4
        """
        sorted_set = sorted(data_set)
        n = len(sorted_set)

        # Calculate Q1 (first quartile)
        q1_position = (n + 1) * 0.25
        if q1_position.is_integer():
            q1 = sorted_set[int(q1_position) - 1]
        else:
            # Interpolate between two positions
            lower_pos = int(q1_position) - 1
            upper_pos = int(q1_position)
            q1 = (sorted_set[lower_pos] + sorted_set[upper_pos]) / 2

        # Calculate Q3 (third quartile)
        q3_position = (n + 1) * 0.75
        if q3_position.is_integer():
            q3 = sorted_set[int(q3_position) - 1]
        else:
            # Interpolate between two positions
            lower_pos = int(q3_position) - 1
            upper_pos = int(q3_position)
            q3 = (sorted_set[lower_pos] + sorted_set[upper_pos]) / 2
        return q3 - q1

    @staticmethod
    def get_full_list_from_frequency(data_set: list[tuple[int, int]]) -> list[int]:
        """Get the full list of numbers from a list of tuples (value, frequency)"""
        full_list = []
        for value, frequency in data_set:
            if frequency > 0:
                full_list += [value] * frequency
        return full_list
