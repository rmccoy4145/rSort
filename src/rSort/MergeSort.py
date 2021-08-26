class MergeSort:

    def __init__(self, passArray):
        self.array = passArray
        self.name = "MergeSort"
        self.compares = 0
        self.swaps = 0

    def execute(self):
        self.recursiveMergeSort(self.array)
        return self.array

    def getSwaps(self):
        return self.swaps

    def getCompares(self):
        return self.compares

    def getName(self):
        return self.name

    def getArray(self):
        return self.array

    # def recursiveMergeSort(self, array):
    #     if len(array) <= 1:
    #         return array
    #
    #     mid = len(array) // 2
    #     head = array[:mid]
    #     tail = array[mid:]
    #
    #     self.recursiveMergeSort(head)
    #     self.recursiveMergeSort(tail)
    #
    #     return self.merge(array, head, tail)
    #
    # def merge(self, array, head, tail):
    #     headIndex = 0
    #     tailIndex = 0
    #     targetIndex = 0
    #
    #     remaining = len(tail) + len(head)
    #
    #     while remaining > 0:
    #         if headIndex >= len(head):
    #             array[targetIndex] = tail[tailIndex]
    #             tailIndex += 1
    #         elif tailIndex >= len(tail):
    #             array[targetIndex] = head[headIndex]
    #             headIndex += 1
    #         elif head[headIndex] < tail[tailIndex]:
    #             array[targetIndex] = head[headIndex]
    #             headIndex += 1
    #         else:
    #             array[targetIndex] = tail[tailIndex]
    #             tailIndex += 1
    #         targetIndex += 1
    #         remaining -= 1
    #     return array

    def recursiveMergeSort(self, array):
        if len(array) > 1:
            self.compares += 1
            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]

            # recursion
            self.recursiveMergeSort(left)
            self.recursiveMergeSort(right)

            #merge
            i = 0 # left array index
            j = 0 # right array index
            k = 0 # merged array index

            # compare left/right elements, insert into merged
            while i < len(left) and j < len(right):
                self.compares += 1
                self.swaps += 1
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            # insert left over elements from left to the merged array
            while i < len(left):
                self.compares += 1
                self.swaps += 1
                array[k] = left[i]
                i += 1
                k += 1

            # insert left over elements from right to merged array
            while j < len(right):
                self.compares += 1
                self.swaps += 1
                array[k] = right[j]
                j += 1
                k += 1


