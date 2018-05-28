###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trips = []
    cowsCopy = cows.copy()
    sortedCows = sorted(cowsCopy.items(), key=lambda x: x[1], reverse = True)
    while sum(cowsCopy.values()) > 0:
        ship = []
        total = 0
        for cow, value in sortedCows:
            if cowsCopy[cow] != 0 and value + total <= limit:
                ship.append(cow)
                total += value
                cowsCopy[cow] = 0
        trips.append(ship)
    return trips
# Problem 2
def brute_force_cow_transport(cows,limit=10):

    def itempick(D):
        m = []
        for x in D:
            box =[]
            for i in x:
                box += [i[0]]
            m.append(box)
        return m
    
    cowsCopy = cows.copy()
    cowslist = sorted(cowsCopy.items(), key=lambda x: x[1])
    power_list = get_partitions(cowslist)
    best_rout = []
    best_counter = len(cowslist)+1
#    if best_counter<len(next(power_list)):
#        best_rout = itempick(best_rout)
#        return best_rout
#    else:
    for minor_set in power_list:
        temp_rout = []
        temp_counter = 0
        flag = True
        temp_counter = len(minor_set)
        for set_part in minor_set:
            if flag:
                weight_sum = 0
                
            else:
                break
            
            for item in set_part:
                if item[1] + weight_sum <= limit:
                    weight_sum += item[1]

                else:
                    temp_rout =[]
                    weight_sum =0
                    flag = False

                    break
        if temp_counter < best_counter and weight_sum!= 0:
            
            best_counter = temp_counter
            temp_rout = minor_set
            best_rout = temp_rout
            print(temp_rout,"t")
        else:

            continue
    best_rout = itempick(best_rout)
    return best_rout
#    power_list = sorted(get_partitions(cows), key = len)
#
#
#    
#    possibilities = []
#    for i in power_list:
#        ship = []
#        for j in i:
#            ship_weights = []
#            for k in j:
#                ship_weights.append(cows[k])
#                #print(ship_weights)
#            ship.append(sum(ship_weights))
#            #print(ship)
#        if all(d <= limit for d in ship):
#            possibilities.append(i)
#    # possibiliies now contains some duplicates, which need to be removed
#    pruned_possibilities = []
#    for k in possibilities:
#        if k not in pruned_possibilities:
#            pruned_possibilities.append(k)
#    # now find the minimum list length:
#    min_list_len = min(map(len, pruned_possibilities))
#    for l in pruned_possibilities:
#        if len(l) == min_list_len:
#            return l
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    greedy_start = time.time()
    greedy_results = greedy_cow_transport(cows, limit = 10)
    greedy_end = time.time()
    print('Greedy Algorithm time:', greedy_end -greedy_start)
    brute_force_start = time.time()
    brute_force_results = brute_force_cow_transport(cows, limit = 10)
    brute_force_end = time.time()
    print('Brute force time:', brute_force_end - brute_force_start)
    print('Greedy Algorithm results:', greedy_results)
    print('Number of trips returned by Greedy Algorithm:', len(greedy_results))
    print('Brute Force Algorithm results:', brute_force_results)
    print('Number of trips returned by Brute Force Algorithm:', len(brute_force_results))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
#
#print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows,10))
print(brute_force_cow_transport({'Luna': 41, 'Buttercup': 11, 'Starlight': 54, 'Betsy': 39}, 145))
print(brute_force_cow_transport({'Daisy': 50, 'Betsy': 65, 'Buttercup': 72}, 75))
print(brute_force_cow_transport({'Lotus': 40, 'MooMoo': 50, 'Horns': 25, 'Boo': 20, 'Miss Bella': 25, 'Milkshake': 40}, 100))