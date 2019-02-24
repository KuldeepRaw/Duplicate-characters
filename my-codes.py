# Find the number of occurrences of a character using for loop in Python

def count_repeat(s):
    '''
    (str) -> int
    return the occurence of values in the word

    >>> count_repeat('dhgssjhjj')
    >>> 2
    '''
    repeat = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeat = repeat + 1
    return repeat        
        




# Shift each item in L one position to the left and shift the first item to the last position using for loop in Python.
    
def shift_left(k):
    '''
    (list) -> Nonetype

    Shift each item in L one position to the left and shift the first item to the
    last position using for loop in Python.

    preconditions : len(k) >= 1
    >>> shift_left(['k', 'p', 'f', 'r'])
    >>> ['p', 'f', 'r', 'k']
    '''
    first_item = k[0]

    for i in range(len(k) - 1):
        k[i] = k[i + 1]

    k[-1] = first_item    
