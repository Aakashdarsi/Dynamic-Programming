def mds(set,n,sum):
    dp_table = [[False for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp_table[i][0] = True 
    
    for j in range(sum+1):
        dp_table[0][i] = False 
    
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if set[i-1]>j:
                dp_table[i][j] = dp_table[i-1][j]
            if set[i-1] == j:
                dp_table[i][j] = True 
            if set[i-1] <= j:
                dp_table[i][j] = dp_table[i-1][j] or dp_table[i-1][j-set[i-1]]
    for i in range(n+1):
        for j in range(sum+1):
            print(dp_table[i][j],end=" | ")
        print()
    difference = float("+inf")
    for i in range((sum//2)+1):
        a = i 
        b = sum - i 
        if dp_table[n][i] == True and difference>abs(a-b):
            difference = abs(a-b)
    return difference







set = [2,4,5,2,3]
sum = sum(set)
result = mds(set,len(set),sum)
print(result)