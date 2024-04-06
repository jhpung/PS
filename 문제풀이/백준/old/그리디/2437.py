def solve():
    N = int(input())
    
    ls = sorted(list(map(int, input().split())))
    
    target = 1
    for i in ls:
        if target < i:
            break
        target += i
    
    print(target)
    
solve()