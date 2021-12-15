import math

inputPath = "1 input.txt"

with open(inputPath) as file:
    lines = file.readlines()

# Part 1
prevLine = math.inf
count = 0

for line in lines:
    value = int(line)
    if value > prevLine:
        count += 1
    prevLine = value

print(count)

# Part 2
windowSize = 3
prevSum = math.inf
count = 0

for i in range(len(lines) - windowSize + 1):
    sum = 0
    for j in range(windowSize):
        sum += int(lines[i+j])
    if sum > prevSum:
        count += 1
    prevSum = sum

print(count)
