def subset_count(set,sum,n):
    if sum == 0 :
        return True
    
    if n == 0 : 
        return False 
    if set[n-1] >sum:
        return subset_count(set,sum,n-1)
    else:
        return subset_count(set,sum,n-1) + subset_count(set,sum-set[n-1],n-1)






set = [3,3,3,3]
n = len(set)
sum = 6 
result = subset_count(set,sum,n)
print(result)