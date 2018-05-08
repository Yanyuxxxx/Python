def dedupe (items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
g = dedupe(a)
print(list(g))

# 如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合, 然而，这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱 111
print(set(a))
