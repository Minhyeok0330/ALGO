def solution(numbers):
    answer = 0
    dict = {
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }
    return ''.join(dict[number] for number in numbers)

project so hard

print(solution('onetwothreefour'))
프로젝트 진행 중 shopping mood