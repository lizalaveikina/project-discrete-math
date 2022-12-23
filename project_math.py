# Task 1
def count(start=0, step=1): 
    """    
    The function must return an infinite iterator by formula 
    (start, start+1*step, start+2*step, ...)
    count(10) --> 10 11 12 13 14 ...
    """
    while True:
        yield start
        start += step
# for i in count(10, 3):
#     print(i)
# # *********************************
# Task 2
def cycle(iterable):
    """
    Returns an infinite iterator by looping through the contents of the iterator.
    cycle('ABCD') --> A B C D A B C D A B C D...
    cycle('0123456789') --> 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9...
    """
    while True:
        for i in iterable:
            yield i
# for  i in cycle():
#     print(i)
# *********************************
# Task 3 
def repeat(value, times = None):
    """
    The function returns an infinite iterator of value if time is None
    if times is specified, returns the value times times
    repeat(5) --> 5 5 5 ...
    repeat(2, 5) --> 2 2 2 2 2
    >>> for i in repeat(2, 5): print(i)
    2
    2
    2
    2
    2
    >>> for i in repeat(1, 0): print(i)

    >>> for i in repeat(1, -2): print(i)
    
    """
    if times == None:
        while True:
            yield value
    else:
        counter = 0
        while counter < times:
            counter += 1
            yield value
# ********************************
# Task 4 
def product(*iterates):
    """
    Returns a cartesian product of list.
    product('1, 2, 4', '4, 6') --> [1, 4] [1, 6] [2, 4] [2, 6] [4, 4] [4, 6]
    >>> product('1, 2, 4', '4, 6')
    [1, 4] [1, 6] [2, 4] [2, 6] [4, 4] [4, 6]
    """
    ans = [tuple(iterate) for iterate in iterates]
    res_1 = []
    res_2 = []
    res_1.append(res_2)
    for iterate in ans:
        res_1 = [x + [y] for x in res_1 for y in iterate]
    yield res_1
# for i in product((1, 2, 4), (4, 6)):
#     print(i, end=' ')
# *********************************

