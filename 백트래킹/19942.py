import sys
input = sys.stdin.readline

N = int(input())
mp, mf, ms, mv = map(int, input().split())  
ingredients = []
for _ in range(N):
    p, f, s, v, c = map(int, input().split())
    ingredients.append((p, f, s, v, c))

# (비용, path)
answer = []  

def is_valid(path):
    p = f = s = v = cost = 0
    
    for i in path:
        p += ingredients[i][0]
        f += ingredients[i][1]
        s += ingredients[i][2]
        v += ingredients[i][3]
        cost += ingredients[i][4]
        
    if p >= mp and f >= mf and s >= ms and v >= mv:
        return cost
    return -1

# idx 순회하면서 되는거 찾기
def dfs(idx, path):
    if idx > N:
        return
    
    cost = is_valid(path)    
    if cost > 0:
        answer.append((cost, path[:]))
        return
    
    for i in range(idx, N):
        if i not in path:
            path.append(i)
            dfs(i+1, path)
            path.pop()    
    return

dfs(0, [])

if answer:
    answer.sort(key=lambda x:[x[0], x[1]])
    ans = min(answer)
    print(ans[0])
    for i in ans[1]:
        print(i+1, end=" ")
else:
    print(-1)