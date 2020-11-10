# 함수의 동작 과정에서 많이 쓰인다.
# 장점 : 구조간 단순하여 구현이 쉽다 (마지막 위치에 데이터를 넣고 빼는 방식)
#        데이터 저장 / 읽기 속도가 빠르다.
# 단점 : 데이터의 갯수를 미리 지정해야한다.
#        파이썬의 경우에는 재귀함수는 최대 1000번까지만 호출 가능하다
#        저장공간의 낭비가 발생할 수 있다. >> 미리 최대 갯수만큼 공간을 확보해 놓아야하기 때문에
# 구현 방법 : 배열을 이용한 방법, 링크드리스트를 이용하여 구현한 방법 두가지가 존재하며 배열을 이용한 방법을 사용시에 위의 장점과 단점을 가지고 있다.
# 하지만 단순하고 빠른 성능을 위해 주로 사용되므로 링크드리스트보다는 배열을 이용한 구현을 많이 사용한다.

# 재귀함수
def recursive(data) :
    if data < 0 :
        print('ended')
    else :
        print(data)
        recursive(data-1)
        print('returnd ', data)

recursive(4)

# push, pop 구현
data_stack = list()

def push(data) :
    data_stack.append(data)

def pop() :
    data_pop = data_stack[-1] # 가장 마지막에 있는 인덱스 가져오기
    del data_stack[-1]
    print(data_pop)
    return data_pop

push(1)
push(3)
push(4)
push(5)

pop()
pop()
print(data_stack)

# 기존 list 의 제공 메소드 사용
data_stack2 = list()
data_stack2.append(1)
data_stack2.append(2)
data_stack2.append(3)

data_stack2.pop()
print(data_stack2)
