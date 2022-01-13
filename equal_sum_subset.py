def subset_sum(set, sum, n):
    dp_table = [[False for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp_table[i][0] = True # number of elements >= 0 but sum is 0 then we can find a subset definetly!!! 
    
    for  i in range(1,sum+1):
        dp_table[0][i] = False # number of elements are zero and sum val is not zero then we cant find the value 
    for i in range(n+1):
        for j in range(sum+1):
            if set[i-1]>j:
                dp_table[i][j] = dp_table[i-1][j]
            if set[i-1] <= j:
                dp_table[i][j] = dp_table[i-1][j] or dp_table[i-1][j-set[i-1]]
    print("---------DP TABLE ----------")
    for i in range(n+1):
        for j in range(sum+1):
            print(dp_table[i][j],end=" | ")
        print()
    print("---------DP TABLE ----------")
    return dp_table[n][sum]





def equal_sum_subset(set, sum, n):
    if sum & 1 == 1:
        return False
    else:
        return subset_sum(set, sum//2, n)





set = [1,2,1,4]
n = len(set)
result = equal_sum_subset(set, sum(set),n)
print(result)