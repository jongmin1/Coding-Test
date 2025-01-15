from itertools import permutations

n = int(input()) 
k = int(input())
cards = [input().strip() for _ in range(n)]  

perms = permutations(cards, k)

numbers = set()

for perm in perms:
    number = ''.join(perm)
    numbers.add(number)

print(len(numbers))
