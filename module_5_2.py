class House:
    def __init__(self, name, number_of__floors):
        self.name = name
        self.number_of_floors = number_of__floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name} ,количество этажей: {self.number_of_floors}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(str(h1))
print(str(h2))

print(len(h1))
print(len(h2))
