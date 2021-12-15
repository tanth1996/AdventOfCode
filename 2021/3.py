inputPath = "3 input.txt"

with open(inputPath) as f:
    lines = f.readlines()

# Part 1
bitFreq = [{}] # index is bit position, 0 is MSB; value is another dict of len 2 for bit frequencies

for line in lines:
    for position, bit in enumerate(line):
        if bit == "\n": continue
        try:
            bitFreq[position][bit] += 1
        except KeyError:
            bitFreq[position][bit] = 1
        except IndexError:
            bitFreq.append({bit : 1})

gammaStr = ""

for dict in bitFreq:
    maxFreq = 0
    for key in dict.keys():
        if dict[key] > maxFreq:
            maxFreq = dict[key]
            maxKey = key
    gammaStr += maxKey

gamma = int(gammaStr, 2)
epsilon = pow(2, len(gammaStr)) - 1 - gamma

print(gamma*epsilon)

# Part 2
o2List = lines.copy()
o2RatingString = ""
bitFreq = {}

for position in range(len(o2List[0])):
    bitFreq = {}

    for line in o2List:
        bit = line[position]
        try:
            bitFreq[bit] += 1
        except KeyError:
            bitFreq[bit] = 1

    if bitFreq['0'] > bitFreq['1']:
        filterBit = '0'
    else:
        filterBit = '1'

    o2LineIndex = 0
    while(o2LineIndex < len(o2List)):
        line = o2List[o2LineIndex]

        if line[position] != filterBit:
            o2List.pop(o2LineIndex)
        else:
            o2LineIndex += 1

        if len(o2List) == 1:
            break
            
    if len(o2List) == 1:
        break

o2RatingString = o2List[0]

co2List = lines.copy()
co2RatingString = ""
bitFreq = {}

for position in range(len(co2List[0])):
    bitFreq = {}

    for line in co2List:
        bit = line[position]
        try:
            bitFreq[bit] += 1
        except KeyError:
            bitFreq[bit] = 1

    if bitFreq['1'] < bitFreq['0']:
        filterBit = '1'
    else:
        filterBit = '0'

    co2LineIndex = 0
    while(co2LineIndex < len(co2List)):
        line = co2List[co2LineIndex]

        if line[position] != filterBit:
            co2List.pop(co2LineIndex)
        else:
            co2LineIndex += 1

        if len(co2List) == 1:
            break
            
    if len(co2List) == 1:
        break

co2RatingString = co2List[0]

o2Rating = int(o2RatingString, 2)
co2Rating = int(co2RatingString, 2)
print(o2Rating*co2Rating)