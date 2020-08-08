averages = {}

def parseAvgs():
    with open('avgs.txt','r') as f:
        for line in f:
            lst = line.split()
            averages[lst[0]] = float(lst[1])
    

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
print(averages)

print(percentComparison("wage",10000))
        

