'''
시도 횟수 : 4
참고 여부 : O
시간 초과 안 뜨게 하려면 조건 하나하나 나눠서 컷해줘야 할듯..
'''

import sys
input = sys.stdin.readline

def get_diff():
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += stats[i][j]
            elif not visited[i] and not visited[j]:
                link += stats[i][j]
    return abs(start - link)

def dfs(depth):
    global ans
    
    if depth == n:
        # 한 팀이라도 1명 이상이어야 함
        if sum(visited) != 0 and sum(visited) != n:
            ans = min(ans, get_diff())
        return
        
    visited[depth] = 1
    dfs(depth + 1)
    visited[depth] = 0
    dfs(depth + 1)

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = int(1e9)

dfs(0)
print(ans)

"""
최적화 버전
n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = int(1e9)

def is_it():
    global ans
    start, link = 0, 0
    for i in range(n-1):  # n-1까지만 반복
        for j in range(i+1, n):  # i+1부터 시작
            if visited[i] and visited[j]:
                start += stats[i][j] + stats[j][i]
            elif not visited[i] and not visited[j]:
                link += stats[i][j] + stats[j][i]
    ans = min(ans, abs(start - link))

def resolve(idx, cnt):
    global ans
    if ans == 0:  # 차이가 0이면 더 이상 진행할 필요 없음
        return
    if idx == n:
        if 0 < cnt < n:  # 한 팀에 모든 선수가 들어가지 않도록
            is_it()
        return
    
    # 절반까지만 체크
    if cnt < n//2:
        visited[idx] = 1
        resolve(idx + 1, cnt + 1)
    visited[idx] = 0
    resolve(idx + 1, cnt)

resolve(0, 0)
print(ans)"""