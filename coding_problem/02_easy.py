# 블랙잭, 배열, 완전탐색
# 21보다 크지 않는 경우에서 최대한 가까운 카드 3장의 합을 구하시오

# 문제풀이방법 (실패 2장에서 끝나는 경우가 발생)
# 정렬한다.
# 가장 큰값부터 빼준다.
# 최종 값 나옴

# 문제풀이 방법2
# 무식하게 다 풀어준다.

def blackjack_fail(stand_input, data_input) :
    limit_count = stand_input[1]
    data_input.sort(reverse=True)
    result = 0
    use_card_cnt = 0

    print(data_input[0])
    print(data_input[1])
    print(data_input[2])


    for index in range(len(data_input)) : 
        if (limit_count >= data_input[index]) and use_card_cnt < 3 :
            limit_count = limit_count - data_input[index]
            result = result + data_input[index]
            use_card_cnt = use_card_cnt + 1
        

    return result

def blackjack_solve2(stand_input, data_input) :
    limit_value = stand_input[1]
    result = 0

    for i in range(len(data_input)-2) :
        for j in range(len(data_input)-1) :
            for k in range(len(data_input)) :
                sum_value = data_input[i] + data_input[j] + data_input[k]
                if sum_value <= limit_value :
                    result = max(sum_value, limit_value)

    return result



stand_input= list(map(int, input().split(' ')))
data_input = list(map(int, input().split(' ')))

print(blackjack_solve2(stand_input, data_input))


