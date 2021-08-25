class InsertionSort:
    def __init__(self, passedArray):
        self.array = passedArray
        self.name = "InsertionSort"
        self.compares = 0
        self.swaps = 0

    def execute(self):
        sorted = False
        while sorted == False:
            for index in range(len(self.array)):
                self.compares += 1
                if index == 0:
                    continue
                if self.array[index - 1] > self.array[index]:
                    self.insertionShift(index, self.array)
            sorted = True

    def getSwaps(self):
        return self.swaps

    def getCompares(self):
        return self.compares

    def getName(self):
        return self.name

    def getArray(self):
        return self.array

    def insertionShift(self, indexPlaceHolder, array):
        self.swaps += 1
        index = indexPlaceHolder
        while index >= 1:
            current = array[index]
            next = array[index - 1]
            if next > current:
                array[index] = next
                array[index - 1] = current
            index -= 1