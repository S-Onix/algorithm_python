# 친구 네트워크
# 헤시, 집합, 그래프
# step 1 : test_loop 입력
# setp 2 : 관계도 loop 입력
# 확인해봐야할점 리스트 안의 집합에도 in절이 먹는지
# union-find 알고리즘 사용 > 

# 테스트 집합의 마지막을 가져오는것 (실패)
test_set = set()
test_set.add(76)
test_set.add(3)
test_set.add(4)
test_set.add(6)
test_set.add(1)

print(test_set)





# loop_num = int(input())

def friend_network(loop_num) :
    for _ in range(loop_num) :
        network_loop = int(input())
        network_list = list()
        result_set = set()
        for __ in range(network_loop) :
            network = set(map(str, input().split(' ')))
            if not result_set :
                result_set.update(network)
                set_list.append(network)
                continue

            


