def solution(my_string, n):
    answer = ""
    for alphabet in my_string:
        answer = answer + alphabet * n

    return(answer)        