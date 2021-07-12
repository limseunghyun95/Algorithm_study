# 데이터 수신
data = list(map(int, input().split(" ")))

first = data[0] # 초기값만 저장

for index, item in enumerate(data[1:]):

    # 인덱스가 증가함에 따라 이전 데이터와의 차이로 오름차순, 내림차순 여부를 확인
    if item - first == index + 1:
        answer = "ascending"
    elif item - first == -1 * (index + 1):
        answer = "descending"
    else:
        print("mixed")
        exit(0)

print(answer)