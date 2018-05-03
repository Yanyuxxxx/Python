# 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你
# 就需要将这多个值放到另外的容器中，比如列表或者集合里面。比如，你可以像下面
# 这样构造这样的字典:

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)


d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
# d['a'] = 2
# d['a'].append(2)
# d['b'].append(4)
print(d)