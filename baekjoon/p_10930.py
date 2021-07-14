import hashlib

S = input()

print(hashlib.sha256(S.encode()).hexdigest()) # 문자열의 바이트 값으로 해쉬값 출력