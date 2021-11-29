def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    new_list = []
    for l in l1:
        for i in l2:
            if l == i:
                new_list.append(l)
    return new_list
                

"""
    Why is it that this is the go to answer?:
    
    set2 = set(l2)

    return [val for val in l1 if val in set2]
"""