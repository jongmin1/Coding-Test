from collections import deque
import sys
input = sys.stdin.readline

'''
N: 웹페이지 종류의 수 (cache의 개수)
Q: 수행하는 작업의 개수
C: cache 최대 값
CAP: 해당 페이지가 차지하는 메모리 양
'''
N, Q, C= map(int, input().strip().split())
CAP = list(map(int, input().strip().split()))

forw = deque()
backw = deque()

first = 1
present = 0
command = []
cache = 0
for i in range(Q):
    command.append(input().strip().split())

    # 뒤로 가기를 실행할 경우
    if command[i][0] == 'B':
        # 뒤로 가기 공간에 1개 이상의 페이지가 저장되어 있을 때만 2,3번 과정이 실행된다. 0개일 때 이 작업은 무시된다.
        if backw:
            # 현재 보고 있던 웹페이지를 앞으로 가기 공간에 저장한다.
            forw.appendleft(present)
             # 뒤로 가기 공간에서 방문한지 가장 최근의 페이지에 접속한다. 그리고 해당 페이지는 뒤로 가기 공간에서 삭제된다.
            present = backw.pop()
             

    # 앞으로 가기를 실행할 경우
    if command[i][0] == 'F':
        # 앞으로 가기 공간에 1개 이상의 페이지가 저장되어 있을 때만 2,3번 과정이 실행된다. 0개일 때 이 작업은 무시된다.
        if forw:
            # 현재 보고 있던 페이지를 뒤로 가기 공간에 저장한다.
            backw.append(present)
            # 앞으로 가기 공간에서 방문한지 가장 최근의 페이지에 접속한다. 그리고 해당 페이지는 앞으로 가기 공간에서 삭제된다.     
            present = forw.popleft()   
        

    # 웹 페이지에 접속할 경우 
    if command[i][0] == 'A':
        # 앞으로 가기 공간에 저장된 페이지가 모두 삭제된다. 페이지들이 차지하고 있던 크기만큼 현재 사용 캐시에서 줄어든다.
        while forw:
            t = forw.pop()
            cache -= CAP[t - 1]
        # 현재 페이지를 뒤로 가기 공간에 추가하고, 다음에 접속할 페이지가 현재 페이지로 갱신된다. 단, 처음으로 웹페이지에 접속하는 경우라면, 현재 페이지를 뒤로 가기 공간에 추가하지 않는다.
        if first == 1:
            first = 0
            present = int(command[i][1])
            cache += CAP[present - 1]
            continue
        backw.append(present)
        present = int(command[i][1])
        cache += CAP[present - 1]
        # 3번 과정은 2번 과정에서 최대 캐시 용량을 초과할 경우에만 실행된다. 뒤로 가기 공간에서 방문한 지 가장 오래된 페이지 하나를 삭제하며, 그 페이지가 차지하고 있던 크기가 현재 사용 캐시 용량에서 줄어든다.
        while cache > C:
            t = backw.popleft()
            cache -= CAP[t -1]
        
    # 압축을 실행할 경우
    if command[i][0] == 'C':
    # 뒤로 가기 공간에서 같은 번호의 페이지가 연속해서 2개 이상 등장할 경우, 가장 최근의 페이지 하나만 남기고 나머지는 모두 삭제한다.
    # 삭제된 페이지가 차지하고 있던 용량만큼 현재 사용 캐시에서 줄어든다.
        temp = []
        while backw:
            t = backw.pop()
            temp.append(t)
        while temp:
            t = temp.pop()
            if len(temp) == 0:
                backw.append(t)
                break
            if t == temp[-1]:
                cache -= CAP[t - 1]
                continue
            backw.append(t)
                    
print(present)

if len(backw) == 0:
    print(-1)
else:
    while backw:
        print(backw.pop(), end=" ")
print()

if len(forw) == 0:
    print(-1)
else: 
    while forw:
        print(forw.popleft(), end=" ")