def solution(rsp):
    answer = {  # ✅ 들여쓰기 수정
        '2': '0',
        '5': '2',
        '0': '5'
    }
    
    result = []  # ✅ 들여쓰기 수정
    for i in rsp:
        result.append(answer[i])  # ✅ 리스트에 추가

    return ''.join(result)  # ✅ 문자열로 변환하여 반환

print(solution('250'))