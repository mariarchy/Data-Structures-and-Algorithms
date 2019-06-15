# Trees
* Root, branches, and leaves
* Children of one node independent of children of other node
* Each leaf is unique
    * Example: File system/folders
* **Node: ** can have name and "key"
* **Payload: ** Additional information of Node
* **Edge: ** connects two nodes to show relationship between them
* **Root: ** No incoming edges
* **Path: ** Ordered list of nodes that are connected by edges
* **Sibling: **Children of same parent
* **Level: ** number of edges to path from root to node n
      * Root = level 0
* **Height: ** maximum level of any node tree
* **Tree: ** set of edges that connect pairs of nodes
      * One node designated as root
      * Every node n, except root, is connected by an edge from exactly one other node p, where p is the parent of n
      * Unique path traverses from the root to each node
      * **Binary Tree:** If tree has max of 2 children
* **Recursive Definition: ** tree is empty or consists of root and zero or more subtrees
      * Root of subtree connected to root of parent tree by an edge
* Full binary tree with height of h has `2^h - 1` nodes

### Implementation
**List of Lists**
* Store value of root as first element of list
* Second element will be list that represent left subtree
* Third represents right subtree
_Initializing Tree_
```
def BinaryTree(r):
    # constructs root and two empty children 
    return [r, [], []]
```
_Inserting Left Child_
```
def insertLeft(root, newBranch):
    # pop out left node
    t = root.pop(1)
    # check if left contains anything, set oldLeft as left child of newBranch
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], [])
    
    return root
```
_Inserting Right Child_
```
def insertRight(root, newBranch):
    # pop out right node
    t = root.pop(2)
    # check if right contains anything, set oldRight as right child of newBranch
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], [])
    
    return root
```
_Get Root Value_
```
def getRootVal(root):
    return root[0]
```
_Set Root Value_
```
def setRootVal(root, newVal):
    root[0] = newVal
```
_Get Left Child_
```
def getLeftChild(root):
    return root[1]
```
_Get Right Child_
```
def getRightChild(root):
    return root[2 you]
```
**Method2**
```
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else: 
            # pushes down current left child under newNode
            t = BinaryTree(newNode)        
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else: 
            # pushes down current left child under newNode
            t = BinaryTree(newNode)        
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
        
    def getRootVal(self):
        return self.key    
```
**Nodes and References**
```
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        if self.leftChild == None
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def insertRight(self, newNode):
        if self.rightChild == None
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
        
    def getRootVal(self):
        return self.key  
        
    def setRootVal(self, rootVal):
        self.key = rootVal
```
**Preorder**
* Visit root, preorder left then preorder right
* Example: Book chapters and sections with left as most front and right as end
```
def preorder(root):
    if root != None:
        print(root.getRootVal())
        preorder(root.getLeftChild)
        preorder(root.getRightChild)
```
**Postorder**
* Postorder left, postorder right, visit root
```
def postorder(root):
    if root != None:
        postorder(root.getLeftChild)
        postorder(root.getRightChild)
        print(root.getRootVal())
```
**Inorder**
* Inorder left, visit root, ten inorder right
```
def inorder(root):
    if root != None:
        inorder(root.getLeftChild)
        print(root.getRootVal())
        inorder(root.getRightChild)
```
* Change order of print root

### Priority Queue
* Acts like a queue = remove it from the front
* HOWEVER logical order of items inside queue is determined by **priority**
* HIGHEST PRIORITY = FRONT
* LOWEST PRIORITY = BACK
* Enqueuing = setting high priority

### Binary Heap
* Data structure to implement PQ
* Allow to both enqueue and dequeue in `O(logn)`
* Use a tree to take advantage of `O(logn)` time
    * Therefore must be **balanced** - same # of nodes on left and right subtrees of the root
* We keep balanced by creating **complete binary tree** - tree in which each level has all of its nodes
* **Left Child** @ 2p (p = parent node index)
* **Right Child** @ 2p + 1 (p = parent node index)

**Min Heap**

