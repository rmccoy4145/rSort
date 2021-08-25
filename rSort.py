import random
import time

def main():
    # array = random.sample(range(1, 10000), 9999)
    array = [2,4,6,3,4,5,8]

    # bubbleSort(array.copy())
    # intertionSort(array.copy())
    mergeSort(array.copy())


def bubbleSort(array):
    start = time.time()
    sorted = False
    compares = 0
    print('Bubble Sorting the array of {} elements...'.format(len(array)))
    while sorted == False:

        prevElement = array[0]
        sorted = True

        for index in range(len(array)):
            if index == 0:
                continue

            currentElement = array[index]
            if prevElement > array[index]:
                compares += 1
                bubbleSwap(index, prevElement, currentElement, array)
                sorted = False;

            prevElement = currentElement
    end = time.time()
    printStats(array, start, end, compares)

def bubbleSwap(index, prevElement, currentElement, array):
    array[index] = prevElement
    array[index - 1] = currentElement

def intertionSort(array):
    start = time.time()
    sorted = False
    compares = 0
    print('Insertion Sorting an array of {} elements...'.format(len(array)))
    while sorted == False:
        for index in range(len(array)):
            if index == 0:
                continue
            if array[index - 1] > array[index]:
                compares += 1
                insertionShift(index, array)
        sorted = True
        end = time.time()

    printStats(array, start, end, compares)

def insertionShift(indexPlaceHolder, array):
    index = indexPlaceHolder
    while index >= 1:
        current = array[index]
        next = array[index - 1]
        if next > current:
            array[index] = next
            array[index - 1] = current
        index -= 1

def mergeSort(array):
    start = time.time()
    print('Merge Sorting an array of {} elements...'.format(len(array)))

    result = recursiveMergeSort(array, 0)
    end = time.time()

    printStats(result[0], start, end, result[1])

def recursiveMergeSort(array, compares):
    if len(array) <= 1:
        return array
    print("splitting....")
    compares += 1
    mid = len(array)//2
    head = array[:mid]
    tail = array[mid:]

    recursiveMergeSort(head, compares)
    recursiveMergeSort(tail, compares)

    return merge(array, head, tail, compares)

def merge(array, head, tail, compares):
    print("merging...")
    headIndex = 0
    tailIndex = 0
    targetIndex = 0

    remaining = len(tail) + len(head)

    while remaining > 0:
        if headIndex >= len(head):
            array[targetIndex] = tail[tailIndex]
            tailIndex += 1
        elif tailIndex >= len(tail):
            array[targetIndex] = head[headIndex]
            headIndex += 1
        elif head[headIndex] < tail[tailIndex]:
            array[targetIndex] = head[headIndex]
            headIndex += 1
        else:
            array[targetIndex] = tail[tailIndex]
            tailIndex += 1
        targetIndex += 1
        remaining -= 1
    return [array, compares]



def printStats(array, start, end, compares):
    print('NumberOfCompares: {}'.format(str(compares)))
    print("Duration: {} seconds \n".format(time.time() - start))
    # print(array)


if __name__ == '__main__':
    main()

