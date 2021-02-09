# 0 만들기

# 문제 설명
# 테스트 케이스의 갯수가 주어진다
# 숫자 N을 입력한다
# 1~N을 차례대로 작성하는데 +, -, ' ' 을 이용하여 결과가 0이 나오도록 만들어준다.
# 탈출 조건 함수의 매개변수값이 N과 동일하게 될때

import re

def solve(num, result_str) :
    result_str = result_str + str(num)
    print(num)
    # 탈출조건
    if num == N :
        # 문자열 계산
        # 공백 제거
        # +, - 기준으로 숫자 나눠주기
        replaceAll = result_str.replace(' ', '')
        num_list = re.split('+|-', replaceAll)
        print('num_list', num_list)
        oper_list = list()
        cal_result = 0
        is_first = True
        cur_data = ''

        for element in result_str :
            if element == '+' or element == '-' :
                oper_list.append(element)
        
        print('operator : ', oper_list)

        for element in num_list :
            if is_first :
                is_first = False
                print('element ',element)
                cal_result = int(element)
            else :
                operator = oper_list.pop(0)
                if operator == '+' :
                    cal_result = cal_result + int(element)
                else :
                    cal_result = cal_result - int(element)

        if cal_result == 0 :
            result.append(result_str)
    else :
        solve(num+1, (result_str + '+'))
        solve(num+1, (result_str + '-'))
        solve(num+1, (result_str + ' '))
        

result = list()
result_str = ''
test_case = int(input())

for _ in range(test_case) :
    N = int(input())
    solve(1, result_str)
    for element in range(result) :
        print(element)

    
    