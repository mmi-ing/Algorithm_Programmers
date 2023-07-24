def solution(s):
    number_change = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for word, number in number_change.items():
        s = s.replace(word, number)

    return int(s)


if __name__ == "__main__":
    #문자열
    s = "one4seveneight"

    # solution 함수 호출
    result = solution(s)

    # 결과 출력
    print(result)