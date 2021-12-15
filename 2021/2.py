inputPath = "2 input.txt"

with open(inputPath) as f:
    lines = f.readlines()

# Part 1
distance = 0
depth = 0

for line in lines:
    commandUnit = line.split()
    command = commandUnit[0]
    unit = int(commandUnit[1])

    if command == "forward":
        distance += unit
    elif command == "down":
        depth += unit
    elif command == "up":
        depth -= unit
    else:
        raise Exception("Unknown command")

print(distance * depth)

# Part 2
aim = 0
distance = 0
depth = 0

for line in lines:
    commandUnit = line.split()
    command = commandUnit[0]
    unit = int(commandUnit[1])

    if command == "forward":
        distance += unit
        depth += aim*unit
    elif command == "down":
        aim += unit
    elif command == "up":
        aim -= unit
    else:
        raise Exception("Unknown command")

print(distance * depth)