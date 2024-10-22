# 10.9.2024
# Mege Sort Algorithm

# merge method, takes in two arrays and returns a final one
def merge (left, right) :
    # makes a counter for each
    counter1 = 0
    counter2 = 0
    finalArr = []

    # loop through while both of the counters are less than the length of their half
    while counter1 < len(left) and counter2 < len(right) :
        # check which is smaller, add that to the new array, and increment that counter (each side is already sorted)
        if left[counter1] <= right[counter2] :
            finalArr.append(left[counter1])
            counter1 += 1
        else :
            finalArr.append(right[counter2])
            counter2 += 1
        
    # check for each array if there are still elements to be added (still sorted)
    while counter1 < len(left) :
        finalArr.append(left[counter1])
        counter1 += 1
    while counter2 < len(right) :
        finalArr.append(right[counter2])
        counter2 += 1

    return finalArr

# mergeSort method, takes in an array and returns an array
def mergeSort (arr) :
    # base condition, if the length is one it returns inself
    if len(arr) == 1 :
        return arr
    
    # otherwise, find the left and right side of the array, and recursively sort that all the way down to 1
    left = mergeSort(arr[:len(arr) // 2])
    right = mergeSort(arr[len(arr) // 2:])
    
    # return the merge of the left and right side
    return merge(left, right)
    
nums = [1, 3, 33, 456, -4, -4, 67, 999, 1]
print(mergeSort(nums))