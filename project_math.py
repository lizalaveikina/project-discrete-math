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
# Task 5
def gen_perm(iterable,lenn=0):
    if lenn==0 or lenn>len(iterable): lenn=len(iterable)
    if lenn == 1:
        for i in iterable:
            yield i
    else:
        perms = gen_perm(iterable,lenn-1)
        for i in perms:
            yield i
            if len(i) == lenn-1:
                for j in iterable:
                    if i!=j:
                        yield i+j
poem = []
for i in gen_perm("ABCD",2):
    poem.append(i)
for k in poem:
    if len(k) == 1:
        poem.remove(k)
print(poem)
# *********************************
# Task 6
def combinations(iterable, r):
    """
    (str, int) -> Iterator[Tuple[int]]
    Get combinations of iterable
    >>> list(combinations('ABCD', 0))
    [()]
    >>> list(combinations('ABCD', 1))
    [('A',), ('B',), ('C',), ('D',)]
    >>> list(combinations('ABCD', 2))
    [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    >>> list(combinations('ABCD', 3))
    [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
    >>> list(combinations('ABCD', 4))
    [('A', 'B', 'C', 'D')]
    """
    s = tuple(iterable)
    n = len(iterable)
    if r > n:
        return
    elif len(iterable) == r:
        lst = range(r)
        yield tuple(s[i] for i in lst)
    elif r == 0:
        yield ()
    else:
        yield tuple(iterable[i] for i in range(r))
        lst = list(range(1, r+1))
        while lst[0] != n - r + 1:
            i = r
            while lst[i - 1] == n - r + i:
                i -= 1
            lst[i - 1:] = list(range(lst[i - 1] + 1, lst[i - 1] + r - i + 2))
            yield tuple(iterable[i - 1] for i in lst)


# *********************************
# Task 7
def combinations_with_replacement(iterable, r):
    """
    Get combinations of iterable, with replacements
    >>> list(combinations_with_replacement('', 5))
    []
    >>> list(combinations_with_replacement('ABCD', 0))
    [()]
    >>> list(combinations_with_replacement('ABCD', 1))
    [('A',), ('B',), ('C',), ('D',)]
    >>> list(combinations_with_replacement('ABCD', 2))
    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]
    >>> list(combinations_with_replacement('ABCD', 3))
    [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'A', 'D'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'C'), ('A', 'C', 'D'), ('A', 'D', 'D'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'B', 'D'), ('B', 'C', 'C'), ('B', 'C', 'D'), ('B', 'D', 'D'), ('C', 'C', 'C'), ('C', 'C', 'D'), ('C', 'D', 'D'), ('D', 'D', 'D')]
    """
    n = len(iterable)
    if r == 0:
        yield ()
    elif n == 0:
        return
    else:
        lst = [1] * r
        yield tuple(iterable[i - 1] for i in lst)
        while lst[0] != n:
            i = r - 1
            while i > 0 and lst[i] == n:
                i -= 1
            lst[i:] = [lst[i] + 1] * (r - i)
            yield tuple(iterable[i - 1] for i in lst)