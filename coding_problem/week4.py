# 행복한 수 찾기 (숫자가 주어지고 각 자리수의 제곱의 합이 1이 나오는 경우 끝)
# 결과를 저장하는 리스트가 있어야함 > 순환구조의 여부 확인을 위해서

result_value = list()

def solution(num) :
    global result_value
    result_sum = 0
    # 숫자형 타입으로 바꾸기
    while num > 0 :
        mod_num = num % 10
        result_sum += mod_num**2
        num = num // 10  
    if result_sum == 1 :
        return True
    else :
        if result_sum in result_value :
            return False
        result_value.append(result_sum)
        return solution(result_sum)


print(solution(61))


def countUniques(input_list) :
    return_cnt = 1
    for index in range(1, len(input_list)) :
        if input_list[index-1] != input_list[index] :
            return_cnt += 1
    
    return return_cnt


print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))