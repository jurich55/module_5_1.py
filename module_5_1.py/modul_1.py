# class House:
#     def __init__(self, name, number_of_floors):
#         self.name = name
#         self.number_of_floors = number_of_floors
#         self.go_to()
#
#     def go_to(self, new_floor):
#         for i in range(new_floor):
#             new_floor = (i + 1)
#             if new_floor <= number_of_floors and new_floor >= 1:
#                 print(new_floor)
#     #         else:
#     #             print("Такого этажа не существует")
#     #             break
#     #     if new_floor <= 0:
#     #         print("Такого этажа не существует")
#
#
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)