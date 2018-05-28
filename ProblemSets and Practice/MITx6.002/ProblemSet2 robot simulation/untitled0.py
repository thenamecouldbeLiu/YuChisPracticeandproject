L = [3,2]
s = 10
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    if L == []:
        return "no solution"
    elif len(L) == 1 and s%L[0]!=0:
        return "no solution"
    else:
        i =0
        mutiplier_list =[]
        while i <len(L):
            m = s//L[i]
            mutiplier_list.append(m)
            s -= m*L[i]
            i+=1
        if s>0:
            return "no solution"
    return sum(mutiplier_list)
print(greedySum([10, 9, 8, 1], 17))