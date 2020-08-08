#create Dictionary for eye colour 
EyeColours = {}

#method to read from eyecolours.txt into dictioanry 
def FillEyeColours():
    with open('Eye colours.txt', 'r') as ReadOnto:
        for line in ReadOnto:
            component = line.split()
            EyeColours[component[0]] = str(component[1])

#return the output of the users Eye colour
def ReturnComparison(UserKey):
    global EyeColours
    return ("You have a " +UserKey+ " which is a trait shared by  "+EyeColours.get(UserKey))

#list all keys within an dictionary
def ListKeysOfDic(Dictionary):
    for keys in Dictionary:
        print(" " +key+ " ")


#prompt user for input
def PromptUser():
    ListKeys(EyeColours)

def GetUserInput():
    UserEyeColour = input("From the list of Eye colours above enter which colour most accuratly describes you: ")
    return(UserEyeColour)


FillEyeColours()
print(EyeColours)
val = GetUserInput()
print(val)
##ReturnComparison(PromptUser)



    




