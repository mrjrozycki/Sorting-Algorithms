from time import time
import numpy as np

from bubbleSort import BubbleSort
from insertionSort import InsertionSort
from mergeSort import MergeSort

data_random = np.random.randint(50000, size=(50000))

def measure_time(algo_class, data):
    algo = algo_class(data)
    t_start = time()
    algo.sort()
    t_end = time()
    print(f"Sorting done with {algo_class.__name__} algorithm in {round(t_end - t_start,4)} seconds")


if __name__ == "__main__":
    for algo in [BubbleSort, InsertionSort, MergeSort]:
        data = data_random.copy()
        measure_time(algo, data)

