def calculate_structure_sum(date_struct):
    n = 0
    if isinstance(date_struct, int):
        n += date_struct
        return n
    if isinstance(date_struct, str):
        n += len(date_struct)
        return n
    if isinstance(date_struct,list):
        list_ = date_struct
        for j in range(len(list_)):
            n += calculate_structure_sum(list_[j])
        return n
    if isinstance(date_struct, dict):
        dict_ = date_struct
        for j in dict_:
            n += calculate_structure_sum(j)
            n += calculate_structure_sum(dict_[j])
        return n
    if isinstance(date_struct, tuple):
        tuple_ = date_struct
        for j in tuple_:
            n += calculate_structure_sum(j)
        return n
    if isinstance(date_struct, set):
        set_ = date_struct
        for j in set_:
            n += calculate_structure_sum(j)
        return n

data_structure = [
    [1,2,3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
