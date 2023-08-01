def solution(k, m, score):
    #점수 높은 순서로 정렬
    score.sort(reverse=True)
    answer = 0

    #상자에 넣을 수 있는 만큼 사과가 남아있는 동안 돌아감
    while len(score) >= m:
        #점수가 가장 높은 사과 m개를 선택
        box = score[:m]
        answer += min(box) * m
        score = score[m:]  # 선택한 사과 제거
    return answer

if __name__ == "__main__":
    #사과의 최대점수
    k = 3

    #한 상자에 들어가는 사과의 수
    m = 4

    score = [1, 2, 3, 1, 2, 3, 1]

    # solution 함수 호출
    result = solution(k, m, score)

    # 결과 출력
    print(result)