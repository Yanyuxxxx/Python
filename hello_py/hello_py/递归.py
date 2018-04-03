
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

# result = factorial(6)
# print(result)


def ack(m, n):
    print(m, n)
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

# result = ack(3, 4)
# print(result)


def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):

    if len(word) == 0:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

# print(is_palindrome('absba'))


# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
#
# print('Done!')

a = 4
x = 3

while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y

