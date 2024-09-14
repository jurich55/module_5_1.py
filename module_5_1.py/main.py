number_of_floors = 1
new_floor = 1
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'Такого  этажа  не существует')
        else:
            for i in range(1,  new_floor + 1):
                print(i)
            print(f'Вы прибыли на  {new_floor} этаж ')


h1 = House('ЖК Горский', 9)
h2 = House('Домик в деревне', 4)
h1.go_to(5)
h2.go_to(10)
