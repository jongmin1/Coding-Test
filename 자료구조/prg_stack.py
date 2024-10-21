# 뒤에 있는 큰 수 구하기
# 느낀점: 자료구조 부족하므로 관련 문제 풀면서 문제 바라보는 시각 넓히기

def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []

    for i in range(len(numbers)):  
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer