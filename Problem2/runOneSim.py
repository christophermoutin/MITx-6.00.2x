def runOneSim(speed, width, height, min_coverage, robot_type, num_robots):
    """
    Runs one simulation of the robot and returns the number of steps needed to reach min_coverage.
    """
    num_steps = 0
    robotDict = {}
    room_sim = RectangularRoom(width, height)
    numTiles = room_sim.getNumTiles()
    coverage = 0
    #création du dico des robots    
    for i in range(num_robots):
        robotDict[i]= robot_type(room_sim, speed)
        
        
    
    #actual simulation
    while coverage < min_coverage:
        coverage = 0
        for i in range(num_robots):
            robotDict[i].updatePositionAndClean()
        coverage += robotDict[0].room.getNumCleanedTiles()/numTiles
        num_steps += 1

    return num_steps


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    resultList=[]
    for i in range(num_trials):
        resultList.append(runOneSim(speed, width, height, min_coverage, robot_type, num_robots))
    mean = sum(resultList)/len(resultList)
    
    return mean
