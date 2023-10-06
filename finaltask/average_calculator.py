class AverageCalculator:
    def calculate_average(self, numbers):
        if len(numbers) == 0:
            raise ValueError("List must not be empty")
        return sum(numbers) / len(numbers)

    def compare_averages(self, list1, list2):
        avg1 = self.calculate_average(list1)
        avg2 = self.calculate_average(list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
