# Is Unique: Implement an algorithm to determine if a string has all unique
# characters. What if you cannot use additional data structures?

# Naive
def isUnique_naive(s: str) -> bool:
    ch_dict = {}
    for char in s:
        if char in ch_dict: return False
        else:
            ch_dict[char] = 0
    return True

def isUnique_improv1(s: str) -> bool:
    # insert hash map of all letters in the alphabet
    for char in s:
        if lower(char) == -1: return False
        else:
            ch_dict[char] = -1
    return True
