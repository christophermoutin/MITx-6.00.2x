def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
   
    cowDict = cows
    Liste = []
    
    for i in cowDict.keys():
        Liste.append(i)
        
    partitions = []
        
    for item in (get_partitions(Liste)):
        partitions.append(item)
            
    for j in range (1,len(Liste)+1):
       
        for voyageListe in partitions:
           
            if len(voyageListe) == j:
                           
                W = []
                for voyage in voyageListe:
                    totalW = 0
                    for cow in voyage:
                        totalW += cowDict[cow]
                        
                    W.append(totalW)
                    
                    possibleSolution = voyageListe
                
                if max(W) <= limit:
                    return possibleSolution
