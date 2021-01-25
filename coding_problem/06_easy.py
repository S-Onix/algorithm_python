# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 대문자와 소문자, 그리고 숫자로만 이루어져 있으며, 길이는 최대 50이다.

# 문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.

# 문제 풀이법 : SHA-256 algorithm 사용 
# 알아야할 내용 : SHA256 해시값을 구하는 방법 및 사용 라이브러리 
# 

import hashlib
S = input()
encoded_data = hashlib.sha256(S.encode())
print(encoded_data.hexdigest())