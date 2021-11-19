# Postfix evaluation using Stack Data structure.

class postfix: 
    def __init__(self): 
        self.stack = list()
        self.maxsize = 20
        self.top = -1

    def push(self, data): 
        if self.top == self.maxsize - 1: 
            print("Stack is Full!!")
        else: 
            self.top += 1
            self.stack.append(data)

    def pop(self): 
        if self.top == -1: 
            print("Stack is empty!!")
        else: 
            item = self.stack.pop()
            self.top -= 1
            return item

Obj = postfix()
data = [] 
print("Output: ")

while True: 
    value = input("Enter the expression character by character: ")
    if value == '': 
        break
    else: 
        data.append(value)

for i in range(len(data)): 
    if data[i].isdigit() == True: 
        Obj.push(int(data[i]))
    
    elif data[i] == "+": 
        a = Obj.pop()
        b = Obj.pop()
        result = b + a
        Obj.push(result)

    elif data[i] == "-": 
        a = Obj.pop()
        b = Obj.pop()
        result = b - a
        Obj.push(result)

    elif data[i] == "*": 
        a = Obj.pop()
        b = Obj.pop()
        result = b * a
        Obj.push(result)

    elif data[i] == "/": 
        a = Obj.pop()
        b = Obj.pop()
        result = b / a
        Obj.push(result)

    elif data[i] == "%": 
        a = Obj.pop()
        b = Obj.pop()
        result = b % a
        Obj.push(result)

print("Result: ", Obj.stack[0])