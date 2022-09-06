def solution(lottos: list, win_nums: list):
    lottos.sort()
    win_nums.sort()
    
    max = 0
    min = 0

    for i in range(0, len(win_nums)):
        curr_lotto = lottos[i]
        curr_win = win_nums[i]
        if curr_lotto == 0:
            print(curr_lotto)
            max = max + 1
            continue

        if curr_lotto == curr_win:
            max = max + 1
            min = min + 1

    return [max, min]
