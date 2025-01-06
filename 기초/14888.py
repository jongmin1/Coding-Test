import sys
input = sys.stdin.readline

def dfs(depth, total, plus, minus, multiply, divide):
    global max_result, min_result
    
    if depth == N:
        max_result = max(total, max_result)
        min_result = min(total, min_result)
        return
        
    if plus:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiply - 1, divide)
    if divide:
        if total < 0:
            dfs(depth + 1, -(-total // numbers[depth]), plus, minus, multiply, divide - 1)
        else:
            dfs(depth + 1, total // numbers[depth], plus, minus, multiply, divide - 1)

N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))

max_result = -1e9
min_result = 1e9

dfs(1, numbers[0], op[0], op[1], op[2], op[3])

print(max_result)
print(min_result)

'''
import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

N = int(input())
operand = deque(list(map(int, input().split())))
operator_input = list(map(int, input().split()))

operator = []
for i in range(4):
    if i == 0:
        for j in range(operator_input[i]):
            operator.append('+')
    elif i == 1:
        for j in range(operator_input[i]):
            operator.append('-')
    elif i == 2:
        for j in range(operator_input[i]):
            operator.append('*')
    else:
        for j in range(operator_input[i]):
            operator.append('//')
            
perms = list(permutations(operator, N-1))

ans_min = float('inf')
ans_max = -1000000000
for perm in perms:
    a = operand[0]
    for i in range(len(perm)):
        b = operand[i+1]
        if perm[i] == '+':
            rst = a + b
        elif perm[i] == '-':
            rst = a - b
        elif perm[i] == '*':
            rst = a * b
        else:
            if a < 0:
                rst = -(-a // b)
            else:
                rst = a // b
        a = rst
    ans_min = min(ans_min, rst)
    ans_max = max(ans_max, rst)
    
print(ans_max)
print(ans_min)
'''