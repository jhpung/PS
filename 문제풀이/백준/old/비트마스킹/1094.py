X = int(input())

ret = 1

while X != 1:
    r = X % 2

    if r & 1:
        ret += 1
    X //= 2

print(ret)
