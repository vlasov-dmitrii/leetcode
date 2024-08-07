
def max_profit(prices):
    profit = 0
    lowest = prices[0]
    
    for price in prices:
        if price < lowest:
            lowest = price
        difference = price - lowest
        if profit < difference:
            profit = difference
    return profit