N = 100

num = int(input())

r = []
for i in range(num):
    r.append(int(input()))

pado = [0, 1, 1, 1]
for i in range(4, N+1):
    pado.append(pado[i-2]+pado[i-3])

for i in r:
    print(pado[i])    