from random import choice

templates = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
taskData = []

for _ in range(1_000_000):
    taskData.append(choice(templates))

with open('24_T3_task.txt', 'r+') as taskFile:
    taskFile.write(''.join(taskData))
