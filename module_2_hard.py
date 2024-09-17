import random
first_num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(len(first_num)):
    n = random.choice(first_num)
    print(n, '- ', end ='')
    for j in range(1, n):
        for k in range(j+1, n):
            if n % (k + j) == 0:
                print(j, k, sep='', end='')
    print()
    first_num.remove(n)