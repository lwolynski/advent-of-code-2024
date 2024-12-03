def isSorted(listOfNumbers):
    if listOfNumbers == sorted(set(listOfNumbers), reverse=False) or listOfNumbers == sorted(set(listOfNumbers), reverse=True):
        return True
    return False

def checkDiff(listOfNumbers):
    for index in range(len(listOfNumbers)-1):
        diff = abs(listOfNumbers[index] - listOfNumbers[index+1])
        if diff > 3:
            return False
    return True


howManySafe = 0
with open("input.txt", "r") as input:
    for line in input:
        listOfNumbers = list(map(int, line.split()))
        print(listOfNumbers)
        if isSorted(listOfNumbers) and checkDiff(listOfNumbers):
          howManySafe = howManySafe + 1


print(howManySafe)