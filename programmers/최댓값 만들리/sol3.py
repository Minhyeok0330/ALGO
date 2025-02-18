def solution(numbers):
    n =len(numbers)

    for i in range(n):
        for j in range(0, n-i+1):
            print(i, j)