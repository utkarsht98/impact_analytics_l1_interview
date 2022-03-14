# stock price = [ 10, 1, 8, 6, 2]
# buy and sell 
# max profit , buy index and sell index
# [10,2,8,7,1,2,1]
import math

def maxStockProfit(price):
    currBought = price[0]
    maxProfit = -math.inf
    buyIndex = 0
    sellIndex = -1
    currBuyIndex = 0
    # currBuyIndex = 0
    for i in range(1, len(price)):
        if price[i] < currBought:
            currBought = price[i]
            currBuyIndex = i
        else:
            diff = price[i]-currBought
            if maxProfit < diff:
                buyIndex = currBuyIndex
                sellIndex = i
                maxProfit = diff
    return maxProfit, buyIndex, sellIndex

stockPrice = [ 10, 1, 8, 6, 2]
print(maxStockProfit(stockPrice))