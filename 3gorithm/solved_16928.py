from collections import deque
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
board = [0] * 101

# 사다리 정보 저장
for n in range(N):
    start, end = map(int, input().split())
    board[start] = end

# 뱀 정보 저장
for m in range(M):
    start, end = map(int, input().split())
    board[start] = end

    
def bfs():
    q = deque()
    q.append((1,0))
    visited = [0] * 101
    visited[1] = 1

    while q:
        now, cnt = q.popleft()

        # 가장 먼저 100에 도달하는 것의 cnt 리턴
        if now >= 100:
            return cnt
        
        # 주사위 돌림
        for dice in range(1, 7):
            # 다음으로 갈 곳
            next_now = now + dice

            # 다음으로 갈 곳이 100이상이면 포함 안 함 
            # 딱 맞게 100 이어야함
            if next_now > 100:
                continue

            # 사다리나 뱀 만나면 다음으로 갈 곳 해당 번호로 변경
            if board[next_now] != 0:
                next_now = board[next_now]
            
            # 방문한 적 없으면 visit 체크 하고 q에 추가
            if visited[next_now] == 0:
                visited[next_now] = 1
                q.append((next_now, cnt + 1))
            
            print(q)

print(bfs())
# ------------------------------------------
# import sys
# sys.stdin = open("input.txt")

# N, M = map(int, input().split())
# board = [0] * 101

# # 사다리 정보 저장
# for n in range(N):
#     start, end = map(int, input().split())
#     board[start] = end

# # 뱀 정보 저장
# for m in range(M):
#     start, end = map(int, input().split())
#     board[start] = end


# def bfs(start):
#     while now <= 100:
#         max_move = 6
#         for i in range(6, 0, -1):
#             # 백이 넘으면 그냥 끝
#             if now + i >= 100:
#                 break

#             # 사다리 혹은 뱀이 없거나 , 뱀을 만났을 때
#             if board[now+i] == 0 or now+i > board[now+i]:
#                 continue

#             # 가장 멀리 가는 사다리 정보 저장
#             if board[now+i] > max_move:
#                 max_move = board[now+i]

#         # 사디라가 없으면 6 이동, 사다리가 있으면 사다리만큼 이동
#         if max_move > 6:
#             now = max_move
#         else:
#             now += max_move

#         count += 1

# -----------------------------
# import sys
# sys.stdin = open("input.txt")

# N, M = map(int, input().split())
# board = [0] * 101

# # 사다리 정보 저장
# for n in range(N):
#     start, end = map(int, input().split())
#     board[end] = start

# # 뱀 정보 저장
# for m in range(M):
#     start, end = map(int, input().split())
#     board[start] = -1

# # 거꾸로 가자
# now, count, dice = 99, 0, 0
# while now > 1:

#     now -= 1
#     count += 1

#     # 일단 6만큼 감
#     if count == 6:
#         dice += 1
#         count = 0

#     # 6만큼 왔는데 사다리 혹은 뱀을 만날 경우 처리
#     if count == 0:
#         if board[now] > 0:
#             now = board[now]
#             continue
#         elif board[now] != 0 and board[now] < now:
#             now += 1
#             continue

#     # 6가기 전에 사다리 만났을 경우
#     if board[now] > 0:
#         now = board[now]
#         count = 1
#         dice += 1



# print(dice)























