# Implementation of Stack Data Structure

""" A stack is an abstract data type that holds an ordered, linear sequence of items.
 In contrast to a queue, a stack is a last in, first out (LIFO) structure.
 A real-life example is a stack of plates: you can only take a plate from the top of the stack,
 and you can only add a plate to the top of the stack. """

class Stack: 
    def __init__(self): 
        self.stack = list()
        self.maxsize = 10
        self.top = -1

    def push(self, data): 
        if self.top == self.maxsize - 1: 
            print("Stack is Full")
        else: 
            self.top += 1
            self.stack.append(data)

    def pop(self):
        if self.top == -1: 
            print("Stack is EMPTY!!")
        else:
            item = self.stack.pop()
            self.top = -1
            print("Deleted item is: ", item)

    def display(self): 
        print(self.stack)

Obj = Stack()
while(True): 
    print("\n1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")

    choice = int(input("Enter your choice: "))
    if(choice == 1):
        value = int(input("Enter the data: "))
        Obj.push(value)
    
    elif choice == 2: 
        Obj.pop()

    elif choice == 3: 
        Obj.display()
    
    else: 
        break