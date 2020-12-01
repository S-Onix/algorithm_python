# 이진 탐색 : 탐색할 자료를 둘로 나누어 해당 데이터가 있을법한 곳을 탐색하는 방법
# 정렬이 되어있는 전제 조건을 가지고 있다.

# 중앙의 값을 찾고 데이터를 비교 후 이후 탐색할 위치를 지정한다.
import random


def binary_search(list_data, search_data) :
    print(list_data)

    if len(list_data) == 1 and search_data == list_data[0]:
        return True

    if len(list_data) == 1 and search_data != list_data[0] :
        return False

    if len(list_data) == 0 :
        return False 

    medium = len(list_data)//2
    
    if search_data == list_data[medium] :
        return True
    elif list_data[medium] > search_data :
        return binary_search(list_data[:medium], search_data)
    else :
        return binary_search(list_data[medium + 1:], search_data)


data_list = random.sample(range(100), 10)
data_list.sort()
print(binary_search(data_list, 32))
