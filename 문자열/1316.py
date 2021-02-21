n = int(input())
g_cnt = 0
# 마지막꺼 words에 추가
# j번째 글자가 words에 존재하고,words에 존재하면 
# 추가 안하고 넘기기
# 없으면 추가
for i in range(n):
    buff = input()
    words = []
    words.append(buff[0])
    g_cnt += 1
    for j in range(len(buff)):
        if buff[j] != words[-1]:
            if len(buff) != 1 and buff[j] in words:
                g_cnt -= 1
                break
            words.append(buff[j])         
print(g_cnt)

