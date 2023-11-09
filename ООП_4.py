
###___4.3.3___###
class User():
    def __init__(self, name, friends=0):
        self.name = name
        self.friends = friends
    def add_friends(self, n):
        self.friends += n




###___4.3.4___###

class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self,new_color):
        self.color = new_color

    def add_rooms(self,n):
        self.rooms+=n

###___4.3.5___###

from math import pi
class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.diameter = radius*2
        self.area = pi * self.radius * self.radius

###___4.3.6___###

class Bee:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n

###___4.3.7___###

class Gun:
    def __init__(self):
        self.shoot_name = ['pif', 'paf']
        self.fire = False

    def shoot(self):
        print(self.shoot_name[self.fire])
        self.fire = not self.fire


###___4.3.8___###

class Gun:
    def __init__(self):
        self.shoot_name = ['pif', 'paf']
        self.shotscount = 0

    def shoot(self):
        print(self.shoot_name[self.shotscount % 2])
        self.shotscount += 1


    def shots_count(self):
        return self.shotscount

    def shots_reset(self):
        self.shotscount = 0

###___4.3.9___###

class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self,n):
        self.right += n

    def add_left(self,n):
        self.left += n

    def get_result(self):
        if self.right == self.left:
            return "Весы в равновесии"
        elif self.right < self.left:
            return "Левая чаша тяжелее"
        else:
            return "Правая чаша тяжелее"

###___4.3.10___###

from math import sqrt
class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return sqrt(self.x * self.x+ self.y * self.y)

###___4.3.11___###

class Numbers:
    def __init__(self):
        self.numbers = []

    def add_number(self,n:int):
        self.numbers.append(n)

    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.numbers))

    def get_odd(self):
        return list(filter(lambda x: x % 2 == 1, self.numbers))


###___4.3.12___###

class TextHandler:

    def __init__(self):
        self.words_list = []

    def add_words(self,text:str):
        self.words_list.extend(text.split())

    def get_shortest_words(self):
        if self.words_list:
            self.min_lenght = len(min(self.words_list, key=len))
            return list(filter(lambda x: len(x) == self.min_lenght, self.words_list))
        else:
            return []

    def get_longest_words(self):
        if self.words_list:
            self.max_lenght = len(max(self.words_list, key=len))
            return list(filter(lambda x: len(x) == self.max_lenght, self.words_list))
        else:
            return []

###___4.3.13___###

class Todo:
    def __init__(self):
        self.things =[]
        self.min_priority = 1000
        self.max_priority = 0

    def add(self, todo, priority):
        self.things.append((todo, priority))
        if self.min_priority > priority:
            self.min_priority = priority
        if self.max_priority < priority:
            self.max_priority = priority

    def get_by_priority(self,n):
        return [i[0] for i in filter(lambda x: x[1] == n, self.things)]

    def get_low_priority(self):
        return [i[0] for i in filter(lambda x: x[1] == self.min_priority, self.things)]

    def get_high_priority(self):
        return [i[0] for i in filter(lambda x: x[1] == self.max_priority, self.things)]

###___4.3.14___###

class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        return list(dict([[i[1],0] for i in filter(lambda x: x[0] == street, self.delivery_data)]).keys())

    def get_flats_for_house(self, street, house):
        return list(dict([[i[2],0] for i in filter(lambda x: x[0] == street and x[1] == house, self.delivery_data)]).keys())

###___4.3.15___###
import copy
class Wordplay:
    def __init__(self, words:list = []):
        self.words = words.copy()

    def add_word(self, world:str):
        if world not in self.words:
            self.words.append(world)

    def words_with_length(self, n):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args, **kwargs):
        rezult=[]
        patern = set(args)
        for world1 in self.words:
            world = set(world1)
            if len(world - patern) == 0:
                rezult.append(world1)
        return rezult

    def avoid(self,*args, **kwargs):
        rezult=[]
        patern = set(args)
        for world1 in self.words:
            world = set(world1)
            if len(world - patern) == len(world):
                rezult.append(world1)
        return rezult

class Knight:

    def __init__(self,horizontal:str,vertical:int, color:str):
        self.horizontal = horizontal
        self.horizontal_num =ord(horizontal) - ord("a")
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return "N"

    def can_move(self, horizontal:str, vertical:int):
        horizontal_num = ord(horizontal) - ord("a")
        if (horizontal_num - self.horizontal_num) * (horizontal_num - self.horizontal_num) + (vertical - self.vertical) * (vertical - self.vertical) == 5 and 0<=horizontal_num <=8 and 0<=vertical <=8:
            return True
        else:
            return False

    def move_to(self, horizontal:str, vertical:int):
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.horizontal_num = ord(horizontal) - ord("a")
            self.vertical = vertical

    def draw_board(self):
        for vertical in range(8,0,-1):
            for horizontal in "abcdefgh":
                if self.can_move(horizontal, vertical):
                    print("*", end="", sep="")
                elif vertical == self.vertical and horizontal == self.horizontal:
                    print(self.get_char(), sep="", end="")
                else:
                    print(".", end="", sep="")
            print()

