f = open('input_file.txt', 'w')
f.write('Hello\nWorld')
f.close()


"""with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for i, line in enumerate(input_file, 1):
            output_file.write(f'{i}, {line}')
"""