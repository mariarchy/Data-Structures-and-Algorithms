# Strings and Arrays
## Helpful methods
#### Strings
* `sorted(a)`: returns a sorted with char in arrays
```
>>> a = 'hello'
>>> a = sorted(a)
>>> print a
['e','h', 'l', 'l', 'o']
```
* `''.join(sorted(a))`: returns sorted string
```
>>> a = 'hello'
>>> a = ''.join(sorted(a))
>>> print a
ehllo
```
* `str.replace(old, new[, max])`: replaces first occurence of old with new, unless max is assigned, then replaces max-th occurences
  * Does not mutate
```
>>> str = "this is string example....wow!!! this is really string"
>>> str = str.replace("is", "was", 3)
>>> return str
"thwas was string example....wow!!! thwas is really string"
```
* Ask if string is an ASCII string or Unicode string (isUniqueChar question)
  * Shows an eye for detail + foundation in CS
  * **Assume for simplicity the char set is ASCII**
  * If not, need to increase storage size from 128 to 280
  * Unicode is a superset of ASCII and the numbers 0-128 have the same meaning in ASCII as they do in unicode
  ```
  >>> ord("a")
  97
  >>> chr(97)
  'a'
  ```
#### Arrays, Sets, and Hash Tables
* `arr.sort()`: sorts array lexicographically
  * mutates array, so no need to store in variable
```
>>> aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
>>> aList.sort();
[123, 'abc', 'xyz', 'xyz', 'zara']
```
* `list(setA)`: converts set to list
* `listA.insert(index, value)`: inserts value at index
  * mutates array
* `listA.remove(value)`: removes first element matching value
  * mutates array
```
>>> a = [0, 2, 3, 2]
>>> a.remove(2)
>>> a
[0, 3, 2]
```
* `del listA[index]`: removes element at index
  * mutate array
```
>>> a = [3, 2, 2, 1]
>>> del a[1]
>>> a
[3, 2, 1]
```
* `listA.pop(index)`: removes element at index and returns it; pops last element by default
```
>>> a = [4, 3, 5]
>>> a.pop(1)
3
>>> a
[4, 5]
```
* `import collections` ... ``
* `zip(listA, listB)`: creates a single list of tuples with elements from corresponding indices residing in each tuple
```
>>> zip([1, 2, 3], [4, 5, 6])
[(1, 4), (2, 5), (3, 6)]
```
* `min(arr)`: returns min element in array
* `listA.strip()`: strips leading and trailing whitespace
* `map(function_to_apply, list_of_inputs)`: applies function to items in list
    * Most of the times we want to pass all the list elements to a function one-by-one and then collect the output. For instance:
```
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```
    * Map allows us to implement this in a much simpler and nicer way. Here you go:
```
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```
* `reversed(listA)`: Reverse the sequence of a list
* `dict.items()`: returns list of dict's (key, value) tuple pairs
```
>>> dict = {'Name': 'Zara', 'Age': 7}
>>> print "Value : %s" %  dict.items()
Value : [('Age', 7), ('Name', 'Zara')]
```
* `item 1 ^= item2`: EXCLUSIVE OR; returns true if `item1` & `item2` are different
  * Good for comparing items
* `dict.values()`: returns list of values in given dictionary

## Time and Space Complexity
* **Sorting strings**: 
  * Time: `O(nlogn)`
  * Space: `O(1)` *excluding limitations of sorted(a) (O(n)) which stores string a in an array - since it makes a copy of the string*

## Algorithms
Anagrams: use a Hash Table
  * Time: `O(nlogn)` -> sorting + `O(n)` -> comparing, so `O(n)`
  * Space: `O(1)` -> dictionary + `O(n)` -> sorting (limitation of Python), so `O(1)`, but due to limitations of Python, `O(n)`
```
if same length
  count = {} # create dictionary
  for letter in str1:
      check if key exists in count (+1) and if not create key (=1)
  for letter in str2:
      (-1) if key in count
      else 
          create key in count (=1)
  for key in count:
      return false if count[key] != 0:
```

**Find the missing element** between two arrays: 
_Solution 1: Difference between sum of elements_
* **Does not work for large numbers and arrays**: numbers may become too large for program to handle - overflow
* **Does not work for floats**: lose a lot of precision with adding decimal numbers

_Solution 2: Sort then compare elements_
* Time complexity: `O(nlogn)`
```
arr1.sort()
arr2.sort()

for i in range(len(arr2)):
    if arr2[i]!= arr1[i]:
        return arr1[i]
return arr1[i+1]
```

_Solution 2.5: Create an array of tuples_
* Time complexity: `O(nlogn)`
```
arr1.sort()
arr2.sort()

for num1, num2 in zip(arr1, arr2):
  if num1 != num2:
    return num1
return arr1[-1]
```

_Solution 3: Dictionary_
* Time complexity: `O(nlogn)`
```
import collections

# allows us to avoid key errors
d = collections.defaultdict(int)

for num in arr2:
  d[num] += 1
for num in arr1:
  # if no num key exists it will be set to 0
  if d[num] == 0:
    return num
  else:
    d[num] -= 1
```

_Solution 3: Use XOR_
* Time complexity: `O(n)`
* Space complexity: 
```
result = 0
for num in arr1 + arr2:
  # XOR: finds differences
  result ^= num
return result
```

**Find the largest continuous sum** in an int array: 
_Solution 1: _
* Time complexity: `O(n)`
* Space complexity: `O(1)`
```
if len(arr) == 0 then return 0
max_sum = current_sum = first element
for num in arr[1:]:
    # if sum becomes less than current num, sum = current num
    current_sum = max(current_sum + num, num)
    # if current sum > max_sum, set it so
    max_sum = max(current_sum, max_sum)
return max_sum
```

**String Compression:**
_Solution 1:  Run compression algorithm_
* Time complexity: `O(n)`
* Space complexity: `O(1)`
```
result = ""
len = len(str)

if len == 0 then return ""
if len == 1 then return s + "1"

last = s[0]
cnt = 1
i = 1
while i < length:
    increment cnt if s[i] == s[i-1]
    else store count of prev char (s[i-1] + str(cnt)) and set cnt to 1 - preparing for cnt of next letter
    i += 1 - go to next char
    
r = r + s[i-1] + str(cnt) - store last letter values
return r
```

**Unique char in String:**
_Solution 1:  Efficient_
Since we know if `set(s) == len(s)` then all characters are unique, can just return this
```
return len(set(s)) == len(s)
```
_Solution 2:  Manual_
Using a set, we create our own look-up method
```
create set

for char in s:
    if char in set:
      return False
    else:
      set.add(char)
return True
```
```
// cannot form a string of 280 unique characters out of a 128-char alphabet
check if str length is > 128 (ASCII) or 256 (Unicode)

Create an array of boolean values where the flag at index i indicates whether char i in the alphabet is contained in the string.

Use ord(char) to cast to int code and store boolean value at this index

The next time you see this character, you can immediately return false
```
_Solution 2: No additional data structures_
If we cannot use any additional data structures
* Modify the input string by sorting the string in `O(nlogn)` time then linearly check the string for neighboring characters that are identical
