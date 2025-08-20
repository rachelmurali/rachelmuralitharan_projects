class Node(object):
    '''This class represents a single Node.'''

    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)


class BST(object):
    '''This class represents a Binary Search Tree.'''

    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    # Search for a node with the key
    def search(self, key):
        current = self.root
        while ((current != None) and (current.data != key)):
            if (key < current.data):
                current = current.lChild
            else:
                current = current.rChild
            return current

    # Insert a node in the tree
    def insert(self, val):
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root

            while (current != None):
                parent = current
                if (val < current.data):
                    current = current.lChild
                else:
                    current = current.rChild

            if (val < parent.data):
                parent.lChild = newNode
            else:
                parent.rChild = newNode

    # In order traversal - left, center, right
    def inOrder(self, aNode):
        if (aNode != None):
            print(aNode.data)
            aNode.inOrder(aNode.lChild)
            aNode.inOrder(aNode.rChild)

    # Pre order traversal - center, left, right
    def preOrder(self, aNode):
        if (aNode != None):
            print(aNode.data)
            aNode.preOrder(aNode.lChild)
            aNode.preOrder(aNode.rChild)

    # Post order traversal - left, right, center
    def postOrder(self, aNode):
        if (aNode != None):
            print(aNode.data)
            aNode.postOrder(aNode.lChild)
            aNode.postOrder(aNode.rChild)

    # Find the node with the smallest value
    def minimum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.lChild
        return parent

    # Find the node with the largest value
    def maximum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.rChild
        return parent

    # Delete a node with a given key
    def delete(self, key):
        deleteNode = self.root
        parent = self.root
        isLeft = False

        # If empty tree
        if (deleteNode == None):
            return False

        # Find the delete node
        while ((deleteNode != None) and (deleteNode.data != key)):
            parent = deleteNode
            if (key < deleteNode.data):
                deleteNode = deleteNode.lChild
                isLeft = True
            else:
                deleteNode = deleteNode.rChild
                isLeft = False

        # If node not found
        if (deleteNode == None):
            return False

        # Delete node is a leaf node
        if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
            if (deleteNode == self.root):
                self.root = None
            elif (isLeft):
                parent.lChild = None
            else:
                parent.rChild = None

        # Delete node is a node with only left child
        elif (deleteNode.rChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.lChild
            elif (isLeft):
                parent.lChild = deleteNode.lChild
            else:
                parent.rChild = deleteNode.lChild

        # Delete node is a node with only right child
        elif (deleteNode.lChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.rChild
            elif (isLeft):
                parent.lChild = deleteNode.rChild
            else:
                parent.rChild = deleteNode.rChild

        # Delete node is a node with both left and right child
        else:
            # Find delete node's successor and successor's parent nodes
            successor = deleteNode.rChild
            successorParent = deleteNode

            while (successor.lChild != None):
                successorParent = successor

                successor = successor.lChild

            # Successor node right child of delete node
            if (deleteNode == self.root):
                self.root = successor
            elif (isLeft):
                parent.lChild = successor
            else:
                parent.rChild = successor

            # Connect delete node's left child to be successor's left child
            successor.lChild = deleteNode.lChild

            # Successor node left descendant of delete node
            if (successor != deleteNode.rChild):
                successorParent.lChild = successor.rChild

                successor.rChild = deleteNode.rChild

        return True

    def lca(self, val1, val2):
        p1 = self.find_path(self.root, val1)
        p2 = self.find_path(self.root, val2)

        print("printing p1")
        for node in p1:
          print(str(node.data))

        print("printing p2")
        for node in p2:
          print(str(node.data))

        p1idx = len(p1) - 1
        p2idx = len(p2) - 1
        while p1idx >= 0 and p2idx >= 0:
            if p1[p1idx] != p2[p2idx]:
                return p1[p1idx + 1].data
            p1idx -= 1
            p2idx -= 1

        if p1idx < 0 and p2idx >= 0:
            return p1[0].data
        elif p2idx < 0 and p1idx >= 0:
            return p2[0].data
        elif p1idx < 0 and p2idx < 0:
            return p1[0].data

    def find_path(self, root, val):
        if(root != None):
            print("\nroot:", root.data)
      
        if root == None:
            return None

        if root.data == val:
            return []
        else:
            print("\nleft", root.data)
            lpath = self.find_path(root.lChild, val)
            print("\nright", root.data)
            rpath = self.find_path(root.rChild, val)
                    

            correct_path = lpath if lpath is not None else rpath
            return correct_path + [root] if correct_path is not None else None

    # Returns an integer of the right sum of the BST
    def get_l_sum(self):
        queue = [self.root]
        left = 0
    
        while queue:
            bound = len(queue)

            for i in range(bound):
                # pop left node (first in first out)
                node = queue.pop(0)

                # if there's a node, set it as current, append its children to queue
                if(node != None):
                    current = node
                    queue.append(node.rChild)    # append right first so leftmost always last current
                    queue.append(node.lChild)
            if(current != None):
                print("\nadding", current.data)
                left += current.data             # add leftmost node to sum
                    

        return left

    def get_left_sum(self):
        theQueue = [[self.root, 0]]
        final_list = []

        # creates final_list which is a list of lists. Each sublist contains a node and its level in left to right order per level
        while theQueue:
            nodeStuff = theQueue.pop(0)
            if(nodeStuff[0] != None):
                final_list.append(nodeStuff)
                if nodeStuff[0].lChild:
                    theQueue.append([nodeStuff[0].lChild, nodeStuff[1]+1])
                if nodeStuff[0].rChild:
                    theQueue.append([nodeStuff[0].rChild, nodeStuff[1]+1])
                
        sum = self.root.data
        print("sum, ", sum)

        # creates leftmost sum
        prev_level = 0
        for node in final_list:
            level = node[1]
            print("\nnode : ", node[0].data, node[1])
            if(level != prev_level):
                sum += node[0].data
                prev_level = node[1]
                print("node added: ", node[0].data, node[1])
                
        return sum

    def get_balance_factor(self, root, balance = {}):
        if (root != None):
            print("\ncurrent node: ", root.data)
            rfactor = self.get_height(root.rChild)
            lfactor = self.get_height(root.lChild)
            print("    right height: ", rfactor)
            print("    left height: ", lfactor)
            
            
            balance[root.data] = lfactor - rfactor
            
            self.get_balance_factor(root.lChild, balance)
            self.get_balance_factor(root.rChild, balance)
        print(balance)
                    
    def get_height(self, root):
        if(root != None):
            print("root: ", root.data)
            if root.lChild != None and root.rChild != None:
                return 1 + max(self.get_height(root.lChild), self.get_height(root.rChild))
            elif root.lChild != None:
                return 1 + self.get_height(root.lChild)
            elif root.rChild != None:
                return 1 + self.get_height(root.rChild)
            else:
                return 1
        if(root == None):
            return 0
        
            

###############################
#                             #
#   Example run of a BST run  #
#                             #
###############################

def main():
    bst = BST()

    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(28)
    bst.insert(35)
    bst.insert(37)

    print(bst.get_balance_factor(bst.root))


if __name__ == '__main__':
    main()
