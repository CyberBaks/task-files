import os

files = ['1.txt', '2.txt', '3.txt']
file_contents = []

for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents.append((file_name, len(lines), lines))

file_contents.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in file_contents:
        result_file.write(f'{file_name}\n')
        result_file.write(f'{line_count}\n')
        result_file.writelines(lines)
        result_file.write('\n')

print("Готово.")