# Linked Lists
## Singly Linked Lists
* Collection of nodes that form linear sequence
    * Reference to object and next node
* Nodes linked together by pointers
* **Head and tail** pointers
* **Tail** next points to nothing
* **Inserting Node @ Head**
    * Create new node
    * Set element to new element
    * Set new node's  _next_ link to refer to current head
    * Set current _head_ to point to new node
* **Inserting Node @ Tail**
    * Create new node
    * Assign _next_ reference to _None_
    * Set current node's _next_ link to refer to new node
    * Set _tail_ to new node
* **Removing from Head**
    * Set _head_ to next node
    * Set old head node to _None_
    * Set old head _Next_ to _None_
* **Removing from Tail**
    * Cannot easily delete last node since no previous reference available to set _tail_ to once last is deleted
    * **Need a Doubly Linked List**
### Implementation
```
class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c

a.value
>>> 1
a.nextNode.value
>>> 2
```
### Analysis
**Pros**
* Constant time insertion and deletions in any position
    * Arrays always require linear time (to expand) where it always doubles size of list
* Linked lists: don't need to specify sizes ahead of time
**Cons**
* `O(k)` time to go from head to kth element
    * Arrays have constant time to access element

## Doubly Linked Lists
* a LL where node keeps reference to node **before and after** it
* Greater variety of `O(1)`time operations - **insertions and deletions**
* **Next** 
* **Prev**
* **Header** and **Trailer** nodes: "dummy" nodes known as sentinels
### Insertion
* **@ Front**
    * New Node: set prev to header && next to header.next
    * Header: set next to new node
    * OldHead: set prev to new node
### Deletion
* **@ Front**
    * NewHead: set prev to header
    * Header: set next to newHead
    * OldHead: set prev and next to None
### Implementation
```
class DLLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = self.prev = None

a = DLLNode(1)
b = DLLNode(2)
c = DLLNode(3)

# Circly LL
a.prev = c
#######
a.next = b
b.prev = a
b.next = c
c.prev = b
# Circly LL
c.next = a
######
```
### Analysis
### Algorithms 
### **Singly LL Cycle Check**
```
def cycle_check(node):
    cycle1 = cycle2 = node
    
    while cycle1 != None and cycle2.next != None:
        # if two racers run around a track, one at 2x the first's speed, the first is bound to meet the second
        if cycle1 is cycle2  # can use == too
            return True
    return False
```
**Linked List Reversal**
```
def reversal(head):

curr = head
next = None
prev = None

while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
return prev
```