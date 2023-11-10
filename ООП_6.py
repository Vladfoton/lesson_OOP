'''

###__6.1.15__###

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        yield from (self.x, self.y, self.z)

###__6.1.16__###

class DevelopmentTeam:
    def __init__(self):
        self.junior = []
        self.senior = []

    def add_junior(self,*args):
        self.junior.extend(args)

    def add_senior(self,*args):
        self.senior.extend(args)

    def __iter__(self):
        yield from [(i, 'junior') for i in self.junior] + [(i, 'senior') for i in self.senior]

###__6.1.17__###

class AttrsIterator:
    def __init__(self, obj):
        self.iterator =iter(([(key, value) for key, value in obj.__dict__.items()] ))

    def __iter__(self):
        return self.iterator

    def __next__(self):
        return next(self.iterator)

###__6.1.18__###

class SkipIterator:
    def __init__(self, iterable, n):
        self.iterator =iter(iterable)
        self.skip = []
        try:
            while self.iterator:
                self.skip.append(next(self.iterator))
                for _ in range(n):
                    next(self.iterator)
        except StopIteration:
            self.skip = iter(self.skip)


    def __iter__(self):
        return self.skip

    def __next__(self):
        return next(self.skip)

###__6.1.19__###
from random import shuffle
class RandomLooper:

    def __init__(self, *args):
        self.list=[]
        for i in args:
            self.list.extend(i)
        shuffle(self.list)
        self.list = iter(self.list)


    def __iter__(self):
        return self.list

    def __next__(self):
        return next(self.list)

'''


###__6.1.20__###

class Peekable:
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def peek(self, default=StopIteration):
        try:
            return self.iterable[0]
        except:
            if default != StopIteration:
                return default
            else:
                raise StopIteration

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable:
            return self.iterable.pop(0)
        else:
            raise StopIteration


###__6.1.21__###

class LoopTracker:
    def __init__(self, iterable):
        self.iter = list(iterable)
        self.iterable = list(iterable)
        self.accesses1 = 0
        self.empty_accesses1 = 0

    @property
    def accesses(self):
        return self.accesses1

    @property
    def empty_accesses(self):
        return self.empty_accesses1

    @property
    def first(self):
        try:
            return self.iter[0]
        except:
            raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        try:
            return self.last_object
        except:
            raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        return len(self.iterable) == 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.is_empty():
            self.empty_accesses1 += 1
            raise StopIteration
        else:
            self.accesses1 += 1
            self.last_object = self.iterable.pop(0)
            return self.last


###__6.2.10__###

class ReversedSequence:
    def __init__(self, sequence):
        if isinstance(sequence, list):
            self.sequence = sequence
        else:
            self.sequence = list(sequence)

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, item):
        return self.sequence[len(self) - item - 1]

    def __setitem__(self, item, value):
        self.sequence = self.sequence.extend(value)

    def __iter__(self):
        yield from reversed(self.sequence)


###__6.2.11__###

class SparseArray:
    def __init__(self, default):
        self.default = default
        self.array = {}

    def __setitem__(self, key, value):
        self.array[key] = value

    def __getitem__(self, key):
        if key in self.array:
            return self.array[key]
        else:
            return self.default

    def __len__(self):
        return len(self.array)


###__6.2.12__###
from copy import copy


class CyclicList:

    def __init__(self, iterable):
        if isinstance(iterable, list):
            self.iterable = copy(iterable)
        else:
            self.iterable = list(iterable)

    def append(self, item):
        self.iterable.append(item)

    def __setitem__(self, key, value):
        self.iterable[key] = value

    def __getitem__(self, item):
        if item > len(self.iterable) - 1:
            return self.iterable[item % (len(self.iterable))]
        else:
            return self.iterable[item]

    def __len__(self):
        return len(self.iterable)

    def pop(self, key=-1):
        return self.iterable.pop(key)


###__6.2.13__###
from copy import deepcopy


class SequenceZip:
    def __init__(self, *items):
        self.items = deepcopy(items)
        self.len = len(items)
        if self.items:
            self.min_len = min(len(i) for i in items)
        else:
            self.min_len = 0

    @staticmethod
    def zip_zip(iterable, key):
        return tuple(j[key] for j in iterable)

    def __iter__(self):
        for i in range(self.min_len):
            yield self.zip_zip(self.items, i)

    def __len__(self):
        return self.min_len

    def __getitem__(self, key):
        return self.zip_zip(self.items, key)


###__6.2.14__###

class OrderedSet:
    def __init__(self, iterable=[]):
        self.iterable = {i: None for i in iterable}

    def add(self, key):
        self.iterable[key] = None

    def discard(self, key):
        if key in self.iterable:
            self.iterable.pop(key)

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        yield from list(self.iterable.keys())

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return tuple(self.iterable.keys()) == tuple(other.iterable.keys())
        elif isinstance(other, set):
            return sorted(self.iterable) == sorted(other)
        else:
            return NotImplemented


###__6.2.15__###
import copy


