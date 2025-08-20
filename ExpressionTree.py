#  File: ExpressionTree.py

#  Description: Creates an expression tree and performs recursive functions on it such as evaluate, pre-order, and post-order.


import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

# takes in element that could be recurring and string it is in
# outputs index of each recurrence
    
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[ len(self.stack) - 1 ]

    def is_empty(self):
        return len(self.stack) == 0

    # CHANGES: copied str function from Github
    def __str__(self):
        return str(self.stack)

    def isIn(self, previous):
        for ch in self.stack:
            if(previous == ch):
                return True
        return False

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)


class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)


    def create_tree (self, expr):
    # creates an expression tree based on an expression string, returns self.root of the tree

        expr_list = expr.split(" ")      # splits the expression string into a list where each character is an element    
            

        stackNode = Stack()              # creates a stack to hold all the nodes that will be appended to the tree 
         
        current = Node()                 # creates the parent node

        for ch in expr_list:             # loops through the expression string

            if (ch == '('):              # creates an empty left child node and adds current into stack; sets the current to left child
                current.lChild = Node()
                stackNode.push(current)
                current = current.lChild
                
            elif (ch.isdigit() or ch.replace('.','',1).isdigit()):  # checks if is digit or is decimal
                current.data = ch                                   # assigns child of operator to the digit
                current = stackNode.pop()                           # sets current back to node which is the parent of the child just set
      
            elif(ch in operators):                             
                current.data = ch                                   # assigns child of operator to the digit 
                current.rChild = Node()                             # creates empty rChild node for later
                stackNode.push(current)
                current = current.rChild                            # sets current to the rChild
                 
            elif (ch == ')'):                                       # pops stack if it is not empty                         
                if(stackNode.is_empty() == False):
                    current = stackNode.pop()
   
            
              
        self.root = current                                        # sets self.root to current and returns self.root
        return self.root

    

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # print("\n in evaluate", self.root.data)
        if(self == None):                                # checks whether the tree is empty, if the tree is empty, there is no math to be done
            return 0
        if(aNode.lChild == None and aNode.rChild == None):  # checks whether the math for the node in questsion is finished and the opperand is returned
            return aNode.data                               # base case

        solveLeft = float(self.evaluate(aNode.lChild))    # recursively holds the digits/ mathematics that are the left child of the operand node in question
        solveRight = float(self.evaluate(aNode.rChild))   # recursively holds the digits/ mathematics that are the right child of the operand node in question

        # performs math with solveLeft and solveRight depending on which operator is in the node datapoint
        if(aNode.data == "+"):
            answer = solveLeft + solveRight
        elif(aNode.data == "-"):
            answer = solveLeft - solveRight
        elif(aNode.data == "*"):
            answer = solveLeft * solveRight
        elif(aNode.data == "/"):
            answer = solveLeft / solveRight
        elif(aNode.data == "//"):
            answer = solveLeft // solveRight
        elif(aNode.data == "**"):
            answer = solveLeft ** solveRight
        elif(aNode.data == "%"):
            answer = solveLeft % solveRight

        return answer
            
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        preStr = str(aNode.data)                           # initializes the preStr variable with the data in the root of the tree and holds string version of data to be added to preStr

        if(aNode.lChild != None):
            preStr += " " + self.pre_order(aNode.lChild)   # adds the data point of the left child to the string, keeps recurring until hits the base of left child
        if(aNode.rChild != None):
            preStr += " " + self.pre_order(aNode.rChild)   # adds the data point of the right child to the string, keeps recurring until hits the base of right child

        return preStr

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        postStr = ""                                 # initializes the preStr variable with the data in the root of the tree
        
        if(aNode.lChild != None):
            postStr += self.post_order(aNode.lChild) + " "   # adds the data point of the left child to the string, keeps recurring until hits the base of left child
        if(aNode.rChild != None):
            postStr += self.post_order(aNode.rChild) + " "   # adds the data point of the right child to the string, keeps recurring until hits the base of right child

        postStr += str(aNode.data)                   # accounts for adding the root to the end of the string and adding the string version of the node datapoints
        
        return postStr

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))
    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())
    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())
if __name__ == "__main__":
    main()



