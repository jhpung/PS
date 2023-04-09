

a = ['사과','딸기', '포도', '배']
n = len(a)

def go(num=int):
    ret = ""

    for i in range(4):
        if num & (1 << i):
            ret += a[i] + " "

    print(ret)

for i in range(1, n):
    go(1 | (1 << i))

