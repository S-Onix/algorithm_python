# 버블 정렬 : 인접한 두 수를 비교 후 오름차순, 내림차순에 따라 데이터를 스왑해준다.

bubble_sort_arr = list()
bubble_sort_arr.append(10)
bubble_sort_arr.append(2)
bubble_sort_arr.append(5)
bubble_sort_arr.append(23)
bubble_sort_arr.append(543)
bubble_sort_arr.append(1)
bubble_sort_arr.append(87)
bubble_sort_arr.append(6)

# 스왑이 발생하지 않을 경우 더이상 진행하지 않고 for문을 끝낸다.
for data in range(0, len(bubble_sort_arr)-1) :
    swap = False
    for compare in range(0, len(bubble_sort_arr) - data - 1) :
        if bubble_sort_arr[compare] > bubble_sort_arr[compare+1]:
            bubble_sort_arr[compare], bubble_sort_arr[compare+1] = bubble_sort_arr[compare+1], bubble_sort_arr[compare]
            swap = True
        
    if swap == False :
        break

print(bubble_sort_arr)