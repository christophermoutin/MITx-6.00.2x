class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.setRobotDirection(random.uniform(0,360))
        newPos = self.position.getNewPosition(self.direction,self.speed)
        if newPos.getX() < 0 or newPos.getX() > self.room.width or newPos.getY() < 0 or newPos.getY() > self.room.height:
            self.setRobotDirection(random.uniform(0,360))
        else:
            self.position = newPos
            self.room.cleanTileAtPosition(newPos)
