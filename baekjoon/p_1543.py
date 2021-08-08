# source : https://www.acmicpc.net/problem/1543

doc = input()
word = input()

count = 0
while word in doc:

    doc = doc.replace(word, "★", 1)
    count += 1

print(count)