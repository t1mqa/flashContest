with open('24_T1_task.txt', 'r') as taskFile:
    line = taskFile.readline()
    data = line.split('P')
    data = [x for x in data if len(x) >= 2 and x[0] == 'Z' and x[-1] == 'V']
    print(len(max(data, key=len)))

with open('24_T1_task.txt', 'r') as taskFile:
    line = taskFile.readline()
    data = line.split('P')
    parsedData = []
    for x in data:
        if len(x) >= 2:
            if x[0] == 'Z' and x[-1] == 'V':
                parsedData.append(x)
    print(len(max(parsedData, key=len)))
