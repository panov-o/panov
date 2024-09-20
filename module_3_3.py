def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

value_list = [5, 'пять', False]
print_params(*value_list)
value_dict = {'a':12, 'b':'new', 'c':False}
print_params(**value_dict)
value_list_2 = [54.32, 'Строка']
print_params(*value_list_2, 42)
print_params(b = 25)
print_params(c = [1,2,3])
