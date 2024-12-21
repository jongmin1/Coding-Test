n1 = [1, 2, 3, 4, 5]
n2 = [2, 1, 2, 3, 2, 4, 2, 5]
n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    cnt = [0, 0, 0]
    lenN1 = len(n1)
    lenN2 = len(n2)
    lenN3 = len(n3)
    for i in range(len(answers)):
        if n1[i%lenN1] == answers[i]:
            cnt[0] += 1
        if n2[i%lenN2] == answers[i]:
            cnt[1] += 1
        if n3[i%lenN3] == answers[i]:
            cnt[2] += 1

    maxCnt = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == maxCnt:
            answer.append(i+1)
    answer.sort()
    return answer