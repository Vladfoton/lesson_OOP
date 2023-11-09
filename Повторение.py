#### 2.1.4#########
#from builtins import function


def darts(n: int) -> None:
    def fit(matrix, n: int, start: int):
        for row in range(start, start+n):
            for col in range(start, start+n):
                matrix[row][col] = start + 1
        return matrix

    def create_matrix(n):
        matrix=[]
        for i in range(n):
            temp = [1 for _ in range(n)]
            matrix.append(temp)
        return matrix

    rezult = create_matrix(n)
    for num in range (1, n//2+1):
        rezult=fit(rezult, n-2*num, num)

    for i in range(n):
        print(*rezult[i])

# darts(18)

###2.1.5##########
def is_brackets_correct(string:str) -> bool:
    counter = 0
    for ch in string:
        if ch == "(":
            counter += 1
        if ch == ")":
            counter -= 1
        if counter <0:
            return False
    if counter == 0:
        return True
    else:
        return False

# print(is_brackets_correct(input()))

#########

#####2.1.6############

def inversions(sequence: list) -> int:
    count=0
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            if sequence[i] > sequence[j]:
                count+=1
    return count
# sequence = [4, 3, 2, 1]
#
# print(inversions(sequence))

###########

######2.1.7##########
import sys
def pokemons():
    list1 = [i.strip() for i in sys.stdin]
    return len(list1) - len(set(list1))

#print(pokemons())



###########

######2.1.9##########

import sys
def coords():
    list1 = [i.strip() for i in sys.stdin]
    for poz in list1:
        x,y = poz[1:-1].split(", ")
        print(abs(float(x)) <= 90 and abs(float(y)) <= 180)

#coords()

###########

######2.1.10##########

def quantify(iterable: list, predicate):
    count=0
    for i in iterable:
        if not predicate:
            predicate = bool
        count += predicate(i)
    return count

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(quantify(numbers, lambda x: x > 1))
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(quantify(numbers, lambda x: x % 2 == 0))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(quantify(numbers, lambda x: x < 0))

def pycon():
    import calendar
    import datetime
    year = int(input())
    month = int(input())
    # currdata = datetime.datetime(year, month)
    days = [i[3] for i in calendar.monthcalendar(year, month)]
    if not days[0]:
        days.pop(0)
    currdate = datetime.date(year=year, month=month, day=days[3])
    print(currdate.strftime("%d.%m.%Y"))

# pycon()

def is_integer(string):
    if string[0] =="-":
        string = string[1:]
    for c in string:
        if not c.isdigit():
            return False
    else:
        return True
# print(is_integer('199'))
# print(is_integer('-43'))
# print(is_integer('5f'))
# print(is_integer('5.0'))
# print(is_integer('1.1'))

def is_decimal(string):
    try:
        float(string)
        return True
    except:
        return False

# print(is_decimal('100'))
# print(is_decimal('199.1'))
# print(is_decimal('-0.2'))
# print(is_decimal('.-95'))
# print(is_decimal('-.95'))
# print(is_decimal('.10'))

def is_fraction(string):
    import re
    fff="^-?[0123456789]{1,}\/0*?[123456789][0123456789]*$"
    if re.match(fff, string):
        return True
    else:
        return False

# print(is_fraction('1000/1'))
# print(is_fraction('-54/9'))
# print(is_fraction('71'))
# print(is_fraction('1 / 82'))
# print(is_fraction('1/0'))
# print(is_fraction('3/-7'))

def intersperse(iterable:iter, delimiter: str):
    if iterable:
        iter1 = iter(iterable)
        c=next(iter1)
        try:
            while True:
                yield c
                c = next(iter1)
                yield delimiter
        except:
            pass


# print(*intersperse([1, 2, 3], 0))
#
# inter = intersperse('beegeek', '!')
# print(next(inter))
# print(next(inter))
# print(*inter)
#
# iterable = iter('Beegeek')
#
# print(*intersperse(iterable, '+'))
#
# print(*intersperse('A', '...'))
#
# print(*intersperse([], 100))

def annual_return(start:int, percent:int, years:int):
    for _ in range(years):
        start += start*percent/100
        yield start

# for value in annual_return(70000, 8, 10):
#     print(round(value))

def pluck(data: dict, path:str, default=None):

    path = [i for i in path.split(".")]

    def get_data(data:dict, path:list, default = default):
        if len(path) == 1:
            try:
                rezult = data[path[0]]
                return rezult
            except KeyError:
                return default

        else:
            key = path.pop(0)
            if isinstance(data[key], dict):
                return get_data(data[key], path, default)
            else:
                return data[key]
    return get_data(data, path, default)


# d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
#
# print(pluck(d, 'x'))
#
# dd = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
#
# print(pluck(dd, 'a.b'))
#
# d = {'a': {'b': {'c': {'d': {'e': 4}}}}}
#
# print(pluck(d, 'a.b.c'))

def recviz(funct, count=0):
    funct.recursion_counter = 0
    def wrapper(*args, **kwargs):

        def add_k(obj):  # если строка добавить кавычки
            if isinstance(obj, str):
                return "'" + obj + "'"
            else:
                return str(obj)
        def create_arguments_string(args, kwargs):
            rez=""
            if args:
                args = list(args)
                c=args.pop(0)
                rez = add_k(c)
                for c in args:
                    rez +=f", {add_k(c)}"
            for key, values in kwargs.items():
                rez += f", {key}={add_k(values)}"
            return rez
        print(f"{'    '*funct.recursion_counter}-> {funct.__name__}({create_arguments_string(args, kwargs)})")
        funct.recursion_counter += 1
        rez=funct(*args, **kwargs)
        funct.recursion_counter -=1
        print(f"{'    '*funct.recursion_counter}<- {add_k(rez)}")

        return rez
    return wrapper


# @recviz
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# fib(4)
#
#
# @recviz
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# fact(5)


class ElectricCar:
    pass


car = ElectricCar()

car.color = 'black'

delattr(car, 'color')

print(getattr(car, 'color', None))
print(car.__dict__)





