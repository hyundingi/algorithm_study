T = int(input())

for t in range(T):

    N = int(input())
    # 내 방 입력받기
    myrooms = [list(map(int, input().split())) for _ in range(N)]
    # 출발하는 곳 순으로 정렬
    myrooms.sort(key=lambda x:x[1])
    count = 0

    while myrooms:
        # 복도 사용 리스트
        visited = [0] * 200

        for room in range(len(myrooms)):
            start = myrooms[room][0]
            arrive = myrooms[room][1]

            # 시작하는 게 홀수일 떼 사용 복도
            if start % 2 == 1:
                start //= 2

            # 시작하는게 짝수일때 사용 복도
            else:
                start = start // 2 - 1

            # 끝나는게 홀수일 때 사용 복도
            if arrive % 2 == 1:
                arrive //= 2
            # 끝나는게 짝수일 때 사용 복도
            else:
                arrive = arrive // 2 - 1

            # 도착하는 곳이 더 뒤에 있는 곳
            if start < arrive:
                # 방문한 적 있으면 continue
                if visited[start:arrive+1].count(1):
                    continue
                for i in range(start, arrive+1):
                    visited[i] += 1

            # 출발하는 곳이 더 뒤에 있는 곳
            else:
                if visited[arrive:start+1].count(1):
                    continue
                for i in range(arrive, start+1):
                    visited[i] += 1

            myrooms.pop(room)
            count += 1

    print(f'#{t+1} {count}')


# T = int(input())
#
# for t in range(T):
#
#     N = int(input())
#     # 내 방 입력받기
#     myrooms = [list(map(int, input().split())) for _ in range(N)]
#     # 출발하는 곳 순으로 정렬
#     myrooms.sort(key=lambda x:x[0])
#     # 방문 기록
#     visited = [0] * N
#
#     # 단위 체크
#     count = 1
#     while True:
#         # 출발점 체크
#         # 체크 하면서 home 설정
#         for i in range(N):
#             if visited[i] == 0:
#                 visited[i] = count
#                 arrive = myrooms[i][1]
#                 break
#
#         # 내가 출발할 방과 앞에 있던 애가 돌아갈 방 동선이 겹치는지 확인
#         # arrive - 앞에 애가 들어간 곳
#         for i in range(1, N):
#             # 방문 했던 곳이면 패스
#             if visited[i] != 0:
#                 continue
#
#             # 1. 방문 안 했으면서
#             # 2. 이전에 들어간 방보다 내가 나올 방이 더 앞에 있고
#             # 3. 이전에 들어간 방 - 내가 나올 방 의 차가 1이면서 이전에 들어간 방이 홀수라면 !!!! <- 패스해야함
#             else:
#                 if myrooms[i][0] > arrive:
#                     if myrooms[i][0] - arrive == 1 and arrive % 2 != 0:
#                         continue
#                     visited[i] = count
#                     arrive = myrooms[i][1]
#
#         # 단위 +1
#         count += 1
#
#         print(visited)
#         # 모두 다 돌아갔으면 끝
#         if visited.count(0) == 0:
#             print(f'#{t+1} {max(visited)}')
#             break
