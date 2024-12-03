leftList = []
rightList = []
similarityScore = 0
temp = []

with open("input.txt", "r") as input:
    for line in input:
        temp = line.split()
        leftList.append(int(temp[0]))
        rightList.append(int(temp[1]))

for value in leftList:
    similarityScore = similarityScore + value * rightList.count(value)

print(similarityScore)