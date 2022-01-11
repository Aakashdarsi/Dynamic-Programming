wt = [3,2,4] # Weight array
profit = [6,8,7] # Profit array
w = 8  # Bag or Knapsack Weight
n = 3 
dp_table = [[-1 for i in range(w+1)] for j in range(n+1)] # for generating a tabular dp
for i in range(n+1): # i indicating the number of items
    for j in range(w+1): # j indicating the weights ranging from o to n (INCLUSIVE)
        if i == 0 or j == 0: # if number of items is zero or bag weight is zero then max profit is zero
            dp_table[i][j] = 0 
        elif (wt[i-1]>j): # if weight of the element is greater than bag weight
            dp_table[i][j] = dp_table[i-1][j] #moving to previous number of items
        else:
            dp_table[i][j] = max(dp_table[i-1][j],profit[i-1]+dp_table[i-1][j-wt[i-1]]) #getting the max profit
print(dp_table[n][w])