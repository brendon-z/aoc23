import re

input = open("input.txt", "r")

# part one
sum = 0
for line in input:
    firstDigit = re.search(r"\d", line)
    secondDigit = re.search(r"\d", line[::-1])

    if (firstDigit == None or secondDigit == None):
        sum += 0
    else:
        sum += int(line[firstDigit.start()] + line[::-1][secondDigit.start()])
print(sum)

# part two
input = open("input.txt", "r")

dict = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine": "9"}

sum = 0
for line in input:
    firstDigit = re.search(r"\d", line)
    secondDigit = re.search(r"\d", line[::-1])
    
    startingIndex = len(line)
    startingWord = ""
    for word in dict:
        if line.find(word) != -1 and line.find(word) < startingIndex:
            startingIndex = line.find(word)
            startingWord = dict[word]
                
    endingIndex = 0
    endingWord = ""
    for word in dict:
        if line.find(word) != -1 and line.rfind(word) > endingIndex:
            endingIndex = line.rfind(word)
            endingWord = dict[word]
            
    first = "0"
    last = "0"
    if (firstDigit == None or firstDigit.start() > startingIndex):
        first = startingWord
    else:
        first = line[firstDigit.start()]
        
    if (secondDigit == None or (len(line) - 1 - secondDigit.start()) < endingIndex):
        last = endingWord
    else:
        last = line[::-1][secondDigit.start()]

    sum += int(first + last)
    print(line, first, last, int(first + last))

print(sum)