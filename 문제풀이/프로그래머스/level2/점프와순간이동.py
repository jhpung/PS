import math

def solution(n = 0):
    result = 0
    curr = n
    
    if n == 1 or n == 2:
        return 1
    
    while n != 0:
        if n % 2 == 0:
            n /= 2
            continue
        n -= 1
        result += 1
        
    
    return result