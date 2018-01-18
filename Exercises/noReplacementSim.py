import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    tot = 0.0
    for t in range(numTrials):
        balls = ['r','r','r','g','g','g']
        result = []
        for i in range(3):
            result.append(balls.pop(random.randint(0,len(balls)-1)))
        if result == ['r','r','r'] or result == ['g','g','g']:
            tot+=1.0
    
    return tot/float(numTrials)
