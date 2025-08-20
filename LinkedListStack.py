#  File: LinkedListStack.py

#  Description: Creates a class stack by utilizing a linked list.  


import time

class Link(object):
  ''' This class represents a link between data items only'''
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data) + " --> " + str(self.next)



class LinkedList(object):
  ''' This class implements the operations of a simple linked list'''
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    '''inset data at begining of a linked list'''
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    ''' Inset the data at the end of a linked list '''
    newLink = Link(data)
    current = self.first

    if (current == None):
      self.first = newLink
      return
    # find the last and insert it there. 
    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink(self, data):
    ''' find to which data is the link of a given data inside this linked list'''
    current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if. 
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink(self, data):
    ''' Removes the data from the list if exist and fix the link problems.'''

    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
    
      current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next
    return current

  def __str__(self):
    return str(self.first)


class Stack (object):

    def __init__ (self):
        self.linkedLst = LinkedList()
        self.previous = None
        self.next = None
        self.inputs = []

    # add an item to the top of the stack
    def push (self, item):                          # single line code has a time complexity of O(1)
        if(len(self.inputs) == 0):
            self.linkedLst.insertFirst(item)
            self.inputs.append(item)
        else:
            self.linkedLst.insertLast(item)
            self.inputs.append(item)         

    # remove an item from the top of the stack
    def pop(self):                                  # single line code has a time complexity of O(1)
        self.linkedLst.deleteLink(self.inputs[len(self.inputs) - 1])   # finds the last value in list inputs and removes it from the linked list
        self.inputs.pop(len(self.inputs) - 1)                          # removes last element of inputs to set the new last element of linked list
        return self.linkedLst.first
        

    # check what item is on top of the stack without removing it
    def peek(self):                             # single line code has a time complexity of O(1)
        return self.linkedLst.findLink(self.inputs[len(self.inputs) - 1])

    # check if a stack is empty 
    def isEmpty (self):                         # single line code has a time complexity of O(1)
        return (len(self.pushQueue) == 0)

    # return the number of elements in the stack
    def size(self):                             # single line code has a time complexity of O(1)
        return (len(self.linkedLst))

    # a string representation of this stack. 
    def __str__(self):                          # single line code has a time complexity of O(1)
        return str(self.linkedLst)
        

def main():
    while(True):
        stack = Stack()
        start = time.time()
        listLen = 0
        print("\nEnter integers to push into the stack. Type 0 to stop: ")
        num = input("Enter a number to push: ")

        # Asks user to enqueue numbers into the queue. Checks if inputs are valid.
        while(num != "0"):                                     # loop happens an n number of times based on user. Best case is 1, and worst case is infinity.
            if(num.isdigit() == False):
                print("Your input is invalid.\n")
                num = input("Enter a number to push: ")
            else:
                stack.push(num)
                listLen += 1
                print("\nUpdated stack: ", stack)
                num = input("Enter a number to push: ")

        # asks user to either chose a peak or not
        while(True):                                           # loop happens an n number of times based on user. Best case is 1, and worst case is infinity.
            print("\nSelect whether to peek the list or not. 1 to peek or 0 to move on.")
            selection = input("\nEnter choice: ")
            if(selection == "0"):
                break
            elif(selection != "0" and selection != "1"):
                print("\ninvalid input")
            else:
                print(stack.peek())
                print("\nCurrent stack:", stack)
                
                
        
        print("\nThe stack will now be pop-ed.\n")
        if(listLen == 0):
            print("The stack was empty and couldn't be pop-ed")

        # Empties the stack 
        count = 0
        while(count != listLen):                 # loop happens an n number of times based on length of number of inputs entered
            print("Pop-ing element", count, ": ", stack.pop())
            count += 1

        # asks user to either continue with the program or exit
        while(True):                                           # loop happens an n number of times based on user. Best case is 1, and worst case is infinity.
            print("\nIf you want to create a new stack, select 1. If you want to exit, select 0: ")
            selection = input("Enter choice: ")
            if(selection == "1" or selection == "0"):
                break

        if(selection == "0"):
            finish = time.time()
            print("\nRunning time of program: " + str(finish - start))
            print("\nGoodbye!")
            break

main()
# Time Complexity: As this code only has single line statements and singular loops, the time complexity of the main method is O(n)

