def solution(s1, s2):
    answer = 0
    
    for char in s1:
        if char in s2:
            answer += 1
    return answer