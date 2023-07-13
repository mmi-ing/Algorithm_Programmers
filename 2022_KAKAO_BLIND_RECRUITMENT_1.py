def solution(id_list, report, k):
    #중복제거
    report = list(set(report))
    
    #유저ID: 신고한ID 딕셔너리 생성
    id_dict = {}
    
    for i in id_list:
        id_dict[i] = []
    
    bad_id_list=[]
    for i in report:
        user_id, bad_id = i.split()
        bad_id_list.append(bad_id)
        if user_id in id_dict:
            id_dict[user_id].append(bad_id)
    
    #k개 이상인 id 찾기 (정지된 ID 찾기)
    real_bad_id = []
    for i in bad_id_list:
        if bad_id_list.count(i) >= k and i not in real_bad_id:
            real_bad_id.append(i)
            
    #유저가 신고한 ID 중 정지된 ID의 개수를 파악하기
    answer = []
    for user_id, bad_ids in id_dict.items():
        cnt = 0
        for bad_id in bad_ids:
            if bad_id in real_bad_id:
                cnt += 1
        answer.append(cnt)
    
    return answer

if __name__ == "__main__":
    # 사용자 id_list
    id_list = ["muzi", "frodo", "apeach", "neo"]

    # 사용자가 신고한 목록
    report =  ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]

    # 신고 기준 횟수
    k = 2

    # solution 함수 호출
    result = solution(id_list, report, k)

    # 결과 출력
    print(result)