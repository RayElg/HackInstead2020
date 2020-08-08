def percentComparison(key, value):
    incomeAvg = 50000
    if(key == "income"): #Temporary way of evaluating keys
        percentDiff = (abs(value-incomeAvg)/((incomeAvg+value)/2)) * 100
        if (value > incomeAvg):
            return ("Your " + key + " is " + str(percentDiff) + "% greater than average")
        elif (incomeAvg > value):
            return ("Your " + key + " is " + str(percentDiff) + "% less than average")
        else:
            return ("Your " + key + " is average!")

print(percentComparison("income",10000))
        
