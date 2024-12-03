leftList = []
rightList = []
totalDistance = 0
temp = []

with open("input.txt", "r") as input:
    for line in input:
        temp = line.split()
        leftList.append(int(temp[0]))
        rightList.append(int(temp[1]))

leftList = sorted(leftList, reverse=False)
rightList = sorted(rightList, reverse=False)

for index in range(len(leftList)):
    totalDistance = totalDistance + (abs(leftList[index] - rightList[index]))

print(totalDistance)