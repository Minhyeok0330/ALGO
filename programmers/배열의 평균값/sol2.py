def solution(numbers):
    answer = 0

    total = 0
    i = 0

    for number in numbers:
        total = total + number
        i = i + 1
    
    print(total, i)

    answer = total / i

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))