# 10.27.2024
# Insertion Sort Algorithm

# function to take in the array
def insertionSort (data) :
    # loop through every element except for the first
    for index in range (1, len(data)) : 
        # assign the current element to a variable, and an index for the data before
        current = data [index]
        index2 = index - 1
        # while loop to ensure the second index is in bounds, and that the previous data is greater than the element (otherwise it would move on to next element)
        while index2 > -1 and data [index2] > current :
            # swap the points, and decrement the second index so it can continue to sort itself out
            data [index2 + 1] = data [index2]
            data [index2] = current
            index2 -= 1
    return data

data = [1, 14, 3, 2, 15, 77, 0]
print(insertionSort(data))
