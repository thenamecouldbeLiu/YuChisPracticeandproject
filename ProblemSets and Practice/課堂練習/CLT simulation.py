import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    if type(numTrials)==int or float:
        L =[]
        L.append(numTrials)
        numTrials =L
    sampledict = dict(((x),0) for x in numTrials)

    all_red = []
    all_green = []
    bucket = []
    for i in range(3):
        all_red.append("red")
        all_green.append("green")
        bucket.append("green")
        bucket.append("red")
    for num in numTrials:
        for trial in range(num):
            if random.sample(bucket, 3) == all_red or random.sample(bucket, 3)==all_green:
                sampledict[num] += 1
        print(sampledict)
    MCS_result = []
    for key, value in sampledict.items():
        MCS_result.append(value/key)
        
    return MCS_result