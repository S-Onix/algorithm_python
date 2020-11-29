# 삽입 정렬 : 데이터를 특정 위치에 삽입하는 알고리즘
# 1. 인덱스의 값을 이전 값과 비교
# 2. 인덱스의 값이 이전 값보다 작으면 스왑
# 3. 아니면 break

def insertion_sort(data) :
    for index in range(1, len(data)) :
        for change_index in range(index, 0, -1) :
            if data[change_index] < data[change_index - 1] :
                data[change_index], data[change_index - 1] = data[change_index - 1], data[change_index]
            else :
                break


insertion_data = [2123,42345,123,123345,234,235,2345,234,123]

insertion_sort(insertion_data)

print(insertion_data)