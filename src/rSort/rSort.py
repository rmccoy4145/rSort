import random
import time
from MergeSort import MergeSort
from QuickSort import QuickSort
from InsertionSort import InsertionSort
from BubbleSort import BubbleSort

def main():
    array = random.sample(range(1, 10000), 100)
    # array = [231,424,6345,3546,454645,56546,8456,821,9765,56546,7765]

    print("Array to sort....")
    print(array)

    algos = [
        BubbleSort(array),
        # InsertionSort(array),
        # MergeSort(array),
        # QuickSort(array)
    ]

    for algo in algos:
        start = time.time()
        print('{} is Sorting an array of {} elements...'.format(algo.getName(), len(algo.getArray())))

        result = algo.execute()

        printStats(result, start, algo.getCompares(), algo.getSwaps())


def printStats(array, start, compares, swaps):
    print('NumberOfCompares: {}'.format(str(compares)))
    print('NumberOfSwaps: {}'.format(str(swaps)))
    print("Duration: {} seconds \n".format(time.time() - start))
    print(array)


if __name__ == '__main__':
    main()

