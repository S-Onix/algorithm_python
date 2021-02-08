# 정렬 15분

def solve(num) :
    dict_list = list()
    for _ in range(num) :
        x, y = map(int, input().split(' '))
        dict_list.append({'x' : x, 'y' : y})

    result = sorted(dict_list, key=lambda x:(x['x'], x['y']))
    
    for el in result :
        print(el['x'], el['y'])


solve(int(input()))