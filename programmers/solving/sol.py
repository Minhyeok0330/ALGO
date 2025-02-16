def solution(my_string, letter):
    result = ''

    for i in my_string:
        if i == letter:
            continue

        result = result + i
    
    return result