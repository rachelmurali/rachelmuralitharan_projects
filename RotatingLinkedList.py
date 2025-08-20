#  File: Secret.py
#  Description: Rotates a linked list to the right (clockwise) rot places times number of times 

import sys
class Link (object):
    # do not change this constructor
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
class LinkedList (object):
    # create a linked list -- do not change this constructor
    def __init__(self):
        self.first = None
    # helper function to add an item at the end of a list
    # you can use this if you want, but do not delete it
    def insert_last (self, data): 
        newLink = Link(data)
        current = self.first
        if current == None:
            self.first = newLink
            return
        while current.next != None:
            current = current.next
        current.next = newLink
    # helper function to copy the contents of the current linked list
    # returns new linked list
    # you can use this if you want, but do not delete it
    def copy_list(self):
        new_list = LinkedList()
        curr = self.first
        while curr:
            new_list.insert_last(curr.data)
            curr = curr.next
        return new_list
    # helper function to count number of links
    # returns number of links
    # you can use this if you want, but do not delete it
    def num_links(self):
        curr = self.first
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res
    # string representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        curr_items = []
        curr = self.first
        res = ""
        while curr:
            curr_items.append(curr.data)
            if len(curr_items) == 10:
                res += "  ".join(map(str, curr_items)) + "\n"
                curr_items = []
            curr = curr.next
        # print the remaining items
        if len(curr_items):
            res += "  ".join(map(str, curr_items))
        return res
    
    # COMPLETE THIS FUNCTION
    # return a new linked list that results from the rotation
    # do not change this linked list
    """
    def rotate(self, rot_amt, t):
        links = self.num_links()
        n = (rot_amt * t) % links
        res = self.copy_list()
        if n == 0 or links <= 1:
            # the rotated result is the same as the current list
            return res
    
        slow = res.first
        fast = res.first
        print("slow and fast set as res.first", slow.data, fast.data)
        print(res)
        
        for i in range(n):
            fast = fast.next
        print("fast changes based on n", n, fast.data)
        print(res)
        
        while fast.next:
            print("fast", fast.data)
            slow = slow.next
            fast = fast.next
            print("in while slowdata", slow.data)
        print(res)
        # slow == n - 1
        
        slownxt = slow.next
        slow.next = None
        print("slownxt", slownxt.data)
        print(res)
        fast.next = res.first
        print("fast.next", fast.next.data)
        res.first = slownxt
        print(res)
        print("res.first", slownxt.data)
        print("returning res", res, slow)
        return res
    """
    def rotate(self, rot_amt, t):
        links = self.num_links()
        n = (rot_amt * t) % links
        res = self.copy_list()
        
        if n == 0 or links <= 1:
            # the rotated result is the same as the current list
            return res

        for i in range (n):
            print("in",n, self)
            
            current = res.first
            previous = res.first
            print("current", current.data)
            
            while(current.next != None):
                previous = current
                current = current.next
            print("finished loop, have last", current.data, previous.data)
                  
            previous.next = current.next
            print("deleted current", previous.data, current.data)
            print(self)
                
            current.next = res.first
            res.first = current
            print("self before return", res)
            print("made last first element", current.data)

        return res
                
        

data = [1,2,3,4,5]
ll = LinkedList()

# populate linked list with data
for d in data:
    ll.insert_last(d)

rotated = ll.rotate(2, 2)
# print the original list
print(ll)

# print the new list that results from calling rotate()
print(rotated)
"""
# DO NOT CHANGE MAIN
def main():
    ll = LinkedList()
    
    data = list(map(int, input().split()))
    # populate linked list with data
    for d in data:
        ll.insert_last(d)
    rot_amt, t = list(map(int, input().split()))
    rotated = ll.rotate(rot_amt, t)
    # print the original list
    print(ll)
    # print the new list that results from calling rotate()
    print(rotated)
if __name__ == "__main__":
""" 

