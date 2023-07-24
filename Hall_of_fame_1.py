import heapq

def solution(k, score):
    #힙 큐 초기화
    heap = []
    #매일 발표된 명예의 전당의 최하위 점수를 담을 리스트
    result = []
    
    for s in score:
        #힙 큐에 원소 추가
        heapq.heappush(heap, s)
        
        #힙 큐의 크기가 k보다 크면, 가장 작은 원소를 제거
        if len(heap) > k:
            heapq.heappop(heap)
            
        #매일 명예의 전당의 최하위 점수를 result에 추가
        result.append(heap[0])
        
    return result


if __name__ == "__main__":
    #명예의 전당
    k = 3

    #점수
    score = [10, 100, 20, 150, 1, 100, 200]

    # solution 함수 호출
    result = solution(k, score)

    # 결과 출력
    print(result)
