def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n < 2:  # не 0 и не 1
            res = 'Не простое и не сложное'
        elif n == 2:
            res = '- Простое'
        else:
            k = int(n/2 + 1)
            for a in range(2, int(k + 1)):
                if n % a == 0:
                    res = 'Составное'
                else:
                    res = 'Простое'
        print(res)
        return n
    return wrapper

@is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

# Результат консоли:
# Простое
# 11
