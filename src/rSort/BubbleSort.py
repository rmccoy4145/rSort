class BubbleSort:
    def __init__(self, passedArray):
        self.array = passedArray
        self.name = "InsertionSort"
        self.compares = 0
        self.swaps = 0

    def execute(self):
        sorted = False
        while sorted == False:

            prevElement = self.array[0]
            sorted = True

            for index in range(len(self.array)):
                self.compares += 1
                if index == 0:
                    continue

                currentElement = self.array[index]
                if prevElement > self.array[index]:
                    self.swaps += 1
                    self.bubbleSwap(index, prevElement, currentElement, self.array)
                    sorted = False;

                prevElement = self.array[index]
        return self.array

    def getCompares(self):
        return self.compares

    def getSwaps(self):
        return self.swaps

    def getName(self):
        return self.name

    def getArray(self):
        return self.array

    def bubbleSwap(self, index, prevElement, currentElement, array):
        array[index] = prevElement
        array[index - 1] = currentElement