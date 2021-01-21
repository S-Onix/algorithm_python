#여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 
# ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 
#  여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 
#  하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
#  이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

# 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
# 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
# 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

# 이 풀이의 문제점 : 데이터와 인덱스를 묶어 생각하지 않았기 때문에 동일한 우선순위에 대해서는 고려를 하지 못함
# stack, queue를 동시에 사용하여 문제를 풀어보려고 시도함
def solve(num) :
    for index in range(1, num+1) :
        queue_size, find_index = list(map(int, input().split(' '))) 
        input_list = list(map(int, input().split(' ')))
        
        temp_list = input_list.copy()
        queue_list = input_list.copy()
        input_list.sort(reverse=True)
        result = list()
        count = 0
        
        print(temp_list[find_index])

        while True :
            print (input_list)
            print(queue_list)
            if input_list[0] == queue_list[0] :
                count = count + 1
                if input_list[0] == temp_list[find_index] :
                    result.append(count)
                    break
                else :
                    input_list.pop(0)
                    queue_list.pop(0)
            else :
                queue_list.append(queue_list.pop(0))
    return result

 
def solve_2(num) :
    result = list()
    for _ in range(num) :
        n, m = list(map(int, input().split(' ')))
        queue = list(map(int, input().split(' ')))
        # 아래 코드 실행시 [2,1,4,3]의 데이터가 [(2,0),(1,1),(4,2),(3,3)] 과 같이 인덱스번호를 같이 소유하게됨
        queue = [(i, idx) for idx, i in enumerate(queue)] 
        count = 0
        
        while True :
            if queue[0][0] == max(queue, key=lambda x: x[0])[0] :
                count += 1
                if queue[0][1] == m :
                    result.append(count)
                    break
                else :
                    queue.pop(0)
            else :
                queue.append(queue.pop(0))
    return result


num = int(input())
print(solve_2(num))