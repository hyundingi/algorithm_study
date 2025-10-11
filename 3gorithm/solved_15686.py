import sys
sys.stdin = open('input.txt')

# 도시의 치킨거리는 모든 집의 치킨 거리의 합이다.
# 0 - 빈칸 / 1 - 집 / 2 - 치킨집

def recur(start):
    if len(path) == M:
        print(path)
        return chicken_length(path)
    
    for i in range(start, len(chicken)):
        
        path.append(chicken[i])
        recur(i + 1)
        path.pop()
    
def chicken_length(list):
    global result
    total = 0
    for i in range(len(house)):
        if total > result:
            return 
        length = 2 * N
        y, x = house[i]

        for m in range(M):
            my, mx = list[m]
            length = min(length, abs(y - my) + abs(x - mx))

        total += length
    
    result = min(total, result)
    # print(list, result)

        

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
house, chicken = [], []
path = []
result = (2 * N) ** 2

for y in range(N):
    for x in range(N):
        # 집 위치 구하기
        if city[y][x] == 1:
            house.append((y, x))
        
        # 치킨집 위치 구하기
        elif city[y][x] == 2:
            chicken.append((y, x))

# M 개의 치킨집 경우의 수를 구함
recur(0)
print(result)