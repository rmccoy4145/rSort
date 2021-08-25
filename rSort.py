import random
import time
from MergeSort import MergeSort
from QuickSort import QuickSort
from InsertionSort import InsertionSort
from BubbleSort import BubbleSort

def main():
    # array = random.sample(range(1, 10000), 9999)
    array = [2,4,6,3,4,5,8]

    algos = [BubbleSort(array), InsertionSort(array), MergeSort(array), QuickSort(array)]

    for algo in algos:
        start = time.time()
        print('{} is Sorting an array of {} elements...'.format(algo.getName(), len(algo.getArray())))

        result = algo.execute()

        printStats(result, start, algo.getCompares())


def printStats(array, start, compares):
    print('NumberOfCompares: {}'.format(str(compares)))
    print("Duration: {} seconds \n".format(time.time() - start))
    # print(array)


if __name__ == '__main__':
    main()

