import numpy as np

class InsertionSort:
    def __init__(self, data):
        self.data = data
        print(f"Data to be sorted: {self.data}")

    def sort(self):
        for number in range(1, len(self.data)):
            index = number
            while index > 0 and self.data[index-1] > self.data[index]:
                self.data[index], self.data[index-1] = self.data[index-1], self.data[index]
                index -= 1

        print(f"Sorted data:       {self.data}")



if __name__ == "__main__":
    data_random = np.random.randint(1000, size=(1000))
    IS = InsertionSort(data_random)
    IS.sort()