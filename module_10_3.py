
from random import randint     # Для генерации случайного целого числа
from time import sleep        # Для ожидания
import threading                # Для работы с потоками

lock = threading.Lock()     # для блокировки потоков

class Bank:
    def __init__(self, balance: int, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            random_number = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += random_number   # пополняем баланс случайной суммой
            print(f'Пополнение: {random_number}. Баланс: {self.balance}')
            sleep(0.001)        # имитируем скорость выполнения пополнения


    def take(self):
        for i in range(100):
            random_number = randint(50, 500)
            print(f'Запрос на {random_number}')
            if random_number <= self.balance:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank(0, lock)
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
