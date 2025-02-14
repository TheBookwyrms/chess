import os

folders = os.listdir(os.getcwd())
attempt_3 = f'{os.getcwd()}\{folders[1]}'
files = os.listdir(attempt_3)
this_file = os.path.realpath(__file__).split('\\')[-1]

new_files = []
for file in files:
    if file[(len(file)-3):] == '.py':
        new_files.append(f'{attempt_3}\{file}')

total_lines = 0
fors = 0
whiles = 0
defs = 0
for file in new_files:
    lines = 0
    with open(file, 'r', errors='ignore') as a_file:
        text = a_file.readlines()
        file = file.split('\\')[-1]
        for line in text:
            lines += 1
            if file != this_file:
                if "for" in line:
                    fors += 1
                if "while" in line:
                    whiles += 1
                if "def" in line:
                    defs += 1
        total_lines += lines
        print(f"number of lines in {file:^39} is {lines}")
print(f'in total number of {'lines written':^39} is {total_lines}')
print(f'in total number of {'for loops':^39} is {fors}')
print(f'in total number of {'while loops':^39} is {whiles}')
print(f'in total number of {'functions defined':^39} is {defs}')