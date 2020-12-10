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