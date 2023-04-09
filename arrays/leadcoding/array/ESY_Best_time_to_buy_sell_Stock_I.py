"""
************************************** PLEASE SOLVE ALL 4 TYPES OF THIS PROBLEM FROM LC ********************************
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def solution(prices):
    min_price, max_profit = float('inf'), 0
    for price in prices:
        min_price = min(price, min_price)
        current_max_profit = price - min_price
        max_profit = max(current_max_profit, max_profit)
    return max_profit


# poor design of solution assumes highest with lowest can cause a bigger profit

"""
Again the problem remained same you did not learn from your past mistake of not to look for smaller picture and trying 
to solve it for broader picture only look for smaller picture and then exaggarate 
"""

25303899
def solution_wrong(prices):
    # Problem in this approach [3,3,5,0,0,3,1,4]
    max_from_right, max_index = -1, -1
    min_from_left, min_index = 9999999999, -1
    # zero tak jaao lekin print nahi karna length se ek kam chalna aur -1 is operation
    for i in range(len(prices) - 1, 0, -1):
        if prices[i] > max_from_right:
            max_from_right = prices[i]
            max_index = i
    print(max_index)
    for j in range(0, max_index):
        if prices[j] < min_from_left:
            min_from_left = prices[j]
            min_index = j
    print(min_index)

    if min_index != -1 and max_index != -1:
        if min_from_left < max_from_right:
            return max_from_right - min_from_left
        else:
            return 0
    else:
        return 0

if __name__ == "__main__":

    print(solution([1,2,3,4,5]))
