#Project 1
def simpleExpressionIsValid(): #Define the function

    expr = input ("Please enter an expression of the form 'number+number': ") #Define the expression

    sign1 = expr.find ("+") #Define the addition sign

    sign2 = expr.find ("-") #Define the subtraction sign

    sign3 = expr.find ("*") #Define the multiplication sign

    sign4 = expr.find ("/") #Define the division sign

    if sign1 >= 0: #If a "+" sign is found

        first = expr [:sign1] #Define the first number

        second = expr [sign1+1:] #Define the second number

        try: #Test if the function is valid

            sum = int (first) + int(second) #Define the sum of both numbers

            print("True") #Print a confirmation message

        except ValueError: #If the function produces an error

            print("False") #Print an error message

    elif sign2 >= 0: #If a "-" sign is found

        first = expr [:sign2] #Define the first number

        second = expr [sign2+1:] #Define the second number

        try: #Test if the function is valid

            sum = int (first) - int(second) #Define the sum of both numbers

            print("True") #Print a confirmation message

        except ValueError: #If the function produces an error

            print("False") #Print an error message

    elif sign3 >= 0: #If a "*" sign is found

        first = expr [:sign3] #Define the first number

        second = expr [sign3+1:] #Define the second number

        try: #Test if the function is valid

            sum = int (first) * int(second) #Define the sum of both numbers

            print("True") #Print a confirmation message

        except ValueError: #If the function produces an error

            print("False") #Print an error message

    elif sign4 >= 0: #If a "/" sign is found

        first = expr [:sign4] #Define the first number

        second = expr [sign4+1:] #Define the second number

        try: #Test if the function is valid

            sum = int (first) / int(second) #Define the sum of both numbers

            print("True") #Print a confirmation message

        except ValueError: #If the function produces an error

            print("False") #Print an error message

    else: #If a sign is not found
    
        print ("False") #Print an error message

simpleExpressionIsValid()
