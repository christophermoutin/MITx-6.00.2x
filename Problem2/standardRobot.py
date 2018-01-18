class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        newPos = self.position.getNewPosition(self.direction,self.speed)
        if newPos.getX() < 0 or newPos.getX() > self.room.width or newPos.getY() < 0 or newPos.getY() > self.room.height:
            self.setRobotDirection(random.uniform(0,360))
        else:
            self.position = newPos
            self.room.cleanTileAtPosition(newPos)