class AttrDict:
    def __init__(self, data: dict = {}):
        self.__dict__.update(copy.deepcopy(data))
        self.data = copy.deepcopy(data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        setattr(self, key, value)


###__6.2.16__###
import copy


class PermaDict:
    def __init__(self, data: dict = {}):
        self.data = copy.deepcopy(data)
        self.extradata = {}

    def keys(self):
        return list(self.data.keys()) + list(self.extradata.keys())

    def values(self):
        return list(self.data.values()) + list(self.extradata.values())

    def items(self):
        return [(key, value) for key, value in self.data.items()] + [(key, value) for key, value in
                                                                     self.extradata.items()]

    def __len__(self):
        return len(self.data) + len(self.extradata)

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return self.extradata[key]

    def __iter__(self):
        yield from self.data | self.extradata

    def __delitem__(self, key):

        if key in self.extradata:
            self.extradata.pop(key)

    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError('Изменение значения по ключу невозможно')
        self.extradata[key] = value


###__6.2.17__###
import copy


class HistoryDict:

    def __init__(self, data={}):
        self.data = {key: [value] for key, value in copy.deepcopy(data).items()}

    def keys(self):
        return list(self.data.keys()) if self.data else ""

    def values(self):
        return [i[-1] for i in self.data.values()] if self.data else ""

    def items(self):
        return [(key, value[-1]) for key, value in self.data.items()] if self.data else ""

    def __getitem__(self, item):
        if item in self.data:
            return self.data[item][-1]
        else:
            raise KeyError

    def __setitem__(self, item, value):
        if item in self.data:
            self.data[item].append(value)
        else:
            self.data[item] = [value]

    def __len__(self):
        return len(list(filter(lambda x: x[-1] != None, self.data.values())))

    def __iter__(self):
        yield from [i for i in self.data.keys()]

    def __delitem__(self, key):
        self.data.pop(key)

    def history(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return []

    def all_history(self):
        return {key: value for key, value in self.data.items()}


###__6.2.18__###
import copy


class MutableString:

    def __init__(self, string: str = ""):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.string}')"

    def __len__(self):
        return len(self.string)

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()

    def __iter__(self):
        yield from list(self.string)

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.string + other.string)

    def __setitem__(self, key, value):
        temp = list(self.string)
        temp[key] = value

        self.string = "".join(temp)

    def __getitem__(self, key):
        temp = list(self.string)
        if isinstance(key, slice):
            return MutableString("".join(temp[key]))
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        return MutableString("".join(temp[key]))

    def __delitem__(self, key):
        if isinstance(key, slice):
            temp = list(self.string)
            del temp[key]
            self.string = "".join(temp)
        if isinstance(key, int):
            temp = list(self.string)
            self.string = "".join(temp[:key] + temp[key + 1:])


###__6.2.18__###

class Grouper:

    def __init__(self, iteable, key):
        self.groups = {}
        self.key = key
        for item in copy.deepcopy(iteable):
            if key(item) in self.groups:
                self.groups[key(item)].append(item)
            else:
                self.groups[key(item)] = [item]

    def add(self, item):
        if self.key(item) in self.groups:
            self.groups[self.key(item)].append(item)
        else:
            self.groups[self.key(item)] = [item]

    def group_for(self, item):
        return self.key(item)

    def __len__(self):
        return len(self.groups)

    def __iter__(self):
        yield from ((key, values) for key, values in self.groups.items())

    def __getitem__(self, item):
        return self.groups[item]

    def __contains__(self, item):
        return item in self.groups


###__6.3.13__###

def print_file_content(filename: str):
    try:
        f = open(filename, "r", encoding='utf-8')
        with f:
            string = f.read()
            while string:
                print(str(string))
                string = f.read()

    except:
        print("Файл не найден")


###__6.3.14__###

def non_closed_files(files: list):
    return list(filter(lambda x: not x.closed, files))


###__6.3.15__###

def log_for(logfile: str, date_str: str):
    with open(logfile, "r", encoding='utf-8') as input_file, \
            open(f"log_for_{date_str}.txt", "w", encoding='utf-8') as output_file:
        string = input_file.readline()
        while string:
            date = string[:10]
            info = string[11:]
            if date == date_str:
                output_file.write(f'{info}')
            string = input_file.readline()


###__6.4.21__###


def is_context_manager(obj):
    return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')


###__6.5.5__###

class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return True


###__6.5.6__###

class Greeter:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, *args, **kwargs):
        print(f"До встречи, {self.name}!")
        return True


###__6.5.7__###

class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):

        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
            return True
        except:
            print("Незакрываемый объект")
            return True


###__6.5.8__###

class ReadableTextFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, mode='r', encoding='utf-8')
        self.text = [x[:-1] if '\n' in x else x for x in self.file.readlines()]
        return self.text

    def __exit__(self, *args, **kwargs):
        self.file.close()


###__6.5.9__###

class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.text = self.file.readlines()
        return self.text

    def __exit__(self, *args, **kwargs):
        self.file.close()


###__6.5.10__###
import sys


class UpperPrint:

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.upper

    def upper(self, text):
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write


###__6.5.11__###

class Suppress:
    def __init__(self, *args):
        self.exception_list = args

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("*",exc_type,"**", exc_val,"***",exc_tb, sep = "\n")
        if exc_type in self.exception_list:
            # print(exc_val, type(exc_val))
            self.exception = exc_val
            return True

        else:
            self.exception = None
            return False


###__6.5.12__###  ##SPICE##

class WriteSpy:
    def __init__(self,file1, file2, to_close:bool=False):
        self.to_close = to_close
        self.file2 = file2
        self.file1 = file1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file1.close()
        self.file2.close()



    def write(self,text):
        self.file1.write(text)
        self.file2.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        return self.file1.writable() and self.file2.writable()

    def closed(self):
        return self.file1. and self.file2.close()




if __name__ == '__main__':
    f1 = open('file1.txt', mode='w')
    f2 = open('file2.txt', mode='w')

    with WriteSpy(f1, f2, to_close=True) as combined:
        print(combined.closed())
        f1.close()
        print(combined.closed())
        f2.close()
        print(combined.closed())