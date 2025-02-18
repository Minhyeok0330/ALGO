def solution(n):
    answer = 0

    while n > 0:
        a, b = divmod(n, 10)
        # a = divmod(n, 10)[0] # n // 10
        # b = divmod(n, 10)[1] # n % 10
        
        answer += b
        n = a

    return answer