###___4.4.15___###

from math import pi
class Circle:
    def __init__(self,radius):
        self._radius = radius
        self._diameter = radius*2
        self._area = pi * self._radius * self._radius

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area

###___4.4.16___###

class BankAccount:
    def __init__(self,balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError("На счете недостаточно средств")

    def transfer(self,account, amount):
        try:
            self.withdraw(amount)
            account.deposit(amount)

        except ValueError:
            raise ValueError("На счете недостаточно средств")

###___4.4.17___###

class User:

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def name_is_valid(self, name):
        return name and isinstance(name, str) and name.isalpha()

    def age_is_valid(self, age):
        return age and isinstance(age, int) and 0<=age<=110

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        if self.name_is_valid(name):
            self._name = name
        else:
            raise ValueError("Некорректное имя")

    def set_age(self, age):
        if self.age_is_valid(age):
            self._age = age
        else:
            raise ValueError("Некорректный возраст")


###___4.5.13___###

class Rectangle:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.calculate_parameters()

    def set_length(self, length):
        self._length = length
        self.calculate_parameters()

    def get_length(self):
        return self._length

    def set_width(self, width):
        self._width = width
        self.calculate_parameters()

    def get_width(self):
        return self._width

    def calculate_parameters(self):
        self.perimeter = (self._length + self._width) * 2
        self.area = self._length * self._width


###___4.5.14___###

class HourClock:

    def __init__(self, hours):
        self.hours = hours

    def set_hours(self, hours):
        if isinstance(hours, int) and 1 <= hours <= 12:
            self._hours = hours
        else:
            raise ValueError("Некорректное время")

    def get_hours(self):
        return self._hours

    hours = property(get_hours, set_hours)


###___4.5.15___###

class Person:
    def __init__(self,name, surname):
        self.name = name
        self.surname = surname


    def get_fullname(self):
        return self._name+" "+self._surname

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname
    def set_fullname(self, info):
        self._name, self._surname = info.split()

    def set_name(self,name):
        self._name = name

    def set_surname(self,surname):
        self._surname = surname

    fullname = property(get_fullname, set_fullname)
    name = property(get_name, set_name)
    surname = property(get_surname, set_surname)



###___4.6.13___###

class Person:
    def __init__(self,name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def fullname(self):
        return self._name+" "+self._surname

    @fullname.setter
    def fullname(self, fullname):
        self._name, self._surname = fullname.split()


###___4.6.14___###
def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10 ** 9

class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password


    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError("Изменение логина невозможно")

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = hash_function(password)

###___4.6.15___###

import math
from math import sqrt


class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.b ** 2 - 4 * self.a * self.c

    @property
    def x1(self):
        if self.d < 0:
            return None
        else:
            return (-self.b - sqrt(self.d)) / (2 * self.a)

    @property
    def x2(self):
        if self.d < 0:
            return None
        else:
            return (-self.b + sqrt(self.d)) / (2 * self.a)

    @property
    def view(self):
        if self.a == 0:
            aa = "0x^2"
        else:
            aa = str(self.a) + "x^2"
        if self.b == 0:
            bb = " + 0x"
        elif self.b < 0:
            bb = f" - {str(abs(self.b))}x"
        else:
            bb = f" + {str(self.b)}x"

        if self.c == 0:
            cc = f" + 0"
        elif self.c < 0:
            cc = f" - {str(abs(self.c))}"
        else:
            cc = f" + {str(abs(self.c))}"

        return aa + bb + cc

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, coefficients):
        self.a = coefficients[0]
        self.b = coefficients[1]
        self.c = coefficients[2]
        self.d = self.b ** 2 - 4 * self.a * self.c

###___4.6.15___###

class Color:

    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    @hexcode.setter
    def hexcode(self,hexcode):
        self._hexcode = hexcode
        self._r = int(hexcode[0:2], 16)
        self._g = int(hexcode[2:4], 16)
        self._b = int(hexcode[4:6], 16)


###___4.7.11___###

class Circle:

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)


###___4.7.12___###

class Rectangle:

    def __init__(self,length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)


###___4.7.13___###
from math import sqrt


