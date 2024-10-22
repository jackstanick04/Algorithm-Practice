# make block object, taking in a value and weight
class block :
    # instance variables are made inside of the constructor
    def __init__ (self, value, weight) :
        self.value = value
        self.weight = weight

# main program

# merge sort but descending, takes in list for left and right, merge method
def merge (left, right) :
    counter1 = 0
    counter2 = 0    
    finalArr = []

    while counter1 < len(left) and counter2 < len(right) :
        if left[counter1] >= right[counter2] :
            finalArr.insert(0, left[counter1])
            counter1 += 1
        else :
            finalArr.insert(0, right[counter2])

    while counter1 < len(left) :
        finalArr.insert(0, left[counter1])
        counter1 += 1
    while counter2 < len(right) :
        finalArr.append(right[counter2])
        counter2 += 1

    return finalArr

# mergeSort original method, takes in one list
def mergeSort (data) :
    if len(data) == 1 :
        return data
    left = mergeSort(data[:len(data) // 2])
    right = mergeSort(data[len(data) // 2 :])
    return merge(left, right)

# # method to optimize, which takes in a list of items and a weight limit
# def program (items, limit) :
#     # call sorting method to sort the data descending

data = [10, 4, 100, 99, 8]
print(mergeSort(data))
print("hi")

