#Brython things...
from browser import document
from browser.html import P, STRONG
import re

#The dictionaries
averages = {}
facts = {}

#METHODS USED FOR NUMERICAL FUNCTIONS 

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
        return ("Your " + re.sub("[\(\[].*?[\)\]]", "", key) + " is " + str((int(percentDiff*100))/(100.0)) + "% greater than the worldwide average, " + str(avg))
    elif (avg > value):
        return ("Your " + re.sub("[\(\[].*?[\)\]]", "", key) + " is " + str((int(percentDiff*100))/(100.0)) + "% less than the worldwide average, " + str(avg))
    else:
        return ("Your " + re.sub("[\(\[].*?[\)\]]", "", key) + " is average!")


parseAvgs()
parseFacts()
print(facts)
print(averages)

#dictionaries used for non numerical component
EyeColours = {}
Contient = {}
Sex = {}

#METHODS USED FOR NON NUMERICAL COMPONENT

#method to read from eyecolours.txt into dictioanry 
def FillDictionarys():
    with open('Eye colours.txt', 'r') as ReadOnto:
        for line in ReadOnto:
            component = line.split()

            if component[0] == "EYE":
                EyeColours[component[1]] = str(component[2])

            elif component[0] == "CONTINENT":
                if component[1] == "South":
                    Contient[component[1] +" "+ component[2]] = str(component[3])
                elif component[1] == "North":
                    Contient[component[1] +" "+ component[2]] = str(component[3])
                else:
                    Contient[component[1]] = str(component[2])
            
            elif component[0] == "SEX":
                Sex[component[1]] = str(component[2])


#return the output of the users Eye colour
def ReturnEyeComparison(UserKey):
    global EyeColours
    return ("You have a " +UserKey+ " eyes, which is a trait shared by  " +EyeColours.get(UserKey)+ "%" + " of the population")

def ReturnContComparison(UserKey):
    global Contient
    return ("You live in " +UserKey+ ", " +UserKey+ " is also home to " +Contient.get(UserKey)+ "%" + " of the population")

def ReturnSexComparison(UserKey):
    global Sex
    return ("Your sex is " +UserKey+ ", this means your the same sex as " +Sex.get(UserKey)+ "%" + " of the population")


#list all keys within an dictionary
def ListKeysOfDic(Dictionary):
    counter = 1
    for keys in Dictionary.keys():
        print(str(counter)+". " + keys + " ")
        counter = counter + 1
    

#gets the users input
def GetEyeUserInput():
    UserEyeColour = input("Choose from the list of Eye colours and enter which colour most accuratly describes yours: ")
    return(UserEyeColour)

#get the user input
def GetContientUserInput():
    UserContienet = input("Choose from the list of Contient and enter which Continet most accurtly describes where you come from: ")
    return(UserContienet)

#get the user input
def GetSexInput():
    UserSex = input("Choose from the list of sexs which most accurtly describes what sex you are: ")
    return(UserSex)



#conbines functionality of getting user input and listing keys
def ComputeInputEyeColour():
    ListKeysOfDic(EyeColours)
    val = GetEyeUserInput()
    return(val)

#combines Funcitonaliy of getting userinput and listing keys
def ComputeInputContienet():
    ListKeysOfDic(Contient)
    val = GetContientUserInput()
    return(val)

#combines functonaliy of getting userinput and listing keys
def ComputeInputSex():
    ListKeysOfDic(Sex)
    val = GetSexInput()
    return(val)

FillDictionarys()

        
#This is for running in commandline. to do so, comment out brython code and uncomment this.
##for key in averages.keys(): #Iterate through keys
##    print("What is your " + key)
##    print(percentComparison(key,float(input(" ")))) #user input & function call
##    print(facts[key]) #Print fact about this stat


keySequence = [
        ["numerical","salary(CAD)"],
        ["numerical","height(cm)"],
        ["numerical","worth(Net,CAD)"],
        ["NonNumerical","eye colour"],
        ["NonNumerical","continent"],
        ["Nonnumerical","sex"],
        ["Nonnumerical","FinalScreen"]
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
            

    if keySequence[currentKeyIndex][0] == "NonNumerical":
        try:
            if keySequence[currentKeyIndex][1] == "eye colour":
                document["question"] <= P("(Please selection an eye colour from below that best describes you)")
                document["question"] <= P(("1. "+STRONG("Brown"))+(" 2. "+STRONG("Blue"))+(" 3. "+STRONG("Hazel"))+(" 4. "+STRONG("Amber")))
                document["question"] <= P(("5. "+STRONG("Green"))+(" 6. "+STRONG("Red/Violet"))+(" 7. "+STRONG("Heterochromia"))+(" 8. "+STRONG("Other")))
                
                document["zone"] <= P(ReturnEyeComparison((userIn)))

                if((currentKeyIndex + 1) < len(keySequence)):
                    currentKeyIndex += 1
                document["question"].clear()
                document["question"] <= P(STRONG("What is your " + keySequence[currentKeyIndex][1] + "?"))
                document["question"] <= P("(Please select which continent you currently live on)")
                document["question"] <= P(("1. "+STRONG("Asia"))+(" 2. "+STRONG("Africa"))+(" 3. "+STRONG("Europe")))
                document["question"] <= P(("4. "+STRONG("South America"))+(" 5. "+STRONG("North America"))+(" 6. "+STRONG("Oceania")))
            
            if keySequence[currentKeyIndex][1] == "continent":

                document["zone"] <= P(ReturnContComparison((userIn)))

                if((currentKeyIndex + 1) < len(keySequence)):
                    currentKeyIndex += 1
                document["question"].clear()
                document["question"] <= P(STRONG("What is your " + keySequence[currentKeyIndex][1] + "?"))
                document["question"] <= P("(Please select which sex most accurately describes you)")
                document["question"] <= P(("1. "+STRONG("Male"))+(" 2. "+STRONG("Female"))+(" 3. "+STRONG("Intersex")))

            if keySequence[currentKeyIndex][1] == "sex":

                document["zone"] <= P(ReturnSexComparison((userIn)))

                if((currentKeyIndex + 1) < len(keySequence)):
                    currentKeyIndex += 1
                document["question"].clear()
                document["question"] <= P(STRONG("End of program!"))
            
            if keySequence[currentKeyIndex][1] == "Finalscreen":
                document["question"].clear()
                document["question"] <= P(STRONG("The End!"))

        
        except ValueError:
            document["zone"] <= P("Please double check your input")



            








    #create the second section of code for elif second for not numerical

#Link our python method to the submit button...
document["submitButton"].bind("click",submitClicked)
