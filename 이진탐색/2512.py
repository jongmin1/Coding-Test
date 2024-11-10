# 제대로된 이진탐색 문제를 처음 풀어보는듯...
# 이 문제를 이진탐색으로 풀어야 한다는 것을 알기 위해서는 
# 이렇게 생긴 문제는 이진탐색으로 풀었다는 경험이 필요할 것 같음
 

from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().strip().split()))
budget = int(input())

if sum(requests) - budget < 0:
    print(max(requests))
else:
    start, end = 1, max(requests)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for r in requests:
            if r > mid:
                total += mid
            else:
                total += r
        if total <= budget:  
            start = mid + 1
        else: 
            end = mid - 1

    print(end)
    

'''
from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
budgetList = list(map(int, input().strip().split()))
budget = int(input())

if sum(budgetList) - budget < 0:
    print(max(budgetList))
else:
    budgetList.sort()
    idx = bisect_left(budgetList, budget/len(budgetList))
    divbyLenofBudget = budgetList[idx-1]
    underBudgets = budgetList[:idx]
    overBudgets = budgetList[idx:]
    
    rst = (divbyLenofBudget*len(underBudgets)-sum(underBudgets)) + (budget/len(budgetList) - divbyLenofBudget)*len(budgetList)
   
    print(divbyLenofBudget + int(rst//len(overBudgets)))
    

'''