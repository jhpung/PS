from collections import deque

while True:
    inputs = list(map(int, input().split()))
    
    n = inputs[0]
    
    if len(inputs) == 1 and n == 0:
        break

    squares = inputs[1:] + [0]
    stack = deque()
    answer = 0
    
    for index, height in enumerate(squares):
        if not stack:
            stack.append((index, height))
        
        while stack:
            top_index, top_height = stack[-1]
            
            if top_height <= height:
                break
            
            stack.pop()
            
            answer = max(((index - top_index) * top_height), answer)
        
        stack.append((index, height))
    
    while stack:
        top_index, top_height = stack.pop()
        
        if not stack:
            width = n
        else:
            width = (n - top_index)
        answer = max(width * top_height, answer)
    
    print(answer)   
    