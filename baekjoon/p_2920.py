data = list(map(int, input().split(" ")))

first = data[0]

for index, item in enumerate(data[1:]):

    if item - first == index + 1:
        answer = "ascending"
    elif item - first == -1 * (index + 1):
        answer = "descending"
    else:
        print("mixed")
        exit(0)

print(answer)
