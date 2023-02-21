import numpy as np

class MergeSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self.data = mergeSort(self.data)

def mergeSort(data):
    if len(data) > 1:
        mid = len(data)//2

        left = data[:mid]
        right = data[mid:]

        mergeSort(left)
        mergeSort(right)

        left_index = right_index = index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                data[index] = left[left_index]
                left_index += 1
            else:
                data[index] = right[right_index]
                right_index += 1
            index +=1
        
        while left_index < len(left):
            data[index] = left[left_index]
            left_index += 1
            index += 1

        while right_index < len(right):
            data[index] = right[right_index]
            right_index += 1
            index += 1

    return data



if __name__ == "__main__":
    data_random = np.random.randint(10, size=(10)).tolist()
    MS = MergeSort(data_random)
    MS.sort()