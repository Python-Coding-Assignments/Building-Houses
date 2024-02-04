from Constants import MAXIMUM, MINIMUM
from Classes import House
import string

def menu1(houses):
    """This function creates a new instance of House and appends this new instance of House to the end of an already existing list containing elements of type House"""

    #declaration and initialization of variables
    base = 0
    flag0 = flag = flag2 = flag3 = False
    houseName = ""
    newHouse = House()

    #while loop which runs until flag0 is not equal to False
    while flag0 == False:
        #getting the name of the house from the user
        houseName = input("What would you like to name the house?: ")

        #conditional statement which evaluates to True if the number of elements in houses is greater than zero
        if len(houses) > 0:
            #for loop which iterates over each integer between zero, inclusive, and the total number of elements in houses, exclusive
            for i in range(0, len(houses)):
                #conditional statement which evaluates to True if the name of the house given by the user matches any existing house's name
                if houseName == houses[i].getName():
                    flag3 = True
                    print("House named '" + houseName + "' already exists")

        #conditional statement which evaluates to True if flag3 is False
        if flag3 == False:
            flag0 = True            

    #getting input for the size of the house's base
    base = input("\nThe maximum size of the house's base is 37 units and the minimum size 3.\nWhat length of the base would you like your house to be?: ")

    #while loop which runs until flag no longer is False
    while flag == False:
        #for loop which iterates over the integers between zero, inclusive, and the total number of characters within the base, exclusive
        for i in range(0, len(base)):
            #conditional statement which evaluates to True if character at index i within the string called base is not found within the string called string.digits
            if base[i] not in string.digits:
                flag2 = True           

        #conditional statement which evaluates to True if flag2 is False
        if flag2 == False:
            #converting base from being an object of type string to an object of type integer
            base = int(base)

            #conditional statement checking if value of base is greater than or equal to MINIMUM and less than or equal to MAXIMUM
            if base <= MAXIMUM and base >= MINIMUM:
                flag = True

        #conditional statement which evaluates to True if flag is False
        if flag == False:        
            #getting input for the size of the house's base
            base = input("What length of the base would you like your house to be?: ")    

        flag2 = False 

    #creating instance of new house and setting the new instance's border and fill characters
    newHouse = House(base, houseName)
    newHouse.setBorderChar()
    newHouse.setFillChar() 

    #appending new instance of house to list
    houses.append(newHouse)