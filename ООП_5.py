####__5.1.15__####

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
    def __init__(self):
        self.program_name = "GenerationPy"
        self.environment = "release"
        self.loglevel = "verbose"
        self.version = "1.0.0"


####__5.2.13__####
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'


####__5.2.14__####

class Rectangle:

    def __init__(self, length, width):
        self.width = width
        self.length = length

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


####__5.2.15__####

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


####__5.2.16__####


class IPAddress:
    from functools import singledispatchmethod

    @singledispatchmethod
    def __init__(self, data):
        raise TypeError("data must be string , list or tuple")

    @__init__.register(str)
    def string(self, data):
        self.ip = data

    @__init__.register(list)
    @__init__.register(tuple)
    def iterable(self, data):
        self.ip = ".".join([str(i) for i in data])

    def __str__(self):
        return self.ip

    def __repr__(self):
        return f"{type(self).__name__}('{self.ip}')"

####__5.2.17__####

class PhoneNumber:

    def __init__(self, phone_number:str):
        self.phone_number = phone_number.replace(" ", "")

    def __str__(self):
        return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"

    def __repr__(self):
        return f"{type(self).__name__}('{self.phone_number}')"


####__5.2.18__####

class AnyClass:
    def __init__(self, *args, **kwargs):
        self.dict_data = kwargs
        for key, value in self.dict_data.items():
            setattr(self, key, value)



    def __str__(self):
        return f"{type(self).__name__}: {', '.join([f'{i}={str([j])[1: -1] if isinstance(j,str) else j}' for i,j in self.dict_data.items()])}"

    def __repr__(self):
        return f"{type(self).__name__}({', '.join([f'{i}={str([j])[1: -1] if isinstance(j,str) else j}' for i,j in self.dict_data.items()])})"



####__5.3.11__####

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other,Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented


    def __repr__(self):
        return f'{type(self).__name__}({self.x}, {self.y})'

####__5.3.18__####
from functools import total_ordering

@total_ordering
class Word:
    def __init__(self,word:str):
        self.word = word

    def __repr__(self):
        return f"{type(self).__name__}('{self.word}')"

    def __str__(self):
        return f'{self.word.lower().capitalize()}'

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Word):
            return len(self.word) <= len(other.word)
        return NotImplemented


####__5.3.19__####
from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year:int, month:int):
        self.year = year
        self.month = month

    def __repr__(self):
        return f'{type(self).__name__}({self.year}, {self.month})'

    def __str__(self):
        return f'{self.year}-{self.month}'

    @staticmethod
    def converter(other):
        if isinstance(other,Month):
            return other
        elif isinstance(other,tuple) and len(other) ==2:
            return Month(other[0], other[1])
        else:
            return None

    def __eq__(self, other):
        other = self.converter(other)
        return self.month == other.month and self.year == other.year if other else NotImplemented

    def __lt__(self,other):
        other = self.converter(other)
        if other:
            if self.year == other.year:
                return self.month < other.month
            else:
                return self.year < other.year
        else:
            return NotImplemented

    def __le__(self,other):
        other = self.converter(other)
        if other:
            if self.year == other.year:
                return self.month <= other.month
            else:
                return self.year < other.year
        else:
            return NotImplemented

####__5.3.20__####

from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version:str):
        temp = [int(i) for i in version.split(".")]
        self.version =[0, 0, 0]
        try:
            self.version[0] = temp[0]
            self.version[1] = temp[1]
            self.version[2] = temp[2]
        except IndexError:
            pass

    def __str__(self):
        return f'{".".join(map(str, self.version))}'

    def __repr__(self):
        return f'{type(self).__name__}({str([".".join(map(str, self.version))])[1:-1]})'

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.version < other.version
        else:
            return NotImplemented



####__5.4.10__####

class ReversibleString:
    def __init__(self, string:str):
        self.string = string

    def __str__(self):
        return self.string

    def __neg__(self):
        return ReversibleString(self.string[::-1])

####__5.4.11__####

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'{str(self.amount)} руб.'
    def __pos__(self):
        return Money((-(self.amount <= 0) + (self.amount >= 0)) * self.amount)

    def __neg__(self):
        return Money((-(self.amount >= 0) + (self.amount <= 0)) * self.amount)


