# 병합 정렬
# 재귀용법을 사용한 정렬 알고리즘
# 1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다
# 2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
# 3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합친다.
    
def merge_split(data) :
    # 최소 단위로 쪼개는 과정이 필요하다.
    if len(data) <= 1 :
        return data
    
    # 중앙을 기준으로 오른쪽 왼쪽을 반복해서 쪼개준다.
    medium = int(len(data)/2)
    left_arr = merge_split(data[:medium])
    right_arr = merge_split(data[medium:])

    # 쪼개진 배열을 합치는 과정이 필요하다. (정렬필요함) >> 첫단계는 1개 1개 > 두번쨰는 2개 2개 ..... 점차 합쳐지는 과정이다.
    return merge(left_arr, right_arr)

def merge(left_data, right_data) :
    # 최종적으로 합쳐진 리스트 변수
    merge_arr = list()
    # 왼쪽, 오른쪽 인덱싱 번호 (하나의 리스트라도 완료되었는지 확인이 필요하기 때문에 선언)
    left_index = 0
    right_index = 0
    # 왼쪽 혹은 오른쪽 배열이 전부 탐색된 경우를 나타냄
    while left_index < len(left_data) and right_index < len(right_data) :
        if left_data[left_index] > right_data[right_index] :
            merge_arr.append(right_data[right_index])
            right_index += 1
        else :
            merge_arr.append(left_data[left_index])
            left_index += 1
    
    # 오른쪽 배열이 전부 탐색 되었지만 왼쪽 배열이 남아있는 경우
    if left_index < len(left_data) :
        merge_arr.extend(left_data[left_index:])
    # 왼쪽 배열이 전부 탐색 되었지만 오른쪽 배열이 남아있는 경우
    if right_index < len(right_data) :
        merge_arr.extend(right_data[right_index:])

    return merge_arr

test_arr = [15,21,56,18,163,2516,231,86,123,1,861,231,56,18,91,563,1689,156]
print(merge_split(test_arr))

