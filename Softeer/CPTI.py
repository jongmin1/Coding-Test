'''
시도 횟수 : 2
참고 여부 : O
시간 복잡도 줄이는거 몰라서 참고함
'''

import sys
from collections import defaultdict
input = sys.stdin.readline

def binary_to_int(s):
    # 이진 문자열을 정수로 변환
    return int(s, 2)

# 사람 수, CPTI 길이
N, M = map(int, input().strip().split())

# CPTI를 정수로 변환하여 저장
cpti_count = defaultdict(int)
for _ in range(N):
    cpti = binary_to_int(input().strip())
    cpti_count[cpti] += 1

result = 0
# 각 CPTI에 대해
processed = set()  # 이미 처리한 CPTI 쌍을 기록
for cpti in cpti_count:
    # 같은 CPTI를 가진 사람들 중 2명을 선택하는 경우의 수
    count = cpti_count[cpti]
    if count > 1:
        result += (count * (count - 1)) // 2
    
    # 현재 CPTI와 비트가 1~2개 다른 모든 경우 검사
    for i in range(M):
        # 1비트 차이나는 경우
        diff1 = cpti ^ (1 << i)
        if diff1 != cpti and diff1 in cpti_count and (cpti, diff1) not in processed and (diff1, cpti) not in processed:
            result += cpti_count[cpti] * cpti_count[diff1]
            processed.add((cpti, diff1))
        
        # 2비트 차이나는 경우
        for j in range(i + 1, M):
            diff2 = cpti ^ (1 << i) ^ (1 << j)
            if diff2 != cpti and diff2 in cpti_count and (cpti, diff2) not in processed and (diff2, cpti) not in processed:
                result += cpti_count[cpti] * cpti_count[diff2]
                processed.add((cpti, diff2))

print(result)