####__5.4.12__####
from math import sqrt
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{type(self).__name__}({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __pos__(self):
        return Vector(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)

####__5.4.13__####

class ColoredPoint:
    def __init__(self, x, y, color = (0,0,0)):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f'{type(self).__name__}({self.x}, {self.y}, {self.color})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __pos__(self):
        return self.__class__(self.x, self.y, self.color)

    def __neg__(self):
        return self.__class__(-self.x, -self.y, self.color)

    def __invert__(self):
        return self.__class__(self.y, self.x, (255-self.color[0], 255-self.color[1], 255-self.color[2]))


####__5.4.14__####__CHILI___CHILI___!!!!!!!!!!!!

class Matrix:
    def __init__(self, rows:int, cols:int, value = 0):
        self.value =value
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[-1].append(value)
        self.matrix = matrix
        self.rows = rows
        self.cols = cols

    def __repr__(self):
        return f'{self.__class__.__name__}({self.rows}, {self.cols})'

    def __str__(self):
        result=""
        for row in range(self.rows):
            result+=" ".join(map(str, self.matrix[row]))
            result+="\n"
        result = result[:-1]
        return result


    def get_value(self,row, col):
        return self.matrix[row][col]

    def set_value(self,row, col, value):
        self.matrix[row][col] = value

    def __pos__(self):
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.set_value(row, col, self.matrix[row][col])
        return result

    def __neg__(self):
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.set_value(row, col, -self.matrix[row][col])
        return result

    def __invert__(self):
        result = Matrix(self.cols, self.rows)
        for row in range(result.rows):
            for col in range(result.cols):
                result.set_value(row, col, self.matrix[col][row])
        return result

    def __round__(self, n=None):
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.set_value(row, col, round(self.matrix[row][col], n))
        return result

####__5.5.9__####

class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return self.__class__(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates )
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other,int|float):
            return self.__class__(self.proteins * other, self.fats * other, self.carbohydrates * other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other,int|float):
            return self.__class__(self.proteins / other, self.fats / other, self.carbohydrates / other)
        else:
            return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other,int|float):
            return self.__class__(self.proteins // other, self.fats // other, self.carbohydrates // other)
        else:
            return NotImplemented

####__5.5.10__####

class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int|float):
            return self.__class__(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int|float):
            return self.__class__(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int|float):
            return self.__class__(self.x / other, self.y / other)
        else:
            return NotImplemented

####__5.5.11__####

class SuperString:
     def __init__(self, string:str):
         self.string = string

     def __str__(self):
         return f'{self.string}'

     def __add__(self, other):
         if isinstance(other, SuperString):
             return self.__class__(self.string + other.string)
         else:
             return NotImplemented

     def __mul__(self, other):
         if isinstance(other, int | float):
             return self.__class__(self.string * other)
         else:
             return NotImplemented

     def __rmul__(self, other):
         if isinstance(other, int | float):
             return self.__class__(self.string * other)
         else:
             return NotImplemented

     def __truediv__(self, other):
         if isinstance(other, int | float):
             return self.__class__(self.string[:len(self.string) // other])
         else:
             return NotImplemented

     def __lshift__(self, n):
         if isinstance(n, int | float):
             if 0 < n < len(self.string):
                 return self.__class__(self.string[:-n])
             elif n == 0:
                 return self.__class__(self.string)
             else:
                 return self.__class__("")
         else:
             return NotImplemented

     def __rshift__(self, n):
         if isinstance(n, int | float):
             if 0 < n < len(self.string):
                 return self.__class__(self.string[n:])
             elif n == 0:
                 return self.__class__(self.string)
             else:
                 return self.__class__("")
         else:
             return NotImplemented


####__5.5.20__####

class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes =self.check_time(hours, minutes)
    @staticmethod
    def check_time(hours, minutes):
        if hours >=24:
            hours1 = hours % 24
        else:
            hours1 = hours
        if minutes >=60:
            minutes1 = minutes % 60
            hours1 += minutes // 60
        else:
            minutes1 = minutes
        return hours1, minutes1

    def __str__(self):
        return f'{self.hours if self.hours>9 else "0"+str(self.hours)}:{self.minutes if self.minutes>9 else "0"+str(self.minutes)}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            # hours, minutes = self.check_time(self.hours + other.hours, self. minutes + other.minutes)
            return self.__class__(self.hours + other.hours, self. minutes + other.minutes)
        else:
            return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            hours, minutes = self.check_time(self.hours + other.hours, self. minutes + other.minutes)
            self.hours = hours
            self.minutes = minutes
            return self
        else:
            return NotImplemented

####__5.5.21__####

class Queue:
    from functools import singledispatchmethod
    def __init__(self, *args):
        self.queue = list(args)

    def __str__(self):
        return f'{" -> ".join(map(str,self.queue))}'

    def __iadd__(self, *args):
        if isinstance(args[0], self.__class__):
            self.queue.extend(args[0].queue)
            return self
        else:
            return NotImplemented

    def __add__(self, *args):
        if isinstance(args[0], self.__class__):
            self.queue.extend(args[0].queue)
            result = self.__class__()
            result.queue = self.queue
            return result
        else:
            return NotImplemented

    def add(self, *args):
        if isinstance(args, self.__class__):
            self.queue.extend(args.queue)
            return self
        elif isinstance(args, tuple|list):
            return self.__class__(self.queue.extend(list(args)))
        else:
            return NotImplemented


    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def __rshift__(self, n):
        if isinstance(n, int | float):
            result = self.__class__()
            if 0 < n < len(self.queue):
                result.queue = self.queue[n:]
                return result
            elif n == 0:
                result.queue = self.queue
                return result
            else:
                return self.__class__("")
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.queue == other.queue

####__5.6.9__####

class Calculator:
    def __call__(self, a, b, operation):
        try:
            return eval(f"{a}{operation}{b}")
        except ZeroDivisionError:
            raise ValueError("Деление на ноль невозможно")

####__5.6.10__####

class RaiseTo:

    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x:int| float):
        return x ** self.degree

####__5.6.11__####
from random import randint
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randint(1,self.sides)


####__5.6.12__####

class QuadraticPolynomial:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __call__(self,x):
        return self.a * x**2 + self.b * x + self.c

####__5.6.13__####

class Strip:

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)

