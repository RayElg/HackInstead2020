#create Dictionary for eye colour 
EyeColours = {}

#method to read from eyecolours.txt into dictioanry 
def FillEyeColours():
    with open('Eye colours.txt', 'r') as ReadOnto:
        for line in ReadOnto:
            component = line.split()
            if component[0] == "EYE":
                EyeColours[component[1]] = str(component[2])


#return the output of the users Eye colour
def ReturnComparison(UserKey):
    global EyeColours
    return ("You have a " +UserKey+ " eyes, which is a trait shared by  " +EyeColours.get(UserKey)+ "%" + " of the population")


#list all keys within an dictionary
def ListKeysOfDic(Dictionary):
    counter = 1
    for keys in Dictionary.keys():
        print(str(counter)+". " + keys + " ")
        counter = counter + 1
    

#gets the users input
def GetUserInput():
    UserEyeColour = input("From the list of Eye colours above enter which colour most accuratly describes yours: ")
    return(UserEyeColour)

#conbines functionality of getting user input and listing keys
def ComputeInputEyeColour():
    ListKeysOfDic(EyeColours)
    val = GetUserInput()
    return(val)



FillEyeColours()
print(ReturnComparison(ComputeInputEyeColour()))





    




