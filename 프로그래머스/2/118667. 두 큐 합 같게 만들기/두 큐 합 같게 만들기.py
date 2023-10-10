from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    # 시간초과 발생해서 deque 사용
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    total = (sum(queue1) + sum(queue2))
    
    # 홀수면 목표 달성 불가
    if total % 2 == 1:
        answer = -1
    
    # total 보다 큰 원소가 있으면 목표 달성 불가
    else:
        # 만들어야 하는 합
        total //= 2
        for i in range(len(queue1)):
            if queue1[i] > total or queue2[i] > total:
                answer = -1
                break

        # 그게 아니면, 더 큰 곳에서 빼고 더 작은 곳에 넣어주기
        else:
            possible = True
            cnt = 0
            total_1 = sum(queue1)
            total_2 = sum(queue2)
            
            # 두 큐의 합이 같아질 때까지 반복
            while total_1 != total_2:
                
                if total_1 > total_2:
                    # 시간초과 때문에 각 큐의 합에서 빼주고 더해줌
                    total_1 -= queue1[0]
                    queue2.append(queue1.popleft())
                    total_2 += queue2[-1]
                    
                elif total_2 > total_1:
                    total_2 -= queue2[0]
                    queue1.append(queue2.popleft())
                    total_1 += queue1[-1]
                
                # 이 과정이 실행될 때마다 카운트
                cnt += 1
                
                # 두 큐에서 모두 원소가 바뀌어본 경우에도 안되면,
                if cnt > (len(queue1) + len(queue2)) * 2:
                    possible = False
                    answer = -1
                    break

            if possible:
                answer = cnt
    
    return answer