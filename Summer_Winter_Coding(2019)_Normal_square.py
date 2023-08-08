def solution(W, H):
    a, b = W, H
    
    #최대공약수(gcd) 구하기
    while b != 0:
        a, b = b, a % b
    gcd = a
    
    #사용할 수 있는 정사각형의 개수 구하기
    #전체 - 대각선으로 잘린 정사각형의 수
    answer = W * H - (W + H - gcd)
    return answer

if __name__ == "__main__":
    #가로의 길이
    W = 8

    #세로의 길이
    H = 12

    # solution 함수 호출
    result = solution(W, H)

    # 결과 출력
    print(result)