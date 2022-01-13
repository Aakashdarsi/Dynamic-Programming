def count_subsets(set, n, sum):
    dp_table = [[0 for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp_table[i][0]= 1    
    for  i in range(1,sum+1):
        dp_table[0][i] = 0 # number of elements are zero and sum val is not zero then we cant find the value 
    for i in range(1,n+1):
        
         
        for j in range(1,sum+1):
            if set[i-1]>j:
                dp_table[i][j] = dp_table[i-1][j]
            if set[i-1] <= j:
                dp_table[i][j] = dp_table[i-1][j] + dp_table[i-1][j-set[i-1]]
    print("---------DP TABLE ----------")
    for i in range(n+1):
        for j in range(sum+1):
            print(dp_table[i][j],end=" | ")
        print()
    print("---------DP TABLE ----------")
    return dp_table[n][sum]










sete = [3,3,3,3]
n = len(sete)
sum = 6
result = count_subsets(sete, n, sum)
print(result)