def arrayManipulation(n, queries):
    retarr = [0] * n

    for retSet in queries:
        start, end, val = retSet
        
        for index in range(start-1, end):
            retarr[index] = retarr[index] + val

    return max(retarr)
