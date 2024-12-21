from collections import deque
MAX = 100001

N, K = map(int, input().split())

visited = [-1] * MAX

def bfs(start):
    queue = deque([start])
    visited[start] = 0 

    while queue:
        current = queue.popleft()

        if current == K:
            return visited[current]

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1  
                queue.append(next_pos)

print(bfs(N))