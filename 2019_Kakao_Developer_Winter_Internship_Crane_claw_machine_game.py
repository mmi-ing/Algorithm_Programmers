def solution(board, moves):
    #바구니를 담을 리스트
    basket = []
    #터트려져 사라진 인형의 개수
    answer = 0   

    for i in moves:
        for line in board:
            #인형이 있는 칸인 경우 (없는 경우 아무일도 일어나지 않음)
            if line[i - 1] > 0:   
                #바구니의 마지막 인형과 같은 경우
                if basket and basket[-1] == line[i - 1]: 
                    #바구니에서 마지막 인형 제거하고 인형 두 개 사라짐
                    basket.pop()  
                    answer += 2
                else:
                    #바구니에 인형 추가
                    basket.append(line[i - 1])  
                #board에서 인형 제거
                line[i - 1] = 0  
                break

    return answer

if __name__ == "__main__":
    #게임 화면의 격자의 상태가 담긴 2차원 배열
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]

    #인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열
    moves = [1, 5, 3, 5, 1, 2, 1, 4]

    # solution 함수 호출
    result = solution(board, moves)

    # 결과 출력
    print(result)