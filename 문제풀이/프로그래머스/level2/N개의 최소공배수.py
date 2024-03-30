def solution(arr = []):
    answer = 0
    done = False
    mx = max(arr)
    answer = mx
    
    done = all(answer % num == 0 for num in arr)
    
    while not done:
        answer += mx
        done = all(answer % num == 0 for num in arr)
        
    return answer

print(solution([2,6,8,14]))