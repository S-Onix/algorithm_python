# 재귀용법 : 메소드 안에서 동일한 메소드(함수)를 호출하여 최종적인 값을 추출하는 방법
# 이미 검색한 값에 대해서 중복적으로 호출하여 메모리상 과부하가 걸릴 수 있다
# 추후에 메모라이즈라는 기법을 사용하여 중복을 줄이는 방법이 존재한다.
# 팩토리얼을 recursive_call 을 활용하여 알고리즘 만들기
# 파이썬에서 재귀 함수는 길이가 1000회 이하여야 함 (파이썬 정책)

# 일반적인 사용법 1
def factorial_call(data) :
    if data > 1 :
        return data * factorial_call(data-1)
    else :
        return data

for num in range(0,10) :
    print(factorial_call(num))

# 일반적인 사용법 2
def factorial_call2(data) :
    if data < 2 :
        return data
    return_value = data * factorial_call2(data - 1)
    return return_value

# 재귀용법의 패턴
# 1. 입력이 일정값보다 크면 자기 자신을 호출한다.
# 2. 자기 자신을 호출할 때 일정수 만큼 작은 매개변수로 호출한다.

# 일반적인 재귀형태
def function(입력) :
    if 입력 > 일정값 : # 입력이 일정값 이상이면
        return function(입력 - 1) # 입력값보다 작은 값
    else :
        return 일정값, 입력값 또는 특정값  # 재귀 호출 종료

# 일반적인 재귀형태2
def function2(입력) :
    if 입력 <= 일정값 :             # 입력이 일정 값보다 작으면
        return 일정값 또는 입력값    # 재귀 호출 종료
    function2(입력값보다 작은 값)
    return 결과값