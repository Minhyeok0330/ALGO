def solution(n):
    answer = 0
    for n in range(n+1):
        if n % 2 == 1:
            continue
        else:
            answer = answer + n
    return answer

print(solution(10))