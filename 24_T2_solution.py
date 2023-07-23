with open('24_T2_task.txt', 'r') as taskFile:
    line = taskFile.readline()
    data = line.split("CAPYBARA")
    data = [x for x in data if x.count('Y') <= 4]
    print(len(max(data, key=len)))


with open('24_T2_task.txt', 'r') as taskFile:
    line = taskFile.readline()
    data = line.split("CAPYBARA")
    parsedData = []
    for substring in data:
        if substring.count('Y') <= 4:
            parsedData.append(substring)
    print(len(max(parsedData, key=len)))