####__5.6.14__####

class Filter:
    def __init__(self, predicate=None):
        self.predicate = predicate or bool

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))


####__5.6.15__####
from datetime import date
class DateFormatter:
    formats = __data = {
        "ru": r"%d.%m.%Y",
        "us": r"%m-%d-%Y",
        "ca": r"%Y-%m-%d",
        "br": r"%d/%m/%Y",
        "fr": r"%d.%m.%Y",
        "pt": r"%d-%m-%Y"
        }
    def __init__(self, country_code):
        self.format =self.formats[country_code]


    def __call__(self,d:date):
        return d.strftime(self.format)

####__5.6.16__####

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self,*args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

####__5.6.17__####

class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache ={}

    def __call__(self, *args):
        if (args) in self.cache:
            return self.cache[(args)]
        else:
            self.cache[(args)] = self.func(*args)

            return self.cache[(args)]


@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


####__5.6.18__####__CHILI___###

class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, obj):
        return tuple( getattr(obj, i) for i in self.args)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


####__5.7.10__###
from math import sqrt
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int (sqrt(self.x * self.x + self.y * self.y))

    def __float__(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def __complex__(self):
        return complex (self.x, self.y)


####__5.7.11__###

class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 9 / 5) +32

    def from_fahrenheit(temperature):
        return Temperature((temperature - 32) * 5 / 9)

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

####__5.7.12__###__CHILI___CHILI___!!!___####
from functools import total_ordering
@total_ordering
class RomanNumeral:
    _roman = {'IV': 4,
              'IX': 9,
              'XL': 40,
              'XC': 90,
              'CD': 400,
              'CM': 900,
               'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000
              }
    _decimal = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
               20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC',
               300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M'}
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'
        # return f'{self.number}, {self.from_roman(self.number)} , {self.from_decimal(self.from_roman(self.number))}'

    def __int__(self):
        return self.from_roman(self.number)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.from_roman(self.number) == self.from_roman(other.number)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.from_roman(self.number) < self.from_roman(other.number)
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            summ = self.from_roman(self.number) + self.from_roman(other.number)
            return self.__class__(self.from_decimal(summ))
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            sub = self.from_roman(self.number) - self.from_roman(other.number)
            return self.__class__(self.from_decimal(sub))
        else:
            return NotImplemented



    @staticmethod
    def from_roman(number:str):
        result = 0
        while number:
            if number[:2] in RomanNumeral._roman:
                result += RomanNumeral._roman[number[:2]]
                number = number[2:]
            elif number[:1] in RomanNumeral._roman:
                result += RomanNumeral._roman[number[:1]]
                number = number[1:]
        return result

    @staticmethod
    def from_decimal(number:int):
        _decimal = RomanNumeral._decimal
        result = ""
        d1000 = number // 1000
        if d1000:
            number = number % 1000
        d100 = number // 100
        if d100:
            number = number % 100

        d10 = number // 10
        if d10:
            number = number % 10

        d1 = number
        return _decimal[1000]*d1000 + _decimal[100 * d100] + _decimal[10 * d10] + _decimal[d1]


