# 10.22.2024
# Descending Merge Sort Algorithm

# method to merge two sorted arrays
def merge (left, right) :
    # instanciate a final array and a left and right counter
    leftCount = 0
    rightCount = 0
    finalArr = []

    # while both are less than their end, compare and add the the biggest ones first (how it becomes descending)
    while leftCount < len(left) and rightCount < len(right) :
        if left[leftCount] > right[rightCount] :
            finalArr.append(left[leftCount])
            # increment the count
            leftCount += 1
        else :
            finalArr.append(right[rightCount]) 
            rightCount += 1

    # check if either array still has data and then add all into the first
    while leftCount < len(left) :
        finalArr.append(left[leftCount])
        leftCount += 1
    while rightCount < len(right) :
        finalArr.append(right[rightCount])
        rightCount += 1

    return finalArr

# merge sort recursive method, takes in one array
def mergeSort (data) :
    # base case if the length is one, just return it
    if len(data) == 1 :
        return data
    # otherwise call merge sort to sort the left and right half recursively,then call merge on the two halves and return it
    left = mergeSort(data[:len(data) // 2])
    right = mergeSort(data[len(data) // 2:])
    return merge(left, right)

data = [1, 3, 77, 66, 4]
print(mergeSort(data))