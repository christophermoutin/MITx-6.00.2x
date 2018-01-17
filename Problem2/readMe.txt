Introduction

In this problem set you will practice designing a simulation and implementing a program that uses classes.

As with previous problem sets, please don't be discouraged by the apparent length of this assignment. There is quite a bit to read and understand, but most of the problems do not involve writing much code.
Getting Started

Download and save

pset2.zip: A zip file of all the files you need, including:

    ps2.py, a skeleton of the solution.

    ps2_visualize.py, code to help you visualize the robot's movement (an optional - but cool! - part of this problem set).

    ps2_verify_movement35.pyc, precompiled module for Python 3.5 that assists with the visualization code.

REVIEW OBJECT ORIENTED PROGRAMMING AND CLASSES

This and future problem sets will require you to know OOP. If you need a refresher, please visit these links and make sure you are familiar with these topics.

    Implementing new classes and their attributes.
    Understanding class methods.
    Understanding inheritance.
    Telling the difference between a class and an instance of that class - recall that a class is a blueprint of an object, whilst an instance is a single, unique unit of a class.
    Utilizing libraries as black boxes.

Note: If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.

Problem 1: RectangularRoom Class
Problem 1: RectangularRoom Class
10.0/10.0 points (graded)

You will need to design two classes to keep track of which parts of the room have been cleaned as well as the position and direction of each robot.

In ps2.py, we've provided skeletons for the following two classes, which you will fill in in Problem 1:

    RectangularRoom: Represents the space to be cleaned and keeps track of which tiles have been cleaned.
    Position: We've also provided a complete implementation of this class. It stores the x- and y-coordinates of a robot in a room.

Read ps2.py carefully before starting, so that you understand the provided code and its capabilities.
Problem 1

In this problem you will implement the RectangularRoom class. For this class, decide what fields you will use and decide how the following operations are to be performed:

    Initializing the object
    Marking an appropriate tile as cleaned when a robot moves to a given position (casting floats to ints - and/or the function math.floor - may be useful to you here)
    Determining if a given tile has been cleaned
    Determining how many tiles there are in the room
    Determining how many cleaned tiles there are in the room
    Getting a random position in the room
    Determining if a given position is in the room

Complete the RectangularRoom class by implementing its methods in ps2.py.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only a couple of lines of code.)

 Problem 2: Robot Class
10.0/10.0 points (graded)

In ps2.py we provided you with the Robot class, which stores the position and direction of a robot. For this class, decide what fields you will use and decide how the following operations are to be performed:

    Initializing the object
    Accessing the robot's position
    Accessing the robot's direction
    Setting the robot's position
    Setting the robot's direction

Complete the Robot class by implementing its methods in ps2.py.

Note: When a Robot is initialized, it should clean the first tile it is initialized on. Generally the model these Robots will follow is that after a robot lands on a given tile, we will mark the entire tile as clean. This might not make sense if you're thinking about really large tiles, but as we make the size of the tiles smaller and smaller, this does actually become a pretty good approximation.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only a couple of lines of code.)

Note: The Robot class is an abstract class, which means that we will never make an instance of it. Read up on the Python docs on abstract classes at this link and if you want more examples on abstract classes, follow this link.

In the final implementation of Robot, not all methods will be implemented. Not to worry -- its subclass(es) will implement the method updatePositionAndClean()

 Problem 3: StandardRobot Class
10.0/10.0 points (graded)

Each robot must also have some code that tells it how to move about a room, which will go in a method called updatePositionAndClean.

Ordinarily we would consider putting all the robot's methods in a single class. However, later in this problem set we'll consider robots with alternate movement strategies, to be implemented as different classes with the same interface. These classes will have a different implementation of updatePositionAndClean but are for the most part the same as the original robots. Therefore, we'd like to use inheritance to reduce the amount of duplicated code.

We have already refactored the robot code for you into two classes: the Robot class you completed in Problem 2 (which contains general robot code), and a StandardRobot class that inherits from it (which contains its own movement strategy).

Complete the updatePositionAndClean method of StandardRobot to simulate the motion of the robot after a single time-step (as described on the Simulation Overview page).

class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

We have provided the getNewPosition method of Position, which you may find helpful:

