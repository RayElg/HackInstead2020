averages = {}
facts = {}

def parseAvgs():
    with open('avgs.txt','r') as f:
        for line in f:
            lst = line.split()
            averages[lst[0]] = float(lst[1])

def parseFacts():
    global facts
    isKey = True
    with open('facts.txt','r') as f:
        stripped = [line.strip() for line in f.readlines()]
        for line in stripped:
            if isKey:
                key = line
                isKey = False
            else:
                fact = line
                isKey = True
                facts[key] = fact

def percentComparison(key, value):
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

        

for key in averages.keys():
    print("What is your " + key)
    print(percentComparison(key,float(input(" "))))
    print(facts[key])
