# 6.00.2x Problem Set 2: Simulating robots

import math
import random
import numpy as np
import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
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
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)

class RectangularRoom(object):
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.tiles = dict(((x, y), 0) for x in range(width) for y in range(height))
    
    def cleanTileAtPosition(self, pos):
        self.tiles[(int(pos.x), int(pos.y))] += 1

    def isTileCleaned(self, m, n):
        return bool(self.tiles[(m, n)])
    
    def getNumTiles(self):
        return int(self.width * self.height)

    def getNumCleanedTiles(self):

        return sum(self.tiles.values())

    def getRandomPosition(self):
        return Position(random.random() * self.width, random.random() * self.height)

    def isPositionInRoom(self, pos):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

# 2. Robot
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        self.room = room
        self.speed = speed
        self.dir = int(random.random() * 360)
        self.pos = self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.pos)

    def getRobotPosition(self):
        return self.pos
    
    def getRobotDirection(self):
        return self.dir

    def setRobotPosition(self, position):
        if self.room.isPositionInRoom(position):
            self.pos = position
        else:
            raise ValueError

    def setRobotDirection(self, direction):
        if type(direction) != int:
            raise TypeError
        if direction not in range(360):
            raise ValueError
        self.dir = direction
        
    def updatePositionAndClean(self):
        raise NotImplementedError # don't change this!

# 3. StandardRobot
class StandardRobot(Robot):
    def updatePositionAndClean(self):
        new_pos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(self.pos)
        else:
            self.setRobotDirection(int(random.random() * 360))

# 4. runSimulation
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type, animate=False):
    total_steps = 0
    for __ in range(num_trials):
        if animate:
            anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        robots = []
        for i in range(num_robots):
            robots.append(robot_type(room, speed))
        while room.getNumCleanedTiles() / float(room.getNumTiles()) < 1 and room.getNumCleanedTiles() / float(room.getNumTiles())<min_coverage:
            if animate:
                anim.update(room, robots)
            for robot in robots:
                robot.updatePositionAndClean()
            total_steps += 1
        if animate:
            anim.update(room, robots)
            anim.done()
    return total_steps / float(num_trials)

# 5. RandomWalkRobot
class RandomWalkRobot(Robot):
    def updatePositionAndClean(self):
        new_pos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(self.pos)
        self.setRobotDirection(int(random.random() * 360))