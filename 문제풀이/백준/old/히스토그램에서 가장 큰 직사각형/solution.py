from collections import deque

while True:
    inputs = list(map(int, input().split()))
    
    n = inputs[0]
    
    if n == 0:
        break

    squares = inputs[1:]
    stack = deque()
    answer = 0
    
    for index, height in enumerate(squares):
        if not stack:
            stack.append((index, height))
            continue
        
        top_index, top_height = stack[-1]
        
        if top_height < height:
            stack.append((index, height))
        else:
            while stack:
                top_index, top_height = stack[-1]
            
                if top_height < height:
                    break
            
                stack.pop()
            
                answer = max(((index - top_index) * top_height), answer)
                new_start = top_index
            stack.append((new_start, height))

    while stack:
        top_index, top_height = stack.pop()
        width = (n - top_index)
        answer = max(width * top_height, answer)
        
    print(answer)   
    