# source : https://www.acmicpc.net/problem/13305

# 초기 자동차에 기름을 주유해야함
# 기름통의 크기는 무제한
# 이동시 1Km마다 1리터의 기름을 사용
# 각 도시마다 주유소가 하나씩 존재
# N = 도시의 갯수
import sys

N = int(sys.stdin.readline().strip()) # 도시의 수
city_dis = list(map(int, sys.stdin.readline().strip().split()))
gas_cost = list(map(int, sys.stdin.readline().strip().split()))

answer = 0
min_cost = 1000000001
for i in range(0, len(gas_cost)):
    if min_cost > gas_cost[i]:
        min_cost = gas_cost[i]
    
    if i < len(city_dis):
        answer += min_cost * city_dis[i]

print(answer)
