# 선택정렬 : 최소값을 찾아 가장 앞의 값과 위치를 바꿈

def selection_sort(data) :
    for index in range(0, len(data) -1 ) :
        lowest = index
        for index2 in range(index+1, len(data)) :
            if data[lowest] > data[index2] :
                lowest = index2
        data[index], data[lowest] = data[lowest], data[index]

data = [1,45,234,5235,523,5234,134,123,423]

selection_sort(data)

print(data)
                
        
