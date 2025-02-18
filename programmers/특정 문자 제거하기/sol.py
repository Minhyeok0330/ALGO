def solution(my_string, letter):
    result = ''

    for i in my_string:
        if i == letter:
            continue

        result += i
    
    return result


#def solution(my_string, letter):
    answer = ''

    for char in my_string:
        if char != letter:
            answer = answer + char

    
    return answer