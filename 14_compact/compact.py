def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [val for val in lst if val]

    # Why wont this work???
    # true_val = []
    # for char in lst:
    #     if char is True:
    #        true_val.append(char)
    # return true_val 

    return [val for val in lst if val]