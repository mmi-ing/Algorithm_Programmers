def solution(ingredient):
    hamburger = 0

    remaining = ingredient.copy()
    while True:
        found_pattern = False
        for i in range(len(remaining)):
            if remaining[i] == 1 and i + 3 < len(remaining):
                if (
                    remaining[i + 1] == 2
                    and remaining[i + 2] == 3
                    and remaining[i + 3] == 1
                ):
                    hamburger += 1
                    remaining = remaining[:i] + remaining[i + 4:]
                    found_pattern = True
                    break
        if not found_pattern:
            break

    return hamburger

if __name__ == "__main__":

    ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

    # solution 함수 호출
    result = solution(ingredient)

    # 결과 출력
    print(result)