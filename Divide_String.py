def solution(s):
    x = 1
    not_x = 0
    answer = 0
    i = 0

    while i < len(s)-1:
        first = s[i]
        nextt = s[i+1]
        if first == nextt:
            if x == not_x:
                answer += 1
                i += 1
            else:
                not_x += 1
                x += 1
                i += 1
            continue
        elif first != nextt:
            not_x += 1
            if x == not_x:
                answer += 1
                i += 2
                not_x = 0
            else:
                i += 1
            if i == len(s) - 1:
                answer += 1

    return answer

if __name__ == "__main__":

    s = "aaabbaccccabba"

    # solution 함수 호출
    result = solution(s)

    # 결과 출력
    print(result)