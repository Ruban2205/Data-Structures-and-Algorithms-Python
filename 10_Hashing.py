# Implementation of hashing with collision techniques. 

"""Hashing is the process of converting an input of any length into a fixed size string or a number using an algorithm.
In hashing, the idea is to use a hash function that converts a given key to a smaller number and uses the small number
as an index in a table called a hash table."""

size = int(input("\nEnter the hash table size: "))
hashTable = [None]*size
print(hashTable)

def insert():
   key = int(input("Enter the value: "))
   hashCode = key % size
   
   if hashTable[hashCode] == None: 
     hashTable[hashCode] = key
     print(key, " is inserted at: ", hashCode)
   else: 
     tempHashCode = (hashCode + 1) % size
     while hashTable[tempHashCode] != None and tempHashCode != hashCode: 
       tempHashCode = (tempHashCode + 1) % size
     if hashTable[tempHashCode] == None: 
       hashTable[tempHashCode] = key
       print(key, " is inserted at: ", tempHashCode)
     else: 
       print("Hash Table is Full!!")

def search(): 
  key = int(input("Enter the data to be searched: "))
  hashCode = key%size

  if hashTable[hashCode] == key:
    print(key,"is found at position",hashCode)
  else:
    tempHashCode = (hashCode+1)%size
    while hashTable[tempHashCode]!=key and tempHashCode!=hashCode and hashTable[tempHashCode]!=None:
      tempHashCode = (tempHashCode+1)%size
      if hashTable[tempHashCode] == key:
        print("The element ",key,"is found at position", tempHashCode)
      else:
        print(key,"not found in the Table!!")


def delete(): 
  mark = 0
  for i in hashTable:
    if i!=None or i!="flag":
      mark = 1
  if mark == 1:
    key = int(input("Enter the data to be deleted: "))
  else:
    print("The hashtable is Empty")
    return
  hashCode = key%size
  
  if hashTable[hashCode] == key:
    print(key,"is deleted!!")
    hashTable[hashCode] = "flag"
  else:
    tempHashCode = (hashCode+1)%size
    while hashTable[tempHashCode]!=key and tempHashCode!=hashCode and hashTable[tempHashCode]!=None:
      tempHashCode = (tempHashCode+1)%size
    if hashTable[tempHashCode] == key:
      print(key,"is deleted!!")
      hashTable[tempHashCode] = "flag"
    else:
      print(key,"not found in the Table")

def display():
  for i in hashTable:
     print(i,end=' ')
  print()

while(1):
  print("\n")
  print("1. INSERT")
  print("2. SEARCH")
  print("3. DELETE")
  print("4. DISPLAY")
  print("5. EXIT")

  userChoice = int(input("Enter your choice: "))

  if userChoice == 1: 
    insert()

  elif userChoice == 2: 
    search()

  elif userChoice == 3: 
    delete() 
  
  elif userChoice == 4: 
    display()

  elif userChoice == 5: 
    print("\nThanks for using HashTable Operations!")
    break 

  else: 
    print("\nInvalid Input!!\n")