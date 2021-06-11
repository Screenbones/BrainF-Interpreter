#--------------------------------------
# Open and Parse BF File
#--------------------------------------
fileName = input("Enter name of Brainf*** file here: ")
file = open(fileName, "r")

programCode = []
validCommands = [">", "<", "+", "-", ".", ",", "[", "]"]

for x in file:
    for y in x:
        if y in validCommands:
            programCode.append(y)

file.close()

#--------------------------------------
# Find Indexes of Matching Brackets
#--------------------------------------
bracketPositions = []

loopIndex = 0
openIndex = []
for x in programCode:
    if x == "[":
        openIndex.append(loopIndex)
    if x == "]":
        openPosition = openIndex.pop()
        bracketPositions.append([openPosition, loopIndex])
    loopIndex += 1

#--------------------------------------
# Set Up BF Cells and Pointers
#--------------------------------------
memCells = []
memPointer = 0
instructionPointer = 0

memCellsStepper = 0
maxCells = 5000
while memCellsStepper < maxCells:
    memCells.append(0)
    memCellsStepper += 1

#--------------------------------------
# Define BF Commands
#--------------------------------------
def moveRight():
    global memPointer
    memPointer += 1
    if memPointer >= maxCells:
        memPointer = 0

def moveLeft():
    global memPointer
    memPointer -= 1
    if memPointer < 0:
        memPointer = maxCells - 1

def incrementCell():
    memCells[memPointer] += 1

def decrementCell():
    memCells[memPointer] -= 1

def outputValue():
    print(chr(memCells[memPointer]), end="")

def takeInput():
    print()
    value = input(">")
    memCells[memPointer] = ord(value[0])

def openBracket():
    global instructionPointer
    if memCells[memPointer] == 0:
        for x in bracketPositions:
            if x[0] == instructionPointer:
                instructionPointer = x[1]
        
def closeBracket():
    global instructionPointer
    if memCells[memPointer] != 0:
        for x in bracketPositions:
            if x[1] == instructionPointer:
                instructionPointer = x[0]

#--------------------------------------
# Execute BF Code
#--------------------------------------
while instructionPointer != len(programCode):
    x = programCode[instructionPointer]
    if x == ">":
        moveRight()
    if x == "<":
        moveLeft()
    if x == "+":
        incrementCell()
    if x == "-":
        decrementCell()
    if x == ".":
        outputValue()
    if x == ",":
        takeInput()
    if x == "[":
        openBracket()
    if x == "]":
        closeBracket()
    instructionPointer += 1