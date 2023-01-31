print('----------writing and writelines-----------')
f = open('input_file.txt', 'w')
print(f.write('Hello\nWorld\n'))   # 12
print(f.writelines(['cat\n', 'dog\n']))   # None
f.close()

print('----------read line-----------')
f = open('input_file.txt', 'r')
print(f.readline())     # Hello
print(f.readline())     # World
print(f.read())         # Hello\n World\n cat\n dog\n
f.close()

print("---printing lines with 'for'---")
f.close()
f = open('input_file.txt', 'r')
for l in f:
    print(l)
f.close()

print("---printing lines with 'for' and 'break'---")
f.close()
f = open('input_file.txt', 'r')
for l in f:
    print(l)
    break

for l in f:
    print(l)
    break
f.close()

print('---printing list with readlines---')
f = open('input_file.txt', 'r')
print(f.readlines())

print('---numeration lines in file---')
input_file = open('input_file.txt', 'r')
output_file = open('output_file.txt', 'w')
for i, lines in enumerate(input_file, 1):
    output_file.write(f'{i}{lines}')
input_file.close()
output_file.close()



"""with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for i, line in enumerate(input_file, 1):
            output_file.write(f'{i}, {line}')
"""
