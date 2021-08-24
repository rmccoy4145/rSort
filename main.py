import time

def bubbleSort(array):
    start = time.time()
    sorted = False
    compares = 0
    print("Sorting the following array..." )
    print(*array)
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
    print("NumberOfCompares: " + str(compares))
    print("Duration: " + str(time.time() - start))
    return array


if __name__ == '__main__':
    print(bubbleSort([1,3,7,3,6,2,6]))

