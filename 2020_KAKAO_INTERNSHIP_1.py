def solution(numbers, hand):
    #키패드 설정
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    #맨 청듬 왼손, 오른손 시작 위치
    left, right = '*', '#'
    answer = ''

    for num in numbers:
        #1, 4, 7을 입력할 때 왼손
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        #3, 6, 9를 입력할 때 오른손
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        #2, 5, 8, 0을 입력할 때 더 가까운 손
        else:
            current = keypad[num]
            left_pos = keypad[left]
            right_pos = keypad[right]
            
            #더 가까운 손가락 구하기(절댓값)
            left_dist = abs(current[0] - left_pos[0]) + abs(current[1] - left_pos[1])
            right_dist = abs(current[0] - right_pos[0]) + abs(current[1] - right_pos[1])
            
            #왼손이 더 가까운 경우
            if left_dist < right_dist:
                answer += 'L'
                left = num
            #오른손이 더 가까운 경우
            elif left_dist > right_dist:
                answer += 'R'
                right = num
            #두 손이 동일하게 가까운 경우
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num

    return answer



if __name__ == "__main__":
    #순서대로 누를 번호가 담긴 배열
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]

    #왼손잡이 / 오른손잡이
    hand = "right"

    # solution 함수 호출
    result = solution(numbers, hand)

    # 결과 출력
    print(result)