class Position(object):

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """

Note: You can pass in an integer or a float for the angle parameter.

Before moving on to Problem 4, check that your implementation of StandardRobot works by uncommenting the following line under your implementation of StandardRobot. Make sure that as your robot moves around the room, the tiles it traverses switch colors from gray to white. It should take about a minute for it to clean all the tiles.

testRobotMovement(StandardRobot, RectangularRoom) Problem 4: Running the Simulation
10.0/10.0 points (graded)

In this problem you will write code that runs a complete robot simulation.

Recall that in each trial, the objective is to determine how many time-steps are on average needed before a specified fraction of the room has been cleaned. Implement the following function:

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.
    """

The first six parameters should be self-explanatory. For the time being, you should pass in StandardRobot for the robot_type parameter, like so:

    avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot) 

Then, in runSimulation you should use robot_type(...) instead of StandardRobot(...) whenever you wish to instantiate a robot. (This will allow us to easily adapt the simulation to run with different robot implementations, which you'll encounter in Problem 6.)

Feel free to write whatever helper functions you wish.

We have provided the getNewPosition method of Position, which you may find helpful:

class Position(object):

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """

For your reference, here are some approximate room cleaning times. These times are with a robot speed of 1.0.

    One robot takes around 150 clock ticks to completely clean a 5x5 room.

    One robot takes around 190 clock ticks to clean 75% of a 10x10 room.

    One robot takes around 310 clock ticks to clean 90% of a 10x10 room.

    One robot takes around 3322 clock ticks to completely clean a 20x20 room.

    Three robots take around 1105 clock ticks to completely clean a 20x20 room.

(These are only intended as guidelines. Depending on the exact details of your implementation, you may get times slightly different from ours.)

You should also check your simulation's output for speeds other than 1.0. One way to do this is to take the above test cases, change the speeds, and make sure the results are sensible.

For further testing, see the next page in this problem set about the optional way to use visualization methods. Visualization will help you see what's going on in the simulation and may assist you in debugging your code.

Visualizing Robots

Note: This part is optional. It is cool and very easy to do, and may also be useful for debugging. Be sure to comment out all visualization parts of your code before submitting.

We've provided some code to generate animations of your robots as they go about cleaning a room. These animations can also help you debug your simulation by helping you to visually determine when things are going wrong.

Here's how to run the visualization:

    In your simulation, at the beginning of a trial, insert the following code to start an animation:

        anim = ps2_visualize.RobotVisualization(num_robots, width, height)

    (Pass in parameters appropriate to the trial, of course.) This will open a new window to display the animation and draw a picture of the room.

    Then, during each time-step, before the robot(s) move, insert the following code to draw a new frame of the animation:

        anim.update(room, robots)

    where room is a RectangularRoom object and robots is a list of Robot objects representing the current state of the room and the robots in the room.

    When the trial is over, call the following method:

        anim.done()

The visualization code slows down your simulation so that the animation doesn't zip by too fast (by default, it shows 5 time-steps every second). Naturally, you will want to avoid running the animation code if you are trying to run many trials at once (for example, when you are running the full simulation).

For purposes of debugging your simulation, you can slow down the animation even further. You can do this by changing the call to RobotVisualization, as follows:

    anim = ps2_visualize.RobotVisualization(num_robots, width, height, delay)

The parameter delay specifies how many seconds the program should pause between frames. The default is 0.2 (that is, 5 frames per second). You can increase this value to make the animation slower or decrease it (0.01 is reasonable) to see many robots cleaning the room at a faster frame rate.

For problem 6, we will make calls to runSimulation() to get simulation data and plot it. However, you don't want the visualization getting in the way. If you choose to do this visualization exercise, before you get started on problem 5 (and before you submit your code in submission boxes), make sure to comment the visualization code out of runSimulation().

 Problem 5: RandomWalkRobot Class
10.0/10.0 points (graded)

iRobot is testing out a new robot design. The proposed new robots differ in that they change direction randomly after every time step, rather than just when they run into walls. You have been asked to design a simulation to determine what effect, if any, this change has on room cleaning times.

Write a new class RandomWalkRobot that inherits from Robot (like StandardRobot) but implements the new movement strategy. RandomWalkRobot should have the same interface as StandardRobot.

Test out your new class. Perform a single trial with the StandardRobot implementation and watch the visualization to make sure it is doing the right thing. Once you are satisfied, you can call runSimulation again, passing RandomWalkRobot instead of StandardRobot.
