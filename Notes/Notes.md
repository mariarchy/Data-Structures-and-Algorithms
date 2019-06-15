# Array Sequences
## Low level Arrays
* Memory stored in bits
* Byte: 8 bits
* Main memory performs RM
* Array designed to restore and retrieve bit in O(1) time
* Keep track of sequence of objects
* Stored in contiguous portion of computer’s memory
* Each character is 2 bytes
**Referential Arrays**
* 100 student names with ID numbers
* How to avoid having to set max number of name length?
* Use object references
* Reference each element to the object 
  * Element can reference same object 
* Copying Arrays: list(primes) => Duplicating list that references same objects – shallow copy
  * Deep copy: use deep copy method in Python library
  * i.e. `counters = [0] *8` => All reference to same “0” object!
  * `Counters[1] += 1` => links to new object
  * `primes.extend(extras)` extends `prime` array with `extras` array - causes end of array to reference objects in `extras`

## Dynamic Arrays
* In Python, don't need to specify length of array
* Python sets array size to be larger than what it needs in the list
* Underlying change in memory (in chunks) as you add
  * Hermit crab grabbing larger and larger shells
* Underlying changes when full
  * Allocate new array `B` with larger capacity
  * Set `B[i] = A[i]` for `i = 0, ..., n-1` where `n` is current number of items
  * Set `A = B`, using `B` as the array supporting the list
  * Insert new element in `A`
* Common rule: have array to be **2x** as large as original
* **Single append operation: O(n) WC**

## Amortization
* Amortization: algorithm
* Overflow at 2, 4, 8, 18, etc. 
* Amortization cost will be **1** at 0, 1, 4, 6, 7, 8, 10, etc.
  * Indices **at and at least 2 after** indices that have overflowed (0, 2, 4, 8, etc.)
  * Indices **1 after** capacity point is `n` (2, 3, 5, 9, etc.)
* Amortized cost = 
  * High cost = (1 + 1) + (2 + 1) + (4 + 1) + (8 + 1) + ...
  * Since all others are + 1, 
  * Amortized cost = [ n * 1 + (1 + 2 + 4 + 8 + ...) ] / n
  * ...
  * = (n + 2n) / n
  * = 3
  * Therefore, **O(1)**

### Libraries Used
* `ctypes`
  * `(cap * ctypes.py_object)()` Create a raw array with specified `cap`
* 
