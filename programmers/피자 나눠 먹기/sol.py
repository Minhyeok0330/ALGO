def solution(slice, n):
    
    if (n % slice == 0):
        p = (n // slice) 
    else:
        p = (n // slice) + 1

    answer = p
    return answer