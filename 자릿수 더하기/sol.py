def solution(n):
    str_list = list(str(n))
    result = []
    for strs in str_list:
        ints = int(strs)
        result.append(ints)
    return sum(result)

print(solution(1234))