from collections import deque
def solution(q1, q2):
    result = 0
    q1 = deque(q1)
    q2 = deque(q2)
    
    q1_total = sum(q1)
    q2_total = sum(q2)
    
    if (q1_total + q2_total)&1:
        return -1
    
    limit = len(q1) + len(q2)
    cnt = 0
    while q1_total != q2_total:
        if result >= limit:
            return -1
        while q2 and q1_total < q2_total:
            num = q2.popleft()
            q1.append(num)
            q1_total += num
            q2_total -= num
            result += 1
        while q1 and q1_total > q2_total:
            num = q1.popleft()
            q2.append(num)
            q2_total += num
            q1_total -= num
            result += 1
    return result
