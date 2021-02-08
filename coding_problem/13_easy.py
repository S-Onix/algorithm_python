# 수 정렬하기 > 20분 추천

# 데이터의 갯수와 데이터의 범위가 존재하는 
# 문제일경우 파이썬 기본 정렬 알고리즘으로는 풀수 없다.
# 파이썬 기본 정렬 알고리즘의 시간복잡도는 O(Nlog(N))
# 따라서 O(N)의 시간복잡도를 가지는 알고리즘을 알고 있어야함
# 기수정렬, 카운팅(계수) 정렬
# 데이터의 개수가 많을 겨웅에는 sys.stdin.realine() 을 사용해야함
# input() < sys.stdin.readline() 속도적인 측면에서 봤을경우

# 카운팅 정렬
# 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법
# 카운팅된 갯수만큼 

import sys

n = int(sys.stdin.readline())

array = [0] * 10001

for i in range(n) :
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001) :
    if array[i] != 0 :
        for j in range(array[i]) :
            print(i)