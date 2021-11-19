# Implementation of Insertion sort and selection sort

"""# INSERTION SORT
# Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
# It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

# Worst complexity: n^2
# Average complexity: n^2
# Best complexity: n
# Space complexity: 1


# SELECTION SORT
# In computer science, selection sort is an in-place comparison sorting algorithm.
# It has an O(n²) time complexity, which makes it inefficient on large lists,
# and generally performs worse than the similar insertion sort.

# Worst complexity: n^2
# Average complexity: n^2
# Best complexity: n^2
# Space complexity: 1"""

class Sort: 
    def InsertionSort(self):
      value = input('Enter the list of numbers: ').split()
      value = [int(x) for x in value]
      print("Given List: ", value)
      for i in range(1,len(value)):
          key = value[i]
          temp = i - 1
          while key < value[temp]and temp>=0:
                  value[temp+1] = value[temp]
                  temp = temp-1
          value[temp+1] = key
      print("Sorted List: ", value)

    def SelectionSort(self):
      data = input('Enter the list of numbers: ').split()
      data = [int(x) for x in data]
      print("Given List: ", data)
      for i in range(0, len(data) - 1):
          minimum = i
          for j in range(i + 1, len(data)):
              if data[j] < data[minimum]:
                  minimum = j
          data[i],data[minimum]=data[minimum],data[i]
      print('Sorted List: ', data)

MenuDriven = Sort()
while(True): 
  print("\n1. INSERTION SORT")
  print("2. SELECTION SORT")
  print("3. EXIT")

  userChoice = int(input("Enter your choice: "))

  if userChoice == 1: 
    MenuDriven.InsertionSort()

  elif userChoice == 2: 
    MenuDriven.SelectionSort() 

  elif userChoice == 3: 
    print("\nThanks for Performing Sorting Algorithms! Thank You by URK20CS2001")
    break

  else:  
    print("\nINVALID INPUT")