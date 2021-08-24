import random
import time

def main():
    array = random.sample(range(1, 10000), 9999)
    # array = [2,4,6,3,4,5,8]

    bubbleSort(array.copy())
    intertionSort(array.copy())
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
    arrayOfArrays = []
    for element in array:
        arrayOfArrays.append([element])

    result = recursiveArrayMerge(arrayOfArrays, 0)
    end = time.time()

    printStats(result[0], start, end, result[1])


def recursiveArrayMerge(array, compares):
    if len(array) == 1:
        finalMerge = array[0]
        for index, currentElement in enumerate(finalMerge):
            insertionShift(index, finalMerge)

        return [finalMerge, compares]

    newArray = []
    for index,currentElement in enumerate(array):
        if index % 2 != 0:
            continue
        compares += 1
        if index == len(array) - 1:
            newArray.append(array[index])
            insertionShift(len(newArray) - 1, newArray)
            return recursiveArrayMerge(newArray, compares)

        partA = currentElement
        partB = array[index + 1]
        tmpMerge = []
        if partA[0] < partB[0]:
            for element in partA:
                tmpMerge.append(element)
            for element in partB:
                tmpMerge.append(element)
        else:
            for element in partB:
                tmpMerge.append(element)
            for element in partA:
                tmpMerge.append(element)
        insertionShift(len(tmpMerge) - 1, tmpMerge)
        newArray.append(tmpMerge)

    return recursiveArrayMerge(newArray, compares)

def printStats(array, start, end, compares):
    print('NumberOfCompares: {}'.format(str(compares)))
    print("Duration: {} seconds \n".format(time.time() - start))
    # print(array)


if __name__ == '__main__':
    main()

