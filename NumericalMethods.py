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
