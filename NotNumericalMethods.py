#create Dictionary for eye colour 
EyeColours = {}
Contient = {}
Sex = {}

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
print(ReturnEyeComparison(ComputeInputEyeColour()))
print(ReturnContComparison(ComputeInputContienet()))
print(ReturnSexComparison(ComputeInputSex()))





    




