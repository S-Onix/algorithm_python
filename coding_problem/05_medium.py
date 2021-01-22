# 키로거
# 난이도 중 / 스택, 구현, 그리디 / 풀이시간 40분
# 창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 
# 며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.
# 키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 
# 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.
# 강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 
# 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.

# 스택을 이용하지 않고
def solve(num) :
    result = list()
    # 데이터 루핑은 리스트의 갯수만큼
    for i in range(num) :
        password_list = input()
        cursor = 0
        solve_list = list()
        print(password_list)
        for element in password_list :
            if element == '<' :
                if cursor < 1 :
                    continue
                else :
                    cursor -= 1
            elif element == '>' :
                if cursor == len(solve_list)-1 :
                    continue
                else :
                    cursor += 1
            elif element == '-' :
                solve_list.pop(cursor)
            else :
                solve_list.append(element)
                cursor += 1
        result.append(''.join(solve_list))
        print(''.join(solve_list))
solve(int(input()))

def solve2(num) :
    for i in range(num) :
        input_list = input()
        left_stack = list()
        right_stack = list()
        for element in input_list :
            if element == '<' :
                if left_stack :
                    right_stack.append(left_stack.pop())
            elif element == '>' :
                if right_stack :
                    left_stack.append(right_stack.pop())
            elif element == '-' :
                if left_stack :
                    left_stack.pop()
            else :
                left_stack.append(element)
        left_stack.extend(reversed(right_stack))
        print(''.join(left_stack))

    
solve2(int(input()))