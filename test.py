import unittest
import numpy as np

from bubbleSort import BubbleSort
from insertionSort import InsertionSort

data_random = np.random.randint(1000, size=(1000))
sorted_by_python = np.sort(data_random)

class TestBubble(unittest.TestCase):
    def test_against_python_sort_method(self):
        """
        Test if using this sorting method you will get same result as if using default python sorting
        """
        BS = BubbleSort(data_random)
        BS.sort()
        self.assertTrue(np.array_equal(BS.data, sorted_by_python))

class TestInsertion(unittest.TestCase):
    def test_against_python_sort_method(self):
        """
        Test if using this sorting method you will get same result as if using default python sorting
        """
        IS = InsertionSort(data_random)
        IS.sort()
        self.assertTrue(np.array_equal(IS.data, sorted_by_python))


if __name__ == '__main__':
    unittest.main()