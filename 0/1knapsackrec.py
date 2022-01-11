def knapsack(wt,profit,w,n):
    if (w == 0) or (n == 0): # If bag weight is zero then we can't  add the elements, and number of items is zero then there is no profit
        return 0 
    
    elif wt[n-1] > w: # If element weight is greater than bag capacity then exclude
        return knapsack(wt,profit,w,n-1)

    else: # U can Include or exclude basing upon the max profits basign upon the conditions
        return max(knapsack(wt,profit,w,n-1), profit[n-1]+knapsack(wt,profit,w-wt[n-1],n-1))







wt = [3,2,4] # Weight array
profit = [6,8,7] # Profit array
w = 8  # Bag or Knapsack Weight
n = 3 # Number of items
max_profit = knapsack(wt,profit,w,n)
print(max_profit)