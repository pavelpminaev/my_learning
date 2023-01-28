"""
('app', [ # Корень
    ('dist', [ # Внутренний узел
        ('index.html'), # Лист
        ('main.py') # Лист
    ]),
    ('index.py'), # Лист
    ('assets', [ # Внутренний узел
        ('favicon.ico'), # Лист
        ('app.css'), # Лист #
    ]),
])
"""
#                  app
#          /        |         \
#        dist    index.py   assets
#       /    \             /     \
# index.html main.py   favicon.ico app.css

"""
{
    "value": 5,
    "children": [
        {"value": 10},
        {"value": 100},
        {"value": "nested", "children": []}
    ]
}
"""


from colorama import init, Fore
init(autoreset=True)


print(Fore.GREEN + 'About CHAIN')



from itertools import chain
a = 'AB', 'BCD'
b = 'DEF'
c = 'A', 'CD'
print(list(chain(a)))
print(list(chain(a, b, c)))

print(list(chain.from_iterable(c)))

li = ['123', '456', '789']
res = list(map(int, list(chain.from_iterable(li))))
sum_of_li = sum(res)
print("Sum of '123', '456', '789' =", sum_of_li, end='\n\n')



print(Fore.GREEN + 'About lambda')

List = [[2, 3, 4], [16, 4, 1, 64], [12, 6, 9, 3]]
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
# Get the second largest element
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)


# filter out all odd numbers
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
ages.sort() # just for sort
adult = list(filter(lambda age: age > 18, ages))
print(Fore.YELLOW + "It's adult people with 'filter()': ", adult)

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(Fore.YELLOW + "It's a double numers in the list with map():", final_list)

# Max number for couple of numbers whit lambda
Max = lambda a, b: a if (a > b) else b
print(Max(1, 2))

# python code to demonstrate working of reduce()
# with a lambda function
# importing functools for reduce()
import functools
# initializing list
lis = [1, 3, 5, 6, 2, ]
# using reduce to compute maximum element from list
print(Fore.RED + "The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis), end='\n\n')


print(Fore.GREEN + 'Example with ISINSTANCE()')
test_list = [1, 2, 3]
print ("Is test_list list? : " + str(isinstance(test_list, list)), end='\n\n')  # True


print(Fore.GREEN + 'Removing levels in trees')
tree1 = [[5], 1, [3, 4]]
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
def remove_first_level(tree_list):
    children = filter(lambda item: isinstance(item, list), tree_list)
    return list(chain(*children))
tree3 = list(chain(tree1, tree2))
print('Demonstrate working of chain(tree1, tree2) function. Our tree =>', tree3)
print('Our tree without first level =>', remove_first_level(tree3))



massiv = [3, 4, 5, 4, 6, 1, 1, 8, 1, 2, 3]

def dublicate(massiv):
    resalt = []
    i = 0
    my_set = set(massiv)
    while i < len(massiv):
        if massiv[i] in my_set:
            my_set.remove(massiv[i])
            i += 1
        else:
            resalt.append(massiv[i])
            i += 1
    print(list(set(resalt)))

dublicate(massiv)


import hexlet.fs as fs

# mkdir вторым параметром принимает список детей,
# которые могут быть либо директориями, созданными mkdir,
# либо файлами, созданными mkfile
tree = fs.mkdir('etc', [
    fs.mkfile('bashrc'),
    fs.mkdir('consul', [
        fs.mkfile('config.json'),

    ]),
])

print(tree)

tree2 = \
    {
    'name': 'etc',
    'children': [
    {
    'name': 'bashrc',
    'meta': {},
    'type': 'file'
    },
    {
    'name': 'consul',
    'children':
    [
    {
    'name': 'config.json',
    'meta': {},
    'type': 'file'
    }
    ],
    'meta': {},
    'type': 'directory'
    }
    ],
    'meta': {},
    'type': 'directory'
    }

print(tree2)


tree = fs.mkdir(
    'my documents',
    [
        fs.mkfile('avatar.jpg', {'size': 100}),
        fs.mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)
"""compress_images(tree)"""
# {
#     'name': 'my documents',
#     'type': 'directory',
#     'children': [
#         {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
#         {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
#     ],
#     'meta': {'hide': False},
# }

print(Fore.RED + '-'*100, end='\n\n')

import copy

tree = fs.mkdir(
    'my documents',
    [
        fs.mkfile('avatar.jpg', {'size': 100}),
        fs.mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)

def compress_images(tree):
    children = fs.get_children(tree)

    def reduce_image_size(node):
        name = fs.get_name(node)
        """if not fs.is_file(node) or not name.endswith('.jpg'):
            return node"""
        meta = fs.get_meta(node)
        new_meta = copy.deepcopy(meta)
        new_meta['size'] //= 2
        return fs.mkfile(name, new_meta)

    new_children = map(reduce_image_size, children)
    new_meta = copy.deepcopy(fs.get_meta(tree))
    return fs.mkdir(fs.get_name(tree), list(new_children), new_meta)

print(compress_images(tree))


print(Fore.RED + '-'*100, end='\n\n')

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])


def dfs(node):
    # Распечатываем имя узла
    print(fs.get_name(node))
    # Если это файл, то возвращаем управление
    if fs.is_file(node):
        return

    # Получаем детей
    children = fs.get_children(node)

    # Применяем функцию dfs ко всем дочерним элементам
    # Множество рекурсивных вызовов в рамках одного вызова функции
    # называется древовидной рекурсией
    list(map(dfs, children))


dfs(tree)

print(Fore.RED + '-'*100, end='\n\n')

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])

owner = 'Pavel'

def change_owner(node, owner):
    name = fs.get_name(node)
    new_meta = fs.get_meta(node)
    new_meta['owner'] = owner
    if fs.is_file(node):
        return fs.mkfile(name, new_meta)
    children = fs.get_children(node)
    new_children = list(map(lambda child: change_owner(child, owner), children))
    new_tree = fs.mkdir(name, new_children, new_meta)
    return new_tree

print(change_owner(tree, owner))

def dfs(node):
    # Распечатываем имя узла
    print(fs.get_name(node))
    # Если это файл, то возвращаем управление
    if fs.is_file(node):
        return

    # Получаем детей
    children = fs.get_children(node)

    # Применяем функцию dfs ко всем дочерним элементам
    # Множество рекурсивных вызовов в рамках одного вызова функции
    # называется древовидной рекурсией
    list(map(dfs, children))

dfs(tree)




def downcase_file_names(node):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    if fs.is_file(node):
        return fs.mkfile(name.lower(), new_meta)
    children