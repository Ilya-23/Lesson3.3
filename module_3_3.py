def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(4, 2.5, 'hello')
print_params([45, 8])
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [25, 'one', (5, 3, 6)]
values_dict = {'a' : 'cat', 'b' : 25, 'c' : False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)