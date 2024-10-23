# 느낀점: 생각은 간단하게! 
# 처음에 레이저 개수를 세서 각 괄호 안에 몇개의 레이저가 있는지 확인하고 +1해서
# 잘려진 막대기 개수를 구하려 함. 괄호 안의 괄호를 생각하니 조건과 구현이 까다로워졌다.
# 레이저가 나올 때마다 잘리 막대기 개수 세는 방법이 훨씬 간단함. 

STRING = input().strip()

stack = []
cnt = 0
for i in range(len(STRING)):
    if STRING[i] == "(":
        stack.append("(")
    else:
        if STRING[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)    
    
    
