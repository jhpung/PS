N = int(input())

a = []

for i in range(N):
    start, end = map(int, input().split())
    a.append((end, start))


a.sort()

end, start = a[0]
ret = 1

for i in range(1, N):
    nend, nstart = a[i]

    if nstart < end:
        continue
    end = nend
    nstart = nstart
    ret += 1

print(ret)
