# 10.27.2024
# Selection Sort Algorithm

# method to take in the array
def selectionSort (data) :
   # loop through the entire list
   for index in range (len(data)) :
       # have a temmporary variable for the swap, as well as a variable for the index of the minimum and the minimum itself
       min = data [index]
       minIndex = index
       # nested loop to then check the rest of the list to compare
       for index2 in range (index + 1, len(data)) :
           # compare the current spot to the min and store min
           if data [index2] < min :
               min = data [index2]
               minIndex = index2
       # switch minimum to end of the sorted part after each iteration
       data [minIndex] = data [index]
       data [index] = min
   return data


data = [1, 3, 15, 4, 7, 18, 99, 98]
print(selectionSort(data))




