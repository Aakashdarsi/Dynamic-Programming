def subsetSum(set, sume, n):
    if  n== 0 and sume !=0: # If number of items is zero and sum to be found is non zero
        return False
    if sume == 0: # If we want to find the sum whose sum is zero we can obviously find without including any element
        return True 

    if (set[n-1])>sume: # If current element is greater than sum required then skip
        return subsetSum(set, sume ,n-1) 
    else:
        return subsetSum(set,sume,n-1) or subsetSum(set,sume - set[n-1],n-1) # Find Subset sum including that and excluding that element






set = [1,2,8] # Set of elements
sume = 5 # Sum to be found
n = len(set) # number of elements in the set
result = subsetSum(set,sume,n) #Function call
if result == False:
    print("Subset can't be found")
else:
    print("Subset found",result)