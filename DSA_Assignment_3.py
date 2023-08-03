
#Q1.Implement binary tree.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
if __name__ == '_main_':
    
  root = Node(1)
    
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)



#Q2.Find height of a given tree.

class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def maxDepth(node):
    if node is None:
        return 0
 
    else:
 
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
  
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  
 
print("Height of tree is %d" % (maxDepth(root)))


#Q3.Perform pre-order,Post-order ,in-order traversal.


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)

def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')

def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal :")
inorder(root)

print("\nPreorder traversal :")
preorder(root)

print("\nPostorder traversal :")
postorder(root)


 
#Q4.Function to print all the leaves in a given binary tree.


class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

def printLeafNodes(root: Node) -> None:
 
    if (not root):
        return
 
    if (not root.left and
        not root.right):
        print(root.data,
              end = " ")
        return
 
    if root.left:
        printLeafNodes(root.left)
 
    if root.right:
        printLeafNodes(root.right)
 
if __name__ == "_main_":
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)
    printLeafNodes(root)



#Q5.Implement BFS and DFS.

from collections import defaultdict

class Graph:
    def __init__(self):
 
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def DFSUtil(self, v, visited):

        visited[v]= True
        print (v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    def DFS(self):
        V = len(self.graph)  #total vertices
 
        visited =[False]*(V)
 
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
 
if __name__ == "_main_":
  g = Graph()
  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(1, 2)
  g.addEdge(2, 0)
  g.addEdge(2, 3)
  g.addEdge(3, 3)
 
  print ("Following is Depth First Traversal",g.DFS)
 
from collections import defaultdict
 
class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
 
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []

        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
if __name__ == '_main_':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)
 


#Q6.Find the sum of all left leaves in a given binary tree.


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
 
def leftLeavesSum(root):
 
    res = 0
    if root is not None:
       
        if isLeaf(root.left):
            res += root.left.key
        else:
            res += leftLeavesSum(root.left)

        res += leftLeavesSum(root.right)
    return res
  
root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)       
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is", leftLeavesSum(root))



#Q7.find the sum of all nodes of the given perfect binary tree.


class newNode:
 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
         
def addBT(root):
    if (root == None):
        return 0
    return (root.key + addBT(root.left) +
                       addBT(root.right))
 
# Driver Code
if __name__ == '_main_':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)
 
    sum = addBT(root)
 
    print("Sum of all the nodes is:", sum)




#Q8.Count subtress that sum up to a given value x in abinary tree.


class getNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def countSubtreesWithSumX(root, count, x):

    if (not root):
        return 0

    ls = countSubtreesWithSumX(root.left,
                               count, x)
 
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    Sum = ls + rs + root.data
 
    if (Sum == x):
        count[0] += 1
    return Sum

def countSubtreesWithSumXUtil(root, x):
    if (not root):
        return 0
    count = [0]
    ls = countSubtreesWithSumX(root.left,
                               count, x)
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    if ((ls + rs + root.data) == x):
        count[0] += 1
    return count[0]
 
 
# Driver Code
if __name__ == '_main_':
 
    root = getNode(5)
    root.left = getNode(-10)
    root.right = getNode(3)
    root.left.left = getNode(9)
    root.left.right = getNode(8)
    root.right.left = getNode(-4)
    root.right.right = getNode(7)
 
    x = 7
    print("Count =",countSubtreesWithSumXUtil(root, x))



#Q9.Find maximum level sum in binary tree.


from collections import deque

class Node:
     
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def maxLevelSum(root):
     
    if (root == None):
        return 0
 
    result = root.data
     
    q = deque()
    q.append(root)
     
    while (len(q) > 0):
        count = len(q)
        sum = 0
        while (count > 0):
            temp = q.popleft()
            sum = sum + temp.data

            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)
                 
            count -= 1   
 
        result = max(sum, result)
 
    return result
     
if __name__ == '_main_':
     
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)
   
    print("Maximum level sum is", maxLevelSum(root))
 


#Q10.Print the nodes at odd levels of a tree.


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
     
    if (root == None):
        return
    if (isOdd):
        print(root.data, end = " ")

    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)
 
# Driver code
if __name__ == '_main_':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)
