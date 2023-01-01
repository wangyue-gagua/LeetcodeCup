""" You are given a 2D integer array orders, where each orders[i] = [pricei, amounti, orderTypei] denotes that amounti orders have been placed of type orderTypei at the price pricei. The orderTypei is:

0 if it is a batch of buy orders, or
1 if it is a batch of sell orders.
Note that orders[i] represents a batch of amounti independent orders with the same price and order type. All orders represented by orders[i] will be placed before all orders represented by orders[i+1] for all valid i.

There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:

If the order is a buy order, you look at the sell order with the smallest price in the backlog. If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.
Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog. If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.
Return the total amount of orders in the backlog after placing all the orders from the input. Since this number can be large, return it modulo 109 + 7. """


from typing import List, Dict
# 优先队列处理会更合理，但是数组居然也能过
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sellList: List[int] = []
        buyList: List[int] = []
        sellListCount: Dict[int, int] = {}
        buyListCount: Dict[int, int] = {}

        for order in orders:
            price, amount, orderType = order
            # print(price, amount, orderType, order)
            # print(sellList, buyList, sellListCount, buyListCount)
            if orderType == 0:
                # buy
                if len(sellList) == 0:
                    if price not in buyList:
                        buyList.append(price)
                        buyList.sort()
                        buyListCount[price] = amount
                    else:
                        buyListCount[price] += amount
                else:
                    while len(sellList) > 0 and sellList[-1] <= price and amount > 0:
                        rest = sellListCount[sellList[-1]] - amount
                        if rest <= 0:
                            amount -= sellListCount[sellList[-1]]
                            # print("amount: ", amount)
                            del sellListCount[sellList[-1]]
                            sellList.pop()
                            # if price not in buyList:
                            #     buyList.append(price)
                            #     buyList.sort()
                            #     buyListCount[price] = amount
                            # else:
                            #     buyListCount[price] += amount
                        else:
                            amount = 0
                            sellListCount[sellList[-1]] = rest
                    if amount != 0:
                        if price not in buyList:
                            buyList.append(price)
                            buyList.sort()
                            buyListCount[price] = amount
                            # print("addamount: ", amount)
                        else:
                            buyListCount[price] += amount
                            # print("add + amount: ", amount, price, buyList)
            else:
                # sell
                if len(buyList) == 0:
                    if price not in sellList:
                        sellList.append(price)
                        sellList.sort(reverse=True)
                        sellListCount[price] = amount
                    else:
                        sellListCount[price] += amount
                else:
                    while len(buyList) > 0 and buyList[-1] >= price and amount > 0:
                        rest = buyListCount[buyList[-1]] - amount
                        if rest <= 0:
                            amount -= buyListCount[buyList[-1]]
                            del buyListCount[buyList[-1]]
                            buyList.pop()
                            # if price not in sellList:
                            #     sellList.append(price)
                            #     sellList.sort(reverse=True)
                            #     sellListCount[price] = amount
                            # else:
                            #     sellListCount[price] += amount
                        else:
                            amount = 0
                            buyListCount[buyList[-1]] = rest
                    if amount != 0:
                        if price not in sellList:
                            sellList.append(price)
                            sellList.sort(reverse=True)
                            sellListCount[price] = amount
                        else:
                            sellListCount[price] += amount
            # print(sellList, buyList, sellListCount, buyListCount)
        return (sum(sellListCount.values()) % (10**9 + 7)  + sum(buyListCount.values()) % (10**9 + 7) ) % (10**9 + 7)

print(Solution().getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]]))
print(Solution().getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]))