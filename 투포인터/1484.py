'''
시도 횟수 : 1
참고 여부 : O
투포인터랑 이분탐색이랑 확실하게 비교하여 알아두자
투포인터 -> 두 개의 포인터를 사용하여 배열이나 수열을 탐색하며 조건을 만족하는 부분을 찾기 위해 사용 O(n)
이분탐색 -> 정렬된 배열에서 특정 값을 빠르게 찾기 위해 사용 O(log n)
'''

import sys
input = sys.stdin.readline

def find_weights(G):
    left = 1
    right = 2
    results = []

    while right > left:
        diff = right**2 - left**2
        if diff == G:
            results.append(right)
            right += 1
        elif diff < G:
            right += 1
        else:
            left += 1

    return results

G = int(input())
results = find_weights(G)

if results:
    for weight in results:
        print(weight)
else:
    print(-1)