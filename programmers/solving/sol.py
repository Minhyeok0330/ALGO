def solution(my_string):
    
    my_string = my_string.lower()
    sorted_string = list[my_string]
    result = sorted_string.sort()
    return ''.join(result)

print(solution('asdfasdfa'))
