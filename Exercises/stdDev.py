def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    mean = 0.0
    tot = 0.0
    if L == []: 
        return float('NaN')
    else : 
        for i in L :
            mean += len(i)
        mean = mean/len(L)
        for i in L : 
            tot += (len(i)-mean)**2
        std = (tot/len(L))**0.5
        return std
