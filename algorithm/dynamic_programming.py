# 동적계획법 (Dynamic Programming)
# 입력 크기가 작은 부분 문제을 해결한 후, 
# 해당 부분 문제의 해를 활용해서 보다 큰 크기의 문제를 해결 최종적으로 전체 문제를 해결하는 알고리즘
# bottom > up(상향식 접근법) 방식으로 문제가 해결된다 >> 핵심 코드는 최소화된 문제를 해결하는 코드
# Memoization 기법을 사용한다. (작은 문제들의 결과를 저장한다.)
# Memoization(메모이제이션) : 프로그램 실행시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 방법
# 문제를 잘게 쪼갤 때, 부분 문제는 중복되어 재활동되는 문제가 발생하는 것을 방지한다.

# 분할 정복 (Divide and conquer)
# 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서 다시 병합하여 문제의 답을 얻는 알고리즘
# 하향식 접근법으로, 상위의 해답을 구하기 위해, 아래로 내려가면서 하위의 해답을 구하는 방식
# 일반적으로 재귀함수로 구현한다.
# 문제를 잘게 쪼개지만 부분 문제는 서로 중복되지 않는다.

# 공통적 : 문제를 잘게 쪼개서, 가장 작은 단위로 분할한다.

# 차이점 : 동적계획법은 부분 문제가 중복될수 있기 때문에 메모이제이션 방식을 사용하고
#          분할정복은 부분 문제가 중복되지 않아 메모이제이션을 사용하지 않는다.


# recursive_call
def recursive_fibo(data) :
    if data <= 1 :
        return data
    return recursive_fibo(data - 1) + recursive_fibo(data - 2)

# 피보나치 수열 문제 (DP로 풀어보기)
def dp_fibo(data) :
    # 입력된 데이터만큼 배열 생성
    cache = [0 for x in range(data)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, data + 1) :
        cache[index] = cache[index-1] + cache[index-2]
    
    return cache[data]