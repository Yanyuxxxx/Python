def avg(x):
    return sum(x)/len(x)

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


g = (98, 89, 85, 88, 80, 75, 65, 60, 30)
m = drop_first_last(g)
print(m)


print('###################')
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)


print('###################')
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


print('###################')
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print(type(line.split(':')))


print('###################')
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)


print('################### 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法')
items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else  head
# sum()函数是一个递归函数，return head + sum(tail) if tail else head这段代码是判断tail是否为空，如果为空则结束递归，返回head值，然后一层一层返回，最终实现加和。
print(sum(items))