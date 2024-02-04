import math
import string
from Constants import MINIMUM, MAXIMUM

class House:
    """Class definition for House"""

    def __init__(self, *arguments):
        """Constructor which initializes and instance of House"""

        #conditional statement which evaluates to True if the number of arbitrary arguments is equal to zero
        if len(arguments) == 0:
            self.__size = 0
            self.__borderChar = ""
            self.__fillChar = ""
            self.__name = ""

        #conditional statement which evaluates to True if the number of arbitrary arguments is equal to two    
        elif len(arguments) == 2:
            self.__size = arguments[0]
            self.__borderChar = "X"
            self.__fillChar = "*"
            self.__name = arguments[1]

        #conditional statement which evaluates to True if the number of arbitrary arguments is equal to four  
        elif len(arguments) == 4:
            self.__size = arguments[0]
            self.__borderChar = arguments[1]
            self.__fillChar = arguments[2]
            self.__name = arguments[3]

    def setSize(self, size):
        """Setter which sets the instance variable size.  This method takes in one additional argument besides self which is used to re-initialize the instance variable size"""

        #conditional statement which evaluates to True if the value of size is valid
        if size > MAXIMUM or size < MINIMUM:
            print("Unable to set size.")

        #conditional statement which evaluates to True if the value of size is invalid    
        else:    
            self.__size = size

    def getSize(self):
        """Getter which returns the instance variable size's value"""

        return self.__size    
    
    def setBorderChar(self):
        """Setter which sets the instance variable borderChar"""

        #declaration and initialization of local variable
        char = ""

        #calling instance method getValidChar and initializing char's value to the method's return value
        char = self.getValidChar(0)
        self.__borderChar = char

    def getBorderChar(self):
        """Getter which returns the instance variable borderChar's value"""

        return self.__borderChar

    def setFillChar(self):
        """Setter which sets the instance variable fillChar"""

        #declaration and initialization of local variable
        char = ""

        #calling instance method getValidChar and initializing char's value to the method's return value
        char = self.getValidChar(1)
        self.__fillChar = char

    def getFillChar(self):
        """Getter which returns the instance variable fillChar's value"""


        return self.__fillChar  

    def setName(self, name):
        """Setter which sets the instance variable name's value.  This method takes in one additional argument besides self which is used to re-initialize the instance variable name"""

        self.__name = name

    def getName(self):
        """Getter which returns the instance variable name's value"""

        return self.__name      
    
    def perimeter(self):
        """Instance method which calculates and returns the perimeter of this House instance"""

        #declaration and initialization of local variables
        perimeterBase = perimeterTri = 0

        #re-initializing local variables to equal accurate perimeters
        perimeterBase = (2 * (self.__size - 1) + self.__size)
        perimeterTri = (2 * (self.__size + 2)) + 2

        #returning the total perimeter of the house as a string
        return str(perimeterBase + perimeterTri)
    
    def area(self):
        """Instance method which calculates and returns the area of this House instance"""

        #declaration and initialization of local variables
        areaBase = areaTri = 0.0

        #re-initializing local variables to equal accurate areas
        areaBase = self.__size * (self.__size - 1)
        areaTri = (math.sqrt(3) / 4) * ((self.__size + 2) ** 2)

        #returning the total area of the house, accurate to two decimal places, as a string
        return "{:.2f}".format(areaBase + areaTri)
    
    def grow(self):
        """Instance method which increments the size of the house's base by one"""

        #conditional statement which evaluates to True if the size of the house's base is less than MAXIMUM
        if self.__size < MAXIMUM:
            #incrementing the size of the house's base by one
            self.__size += 1
            print(self.__name + "'s house grew!")

        #conditional statement which evaluates to True if the size of the house's base is equal to MAXIMUM
        else:
            print(self.__name + "'s house is already the maximum size!")    

    def shrink(self):
        """Instance method which decrements the size of the house's base by one"""

        #conditional statement which evaluates to True if the size of the house's base is greater than MINIMUM
        if self.__size > MINIMUM:
            #decrementing the size of the house's base by one
            self.__size -= 1   
            print(self.__name + "'s house shrank!") 

        #conditional statement which evaluates to True if the size of the house's base is equal to MINIMUM
        else:
            print(self.__name + "'s house is already the minimum size!")    

    @staticmethod
    def getValidChar(num):
        """Static method which returns a valid character for either the border or the fill character.  This method takes in one argument called num which tells this method whether to request the border character or fill character from the user"""

        #declaration and initialization of variables
        flag = False
        char = ""
        
        #while loop which runs until flag is True
        while flag == False:
            #conditional statement which evaluates to True if num equals zero
            if num == 0:
                char = input("Enter in the border character: ")

            #conditional statement which evaluates to True if num does not equal zero    
            else:
                char = input("Enter in the fill character: ")

            #conditional statement which evaluates to True if length of char is equal to one and char is a valid character from a list of valid strings
            if len(char) == 1 and (char in string.punctuation or char in string.ascii_letters or char in string.digits):
                flag = True    

        #returning char
        return char       

    def draw(self): 
        """This method is an instance method that draws out the house that the user designs using his or her input."""

        #declaration and initialization of local variables
        triangle = []
        base = []
        total = []
        array = ""
        triSideLen = 3 + (self.__size * 2)
        alternate = 0
            
        #for loop which iterates over each integer from zero, inclusive, to the integer value of the instance variable size plus two, exclusive    
        for i in range(0, self.__size + 2):
            #for loop which iterates over each integer from zero, inclusive, to i, exclusive
            for j in range(0, i):
                #adding a singular white space to the end of the array
                array += " "   
            
            #adding the border character to the end of the array
            array += self.__borderChar    
            
            #for loop which iterates over each integer from the length of the array, inclusive, and the integer value of triSideLen, exclusive
            for j in range(len(array), triSideLen):
                #conditional statement which evaluates to True if alternate is equal to zero and if the value of triSideLen minus j does not equal one
                if alternate == 0 and (triSideLen - j) != 1:
                    #adding a singular white space to the end of the array
                    array += " "

                #conditional statement which evaluates to True if i is equal to zero, alternate is equal to one, and if other conditions below are satisfied        
                elif (i == 0 and alternate == 1 and (len(array) == 2 or (triSideLen - j) == 3)) or (triSideLen - j) == 1:
                    #adding the border character to the end of the array
                    array += self.__borderChar  

                #conditional statement which evaluates to True if the above conditional statement evaluates to False    
                else:
                    #adding the fill character to the end of the array
                    array += self.__fillChar  

                #conditional statement which evaluates to True if alternate is equal to zero
                if alternate == 0:
                    alternate = 1
                #conditional statement which evaluates to True if alternate is equal to any value other than zero    
                else:
                    alternate = 0                 
            
            #appending array to an initialized list called triangle
            triangle.append(array)

            #re-initializing array and decrementing triSideLen by one
            array = ""
            triSideLen -= 1
            
        #for loop which iterates over each integer between zero, inclusive    
        for i in range(0, (self.__size - 1)):
            #adding a singular whitespace to the end of the array
            array += "  "

            #for loop which iterates over each integer between the length of the array, inclusive, and the integer value of two times the value of size plus one
            for j in range(len(array), (self.__size * 2) + 1):
                #conditional statement which evaluates to True if the following conditions below are meet
                if (j % 2 == 0 and i == 0) or ((j % 2 == 0 and len(array) == 2) or (j % 2 == 0 and len(array) == self.__size * 2)):
                    #adding border character to the end of the array
                    array += self.__borderChar

                #conditional statement which evaluates to True if j mod two is equal to zero and i does not equal zero
                elif j % 2 == 0 and i != 0:
                    #adding the fill character to the end of the array
                    array += self.__fillChar

                #conditional statement which evaluates to True if both conditional statement above evaluate to False   
                else:
                    #adding a singular whitespace to the end of the array
                    array += " "    
            
            #appending the array to the end of the list called base
            base.append(array)

            #re-initializing array
            array = ""  

        #reversing the order of the elements within triangle and base
        triangle.reverse()
        base.reverse()

        #adding the list triangle and base together to a new list called total
        total = triangle + base
        
        print(self.__name + "'s house:")

        #for loop which iterates over each integer between zero, inclusive, and the length of total, exclusive
        for i in range(0, len(total)):
            print(total[i])             

    def summary(self):
        """Instance method which prints a summary of a singular instance of House"""

        #declaration and initialization of variable
        height = round((math.sqrt(3) * (self.__size + 2) * 0.5) + (self.__size))

        #printing information about house to screen
        print("Here is a summary on " + str(self.__name))
        print("   - base width: " + str(self.__size) + " units")
        print("   - maximum height: " + str(height) + " units")
        print("   - perimeter: " + self.perimeter() + " units")
        print("   - area: " + self.area() + " units^2")
        self.draw()   