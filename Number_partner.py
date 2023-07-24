# from collections import Counter 사용
from collections import Counter

def solution(X, Y):
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    common = set(count_X.keys()) & set(count_Y.keys())
    if not common or common == {'0'}:
        return "-1" if not common else "0"
    
    num = []
    for i in common:
        num.extend([i] * min(count_X[i], count_Y[i]))

    result = ''.join(sorted(num, reverse=True))

    return result

# def solution(X, Y):
#     #각 숫자의 개수를 저장할 딕셔너리
#     count_X = {str(i): X.count(str(i)) for i in range(10)}
#     count_Y = {str(i): Y.count(str(i)) for i in range(10)}

#     #공통으로 나온 숫자를 찾음
#     common = set(count_X.keys()) & set(count_Y.keys())
#     if not common or common == {'0'}:
#         return "-1" if not common else "0"

#     #각 숫자에서 공통 숫자의 등장 횟수를 최소 등장 횟수만큼 num 리스트에 추가
#     num = []
#     for i in common:
#         num.extend([i] * min(count_X[i], count_Y[i]))

#     #num 리스트를 내림차순으로 정렬하여 결과를 만듦
#     result = ''.join(sorted(num, reverse=True))

#     return result

if __name__ == "__main__":
    #X 문자열
    X = "100"

    #Y 문자열
    Y = "2345"

    # solution 함수 호출
    result = solution(X, Y)

    # 결과 출력
    print(result)