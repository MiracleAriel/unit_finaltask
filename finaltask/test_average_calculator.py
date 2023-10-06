import pytest
from average_calculator import AverageCalculator

class TestAverageCalculator:

    @classmethod
    def setup_class(cls):
        cls.calculator = AverageCalculator()

    def test_calculate_average_valid(self):
        numbers = [1, 2, 3, 4, 5]
        assert self.calculator.calculate_average(numbers) == 3.0

    def test_calculate_average_empty_list(self):
        with pytest.raises(ValueError):
            self.calculator.calculate_average([])

    def test_compare_averages_first_list_greater(self):
        list1 = [2, 4, 6]
        list2 = [1, 3, 5]
        result = self.calculator.compare_averages(list1, list2)
        assert result == "Первый список имеет большее среднее значение"

    def test_compare_averages_second_list_greater(self):
        list1 = [1, 3, 5]
        list2 = [2, 4, 6]
        result = self.calculator.compare_averages(list1, list2)
        assert result == "Второй список имеет большее среднее значение"

    def test_compare_averages_lists_equal(self):
        list1 = [1, 2, 3]
        list2 = [3, 2, 1]
        result = self.calculator.compare_averages(list1, list2)
        assert result == "Средние значения равны"
