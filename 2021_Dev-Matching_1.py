def solution(lottos, win_nums):
    #1등 로또 번호를 내 로또 번호와 비교하여 일치되는 경우를 확인,
    #1등 로또 번호와 겹치는 로또 번호 제거한 리스트 => 일치하지 않는 애들만 있음
    #가장 높은 등수를 만들 수 있는 경우
    #일치되지 않은 로또 번호 중 0인 애들은 1등 로또 번호의 남은 번호들로 대입
    #대입 후 1등 로또 번호와 내 로또 번호를 비교하여 몇 개가 일치되는 지 확인하고 등수 반환
    lottos_new = len([x for x in lottos if x in win_nums])
    zero_cnt = lottos.count(0)
    
     #가장 낮은 등수를 만들 수 있는 경우
    best = min(6, 7 - (lottos_new + zero_cnt))
    worst = min(6, 7 - lottos_new)
    
    return [best, worst]
    

if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]

    # solution 함수 호출
    result = solution(lottos, win_nums)

    # 결과 출력
    print(result)