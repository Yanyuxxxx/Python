from collections import deque

def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen = history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

if __name__ == '__main__':
    with open(r'/Users/yangyi/Desktop/text_py.rtf') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('_' * 20)


#带有 yield 的函数在 Python 中被称之为 generator（生成器），何谓 generator ？

# 简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
# Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，
# 而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
# 执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
# 而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。