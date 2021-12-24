# source : https://www.acmicpc.net/problem/11399

N = int(input())

data = list(map(int, input().split(" ")))
    
# bubble sort
for i in range(len(data) - 1):
    swap = False
    for j in range(len(data) - i - 1):
        if data[j] > data[j+1]:
            temp = data[j+1]
            data[j+1] = data[j]
            data[j] = temp
            swap = True   
            
    if swap == False:
        break

answer = 0
for i in range(1, len(data)+1):
    answer += sum(data[:i])
    
print(answer)