import sys

# 1. 로컬에서 테스트할 때만 이 줄의 주석을 해제하세요.
# 2. 백준에 제출할 때는 이 줄을 반드시 지우거나 주석 처리해야 합니다.
sys.stdin = open('input.txt')

item = []
for line in sys.stdin:
    parts = line.split()

    if not parts:
        continue

    cmd = parts[0]

    if cmd == 'Chocolate':
        item.append((float(parts[1]), cmd, float(parts[2])))
    elif cmd == 'Coffee':
        item.append((float(parts[1]), cmd, float(parts[2])))
    elif cmd == 'Query':
        item.append((float(parts[1]), cmd))

item.sort(key=lambda x: x[0])


total_r = 0.0

for time, type, n in item:
    if type == 'Query':

        if time > q_time:
            continue

    t = q_time - time
    if type == 'Choco':
        r = 8 * n - (t / 12)
    else:
        r = 2 * n - (t**2 / 79)

    if r > 0:
        total_r += r

# 최종 안전 거리는 (반경 합)과 1.0 중 큰 값
ans = max(1.0, total_r)

# q_time도 :.1f를 붙여주는 것이 예제 출력 형식과 일치합니다.
print(f'{int(q_time)} {ans:.1f}')

