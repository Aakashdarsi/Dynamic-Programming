def subsetSum(set, sume, n):
    if  n== 0 and sume !=0:
        return False
    if sume == 0:
        return True 

    if (set[n-1])>sume:
        return subsetSum(set, sume ,n-1)
    else:
        return subsetSum(set,sume,n-1) or subsetSum(set,sume - set[n-1],n-1)






set = [1,2,8]
sume = 5
n = len(set)
result = subsetSum(set,sume,n)
if result == False:
    print("Subset can't be found")
else:
    print("Subset found",result)