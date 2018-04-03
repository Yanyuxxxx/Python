
been_called = False

def example():
    been_called = True


example()
print(been_called)


def example2():
    global been_called
    been_called = True

example2()
print(been_called)


s = 'abc'
t = [0, 1, 2]

print(zip(s, t))

# t = zip(s, t)
t = list(zip(s, t))

# for pair in t:
#     print(pair)

for letter, number in t:
    print(number, letter)


