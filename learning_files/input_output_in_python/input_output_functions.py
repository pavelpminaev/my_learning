f = open('input_file.txt', 'w')
f.writelines(['Hello\nWorld\n', 'cat\n', 'dog\n'])
f.close()
f = open('input_file.txt', 'r')
print(f.readline())
print(f.readline())
print(f.read())
print('---------------------')

f.close()
f = open('input_file.txt', 'r')
for l in f:
    print(l)
print('---------------------')
f.close()
f = open('input_file.txt', 'r')
for l in f:
    print(l)
    break
for l in f:
    print(l)
    break
print('---------------------')


f = open('input_file.txt', 'r')

"""with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for i, line in enumerate(input_file, 1):
            output_file.write(f'{i}, {line}')
"""
