import numpy as np
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
        
    #create viruses list
    viruses = []
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    
    #create test patient P1
    results = np.zeros(numTrials*300).reshape(300,numTrials)
    resultsPopResist = np.zeros(numTrials*300).reshape(300,numTrials)
    
    #runs numTrials of 300 steps, putting results in an array of 300 lines, 
    # numTrials columns
    for t in range(numTrials) :
        P1 = TreatedPatient(viruses, maxPop)
        for s in range(150):
            P1.update()
            results[s][numTrials-1] += P1.getTotalPop()
            resultsPopResist[s][numTrials-1] += P1.getResistPop(['guttagonol'])
        
        P1.addPrescription('guttagonol')
        for s in range(150,300):
            P1.update()
            results[s][numTrials-1]+=P1.getTotalPop()
            resultsPopResist[s][numTrials-1] += P1.getResistPop(['guttagonol'])
            
    
    #calculating average of virus population size at each step        
    yValues1 = []
    for i in range(300):
        a = sum(results[i].tolist())/len(results[i])
        yValues1.append(a)
        
    yValues2 = []
    for i in range(300):
        a = sum(resultsPopResist[i].tolist())/len(resultsPopResist[i])
        yValues2.append(a)

    pylab.plot(yValues1,label='pop average')
    pylab.plot(yValues2,'r--',label = 'resistant virus population')
    pylab.title('virus pop average at each step')
    pylab.legend()
    pylab.xlabel('Time Steps')
    pylab.ylabel('pop #')
    pylab.show()
