from collections import deque

def solution(queue1, queue2):
    answer = -2
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
            change_1 = queue1
            change_2 = queue2
            total_change_1 = sum(change_1)
            total_change_2 = sum(change_2)
            while total_change_1 != total_change_2:
                if total_change_1 > total_change_2:
                    total_change_1 -= change_1[0]
                    change_2.append(change_1.popleft())
                    total_change_2 += change_2[-1]
                elif total_change_2 > total_change_1:
                    total_change_2 -= change_2[0]
                    change_1.append(change_2.popleft())
                    total_change_1 += change_1[-1]
                cnt += 1
                if cnt > (len(queue1) + len(queue2)) * 2:
                    possible = False
                    answer = -1
                    break
            print(cnt)
            if possible:
                answer = cnt
    
    return answer