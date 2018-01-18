import numpy as np
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    
    #create viruses list
    viruses = []
    for i in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    
    #create test patient P1
    results = np.zeros(numTrials*300).reshape(300,numTrials)
    
    #runs numTrials of 300 steps, putting results in an array of 300 lines, 
    # numTrials columns
    for t in range(numTrials) :
        P1 = Patient(viruses, maxPop)
        for s in range(300):
            P1.update()
            results[s][numTrials-1]+=P1.getTotalPop()
    
    #calculating average of virus population size at each step        
    yValues = []
    for i in range(300):
        a = sum(results[i])/len(results[i])
        yValues.append(a)
    
    x = np.linspace(0,299,300).tolist()
    pylab.plot(yValues,label = 'pop average')
    pylab.title('virus pop average at each step')
    pylab.legend()
    pylab.xlabel('Time Steps')
    pylab.ylabel('pop #')
    pylab.show()
