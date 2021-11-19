# Implementation of Singly linked list

""" A singly linked list is a type of linked list that is unidirectional, that is,
 it can be traversed in only one direction from head to the last node (tail).
 Each element in a linked list is called a node.
 A single node contains data and a pointer to the next node which helps in maintaining the structure of the list."""

class Node: 
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 

class LinkedList: 
    def __init__(self): 
        self.head = None

    def insertAtBeginning(self, data): 
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data): 
        if self.head is None: 
            node = Node(data, self.head)
            self.head = node
            return 
        monkey = self.head 
        while monkey.next: 
            monkey = monkey.next
        node = Node(data, None)
        monkey.next = node 

    def getLength(self): 
        count = 0
        monkey = self.head
        while monkey: 
            count += 1
            monkey = monkey.next 
        return count 

    def insertAtMiddle(self, index, data): 
        if index < 0 or index > self.getLength(): 
            raise Exception("Invalid Index")

        if index == 0: 
            self.insertAtBeginning(data)
            return 
        count = 0
        monkey = self.head 
        while monkey: 
            if count == index - 1: 
                node = Node(data, monkey.next)
                monkey.next = node 
                break

            monkey = monkey.next 
            count += 1

    def display(self): 
        if self.head is None: 
            print("List is EMPTY!")
            return 
        monkey = self.head 
        while monkey: 
            print(monkey.data)
            monkey = monkey.next 

    def deleteMiddle(self, index): 
        if index < 0 or index > self.getLength(): 
            raise Exception("INVALID INDEX")

        if index == 0: 
            self.head = self.head.next 
            return 
        count = 0
        monkey = self.head 
        while monkey: 
            if count == index - 1: 
                temp = monkey.next 
                monkey.next = monkey.next.next 
                break

            monkey = monkey.next 
            count +=1 

MenuDriven = LinkedList()

while(1): 
  print("\n1. INSERT AT BEGINNING")
  print("2. INSERT AT END")
  print("3. INSERT AT MIDDLE")
  print("4. DELETE MIDDLE")
  print("5. DISPLAY")
  print("6. EXIT")

  userInput = int(input("Enter your Choice: "))
  if userInput == 1: 
    BeginningValue = int(input("Enter the Beginning Value: "))
    MenuDriven.insertAtBeginning(BeginningValue)

  elif userInput == 2: 
    EndValue = int(input("Enter the End Value: "))
    MenuDriven.insertAtEnd(EndValue)

  elif userInput == 3: 
    MiddleValueIndex = int(input("Enter the Index: "))
    MiddleValue = int(input("Enter the Middle Value: "))
    MenuDriven.insertAtMiddle(MiddleValueIndex, MiddleValue)

  elif userInput == 4: 
    deleteMiddle = int(input("Enter the Index value wants to be delete: "))
    MenuDriven.deleteMiddle(deleteMiddle)
    print("Successfully Deleted!!")

  elif userInput == 5: 
    MenuDriven.display()

  elif userInput == 6:
    break

  else: 
    print("Your choice ", userInput, " is NOT available in the MENU!!" )