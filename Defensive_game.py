def solution(n, k, enemy):
    #사용한 무적권의 횟수
    used_k = 0

    for round, enemies in enumerate(enemy):
        #남은 병사가 적보다 많거나 같으면 병사를 소모
        if n >= enemies:
            n -= enemies
        #남은 병사가 적보다 적으면 무적권 사용
        else:
            #무적권을 사용할 수 있는 횟수가 남았는지 확인
            if used_k < k:
                used_k += 1
            #무적권을 사용할 수 없으면 게임 종료
            else:
                return round

    return len(enemy)


if __name__ == "__main__":
    #보유한 병사 수
    n = 7

    #사용 가능한 무적권의 횟수
    k = 3

    #매 라운드 마다 공격해오는 적의 수가 순서대로 담긴 정수 배열
    enemy = [4, 2, 4, 5, 3, 3, 1]
   
    # solution 함수 호출
    result = solution(n, k , enemy)

    # 결과 출력
    print(result)