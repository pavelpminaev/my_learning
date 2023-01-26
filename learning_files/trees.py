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

print(Fore.RED + '-'*100, end='\n\n')
print(Fore.RED + '-'*100, end='\n\n')
print(Fore.RED + '-'*100, end='\n\n')
