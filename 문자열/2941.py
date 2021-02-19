all = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
buff = input()
count = 0
for i in all:
    if i in buff:
        buff = buff.replace(i, '1')

print(len(buff))
