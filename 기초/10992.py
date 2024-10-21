N = int(input())

for i in range(1, N):
    
    print(" "*(N-i), end="")
    print('*', end="")
    if i == 1:
        print()
        continue
    print(" "*(2*(i-1)-1), end="")
    print("*")

print("*"*(2*N-1))