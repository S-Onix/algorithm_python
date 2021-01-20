# 스택 (stack)은 기본적인 자료구조 중 하나로, 
# 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
# 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 
# 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 
# 하나의 수열을 만들 수 있다. 
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.


# 문제풀이
# 1. 스택을 쌓아준다. 
# 2. list[index] 와 동일할 경우 pop() > result_list에 저장
# 1~2 를 반복하여 스텍이 빌때까지 반복한다.


# 오답 > index out of range
def stack_num_array(num, input_list) :
    input_index = 0
    i = 1
    stack_list = list()
    stack_list.append(i)
    result = list()
    stack_list.append(i)
    result.append('+')
    while stack_list :
        if input_list[input_index] == stack_list[-1] :
            stack_list.pop()
            input_index = input_index + 1
            result.append('-')
            continue

        i = i + 1
        stack_list.append(i)
        result.append('+')

    return result

# num = input()
# a = list(map(int, input().split(' ')))

# print(stack_num_array(num, a))

num = int(input())
def stack_array_solve(num) :
    count = 1
    stack_list = list()
    result = list()
    for i in range(1, num+1) :
        data = int(input())
        while count <= data:
            stack_list.append(count)
            count += 1
            result.append('+')

        if stack_list[-1] == data :
            stack_list.pop()
            result.append('-')
        else :
            return 'NO'
    return result

print('\n'.join(stack_array_solve(num)))