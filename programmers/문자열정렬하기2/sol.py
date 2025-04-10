def solution(my_string):
    my_string_lower = my_string.lower()  
    sorted_string = "".join(sorted(my_string_lower))  
    return sorted_string