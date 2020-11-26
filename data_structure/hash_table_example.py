# 해쉬테이블
# 키와 데이터를 저장하는 데이터 구조
# 장점
# Key를 통해 데이터를 받아오므로 속도가 획기적으로 빠름.
# 키에 대한 데이터가 있는지(중복) 확인이 쉽니다.
# 단점
# 일반적으로 저장공간이 더 필요하다.
# 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요하다.

# 검색이 많이 필요한 경우 / 저장, 삭제, 읽기가 빈번한 경우 / 캐쉬 구현시 사용된다.

# 파이썬 딕셔너리 타입이 해쉬 테이블의 예이다.

# 리스트 컴프리헨션 >> 내부에 10개의 공간에 0을 세팅한다.

hash_table = list([ 0 for i in range(10)])

def hash_func(key) : 
    return key % 5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord() : 문자의 ASCII(아스키) 코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))

print(hash_func(ord(data1[0])))

def storage_data(data, value) :
    key = ord(data[0])
    hash_addr = hash_func(key)
    hash_table[hash_addr] = value

storage_data('Andy', '010333344444')
storage_data('Dave', '010222244444')
storage_data('Trump', '010555544444')


def get_data(data) :
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))



