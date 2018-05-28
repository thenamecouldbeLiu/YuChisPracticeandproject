import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    if title!= None:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    def getlongestrun(temp):
        best_run = 1
        tempcounter = 1
        place =0
        while place<len(temp)-1:
            if temp[place+1] ==temp[place]:
                tempcounter +=1
                if tempcounter>best_run:
                    best_run = tempcounter
                place+=1
            else:
                tempcounter =1
                place+=1
        return best_run
            
        
    finallist = []
    for trial in range(numTrials):
        temp_result = []
        for numroll in range(numRolls):
            temp_result.append(die.roll())
        finallist.append(getlongestrun(temp_result))
    makeHistogram(finallist,10, 'Number of longest run', 'times happened')
    return sum(finallist)/numTrials
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))