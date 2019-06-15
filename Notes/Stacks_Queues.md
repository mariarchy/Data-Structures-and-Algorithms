# Stacks, Queues, and Deques
* Linear structures
* Difference in how they add and remove elements
## Stacks
* Ordered collection of items where
  * **Top/Head:** where objects are removed and added
  * **Base/Tail:** where least recent object lies - in stack LONGEST
* **LAST IN FIRST OUT:** latest in are first out; oldest in are last out 
* **Order of insertion is order of reversal**
* Example: stack of history + back button > stores stack of previously visited sites where top = most recently visited
### Implementation
* `Stack()` creates new stack
* `push(item)` addes new item to top
* `pop()` removes top item, returns item
* `peek()` returns top item, won't remove
* `isEmpty()`
* `size()`

```
class Stack(object)
    def __init__(self):
        self.items = []
        self.size = 0
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        self.size += 1
    
    def pop(self):
        self.size -= 1
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size():
        return self.size
```

## Queues
* Ordered collection of items where items added to one end (rear) and removed at (front)
  * Enters from rear and makes way to front
* Most recent item at end; item in collection for longest time at front
* **FIFO: FIRST IN FIRST OUT** First come, first served
  * Example: Waiting in line at grocery store, movie, etc.
### Implementation
* `Queue()` creates new empty queue
* `enqueue(item)` add `item` to `rear`
* `dequeue()` remove item at `front` - first item
* `isEmpty()`
* `size()`
* Same as queue but enqueue **adds to INDEX 0**
```
class Queue(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items = []
        
    def enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
```

## Deque
* Double-ended queue; order collection of items similar to queue
* Has **two ends**, `front` and `rear`, and items remain positioned in collection
* Unrestrictive nature of adding and removing items
  * Can be removed + added at **either end**
  * Hybrid DS of Stack + Queue

### Implementation
* `Deque()` creates empty deque
* `addFront(item)` adds item to front
* `addRear(item)` adds item to rear (like queue and stack)
* `removeFront()` removes item from front (like queue)
* `removeRear()` removes item from rear (like stack)
* `isEmpty()`
* `size()`
```
class Deque(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def addFront(self, item):
        self.items.insert(0, item)
    
    def addRear(self, item):
        self.items.append(item)
        
    def removeFront(self):
        return self.items.pop(0)
        
    def removeRear(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
```

### Algorithms
```
class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks:
        # stack e will be in LIFO - stack
        # stack d will be in FIFO - queue
        self.instack = Stack()
        self.outstack = Stack()
     
    # enqueue: addRear()
    def enqueue(self,item):
        # since enqueue for queue is same as stack, push
        self.instack.push(item)
    
    # dequeue: removeFront()
    def dequeue(self):
        if not self.outstack:
            while not self.instack:
                self.outstack.push(self.instack.pop())
        return self.outstack.pop()
    
    # outstack will always contain oldest in rear and newest in front
    # cannot append instack to outstack until outstack is empty
```