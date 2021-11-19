# Implementation of Quick Sort and Merge Sort 

"""# QUICK SORT
# Quicksort is an in-place sorting algorithm.
# Developed by British computer scientist Tony Hoare in 1959 and published in 1961,
# it is still a commonly used algorithm for sorting. When implemented well, it can be
# somewhat faster than merge sort and about two or three times faster than heapsort. 

# Worst complexity: n^2
# Average complexity: n*log(n)
# Best complexity: n*log(n)

# MERGE SORT
# In computer science, merge sort is an efficient,
# general-purpose, and comparison-based sorting algorithm.
# Most implementations produce a stable sort, which means that the order of equal elements
# is the same in the input and output.

# Worst complexity: n*log(n)
# Average complexity: n*log(n)
# Best complexity: n*log(n)
# Space complexity: n"""

#Quick Sort Starts
def partition(array, low, high): 
    i = (low - 1)
    pivotNum = array[high]

    for j in range(low, high): 
        if array[j] <= pivotNum: 
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return(i+1)

def QuickSort(array, low, high): 
    if len(array) == 1: 
        return array
    if low < high: 
        temp = partition(array, low, high)
        QuickSort(array, low, temp-1)
        QuickSort(array, temp+1, high)

# Merge Sort Starts
def Merge(list2, low, mid, high): 
    left = list2[low:mid+1]
    right = list2[mid+1:high+1]
    i = 0
    j = 0
    k = low
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: 
            list2[k] = left[i]
            i += 1
        else: 
            list2[k] = right[j]
            j += 1
        k += 1

    while i < len(left): 
        list2[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right): 
        list2[k] = right[j]
        j += 1
        k += 1

def MergeSort(list2, low, high): 
    if low < high: 
        mid = (low + high) // 2
        MergeSort(list2, low, mid)
        MergeSort(list2, mid+1, high)
        Merge(list2, low, mid, high)

print("Output: ")

while True: 
    print("\n1. QUICK SORT")
    print("2. MERGE SORT")
    print("3. EXIT")

    choice = int(input("Enter your choice: "))
    if choice ==  1: 
        l1 = input("Enter the numbers to be sorted: ").split()
        list1 = []
        num1 = 0
        for i in l1: 
            if i.isdigit() == True: 
                list1.append(int(i))
                num1 += 1
        if num1 == 0: 
            print("There is no ELEMENT to sort!")
            continue
        QuickSort(list1, 0, len(list1)-1)
        print("\nSorted list: ", list1)

    elif choice == 2: 
        l2 = input("Enter the numbers to be sorted: ").split()
        list2 = [] 
        num2 = 0
        for i in l2: 
            if i.isdigit() == True: 
                list2.append(int(i))
                num2 += 1
        if num2 == 0: 
            print("There is no element to sort!!")
            continue
        MergeSort(list2, 0, len(list2)-1)
        print("\nSorted List: ", list2)

    elif choice == 3: 
        break

    else: 
        print("INVALID INPUT")