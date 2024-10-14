N = 40

t = int(input())
c = []
for i in range(t):
    c.append(int(input()))

f = [[0, 0] for i in range(N+1)]
f[0][0] = 1
f[1][1] = 1

for i in range(2, N+1):
    f[i][0] = f[i-1][0] + f[i-2][0]
    f[i][1] = f[i-1][1] + f[i-2][1]
    
# print(f)

for i in c:
    print(f'{f[i][0]} {f[i][1]}')
