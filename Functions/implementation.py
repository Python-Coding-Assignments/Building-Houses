from Functions import menu, menu1
import string

def implementation(userInput, houses):
    """This function determines how the program should flow depending on the user's menu selection.  This function takes in two arguments: the user's menu selection of type string and a list of houses created by the user, containing elements of type House"""

    #declaration and initialization of variables
    flag = flag2 = False
    validIndex = 0

    #conditional statement which evaluates to True if the length of houses is greater than one and the user input is either "2", "3", "4", "6", or "7"
    if len(houses) > 1 and (userInput == "2" or userInput == "3" or userInput == "4" or userInput == "6"):
        print("Here is a list of houses that you created.")

        #for loop which iterates over the integers between zero, inclusive, and the length of the houses list, exclusive
        for i in range(len(houses)):
            print("House " + str(i) + ": " + houses[i].getName())
        
        #while loop which runs while flag is equal to False
        while flag == False:
            #getting house index from user
            validIndex = input("\nWhich house would you like to work with?: ")

            #for loop which iterates over the integers between zero, inclusive, and the length of the houses list, exclusive
            for i in range(0, len(validIndex)):
                #conditional statement which evaluates to True if any character within validIndex is not found in the string called string.digits
                if validIndex[i] not in string.digits:
                    flag2 = True

            #conditional statement which evaluates to True if flag2 is False
            if flag2 == False:
                #converting validIndex from a string object to an integer object
                validIndex = int(validIndex)

                #conditional statement which evaluates to True if the value of validIndex is greater than or equal to zero and less than the length of the houses list
                if validIndex >= 0 and validIndex < len(houses):
                    flag = True

            #conditional statement which evaluates to True if flag2 is True
            else:
                print("A house at that index does not exist.  Tri again.")
                flag2 = False      

    #conditional statement which evaluates to True if the conditional statement above evaluates to False
    else:
        validIndex = 0

    #conditional statement which evaluates to True if the user's input is equal to "1"
    if userInput == "1":
        #calling menu1 function
        menu1.menu1(houses)

    #conditional statement which evaluates to True if the user's input is equal to "2"
    elif userInput == "2":
        houses[validIndex].draw()  

    #conditional statement which evaluates to True if the user's input is equal to "3"
    elif userInput == "3":   
        houses[validIndex].grow() 

    #conditional statement which evaluates to True if the user's input is equal to "4"
    elif userInput == "4":
        houses[validIndex].shrink()   

    #conditional statement which evaluates to True if the user's input is equal to "5"
    elif userInput == "5":
        menu()  

    #conditional statement which evaluates to True if the user's input is equal to "6"
    elif userInput == "6":
        houses[validIndex].summary()

    #conditional statement which evaluates to True if the user's input is equal to "7"
    elif userInput == "7":
        print("\nApplication is now terminating!\nHere is information regarding each house that you created:")

        #for loop which iterates over each integer between zero, inclusive, and the integer value of the length of the houses list, exclusive
        for i in range(0, len(houses)):
            houses[i].summary()
            print()

    #conditional statement which evaluates to True if the user's input is invalid
    else:
        print("Invalid entry!")        