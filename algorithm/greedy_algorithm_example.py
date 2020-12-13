# 탐욕알고리즘
# 최적의 해에 가까운 값을 구하기 위해 사용됨
# 여러 경우 중 하나를 결정해야할 때마다, 매순간 최적이라고 생각되는 경울를 선택하는 방식으로 진행해서, 최종적인 값을 구하는 방식

# 문제 1: 동전문제 >> 입력받은 가격에 대해 500, 100, 50, 10, 1 원으로 동전의 수가 가장 적게 지불하시오

coin_list = [500, 100, 50, 10, 1]

def min_coin_count(value, coin_list) :
    count = 0
    details = list()

    coin_list.sort(reverse=True)
    for coin in coin_list :
        coin_num = value // coin
        count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return count, details

print(min_coin_count(5413,coin_list))


# 문제 2 : 부분 배낭 문제
# 무게 제한이 K인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
# 각 물건은 무게와 가치로 표현될 수 있음
# 물건을 쪼갤 수 잇으므로 물건의 일부분이 배낭에 넣을 수 있음, 그래서 fractional knapsack problem 으로 불림
# fractional knapsack problem 의 반대로 물건을 쪼개서 널을 수 없는 배낭 문제도 존대 (0/1 fractional knapsack problem 으로 불림)

# 어떤 것을 먼저 넣는것이 배낭의 가치를 찾는 것이 중요
# 가치, 무게 튜플형식으로 표현
data_list = [(15,12),(20,10),(25,8),(30,5),(10,10)]

# 무게 대비 가치를 sorting하기
# 무게 당 가치를 구하고 정렬하기
data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)

print(data_list)

def get_max_value(data_list, capacity) :
    data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list :
        if capacity-data[0] >= 0 :
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else :
            fraction = capacity / data[0]
            total_value = data[1] * fraction
            details.append([data[0], data[1], fraction])
            break


    return total_value, details

print(get_max_value(data_list, 8))
