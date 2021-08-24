import time

def main(array):
    bubbleSort(array)
    intertionSort(array)


def bubbleSort(array):
    start = time.time()
    sorted = False
    compares = 0
    print('Bubble Sorting the an array of {} elements...'.format(len(array)))
    while sorted == False:

        prevElement = array[0]
        sorted = True

        for index in range(len(array)):
            if index == 0:
                continue

            currentElement = array[index]
            compares += 1
            if prevElement > array[index]:
                array[index] = prevElement
                array[index - 1] = currentElement
                sorted = False;

            prevElement = currentElement
    end = time.time()
    printStats(array, start, end, compares)

def intertionSort(array):
    start = time.time()
    sorted = False
    compares = 0
    print('Insertion Sorting the an array of {} elements...'.format(len(array)))
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

def printStats(array, start, end, compares):
    print('NumberOfCompares: {}'.format(str(compares)))
    print("Duration: {} seconds".format(time.time() - start))
    print(array)


if __name__ == '__main__':
    main([1,3,7,3,6,2,6])

