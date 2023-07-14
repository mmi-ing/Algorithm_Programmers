import math

def solution(number, limit, power):
    #기사단의 약수의 개수를 저장할 리스트 생성
    divisors_counts = []
    
    #number 범위의 각 수에 대해 약수의 개수를 구하고 리스트에 저장
    for n in range(1, number + 1):
        count = 0
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                count += 2 if i != n // i else 1
        divisors_counts.append(count)

    #리스트에서 limit를 초과하는 값을 찾아 power로 교체
    for i in range(len(divisors_counts)):
        if divisors_counts[i] > limit:
            divisors_counts[i] = power

    # 리스트의 모든 값을 합해 필요한 철의 무게를 구한다.
    answer = sum(divisors_counts)

    return answer


if __name__ == "__main__":
    #기사단원의 수
    number = 5

    #공격력의 제한수치 
    limit = 3

    #제한수치를 초과한 기사가 사용할 무기의 공격력
    power = 2

    # solution 함수 호출
    result = solution(number, limit, power)

    # 결과 출력
    print(result)