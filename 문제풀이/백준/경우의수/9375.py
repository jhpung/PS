import sys
input = sys.stdin.readline

t = int(input())


while t:
    ret = 1
    t -= 1
    d = {}
    n = int(input())

    for i in range(n):
        name, type = input().split()
        if type not in d:
            d[type] = 1
            continue
        d[type] += 1

    for key in d.keys():
        count = d[key]

        ret *= count + 1

    print(ret - 1)
