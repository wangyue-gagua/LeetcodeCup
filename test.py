import bisect
price = [13,5,1,8,21,2]
price.sort()
interval = (price[-1] - price[0]) / (3 - 1)
print(price, interval)
print(bisect.bisect_left(price, price[0] + interval))
print(135 / 5)