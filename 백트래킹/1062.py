'''
시도 횟수 : 3
참고 여부 : O
시간 초과 떠서 참고함
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = []
base = {'a', 'n', 't', 'i', 'c'}

# 단어들에서 anta, tica를 제외하고 필요한 알파벳만 저장
candidates = set()  # 배워야 할 후보 알파벳들
for _ in range(N):
    word = set(input().rstrip()) - base  # 기본 글자 제외한 새로운 글자들
    words.append(word)
    candidates.update(word)

def count_readable_words(learned):
    count = 0
    for word in words:
        if word <= learned:  # word의 모든 알파벳이 learned에 포함되어 있는지
            count += 1
    return count

def dfs(idx, learned):
    if len(learned) == K:
        return count_readable_words(learned)
    
    if idx >= len(candidates):
        return 0
    
    candidates_list = list(candidates)
    result = 0
    
    # 현재 알파벳을 배우는 경우
    learned.add(candidates_list[idx])
    result = max(result, dfs(idx + 1, learned))
    learned.remove(candidates_list[idx])
    
    # 현재 알파벳을 건너뛰는 경우
    result = max(result, dfs(idx + 1, learned))
    
    return result

if K < 5:
    print(0)
else:
    learned = base.copy()  # 기본 글자들은 미리 학습
    K = min(K, len(candidates) + 5)  # 배울 수 있는 전체 글자 수를 넘지 않도록
    print(dfs(0, learned))


'''import sys
input = sys.stdin.readline

N, K = map(int, input().split())
string = [list(input().strip()) for _ in range(N)]
base = set(['a', 'n', 't', 'i', 'c'])
extra = set()
for s in string:
    extra.update(set(s) - base)

# 각각 string - base 해서 남은 알파벳 모아두고, 거기서 하나씩 추가 해보기/
# 그 알파벳 공통 아니어도 K-5한 것만큼 뽑아서 가장 많이 읽을 수 있나
# 그냥 모든 string - base 한 알파벳으로 set
def countReadable(l):
    cnt = 0
    l = set(l)
    l.update(base)
    for i in range(N):
        rst = set(string[i]) - l
        if len(rst) == 0:
            cnt += 1
    return cnt
    
def dfs():
    global max_cnt
    if len(path) == K-5:
        # 몇개 읽을 수 있는지 확인
        cnt = countReadable(path)
        max_cnt = max(max_cnt, cnt)
        return 
        
    for i in extra:
        if i not in path:
            path.append(i)
            dfs()
            path.pop()
    
if K < 5:
    print(0)
else:
    path = []
    max_cnt = 0
    dfs()
    print(max_cnt)'''
