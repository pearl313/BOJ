import sys
input = sys.stdin.readline
'''
- SOD(n): 실질적 약수의 합
- 약수를 일일히 구해서 더하면 -> 시간 초과
- 어떤 수가 n의 약수 == n이 어떤 수의 배수인 것 !
- "1 ~ N까지의 k의 배수의 개수 구하는 방법" 사용할 것
- ex) 6이 주어 지면, 2의 배수가 몇 개 / 3의 배수가 몇 개인지 알아 내면 됨
        6의 약수를 구해 주는 것이 아닌, 소수마다 배수의 개수를 찾아주는 것
'''
n = int(input())
ans = 0
for i in range(2, n):
    ans += (n // i - 1) * i
print(ans % 1000000)