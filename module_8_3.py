class Car:
    def __init__(self, model: str, __vin: int, __numbers: str):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin()
        self.__is_valid_numbers()
    def __is_valid_vin(self):
        vin = self.__vin
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True
    def __is_valid_numbers(self):
        if not isinstance(self.__numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        if not len(self.__numbers) == 6:
            raise IncorrectVinNumber('Неверная длина номера')
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
