def solution(before, after):
    answer = 0
    for char in before:
        if char in after:
            answer += 1
        if len(after) == answer:
            return 1
        else:
            return 0

