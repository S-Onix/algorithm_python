# 퀵 정렬 : 기준점을 정해서 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 함수를 작성함
# 왼쪽, 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복한다.

test_list = [135,21,8,1,6,12,48,32,541]
# 기준점을 중앙으로 잡음
# 중앙의 값보다 작으면 왼쪽 배열
# 중앙의 값보다 크면 오른쪽 배열
def quick_sort(data) :
    if len(data) <= 1 :
        return data

    pivot = data[0]
    left_list = list()
    right_list = list()

    for index in range(1, len(data)) :
        if data[index] > pivot :
            right_list.append(data[index])
        else :
            left_list.append(data[index])

    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


print(quick_sort(test_list))

def comprehension_quick_sort(data) :
    if len(data) <= 1 :
        return data
        
    pivot = data[0]

    left = [item for item in data[1:] if item < pivot] 
    right = [item for item in data[1:] if item >= pivot]

    return comprehension_quick_sort(left) + [pivot] + comprehension_quick_sort(right)
    