import sys
sys.stdin = open('input.txt')

def recur(start, cnt):
    global max_songs, min_guitars
    if len(path) == cnt:
        current_song = play(path)

        if current_song > max_songs:
            max_songs = current_song
            min_guitars = cnt
        return

    for i in range(start, N):
        path.append(i)
        recur(i+1, cnt)
        path.pop()

def play(list):
    can_play = [False] * M
    for i in range(len(list)):
        for m in range(M):
            if songs[list[i]][m]:
                can_play[m] = True

    return can_play.count(True)

N, M = map(int, input().split())
guitars = []
songs = []

for n in range(N):
    g, s = sys.stdin.readline().split()
    song = [1 if char == 'Y' else 0 for char in s]
    songs.append(song)

path = []
max_songs = -1
min_guitars = -1
# N개의 기타를 선택하는 모든 조합
for n in range(1, N+1):
    recur(0, n)
    if max_songs == M:
        break

if max_songs <= 0:
    print(-1)
else:
    print(min_guitars)



