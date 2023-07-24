import string

with open('24_T3_task.txt', 'r') as taskFile:
    data = taskFile.readline()
    for symb in 'BCDE':
        data = data.replace(symb, 'A')
    data = data.replace('AA', '!')
    for symb in string.digits + 'A':
        data = data.replace(symb, ' ')
    data = data.split()
    print(len(max(data, key=len)))

with open('24_T3_task.txt', 'r') as taskFile:
    data = taskFile.readline()
    for symb in 'BCDE':
        data = data.replace(symb, 'A')
    data = data.replace('AA', '!')
    counter = 0
    while '!' * counter in data:
        counter += 1
    print(counter-1)
