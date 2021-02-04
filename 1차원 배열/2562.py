l = []

for i in range(9):
    l.append(int(input()))

m = max(l)
print('{}\n{}'.format(m, l.index(m)+1))
