def greedy_cow_transport(cows,limit):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

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
    sortedCowList = sorted(cowDict, key=cowDict.get, reverse=True)
        
    result = []
    
    while sortedCowList != []:
        trip = []
        tripCost = 0
        
        for cow in sortedCowList:
            if cowDict[cow] + tripCost <= limit:
                tripCost += cowDict[cow]
                trip.append(cow)
        
        result.append(trip)
        
        for cow in trip:
            sortedCowList.remove(cow)            
            
    return result
