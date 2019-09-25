def hourglassSum(arr):
    # Since at least is can be -64 when all 9's
    maxval = -64
    
    # Since spanning range of 3 rows, only go down to the fourth row
    for i_index in range(4):
        # Compute each hour glass value for the row then get the max value
        hg_val = max( [ sum(arr[i_index][i:i+3]) + arr[i_index+1][i+1] + sum(arr[i_index+2][i:i+3]) for i in range(4) ] )
        if maxval < hg_val:
            maxval = hg_val
    
    return maxval