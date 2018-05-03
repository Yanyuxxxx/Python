prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)


# 执行这些计算的时候，需要注意的是       函数创建的是一个只能访问一次的迭 代器。比如，下面的代码就会产生错误:
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
# print(min(prices_and_names))