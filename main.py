# n = int(input("Enter lenght: "))
# user_list = []
# i = 0
# while i < n:
#     word = "Element №" + str(i + 1) + ": "
#     user_list.append(input(word))
#     i += 1
# print(user_list)
# #
# word = "FOOTBALL, BASKETBALL, RIDING"
# hobby = word.split(", ")
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
#     result = ", ".join(hobby)
# print(result)

# persons = {
#     'user_1':{
#         'first_name': 'Vanilla',
#         'last_name': 'Monkey',
#         'age': '47',
#         'address': ('Улица Пушкина', 'дом 41'),
#         'license': ('Вождение', 'Пилотирование', 'Невидимость')
#     },
#     'user_2':{
#         'first_name': 'Leo',
#         'last_name': 'Barsuk',
#         'age': '22',
#         'address': ('Улица Барсучья', 'дом 1'),
#         'license': ('Вождение', 'Барсук',)
#     }
# }
# print(persons['user_1'])
# print(persons['user_2'])
# def minimal(l):
#     min_number = l[0]
#     for el in l:
#         if el < min_number:
#             min_number = el
#     print(min_number)
# nums1 = [3.1, 344.1, 57, 13104, 318.456, 0, 39]
# minimal(nums1)
# data = input('Введите текст: ')
# file = open('data/text.txt', 'a')
#
# file.write(data +'\n')
#
# file.close()
# file = open('data/text.txt', 'r')
#
# for line in file:
#     print(line, end='')
#
# file.close()

# x = 0
# while x == 0:
#     try:
#         x = int(input('Введите число: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print('Введите корректное число!')
# import mymodule as my
# # print(my.name)
# from mymodule import add_3_numbers as add
# print(add(1, 3, 0))
#
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#     def get_data(self):
#         print('Имя:',self.name + '.','Возраст:', self.age, 'года.','Счастлив ли:',self.isHappy)
#
# cat1 = Cat()
# cat1.set_data("Барсик", 5, True)
#
# cat2 = Cat()
# cat2.set_data("Ласка", 4, True)
#
# cat1.get_data()
# cat2.get_data()

# class Cat:
#     name = None
#     age = None
#     isHappy = None
#     def __init__(self, nam=None, age=None, isHappy=None):
#        self.set_data(name, age, isHappy)
#        self.get_data()
#
#     def set_data(self, name=None, age=None, isHappy=None):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#     def get_data(self):
#         print('Имя:',self.name + '.','Возраст:', self.age, 'года.','Счастлив ли:',self.isHappy)
#
# cat1 = Cat("Барсик", 5, True)
# cat2 = Cat("Ласка", 4, True)
# cat3 = Cat("Бомба", 404, False)

class Building:
    year = None
    city = None
    def __init__(self, year, city):
        self.year = year
        self.city = city
    def get_info(self):
        print("Year:", self.year, "City:", self.city)
class school(Building):
    pupils = 0
    def __init__(self, pupils, year, city):
        super(school, self).__init__(year, city)
        self.pupils = pupils

class shop(Building):
    pass

class museum(Building):
    pass


school = school(431, 1999, "Moscow")
school.get_info()
shop = shop(1999, "Moscow")
museum = museum(1999, "Moscow")