class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.b ** 2 - 4 * self.a * self.c

    @property
    def x1(self):
        if self.d < 0:
            return None
        else:
            return (-self.b - sqrt(self.d)) / (2 * self.a)

    @property
    def x2(self):
        if self.d < 0:
            return None
        else:
            return (-self.b + sqrt(self.d)) / (2 * self.a)

    @classmethod
    def from_iterable(cls, iterable):
        return cls(iterable[0], iterable[1],iterable[2])

    @classmethod
    def from_str(cls,string):
        a, b, c = string.split()
        return cls(float(a), float(b), float(c))


###___4.7.14___###

class Pet:
    list_of_pets =[]
    def __init__(self,name):
        self._name = name
        Pet.list_of_pets.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        Pet.list_of_pets.append(self)

    @classmethod
    def first_pet(cls):
        if cls.list_of_pets:
            return cls.list_of_pets[0]
        else:
            cls.data = None

    @classmethod
    def last_pet(cls):
        if cls.list_of_pets:
            return cls.list_of_pets[-1]
        else:
            cls.data = None

    @classmethod
    def num_of_pets(cls):
        return len(cls.list_of_pets)


###___4.7.15___###

class StrExtension:

    def remove_vowels(string: str):
        aaa = string
        for c in "aeiouy":
            aaa = aaa.replace(c, "").replace(c.upper(), "")
        return aaa

    def leave_alpha(string: str):
        rezult=""
        for c in string:
            if c.isalpha():
                rezult +=c
        return rezult

    def replace_all(string:str, chars:str, char:str):
        aaa = string
        for c in chars:
            aaa = aaa.replace(c, char)
        return aaa

###___4.7.16___### CHILI!!!
class CaseHelper:

    @staticmethod
    def is_snake(string:str):
        patern="abcdefghijklmnopqrstuvwxyz_"
        return string[0] !="_" and all(map(lambda x:x in patern,string))

    @staticmethod
    def is_upper_camel(string:str):
        patern = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return string[0].isupper() and all(map(lambda x:x in patern, string))

    @staticmethod
    def to_snake(string:str):
        string = string[0].lower()+string[1:]
        while any(map(lambda x: x in string,"ABCDEFGHIJKLMNOPQRSTU")):
            for c in "ABCDEFGHIJKLMNOPQRSTU":
                if c in string:
                    num = string.find(c)
                    string = string[:num]+"_"+ string[num].lower()+string[num+1:]
        return string

    @staticmethod
    def to_upper_camel(string:str):
        string = string[0].upper()+string[1:]
        while "_" in string:
            num=string.find("_")
            string = string[:num] + string[num+1].upper() + string[num + 2:]
        return string

###___4.8.16___###

from functools import singledispatchmethod
class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError("Аргумент переданного типа не поддерживается")


    @process.register(int)
    @staticmethod
    def int_process(data):
        return data * 2

    @process.register(float)
    @staticmethod
    def float_process(data):
        return data * 2


    @process.register(str)
    @staticmethod
    def str_process(data):
        return data.upper()


    @process.register(list)
    @staticmethod
    def list_process(data):
        return sorted(data)


    @process.register(tuple)
    @staticmethod
    def tuple_process(data):
        return tuple(sorted(data))

###___4.8.17___###
class Negator:
    from functools import singledispatchmethod

    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @neg.register(int)
    @staticmethod
    def int_neg(data):
        return -data

    @neg.register(float)
    @staticmethod
    def float_neg(data):
        return -data

    @neg.register(bool)
    @staticmethod
    def float_neg(data):
        return not data

###___4.8.18___###

class Formatter:
    from functools import singledispatchmethod

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @staticmethod
    def int_format(data):
        print (f"Целое число: {data}")

    @format.register(float)
    @staticmethod
    def float_format(data):
        print (f"Вещественное число: {data}")

    @format.register(list)
    @staticmethod
    def float_format(data):
        print (f"Элементы списка: {str(data)[1:-1]}")


    @format.register(tuple)
    @staticmethod
    def float_format(data):
        print(f"Элементы кортежа: {str(data)[1:-1]}")

    @format.register(dict)
    @staticmethod
    def float_format(data):
        print(f"Пары словаря: {str([(i, j) for i, j in data.items()])[1:-1]}")


###___4.8.19___###_CHILI!!!
import datetime
from datetime import date, timedelta
class BirthInfo:
    from functools import singledispatchmethod
    import datetime


    @singledispatchmethod
    def __init__(self, data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _from_data_format(self, birth_date):
        self.birth_date = birth_date


    @__init__.register(str)
    def _from_data_format(self, birth_date):
        self.birth_date = datetime.date(*[int(i) for i in birth_date.split('-')])

    @__init__.register(list)
    def _from_data_format(self, birth_date):
        self.birth_date = date(year=birth_date[0], month=birth_date[1], day=birth_date[2])

    @property
    def age(self):
        now = date.today()
        delta = now-self.birth_date
        return delta.days // 365

