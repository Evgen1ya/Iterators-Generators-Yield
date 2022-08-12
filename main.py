from collections.abc import Iterable

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f','h',False],
    [1, 2, None],
]

print('---------' + 'Задачие 1'+ '---------' + '\n')
class FlatIterator:
    def __init__(self, list_):
        self.list_ = list_
        self.cursor = -1
        self.list_len = len(self.list_)

    def __iter__(self):
        self.cursor += 1
        self.nested_cursor = 0
        return self

    def __next__(self):
        while self.cursor - self.list_len and self.nested_cursor == len(self.list_[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nested_cursor += 1
        return self.list_[self.cursor][self.nested_cursor - 1]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


print('\n' + '---------' + 'Задачие 2'+ '---------' + '\n')

def flat_generator(nested_list):
    for item in nested_list:
        for el in item:
            yield el

for item in flat_generator(nested_list):
    print(item)

print('\n' + '---------' + 'Задачие 3'+ '---------' + '\n')

nested_list_2 = [[5, 3, [2, [1, 2]]],
    [
    ['a', 'b', 'c'],
    ['d', 'e', 'f','h',False],
    [1, 2, None],
], [3, 4]
    ]

class FlatIter:
    def __init__(self, list_):
        self.list_ = list_
        self.cursor = -1
        self.list_len = len(self.list_)

    def __iter__(self):
        self.cursor += 1
        self.nested_cursor = 0
        self.nested_cursor_2 = -1
        return self

    def __next__(self):
            while self.cursor - self.list_len and self.nested_cursor == len(self.list_[self.cursor]):
                iter(self)
            if self.cursor == self.list_len:
                raise StopIteration
            self.nested_cursor += 1
            self.nested_cursor_2 += 1
            try:
                return self.list_[self.cursor][self.nested_cursor - 1][self.nested_cursor_2 - 1]
            except:
                return self.list_[self.cursor][self.nested_cursor - 1]


for item in FlatIter(nested_list_2):
    print(item)


print('\n' + '---------' + 'Задачие 4'+ '---------' + '\n')


def flat_gen(nested_list_2, ignore_types=(str)):
    for x in nested_list_2:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flat_gen(x)
        else:
            yield x

for item in flat_gen(nested_list_2):
    print(item)

