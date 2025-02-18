def solution(strlist):
    char_len = 0
    str_len = []
    for strs in strlist:
        for char in strs:
            char_len += 1
        str_len.append(char_len)
        char_len = 0
            
    
    return str_len