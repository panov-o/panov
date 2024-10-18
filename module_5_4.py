class House:
    __instance = None
    houses_history = []
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, number_of__floors):
        global houses_history
        self.name = name
        self.number_of_floors = number_of__floors
        House.houses_history.append(self.name)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    # def go_to(self, new_floor):
    #     if new_floor > self.number_of_floors:
    #         print('Такого этажа не существует')
    #     else:
    #         for i in range(new_floor):
    #             print(i+1)
    #
    # def __len__(self):
    #     return self.number_of_floors
    #
    # def __str__(self):
    #     return (f'Название: {self.name} ,количество этажей: {self.number_of_floors}')
    #
    # def __eq__(self, other):
    #     if isinstance(other, House):
    #         return self.number_of_floors == other.number_of_floors
    #     else:
    #         return False
    #
    # def __lt__(self, other):
    #     if isinstance(other, House):
    #         return self.number_of_floors < other.number_of_floors
    #     else:
    #         return False
    #
    # def __le__(self, other):
    #     if isinstance(other, House):
    #         return self.number_of_floors <= other.number_of_floors
    #     else:
    #         return False
    #
    # def __gt__(self, other):
    #     if isinstance(other, House):
    #         return self.number_of_floors > other.number_of_floors
    #     else:
    #         return False
    #
    # def __ge__(self, other):
    #     if isinstance(other, House):
    #         return self.number_of_floors >= other.number_of_floors
    #     else:
    #         return False
    #
    # def __ne__(self, other):
    #     if isinstance(other, House):
    #         return self.number_of_floors != other.number_of_floors
    #     else:
    #         return False
    #
    # def __add__(self, value):
    #     self.number_of_floors += value
    #     return self
    #
    # def __radd__(self, value):
    #     self.number_of_floors += value
    #     return self
    #
    # def __iadd__(self, value):
    #     self.number_of_floors += value
    #     return self

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов

del h2
del h3

print(House.houses_history)

