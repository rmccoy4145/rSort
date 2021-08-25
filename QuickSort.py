import random

class QuickSort:

    def __init__(self, passedArray):
        self.array = passedArray
        self.name = "QuickSort"
        self.compares = 0
        self.swaps = 0

    def getSwaps(self):
        return self.swaps

    def execute(self):
        return self.recursiveQuickSort(self.array, 0, len(self.array))

    def getCompares(self):
        return self.compares

    def getName(self):
        return self.name

    def getArray(self):
        return self.array

    def recursiveQuickSort(self, array, left, right):
        if left < right:
            pivotIndex = random.randint(left, right)
            newPivot = self.partition(array, left, right, pivotIndex)
            self.recursiveQuickSort(array, left, newPivot - 1)
            self.recursiveQuickSort(array, newPivot + 1, right)

        return array

    def partition(self, array, left, right, pivotIndex):
        value = array[pivotIndex]

        self.swap(array, pivotIndex, right)

        storeIndex = left

        i = left
        while i < right:
            if array[i] < value:
                self.swap(array, i, storeIndex)
                storeIndex += 1
                i += 1
        self.swap(array, storeIndex, right)
        return storeIndex

    def swap(self, array, left, right):
        tmpA = array[left]
        tmpB = array[right]
        array[left] = tmpB
        array[right] = tmpA