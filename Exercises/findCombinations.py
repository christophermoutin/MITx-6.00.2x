import numpy as np

"""
Write a function that meets the specifications below. You do not have to use dynamic programming.

Hint: You might want to use bin() on an int to get a string, get rid of the first two characters, add leading 0's as needed, and then convert it to a numpy array of ints. Type help(bin) in the console.

For example,

    If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
    If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
    If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
"""


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    best_result = []
    best_list = [len(choices)*3]
    for i in range(2**len(choices)-1,0,-1):
        list = []
        init = bin(i)[2:]
        #print ("début loop",i)
        
        for s in init :
            list.append(int(s))
        
        while len(list) < len(choices):
            list.insert(0,0)
        #print (list)
        
        result=[]
        for j in range(len(list)):
            result.append(choices[j]*list[j])
        #print ("result",result)
        
        if sum(result) > total:
            #print ("sum result > total")
            continue
        elif sum(result) >= sum(best_result) and sum(result) <= total and sum(list) <= sum(best_list) and sum(list)>0:
            best_result = result
            best_list = list
            #print ("sum result", sum(result), "best", best_list)
        
    if best_list[0] == len(choices)*3:
        #print ("prout")
        best_list = [0 for x in range(len(choices))]
    
    return np.array(best_list)
