from random import choice, randint

templates = ['C', 'A', 'P', 'B', 'R']
taskData = []

for _ in range(1_000_000):
    taskData.append(choice(templates))

task = ''.join(taskData)
yCount = randint(50*2, 60*2)  # Высота капибары - 50-60 см!
capyCount = randint(100, 135)  # Длина тела капибары - 100-135 см!

for index in range(yCount):
    yIndex = randint(0, len(task))
    task = task[:yIndex] + "Y" + task[yIndex:]

for index in range(capyCount):
    capyIndex = randint(0, len(task))
    task = task[:capyIndex] + "CAPYBARA" + task[capyIndex:]

with open('24_T2_task.txt', 'r+') as taskFile:
    taskFile.write(task)
