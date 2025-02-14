def solution(numbers):
    max1 = 0
    max2 = 0
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    answer = max1 * max2
    return answer