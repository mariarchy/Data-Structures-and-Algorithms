# LEETCODE PROBLEM 122 - Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# -----------------------------------------------------------------------------
# Say you have an array for which the ith element is the price of a given stock
# on day i. Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = 0     # buy price for a stock
        sell = 0    # sell price for a stock
        bought = False
        # handle empty array + arrays of size 1
        if prices == []:
            return profit

        for i in range(0, len(prices)-1):
            # if bought and prices[i] < prices[i-1]:
            #     # we have bought a stock and set its price to buy
            #     sell = prices[i-1]
            #     profit += sell - buy
            #     sold = True
            #     bought = False
            if prices[i+1] > prices[i]:
                if bought:
                    sell = prices[i+1]
                    profit += sell-buy
                    # if we have already sold a stock or haven't bought a stock yet
                    buy = prices[i]
                else:
                    buy = prices[i]
                    bought = True
        # now, we only have the last element (the price of stocks on the last day) to traverse
        last = len(prices) - 1
        if bought and prices[last] > buy:
            sell = prices[last]
            profit += sell - buy

        return profit
