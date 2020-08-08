#Brython things...
from browser import document
from browser.html import P, STRONG


#The dictionaries
averages = {}
facts = {}


def parseAvgs(): #Populates averages dictionary from avgs.txt
    with open('avgs.txt','r') as f:
        for line in f:
            lst = line.split()
            averages[lst[0]] = float(lst[1]) #First word in line is key, next is value

def parseFacts(): #Populates facts dictionary from facts.txt
    global facts
    isKey = True
    with open('facts.txt','r') as f:
        stripped = [line.strip() for line in f.readlines()] #removes newline character
        for line in stripped:
            if isKey: #For alternating between lines being the key and being the value
                key = line
                isKey = False
            else:
                fact = line
                isKey = True
                facts[key] = fact #First line is key, then the fact string, repeats

def percentComparison(key, value): #Returns a string detailing the percent difference between the average value and inputted value
    global averages
    avg = averages[key]
    
    percentDiff = (abs(value-avg)/((avg+value)/2)) * 100
    if (value > avg):
        return ("Your " + key + " is " + str(percentDiff) + "% greater than average")
    elif (avg > value):
        return ("Your " + key + " is " + str(percentDiff) + "% less than average")
    else:
        return ("Your " + key + " is average!")



parseAvgs()
parseFacts()
print(facts)
print(averages)

        
#This is for running in commandline. to do so, comment out brython code and uncomment this.
##for key in averages.keys(): #Iterate through keys
##    print("What is your " + key)
##    print(percentComparison(key,float(input(" ")))) #user input & function call
##    print(facts[key]) #Print fact about this stat


keySequence = [
        ["numerical","salary(CAD)"],
        ["numerical","height(cm)"]
        ]

currentKeyIndex = 0
    

#Brython code
def submitClicked(event): #Handles the submit button being clicked
    global currentKeyIndex
    global keySequence

    userIn = (document["userTextBox"].value)

    if keySequence[currentKeyIndex][0] == "numerical":
        try:
            document["zone"] <= P(percentComparison(keySequence[currentKeyIndex][1],float(userIn)))
            document["zone"] <= P(facts[keySequence[currentKeyIndex][1]])

            if ((currentKeyIndex + 1) < len(keySequence)):
                currentKeyIndex += 1
            document["question"].clear()
            document["question"] <= P(STRONG("What is your " + keySequence[currentKeyIndex][1] + "?"))
            
        except ValueError:
            document["zone"] <= P("Please double check your input")
            
    #create the second section of code for elif second for not numerical

#Link our python method to the submit button...
document["submitButton"].bind("click",submitClicked)
