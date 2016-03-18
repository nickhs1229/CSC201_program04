#Project 3
def simpleExpression(): #Define the function

    while (True): #Loop the program

        expr = input ("Please enter an expression of the form 'number+number': ") #Define the expression

        sign1 = expr.find ("+") #Define the addition sign

        sign2 = expr.find ("-") #Define the subtraction sign

        sign3 = expr.find ("*") #Define the multiplication sign

        sign4 = expr.find ("/") #Define the division sign

        if expr == ("end"): #If the user wants to end the program

            print ("Goodbye") #Print an ending message

            break #End the loop

        if sign1 >= 0: #If a "+" sign is found

            first = expr [:sign1] #Define the first number

            second = expr [sign1+1:] #Define the second number

            try: #Test if the function is valid

                sum = int (first) + int(second) #Define the sum of both numbers

                print(first,"+",second,"=",sum) #Print the complete expression

            except ValueError: #If the function produces an error

                print("Invalid expression") #Print an error message

        elif sign2 >= 0: #If a "-" sign is found

            first = expr [:sign2] #Define the first number

            second = expr [sign2+1:] #Define the second number

            try: #Test if the function is valid

                sum = int (first) - int(second) #Define the sum of both numbers

                print(first,"-",second,"=",sum) #Print the complete expression

            except ValueError: #If the function produces an error

                print("Invalid expression") #Print an error message

        elif sign3 >= 0: #If a "*" sign is found

            first = expr [:sign3] #Define the first number

            second = expr [sign3+1:] #Define the second number

            try: #Test if the function is valid

                sum = int (first) * int(second) #Define the sum of both numbers

                print(first,"*",second,"=",sum) #Print the complete expression

            except ValueError: #If the function produces an error

                print("Invalid expression") #Print an error message

        elif sign4 >= 0: #If a "/" sign is found

            first = expr [:sign4] #Define the first number

            second = expr [sign4+1:] #Define the second number

            try: #Test if the function is valid

                sum = int (first) / int(second) #Define the sum of both numbers

                print(first,"/",second,"=",sum) #Print the complete expression

            except ValueError: #If the function produces an error

                print("Invalid expression") #Print an error message

        else: #If a sign is not found
    
            print ("Invalid expression") #Print an error message

simpleExpression()
