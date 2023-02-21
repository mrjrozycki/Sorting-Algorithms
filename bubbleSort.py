import numpy as np

class BubbleSort:
    def __init__(self, data):
        self.data = data


    def sort(self):
        while True:
            finished = True
            for number in range(len(self.data)-1):
                if self.data[number] > self.data[number+1]:
                    self.data[number], self.data[number+1] = self.data[number+1], self.data[number]
                    finished = False
            if finished:
                break


if __name__ == "__main__":
    data_random = np.random.randint(1000, size=(1000)).tolist()
    BS = BubbleSort(data_random)
    BS.sort()