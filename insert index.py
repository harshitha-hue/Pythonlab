import bisect

prices = [10, 20, 30, 50]
new_price = 25
insert_index = bisect.bisect_left(prices, new_price)
print("Insert 25 at index:", insert_index)
