# source : https://www.acmicpc.net/problem/1439

S = input()


# 0으로 만들어주는 케이스에서 뒤집는 횟수 계산
is_continue = False
zero_cnt = 0
for idx, value in enumerate(S):
    if value == "1":
        if is_continue == False:
            zero_cnt += 1
            is_continue = True

    else:
        is_continue = False

# 1로 만들어주는 케이스에서 뒤집는 횟수 계산
is_continue = False
one_cnt = 0
for idx, value in enumerate(S):
    if value == "0":
        if is_continue == False:
            one_cnt += 1
            is_continue = True
    else:
        is_continue = False

print(min(one_cnt, zero_cnt)) # 최솟값 출력