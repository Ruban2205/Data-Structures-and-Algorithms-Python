# Queue Implementation

""" Queue is an abstract data structure, somewhat similar to Stacks.
 Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue) and the other is used to remove data (dequeue).
 Queue follows First-In-First-Out methodology, i.e., the data item stored first will be accessed first. """

class Queue: 
    def __init__(self, size): 
        self.queue = list()
        self.maxsize = size
        self.queue = [None]*self.maxsize
        self.front = -1
        self.rear = -1

    def Insert(self, data): 
        if self.rear == self.maxsize - 1: 
            print("Queue is FULL!")
        else: 
            if self.front == -1: 
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = data

    def Delete(self): 
        if self.front == -1 or self.front == self.maxsize: 
            print("Queue is EMPTY!! Deletion is not Possible!")
        else: 
            print("Deleted Item is: ", self.queue[self.front])
            self.queue[self.front] = None
            self.front += 1

    def Display(self): 
        if self.rear == -1 or self.front == self.maxsize: 
            print("Queue is EMPTY!")
        else: 
            i = self.front 
            while i <= self.rear: 
                print(self.queue[i])
                i += 1

    def Peek(self): 
        if self.rear == -1 or self.front == self.maxsize: 
            print("Queue is EMPTY!")
        else: 
            print(self.queue[self.front])

queueSize = int(input("Enter the Size of Queue: "))
Obj = Queue(queueSize)

while True: 
    print("\n1. INSERT")
    print("2. DELETE")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1: 
        value = int(input("Enter the Data: "))
        Obj.Insert(value)

    elif choice == 2: 
        Obj.Delete()

    elif choice == 3: 
        Obj.Peek()

    elif choice == 4: 
        Obj.Display()

    elif choice == 5: 
        break

    else: 
        print("INVALID CHOICE")