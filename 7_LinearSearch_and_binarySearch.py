# Implementation of Linear search and Binary Search. 

"""# Linear Search 
# In computer science, a linear search or sequential search is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched.[1]
# A linear search runs in at worst linear time and makes at most n comparisons, where n is the length of the list.
# If each element is equally likely to be searched, then linear search has an average case of 
# n+1 / 2 comparisons, but the average case can be affected if the search probabilities for each element vary.
# Linear search is rarely practical because other search algorithms and schemes, such as the binary search algorithm and hash tables,
# allow significantly faster searching for all but short lists.[2]

# Worst complexity: O(n)
# Average complexity: O(n)
# Space complexity: O(1)
# Average performance: O(n/2)


# Binary Search 
# In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop,
# is a search algorithm that finds the position of a target value within a sorted array. Binary search compares
# the target value to the middle element of the array

# Worst complexity: O(log n)
# Average complexity: O(log n)
# Best complexity: O(1)
# Space complexity: O(1)"""


class Search:
    def linearSearch(self, size, list1, key):
        found = 0
        for index in range(size):
            if list1[index] == key:
                print("Number ",list1[index]," is found at index ",index)
                found = 1
                return 
        if found == 0: 
          print("Entered number is NOT in the LIST!!")
              

    def binarySearch(self, numbers, key):
      print("\nGiven ist: ", numbers)
      numbers.sort()
      print("Sorted list: ", numbers, "\n")
      first = 0 
      last = len(numbers)-1
      while first <= last:
        middle = (first + last)//2;
        if numbers[middle] < key: 
          first = middle + 1
        elif numbers[middle] > key: 
          last = middle - 1
        else: 
          return middle
      else: 
        return -1

MenuDriven = Search()
while(True): 
  print("\n1. LINEAR SEARCH")
  print("2. BINARY SEARCH")
  print("3. EXIT")

  userInput = int(input("Enter your choice: "))

  if userInput == 1:
    list1 = []
    size = int(input("\nEnter the size of the list: "))
    for i in range(size):
      num = int(input("Enter a number: "))
      list1.append(num)
    key = int(input("Enter the number to be searched: "))
    MenuDriven.linearSearch(size, list1, key) 

  elif userInput == 2: 
    list1 = []
    size = int(input("\nEnter the size of the list: "))
    for i in range(size):
      num = int(input("Enter a number: "))
      list1.append(num)
    key = int(input("Enter the number to be searched: "))
    index = MenuDriven.binarySearch(list1, key)
    if index == -1: 
      print("Number", key, " is NOT in the list!")
    else: 
      print("Number", list1[index], " is found at index ", index)

  elif userInput == 3: 
    break

  else: 
    print("Choice ", userInput, " is NOT in the MENU!!!")