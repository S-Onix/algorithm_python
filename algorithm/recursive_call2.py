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

# 숫자가 들어있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만들기
data = random.sample(range(100), 10) 

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

    
# 1. 정수 N에 대해
# 2. N이 홀수이면 3 * N + 1 을 하고
# N이 짝수이면 N을 2로 나눈다.
# N이 1이 될때까지 2와 3의 과정을 반복한다.
# 모든 과정을 출력하시오

def recursive_practice(data) :
    print(data)
    if data == 1 :
        return True

    if data % 2 == 0 :
        return recursive_practice(data // 2)
    else :
        return recursive_practice(data * 3 + 1)


# 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지 존재한다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 1+1+2
# 2+2
# 1+3
# 3+1
# 정수 n이 입력으로 주어질때, N을 1,2,3의 합으로 나타낼수 있는 방법의 수를 구하시오

#1       2             3               4               5
#1       1+1           1+1+1           1+1+1+1         1+1+1+1+1
#        2             1+2             1+1+2           1+1+1+2
#                      2+1             1+2+1           1+1+2+1
#                      3               2+1+1           1+2+1+1
#                                      1+3             2+1+1+1
#                                      3+1             1+1+3
#                                      2+2             1+3+1
#                                                      3+1+1
#                                                      1+2+2
#                                                      2+1+2
#                                                      2+2+1   
#                                                      3+2
#                                                      2+3
# 1     2               4               7               13

# >> 4의 경우 1,2,3 의 갯수 합
# >> 5의 경우 2,3,4 의 갯수 합

def sum_otw(data) :
    if data == 1 :
        return 1
    elif data == 2 :
        return 2
    elif data == 3 :
        return 4
    else :
        return sum_otw(data - 3) + sum_otw(data - 2) + sum_otw(data - 1)

print(sum_otw(5))
