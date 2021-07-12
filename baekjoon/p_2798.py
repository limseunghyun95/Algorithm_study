# 카드 갯수와 총합 수신
n, m = map(int, input().split(" "))
# 카드 리스트 수신
cards = list(map(int, input().split(" ")))

sum_max = -1

for i in range(0, len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            _sum = cards[i] + cards[j] + cards[k]
            if _sum > sum_max and _sum <= m:
                sum_max = _sum

print(sum_max)