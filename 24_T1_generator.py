from random import choice

templates = ['P', 'Z', 'V', 'ZV', 'VZ', 'VZVZVZVZVZV', 'ZZZZVVZVVZVZVZVZV', 'ZVVZVZVVVZVZZVVZVZZV', 'ZVVZZVVZ']
taskData = []

for _ in range(1_000_000):
    taskData.append(choice(templates))

with open('24_T1_task.txt', 'r+') as taskFile:
    taskFile.write(''.join(taskData))
