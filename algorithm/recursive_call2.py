# 재귀용법 패턴 연습해보기
# 재귀 용법을 활용하여 1부터 Num까지의 곱이 출력되게 만들기

import random

def multiple(num) :
    if num > 1 :
        return num * multiple(num-1)
    else :
        return num

def multiple2(num) :
    if num < 2 :
        return num
    return_value = num * multiple2(num-1)
    return return_value

print(multiple(4))
print(multiple2(4))


# 숫자가 들어있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만들기
data = random.sample(range(100), 10) 
print(data)

def list_sum1(data) :
    if len(data) == 0 :
        return 0
    if len(data) != 1 :
        return data[-1] + list_sum1(data[:-1]) # 가장 마지막 인덱스부터 더하는 방식
        # return data[0] + list_sum1(data[1:]) # 첫번째 인덱스부터 더하는 방식
    else :
        return data[0]

def list_sum2(data) :
    if len(data) == 0 :
        return 0
    if len(data) <= 1 :
        return data[0]
    return data[-1] + list_sum2(data[:-1])  # 가장 마지막 인덱스부터 더하는 방식
    # return data[0] + list_sum2(data[1:])  # 첫번째 인덱스부터 더하는 방식


print(list_sum1(data))
print(list_sum2(data))

# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드시오
# 첫번째 글자와 마지막 글자가 같으면 true

def recursive_palindrome(data) :
    if len(data) <= 1 :
        return True
    
    if data[0] == data[-1] :
        return recursive_palindrome(data[1:-1])
    else :
        return False

print(recursive_palindrome('LEVEL'))
print(recursive_palindrome('LEVEE'))
    
    
