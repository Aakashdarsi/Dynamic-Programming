def knapsack(wt,profit,w,n):
    dp_table = [[-1 for i in range(w+1)] for j in range(n+1)] #Creating DP table for 0/1 knapsack
    result = 0 # used for storing the results
    if (w == 0) or (n == 0):
        return 0 
    if dp_table[n][w] != -1:
        return dp_table[n][w]
    
    elif wt[n-1] > w:
        return knapsack(wt,profit,w,n-1)
        
    else:
        result = max(knapsack(wt,profit,w,n-1),profit[n-1]+knapsack(wt,profit,w-wt[n-1],n-1))
        dp_table[n][w] = result # update that result with corresponding weight and number of items in the dp table
    return dp_table[n][w]

      






wt = [3,2,4] # Weight array
profit = [6,8,7] # Profit array
w = 8  # Bag or Knapsack Weight
n = 3 # Number of items

max_profit = knapsack(wt,profit,w,n)
print(max_profit)