# 다장조 cdefgabC, 총 8개 음으로 이루어져있다.. 이 문제에서 8개 음은 다으과 같이 숫자로 바꾸어 표현한다. c는 1~ C는 8로 바꾼다.
# 1~8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘다 아니면 mixed 이다.
# 판별하는 프로그램을 만들어라.

# 접근방법
# 1. ascending count / decending count 를 가진다.
# 2. 루프의 첫번쨰로 acending, descending을 결정한다.
# 3. count > 2 초과인 경우 mixed


def check_elevate(input_list) :
    ascending_cnt = 0
    decending_cnt = 0
    for index in range(len(input_list)-1) :
        if (ascending_cnt + decending_cnt) > 1 :
            return 'mixed'
        if input_list[index] < input_list[index+1] :
            ascending_cnt = 1
        else :
            decending_cnt = 1
    
    if ascending_cnt == 1 :
        return 'ascending'
    
    if decending_cnt == 1 :
        return 'descending'



a = list(map(int, input().split(' ')))

print(check_elevate(a))
