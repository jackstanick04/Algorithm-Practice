# 10.9.2024
# Exponential Search Algorithm

# data needs to be sorted before this algorithm works

# takes in a list and a target value
def expSearch (data, value) :
    # while loop until an exponential index's value is greater than the target
    index = 1
    while data [index] < value :
        index *= 2
    # perform a binary search with index and previous check (index /= 2)
    return binarySearch(index // 2, index, data, value)

# recursive method, takes in a low, high, target, and arr
def binarySearch (low, high, arr, target) :
    # make mid variable
    mid = low + ((high - low) // 2)
    # check if the data is not found
    if low > high :
        return -1
    # base case if the midpoint is the target
    if arr [mid] == target :
        return mid
    # search either half depending if mid is bigger or smaller
    elif arr [mid] > target :
        return binarySearch(low, mid - 1, arr, target)
    else :
        return binarySearch(mid + 1, high, arr, target)

data = [2, 3, 5, 9, 78]
print(expSearch(data, 5))