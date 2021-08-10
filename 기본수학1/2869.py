import math

arg = input()
arg = list(map(int, arg.split()))

A = arg[0]
B = arg[1]
V = arg[2]

t = math.ceil((V-B)/(A-B))

print(t)