```
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
```
**Inserting Node**
* Heap insert allows us to:
      * Pro: append node to end, maintaining balanced tree
      * Con: violate heap structure property
          * Avoid this by comparing to parent node
          * If newly added item < parent, swap item with parent
```
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.heapList.percUp(self.currentSize)
        
    
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
```
**Deleting Min**
* Restore root item by taking last item in list and moving to root position
* Moving last item maintains heap structure property
    * But probably destroyed heap order property of binary heap
* Restore heap order property by pushing new root node down to proper posn
    * Swap root with the smallest child less than root
    * Repeat until node less than both children
```
def percDown(self, i):
    while (i*2) < = self.currentSize:
        mc = self.minChild(i)
        if self.heapList[i] > self.heapList[mc]:
            tmp = self.heapList[i]
            self.heapList[i] = self.heapList[mc]
            self.heapList[mc] = tmp
        i = mc

def minChild(self, i):
    if i* 2 + 1 > self.currentSize:
        return i * 2
    else:
        if self.heapList[i*2] < self.heapList[i*2+1]
            return i * 2
        else: 
            return i * 2 + 1
            
def delMin(self):
    retval = self.heapList[1]
    self.heapList[1] = self.heapList[self.currentSize]
    self.currentSize = self.currentSize - 1
    self.heapList.pop()
    self.percDown(1)
    return retval
```
**Building Heaps**
* Easily build by inserting each key one by one
* List is sorted so use binary search to find right posn to insert key @ `O(logn)` operation
* Insert item in middle req `O(n)` operations to shift rest of list to make room for new key
* Therefore, total of `O(nlogn)` operations
* If start with an entire list, can build heap in `O(n)`
```
def buildHeap(self, alist):
    i = len(alist) // 2
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    while (i > 0): 
        self.percDown(i)
        i -= 1
```
### Binary Search Tree (BST)
* Keys < parent go LEFT
* Parent > keys go RIGHT
**Binary Search Tree**
```
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
        
    def __len__(self):
        return self.size
        
    def __iter__(self):
        return self.root.__iter__()
```
* Under Udemy method, duplicate keys are sent to rightChild and NEVER found
    * To handle this, replace duplicate with key instead of setting as rightChild
**Deleting Nodes**
* Find node to delete by searching
* If tree has more than one node, search using _get
    * If only one single node, still check if root == key
    * If key not found, raise error
```
def delete(self, key):
    if self.size > 1:
        nodeToRemove = self._get(key, self.root)
        if nodeToRemove: 
            self.remove(nodeToRemove)
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
    elif self.size == 1 and self.root.key == key:
        self.root = None
        self.size = self.size - 1
    else:
        raise KeyError('Error, key not in tree')
        
def __delitem__(self, key):
    self.delete(key)
```
* **Case 1: ** Node to be deleted has no children
    * Simplest
    * If current has no children (isLeaf)
        * check if current is left or right child of parent
        * Set current.parent.right/leftChild = None
* **Case 2: ** Node has one child
    * Promote child to take place of parent
        * Set the parent of left/right child to current's parent
        * Set parent's left/right child to current's left/right child
        * If current = root, replace root data with child data
* **Case 3:** Node has two children
    * Must replace deleted current node with successor `findSuccessor` and `findMin`, using `spliceOut`
```
elif currentNode.hasBothChildren():
    succ = currentNode.findSuccessor()
    succ.spliceOut()
    currentNode.key = succ.key
    currentNode.payload = succ.payload
    
def findSuccessor(self):
    succ = None
    if self.hasRightChild():
        succ = self.rightChild.findMin()
    else: 
        if self.parent:
            if self.isLeftChild():
                succ = self.parent
            else:
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                self.parent.rightChild = self
    return succ
        
def findMin(self):
    current = self
    while current.hasLeftChild():
        current = current.leftChild
    return current
```
**__iter__ method**
```
def __iter__(self):
    if self:
        if self.hasLeftChild():
            for elem in self.leftChild:
                yield elem
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem
```