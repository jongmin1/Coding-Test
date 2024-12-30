'''
시도 횟수 : 1
참고 여부 : X
'''

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

all = range(N)

diff = 1e9
for comb in combinations(range(N), N//2):
    team1 = comb
    team2 = [i for i in all if i not in comb]
    
    score1 = sum([S[a][b]+S[b][a] for a, b in combinations(team1, 2)])
    score2 = sum([S[a][b]+S[b][a] for a, b in combinations(team2, 2)])
    
    diff = min(diff, abs(score1-score2))

print(diff)
