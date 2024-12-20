from threading import Thread
import time
class Knight(Thread):
    num = 0
    def __init__(self, name, power, num = 0):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.num = num

    def timer(self, name, power, delay = 1):
        counter = 100
        while counter:
            time.sleep(delay)
            self.num += 1
            counter -= power
            print(f'{name} сражается {self.num} день(дня)..., осталось {counter} воинов.')



    def run(self):
        print(f"{self.name}, на нас напали!")
        self.timer(self.name, self.power)
        print(f"{self.name} одержал победу спустя {self.num} дней(дня)!")

threads =[]
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

threads.append(first_knight)
threads.append(second_knight)

for thread in threads:
    thread.join()
print("Все битвы закончились!")
