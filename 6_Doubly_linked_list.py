# Implementation of Doubly Linked List. 

"""In computer science, a doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. ...
The beginning and ending nodes' previous and next links,
respectively, point to some kind of terminator, typically a sentinel node or null, to facilitate traversal of the list"""

class Node: 
  def __init__(self, data=None, next=None, prev=None): 
    self.data = data 
    self.next = next 
    self.prev = prev

class LinkedList: 
  def __init__(self):
    self.head = None

  def insertAtBeginning(self, data): 
    if self.head is None: 
      node = Node(data, self.head, None)
      self.head = node 
      return
    else: 
      node = Node(data, self.head, None)
      self.head.prev = node 
      self.head = node

  def getLength(self):
    count=0
    monkey=self.head 
    while monkey: 
      count+=1
      monkey = monkey.next
    return count 

  def insertSpecificPosition(self, index, data) :
    if index < 0 or index > self.getLength(): 
      raise Exception("Invalid Index")

    if index == 0: 
      self.insertAtBeginning(data)
      return 
    count = 0 
    monkey = self.head

    while monkey: 
      if count == index-1: 
        node = Node(data, monkey.next, monkey)
        print("Item Inserted", data)
        monkey.next.prev = node
        monkey.next = node 
        break 
      monkey = monkey.next
      count += 1

  def deleteAtEnd(self):
    if self.head is None: 
      print("List is Empty, Deletion operation is Abandaned") 
      return None 
    if self.head.next is None: #If one node in a DLL
      print("Deleted item: ", self.head.data)
      temp = self.head 
      temp = None 
      self.head = None 
    else: 
      monkey = self.head 
      while monkey.next != None: 
        monkey = monkey.next 
      print("Deleted item: ", monkey.data)
      monkey.prev.next = None 
      monkey = None 

  def deleteData(self, value): 
    if self.head is None: 
      print("List is empty!!")
      return 
    elif self.head.data == value: 
      print("Deleted item is: ", self.head.data)
      if self.head.next is None: 
        self.head = None 
        return 
      else: 
        self.head = self.head.next
        self.head.prev = None 
        return 
    
    monkey = self.head 
    while monkey: 
      if monkey.data == value and monkey.next is None: 
        self.deleteAtEnd()
      monkey = monkey.next
    else: 
      monkey = self.head
      while monkey.next: 
        if monkey.data == value: 
          print("Deleted item is: ", monkey.data)
          monkey.prev.next = monkey.next 
          monkey.next.prev = monkey.prev
        monkey = monkey.next

  def searchElement(self, value): 
    if self.head is None: 
      print("List is Empty")
      return 
    else: 
      monkey = self.head 
      count = 0 
      while monkey: 
        if monkey.data == value: 
          print(value, " is founded at the position ", count)
          break 
        monkey = monkey.next 
        count += 1
      else: 
        print(value," is NOT in the List!!")

  def display(self):
    if self.head is None: 
      print("List is Empty")
      return 
    monkey = self.head
    while monkey: 
      print(monkey.data)
      monkey = monkey.next 

MenuDriven = LinkedList()
while(1): 
  print("\n1. INSERT AT BEGINNING")
  print("2. INSERT AT SPECIFIC POSITION")
  print("3. DELETE LAST NODE")
  print("4. DELETE A SPECIFIC DATA")
  print("5. SEARCH")
  print("6. DISPLAY")
  print("7. EXIT")

  userInput = int(input("Enter your choice: "))
  if userInput == 1: 
    BegValue = int(input("Enter the Beginning value: "))
    MenuDriven.insertAtBeginning(BegValue)

  elif userInput == 2:
    index = int(input("Enter the index: "))
    userData = int(input("Enter the value: "))
    MenuDriven.insertSpecificPosition(index, userData)

  elif userInput == 3: 
    MenuDriven.deleteAtEnd()

  elif userInput == 4: 
    delValue = int(input("Enter the value to Delete: "))
    MenuDriven.deleteData(delValue)

  elif userInput == 5: 
    searchVal = int(input("Enter the value to be Searched: "))
    MenuDriven.searchElement(searchVal)

  elif userInput == 6:  
    MenuDriven.display()

  elif userInput == 7: 
    break

  else: 
    print(userInput, " is NOT available in the MENU!!")
