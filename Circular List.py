import sys

class Link(object):
  def __init__(self,data, next = None, previous = None):  # initialize next and previous as null
    self.data = data
    self.next = next
    self.previous = previous  

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    # initializing head, last, next, and previous
    self.head = Link(None)
    self.last = self.head

    # Insert an element (value) in the list
  def insert ( self, data ):

      # if list is empty
      if self.head.data == None:
        # sets self.head as new data and links self.head to itself
        self.head = Link(data)
        self.head.next = self.head
        self.head.previous = self.head
        
        # set self.last as itself (only element in list)
        self.last = self.head

      # if there are elements in list 
      else:
        newLink = Link(data, self.head, self.last)
        self.last.next = newLink
        self.head.previous = newLink
        self.last = newLink

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):

    # if no elements in list, return None
    current = self.head
    if(current == None):
      return None
    
    # search and find the position of the given data
    while(current.data != data):
      current = current.next

    return current


  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):
    deletion = self.find(data)

    # if element not found in list, return None
    if deletion == None:
      return None

    else:
      # re-link data to exclude deleted data
      deletion.previous.next = deletion.next
      deletion.next.previous = deletion.previous
      return deletion

    
  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):

    # goes to nth element after start
    for i in range(n-1):
      start = start.next

    # if the element we want to delete == self.head
    # reassign self.head to next element
    if self.head == start:
      self.head = start.next

    # re-link data to exclide deleted data
    newLink = start.next
    start.previous.next = newLink
    newLink.previous = start.previous

    return start.data, newLink

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ): 
    current = self.head
    node = []
    
    # append head node (1)
    node.append(self.head.data)

    # move around circular list and append data until
    # head node is reached
    while(current.next != self.head):
      node.append(current.next.data)
      current = current.next
      
    return str(node)


def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  
  # your code:
  # print out the order in which the soldiers get eliminated
  # print out the number of the soldier that escapes
  circle = CircularList()

  for i in range(1, num_soldiers + 1):
    circle.insert(i)

  # locate start of execution (literally)
  begin = circle.find(start_count)

  if(num_soldiers == 0):
    print([])


  else:
    # make sure one soldier survives and print his number
    while(True):
      elim, begin = circle.delete_after(begin,elim_num)
      print(elim)
      num_soldiers -= 1

      if(num_soldiers < 1):
        break

if __name__ == "__main__":
  main()
