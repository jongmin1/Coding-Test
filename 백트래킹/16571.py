'''
시도 횟수 : 
참고 여부 : O
게임이론 처음 알게 된...
'''

def is_win(now, map_data):
    # 가로 확인
    for i in range(3):
        if map_data[i][0] == now and map_data[i][0] == map_data[i][1] and map_data[i][1] == map_data[i][2]:
            return True
    
    # 세로 확인
    for j in range(3):
        if map_data[0][j] == now and map_data[0][j] == map_data[1][j] and map_data[1][j] == map_data[2][j]:
            return True
    
    # 대각선 확인
    if map_data[0][0] == now and map_data[0][0] == map_data[1][1] and map_data[1][1] == map_data[2][2]:
        return True
    if map_data[0][2] == now and map_data[0][2] == map_data[1][1] and map_data[1][1] == map_data[2][0]:
        return True
    
    return False

def game(now, map_data):
    min_val = 2  # 상대방의 최선의 승패를 저장
    
    for i in range(3):
        for j in range(3):
            if map_data[i][j] == 0:  # 놓을 수 있는 위치
                map_data[i][j] = now  # 여기에 now가 놓는다
                
                # (i,j)에 놓을 때 내가 이길 수 있는 경우라면 상대방은 지므로 -1
                if is_win(now, map_data):
                    min_val = min(min_val, -1)
                
                # 다음 차례를 재귀로 호출후 그 결과를 min에 저장
                min_val = min(min_val, game(2 if now == 1 else 1, map_data))
                
                # 내가 (i, j)에 놓지 않는 경우
                map_data[i][j] = 0
    
    # min은 상대방의 승패를 저장한 것이므로 나의 승패는 반대로 리턴해줘야 함
    if min_val == 1:
        return -1
    elif min_val == 0 or min_val == 2:
        return 0
    else:
        return 1

# 입력 처리
map_data = []
zero = 0  # 맵에서 0개수 카운트

for _ in range(3):
    row = list(map(int, input().split()))
    map_data.append(row)
    zero += row.count(0)

# 0이 홀수면 1, 짝수면 2부터 시작
win = game(1 if zero % 2 != 0 else 2, map_data)

# 결과 출력
if win == 1:
    print('W')
elif win == 0:
    print('D')
else:
    print('L')
