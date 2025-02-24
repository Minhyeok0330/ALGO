def solution(hp):
    
    general = hp // 5
    soldier = hp % 5 // 3
    normal = hp % 5 % 3
    answer = general + soldier + normal
    return answer
print(solution(23))

#그러나 5공 개미를 안 쓰고 3공 개미로 해결 보는게 더 나은 경우도 있음. 
#hp가 소수인 경우 총합이 min을 만들 수 있는 최적화 필요