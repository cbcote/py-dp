from typing import List

# Define the Strategy interface
class SortingStrategy:
    def sort(self, data: List[int]) -> List[int]:
        pass

# Implement concrete strategies
class BubbleSort(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class QuickSort(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

# Context class
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort_data(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)


# Usage
data = [64, 34, 25, 12, 22, 11, 90]

# Using BubbleSort
sorter = Sorter(BubbleSort())
print('BubbleSort:', sorter.sort_data(data.copy()))

# Switching to QuickSort
sorter.set_strategy(QuickSort())
print('QuickSort:', sorter.sort_data(data.copy()))
