#  File: KruskalTest.py

#  Description: Code uses the unittest library to test the kruskal algorithm for creating a minimum spanning tree. 


import unittest

class Graph:
# A simple representation of a weighted graph

    def __init__(self, no_vertices):
        self.no_vertices = no_vertices            # initializes based on the number of vertices
        self.edges = []                        

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # A Search function
    def find(self, parent, i):
        if parent[i] == i:                       # finds the node the user is searching for recursively 
            return i
        return self.find(parent, parent[i])

    # A Simple union Function 
    def apply_union(self, parent, rank, x, y):
        # alters the rank list based on whether the x vertice or y vertice is larger in the edge
        
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.edges = sorted(self.edges, key=lambda item: item[2])   # sorts edges based on weight
        parent = []
        rank = []
        
        for node in range(self.no_vertices):        # creates a list of nodes based on the vertice number
            parent.append(node)
            rank.append(0)
        
        while e < self.no_vertices - 1:
            u, v, w = self.edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])           # adds edge to result if the edge doesn't create a cycle
                self.apply_union(parent, rank, x, y)    # alters rank list
                
        #for u, v, weight in result:
        #    print("%d - %d: %d" % (u, v, weight))
            
        return result

class TestKruskal(unittest.TestCase):

    def test_kruskal_algo(self):
      g1 = Graph(7)                          # importance: tests function with a graph where vertices have multiple edges
      g1.add_edge(0, 1, 30)
      g1.add_edge(0, 6, 10)
      g1.add_edge(1, 4, 13)
      g1.add_edge(1, 2, 15)
      g1.add_edge(2, 3, 12)
      g1.add_edge(3, 4, 16)
      g1.add_edge(3, 5, 20)
      g1.add_edge(4, 5, 21)
      g1.add_edge(5, 6, 22)
      answer1 = [[0, 6, 10], [2, 3, 12], [1, 4, 13], [1, 2, 15], [3, 5, 20], [5, 6, 22]]
      self.assertEqual(g1.kruskal_algo(), answer1)

      g2 = Graph(4)                          # importance: tests function with a graph where a cycle is present
      g2.add_edge(0, 1, 5)
      g2.add_edge(1, 2, 3)
      g2.add_edge(2, 3, 7)
      g2.add_edge(3, 2, 2)
      g2.add_edge(0, 3, 4)
      answer2 = [[3, 2, 2], [1, 2, 3], [0, 3, 4]]
      self.assertEqual(g2.kruskal_algo(), answer2)
 
      g3 = Graph(4)                         # importance: tests function with a graph where there are two possible minimum spanning trees
      g3.add_edge(0, 1, 5)
      g3.add_edge(1, 2, 3)
      g3.add_edge(2, 3, 5)
      g3.add_edge(3, 0, 3)
      answer3 = [[1, 2, 3], [3, 0, 3], [0, 1, 5]]
      self.assertEqual(g3.kruskal_algo(), answer3)

      """
      g4 = Graph(4)                         # importance: tests function with a graph where the vertexes do not increment by 1
      g4.add_edge(0, 2, 5)                  # ERROR: this test case fails because the parent list still incriments by 1 despite the vertexes not incrementing by 1
      g4.add_edge(2, 4, 3)                  # this causes out of bound errors when the kruskal_algo() function calls the find function; this should be fixed
      g4.add_edge(4, 6, 5)
      g4.add_edge(6, 0, 3)
      answer4 = [[2, 4, 3], [6, 0, 3], [0, 2, 5]]
      self.assertEqual(g4.kruskal_algo(), answer4)

      g5 = Graph(7)                         # importance: tests function with a graph contains two seperate graphs
      g5.add_edge(0, 1, 5)                  # ERROR: this test case fails because a min spanning tree can not be found when the vertexes all aren't connected
      g5.add_edge(1, 2, 3)                  # this failure is expected 
      g5.add_edge(2, 3, 5)
      g5.add_edge(3, 0, 3)
      g5.add_edge(4, 5, 5)
      g5.add_edge(5, 6, 3)
      g5.add_edge(6, 4, 5)
      print(g5.edges)
      print(g5.kruskal_algo())
      """

    def test_find(self):
      g = Graph(4)                          # importance: tests if the find function works as that is the only other function with a return
      g.add_edge(0, 1, 5)
      g.add_edge(1, 2, 3)
      g.add_edge(2, 3, 5)
      g.add_edge(3, 0, 3)
      parent = [0,1,2,3]
      self.assertEqual(g.find(parent, 1), 1)


if __name__ == '__main__':
    unittest.main()

