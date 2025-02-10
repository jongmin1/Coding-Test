'''
시도 횟수 : 3
참고 여부 : 세모
> if ans == float('inf') 이거 빼먹음
> 배열 1부터 시작하게 바꿨는데 right < N에서 right <= N 으로 안 바꿔줌 
문제 다 풀고 조건 다시 한 번 확인하는 습관 갖기
'''
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열 생성
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]

left = 0
right = 1
ans = float('inf')

while right <= N:
    current_sum = prefix_sum[right] - prefix_sum[left]
    if current_sum >= S:
        ans = min(ans, right - left)
        left += 1
    else:
        right += 1

print(0 if ans == float('inf') else ans)


'''
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr= list(map(int, input().split()))

sumArr = [0] + arr[:]
for i in range(1, N+1):
    sumArr[i] = sumArr[i] + sumArr[i-1]

left = 1
right = 1
ans = float('inf')
while right <= N:
    diff = sumArr[right] - sumArr[left-1]
    if diff >= S:
        length = right - left + 1
        ans = min(ans, length)
        left += 1
    else:
        right += 1
        
if ans == float('inf'):
    print(0)
else:
    print(ans)
'''