####__5.8.8__###

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return object.__getattribute__(self, 'price') * object.__getattribute__(self, 'quantity')
        elif name == 'name':
            return object.__getattribute__(self, name).title()
        else:
            return object.__getattribute__(self, name)

####__5.8.9__###

class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.__dict__[name] = value

    def __delattr__(self, item):
        print(f'Удаление атрибута {item}')
        del self.__dict__[item]


####__5.8.10__###

class Ord:
    def __getattribute__(self, item):
        return ord(item)

####__5.8.11__###

class DefaultObject:
    def __init__(self, default=None, **kwards):
        self.default = default
        for key, value in kwards.items():
            self.__dict__[key] = value

    def __getattr__(self, item):
        return self.default

####__5.8.12__###

class NonNegativeObject:
    def __init__(self,**kwards):
        for key, value in kwards.items():
            if isinstance(value, int|float) and value < 0:
                value = -value
            self.__dict__[key] = value

####__5.8.13__###

class AttrsNumberObject:

    def __init__(self, **kwards):
        self.attrs_num=0
        for a, v in kwards.items():
            self.__setattr__(a, v)


    def __setattr__(self, key, value):
        self.__dict__[key] = value
        self.__dict__['attrs_num'] +=1

    def __delattr__(self, item):
        self.__dict__['attrs_num'] -= 1
        self.__dict__.pop(item)

####__5.8.14__###

class Const:

    def __init__(self, **kwards):
        self.__dict__.update(kwards)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value
        else:
            raise AttributeError('Изменение значения атрибута невозможно')

    def __delattr__(self, key):
        raise AttributeError('Удаление атрибута невозможно')

####__5.8.15__###

class ProtectedObject:

    def __init__(self, **kwards):
        for k, v in kwards.items():
            object.__setattr__(self, k, v)


    def __setattr__(self, key, value):
            if key[0] == "_":
                raise AttributeError('Доступ к защищенному атрибуту невозможен')
            else:
                object.__setattr__(self, key, value)

    def __getattribute__(self, key):
        if key[0] == "_":
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            return object.__getattribute__(self, key)


    def __delattr__(self, key):
        if key[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__delattr__(self, key)

####__5.9.24__###

def hash_function(obj):
    result1=0
    result2=0
    obj = str(obj)
    for i in range(len(obj)//2):
        result1+=ord(obj[i]) * ord(obj[-1-i])
    if len(obj) % 2 == 1:
        result1+=ord(obj[len(obj)//2])

    for i in range(len(obj)):
        result2 += ((-1)**i) * ord(obj[i]) * (i+1)


    return (result1 * result2) % 123456791

# print(hash_function('python'))

####__5.9.24__###  __CHILI!!!___###

def limited_hash(left:int, right:int, hash_function = hash):

    def funct(obj):
        hash = hash_function(obj)
        if hash > right:
            while hash > right:
                hash = left + hash - right-1

        if hash < left:
            while hash < left:
                hash = hash - left + right + 1
        return hash

    return funct

####__5.10.13__####

class ColoredPoint:

    def __init__(self, x, y, color = (0,0,0)):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y}, '{self.color}')"


    @property
    def atributes(self):
        return (self.x, self.y, self.color)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)
        else:
            raise AttributeError


    def __getattribute__(self, key):
        return object.__getattribute__(self, key)

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.atributes == other.atributes
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.atributes)

####__5.10.14__####

class Row:
    closed = True
    def __init__(self, **kwargs):
        # object.__setattr__(self, "closed", True)
        self.__dict__.update(kwargs)
        self.close()
    @classmethod
    def close(cls):
        cls.closed = False

    def __repr__(self):
        string = ", ".join([f'{key}={str([value])[1:-1]}' for key, value in self.__dict__.items()])
        return f'{self.__class__.__name__}({string})'

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            if self.closed:
                object.__setattr__(self, key, value)
            else:
                raise AttributeError("Установка нового атрибута невозможна")
        else:
            raise AttributeError('Изменение значения атрибута невозможно')

    def __delattr__(self, key):
        raise AttributeError('Удаление атрибута невозможно')


    def __getattribute__(self, key):
        return object.__getattribute__(self, key)

    @property
    def atributes(self):
        return tuple([(key, value) for key, value in self.__dict__.items()])

    def __eq__(self, other):
        if isinstance(other, Row):
            return self.atributes == other.atributes
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.atributes)



