# 특정 정수의 존재여부 찾기

loop_num = int(input())

def specify_num_search(loop_num) :
    result = list()
    for _ in range(loop_num) :
        search_num = int(input())
        num_list = list(map(int, input().split(' ')))
        if search_num in num_list :
            result.append(1)
        else :
            result.append(0)

    return result

# print(specify_num_search(loop_num))

# set 자료형을 이용하여 중복을 피해준다
def specify_num_search_set(loop_num) :
    result = list()
    for _ in range(loop_num) :
        search_num = int(input())
        num_set = set(map(int, input().split()))
        if search_num in num_set :
            result.append(1)
        else :
            result.append(0)

    return result

print(specify_num_search_set(loop_num))