class AssertSortHelper:

    def AssertSortHelper(self):
        return

    @staticmethod
    def isSorted(array):
        sorted = True
        element = array[0]
        for item in array:
            if element > item:
                sorted = False
            element = item
        return sorted