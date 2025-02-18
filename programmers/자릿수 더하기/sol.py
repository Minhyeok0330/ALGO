def solution(n):
    str_list = list(str(n))
    answer = []
    for strs in str_list:
        ints = int(strs)
        answer.append(ints)
    return sum(answer)

print(solution(1234))