def solution(s=str):
    answer = []
    convert_count = 0
    removed_count = 0

    while s != "1":
        convert_count += 1
        removed_count += s.count("0")
        s = s.replace("0", "")
        c = len(s)
        s = bin(int(c)).replace("0b", "")

    return [convert_count, removed_count]
