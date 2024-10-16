# 1 -> 1
# 2 -> 1 + 1 
# 3 -> 2 + 1, 3 

num = 1234
t = []
while num>0:
    num, rem = divmod(num, 10)
    t.append(rem)
    
t.reverse()

print(t)
