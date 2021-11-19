# Stack and Queue Implementation using Linkedlist. 

class Node: 
  def __init__(self, data=None, next=None):
    self.data = data 
    self.next = next 

class LinkedList: 
  def __init__(self): 
    self.head = None
  
  def push(self, data): 
    node = Node(data, self.head)
    self.head = node
  
  def pop(self): 
    if self.head is None: 
      print("Stack is Empty!!")
      return 
    temp = self.head 
    self.head = self.head.next
    print("Popped item is: ", temp.data)
    temp = None 

  def peek(self):
    if self.head == None: 
      return "Stack is Empty!!"
    else: 
      print("Peek value is: ", self.head.data)

  def display(self): 
    if self.head is None: 
      print("Stack is Empty!!")
      return 
    monkey = self.head
    while monkey: 
      print(monkey.data)
      monkey = monkey.next


MenuDriven = LinkedList()
print("Stack Implementation Using LinkedList\n")

while(1): 
  print("\n1. PUSH")
  print("2. POP")
  print("3. PEEK")
  print("4. DISPLAY")
  print("5. EXIT")

  userInput = int(input("Enter your choice: "))
  if userInput == 1: 
    value = int(input("Enter the Value want to PUSH: "))
    MenuDriven.push(value)
  
  elif userInput == 2: 
    MenuDriven.pop()

  elif userInput == 3: 
    MenuDriven.peek()

  elif userInput == 4: 
    MenuDriven.display()

  elif userInput == 5: 
    break
  
  else: 
    print("INVALID INPUT!!")
    print("Your input ", userInput, " is NOT available in the MENU!!")