# stock price = [ 10, 1, 8, 6, 2]
# buy and sell 
# max profit , buy index and sell index
# [10,2,8,7,1,2,1]
import math

def stockPrice(price):
    currBought = price[0]
    maxProfit = -math.inf
    buyIndex = 0
    sellIndex = -1
    for i in range(1, price):
        if price[i] < currBought:
            currBought = price[i]
            buyIndex = i
        else:
            diff = price[i]-currBought
            if maxProfit < diff:
                sellIndex = i
                maxProfit = diff
    return maxProfit