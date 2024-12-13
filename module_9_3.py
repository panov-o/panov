first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = []
second_result = []
len_f = (len(len_f) for len_f in first)
len_s = (len(len_s) for len_s in second)
first_res = zip(len_f, len_s)

for i, e in enumerate(first_res):
    if e[0]-e[1] != 0:
        first_result.append(e[0]-e[1])

for i in range(len(first)):
    second_result.append(len(first[i]) == len(second[i]))

print(list(first_result))
print(list(second_result))