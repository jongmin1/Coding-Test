'''
시도 횟수 : 1
참고 여부 : O
처음 푸는 비트마스킹 문제
'''
import sys
input = sys.stdin.readline

A = int(input().strip(), 2)
B = int(input().strip(), 2)

n = 100000
mask = 2**n -1

print(bin(A & B)[2:].zfill(n))
print(bin(A | B)[2:].zfill(n))
print(bin(A ^ B)[2:].zfill(n))
print(bin(A ^ mask)[2:].zfill(n))
print(bin(B ^ mask)[2:].zfill(n))