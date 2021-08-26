import unittest
from rSort.InsertionSort import InsertionSort

class InsertionSortTest(unittest.TestCase):
    def test_Execute_UnsortedArray_SortedArray(self):
        array = [4, 54, 23, 1, 23, 0, 2523, 535, 543]
        algo = InsertionSort(array)
        result = algo.execute()
        assert result[0] == 0
        assert result[3] == 23
        assert result[6] == 535
        assert result[8] == 2523


if __name__ == '__main__':
    unittest.main()
