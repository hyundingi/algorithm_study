import sys

text = sys.stdin.readline()
a_cnt = text.count('a')

if len(text) == a_cnt and a_cnt == 0:
    print(0)
    sys.exit()

extended_text = text + text
min_swaps = float('inf')

# text에서 a_cnt 길이 만큼의 구간을 확인
for i in range(len(text)):
    # 'a_cnt'만큼의 길이를 가진 구간 내의 'b' 개수 확인
    # 이 'b'들이 밖으로 나가야 'a'들로 꽉 차게 됨
    current_b_cnt = extended_text[i : i + a_cnt].count('b')
    min_swaps = min(min_swaps, current_b_cnt)

print(min_swaps)
