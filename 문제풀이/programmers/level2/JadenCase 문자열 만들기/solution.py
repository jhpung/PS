from curses.ascii import isalpha, isupper


def solution(s: str):
    answer = ''

    words = s.split(' ')

    for word in words:
        temp = list(word)

        if not temp:
            answer = answer + ' '
            continue 

        temp[0] = temp[0].upper()

        for i in range(1, len(temp)):
            temp[i] = temp[i].lower()

        answer = answer + ''.join(temp) + ' '

    return answer.strip()
