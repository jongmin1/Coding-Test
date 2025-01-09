'''
시도 횟수 : 3
참고 여부 : O
마지막 return -1 해주는 부분 >= 이걸로 했었음. 바본가..? 
인덱스로 값 출력하는 거 아닌데 왜 저렇게 생각했지.. 앞으로 
'''
from itertools import combinations

def solve(N):
    nums = [0,1,2,3,4,5,6,7,8,9]
    result = []
    
    for i in range(1, 11):
        for comb in combinations(nums, i):
            comb = sorted(comb, reverse=True)
            num = int(''.join(map(str, comb)))
            result.append(num)
    
    result.sort()
    
    if N > len(result):
        return -1
    return result[N-1]

N = int(input())
print(solve(N))
