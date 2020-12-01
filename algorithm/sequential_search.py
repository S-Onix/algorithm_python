# 순차 탐색 : 정렬된 데이터 중 순차적으로 데이터를 찾는 방법
import random


def sequential_search(search_list, search_data) :
    for index in range(len(search_list)) :
        if search_data == search_list[index] :
            return True
    return False

list_data = random.sample(range(100), 10)
list_data.sort()

print(sequential_search(list_data, 20))