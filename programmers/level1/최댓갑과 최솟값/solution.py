def solution(s):
    l = sorted(list(map(int, s.split(' '))))

    return '{} {}'.format(l.pop(0), l.pop(-1))
