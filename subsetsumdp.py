def subsetSum(set,sume,n):
    dp_table = [[False for i in range(sume+1)] for j in range(n+1)]
    for i in range(n+1):
        dp_table[i][0] = True  # if the sum =0 and number of elements can be or cannot be zero then we can find the result
    
    for j in range(1,sume+1):
        dp_table[0][j] = False # if number of elements is zero and sum of elements is non zero then we can't find the result
    
    for i in range(n+1):
        for j in range(sume+1):
            if set[i-1] > j:
                dp_table[i][j] = dp_table[i-1][j]
            
            if set[i-1]<=j:
                dp_table[i][j] = dp_table[i-1][j] or dp_table[i-1][j-set[i-1]]
    
    for i in range(n+1): # Printing DP Table
        for j in range(sume+1):
            print(dp_table[i][j],end=" | ")
        print()
    
    
    return dp_table[n][sume] # Final output
            




set = [2,2,3]
sume = 5
n = len(set)
result = subsetSum(set,sume,n)
print(result)