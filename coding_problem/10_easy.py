test_input = input()

result_list = list(map(int, test_input))
result_list.sort(reverse=True)

for el in result_list :
    print(el, end='')