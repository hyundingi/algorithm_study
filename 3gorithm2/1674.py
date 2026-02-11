import sys
sys.stdin = open('input.txt')

items = []
for line in sys.stdin:
    parts = line.split()

    if not parts:
        continue

    cmd = parts[0]
    time = float(parts[1])

    if cmd == 'Query':
        items.append((time, cmd))
    else:
        items.append((time, cmd, float(parts[2])))

items.sort()

# 순회하며 query를 만날 때마다 이전 기록 계산
history = []

for item in items:
    cmd = item[1]
    time = item[0]

    if cmd == 'Query':
        total_r = 0
        q_time = time

        # 현재 query 시간까지 발생한 모든 아이템 계산
        for h_time, h_cmd, h_val in history:
            t_delta = q_time - h_time
            r = 0.0

            if h_cmd == 'Chocolate':
                r = 8 * h_val - (t_delta / 12)
            elif h_cmd == 'Coffee':
                r = 2 * h_val - (t_delta ** 2 / 79)

            if r > 0:
                total_r += r

        # 최종 안전 거리는 (반경 합)과 1.0 중 큰 값
        ans = max(1.0, total_r)
        print(f'{int(time)} {ans:.1f}')
    else:
        history.append((time, cmd, float(item[2])))


