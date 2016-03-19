#Project 5
def complexExpression(): #Define the function

    while (True): #Loop the program

        expr = input ("Please enter two or more expressions of the form '(number+number)': ") #Define the expression

        sign1 = expr.find ("+") #Define the addition sign

        sign2 = expr.find ("-") #Define the subtraction sign

        sign3 = expr.find ("*") #Define the multiplication sign

        sign4 = expr.find ("/") #Define the division sign

        if expr == ("end"): #If the user wants to end the program

            print ("Goodbye") #Print an ending message

            break #End the loop

        elif expr == ("last"): #If the user wants to see all of the previous expressions

            try:

                print ("Last addition sum: ",sum1)

            except UnboundLocalError: #If the function produces an error

                print("No history of addition") #Print an error message

            try:

                print ("Last subtraction sum: ",sum2)

            except UnboundLocalError: #If the function produces an error

                print("No history of subtraction") #Print an error message

            try:

                print ("Last multiplication sum: ",sum3)

            except UnboundLocalError: #If the function produces an error

                print("No history of multiplication") #Print an error message

            try:

                print ("Last division sum: ",sum4)

            except UnboundLocalError: #If the function produces an error

                print("No history of division") #Print an error message

        elif sign1 >= 0 and expr.startswith ("(") and expr.endswith (")"): #If a "+" sign is found and the input starts and ends with brackets

            first = expr [:sign1] #Define the first number

            second = expr [sign1+1:] #Define the second number

            try: #Test if the function is valid

                sum1 = int (first) + int(second) #Define the sum of both numbers

                print(first,"+",second,"=",sum1) #Print the complete expression

            except ValueError: #If the function produces an error

                print("Invalid expression") #Print an error message

        elif sign2 >= 0 and expr.startswith ("(") and expr.endswith (")"): #If a "-" sign is found and the input starts and ends with brackets

            first = expr [:sign2] #Define the first number

            second = expr [sign2+1:] #Define the second number

            try: #Test if the function is valid

                sum2 = int (first) - int(second) #Define the sum of both numbers

                print(first,"-",second,"=",sum2) #Print the complete expression

            except ValueError: #If the function produces an error

                print("Invalid expression") #Print an error message

        elif sign3 >= 0 and expr.startswith ("(") and expr.endswith (")"): #If a "*" sign is found and the input starts and ends with brackets

            first = expr [:sign3] #Define the first number

            second = expr [sign3+1:] #Define the second number

            try: #Test if the function is valid

                sum3 = int (first) * int(second) #Define the sum of both numbers

                print(first,"*",second,"=",sum3) #Print the complete expression

            except ValueError: #If the function produces an error

                print("Invalid expression") #Print an error message

        elif sign4 >= 0 and expr.startswith ("(") and expr.endswith (")"): #If a "/" sign is found and the input starts and ends with brackets

            first = expr [:sign4] #Define the first number

            second = expr [sign4+1:] #Define the second number

            try: #Test if the function is valid

                sum4 = int (first) / int(second) #Define the sum of both numbers

                print(first,"/",second,"=",sum4) #Print the complete expression

            except ValueError: #If the function produces an error

                print("Invalid expression") #Print an error message

        else: #If a sign is not found
    
            print ("Invalid expression") #Print an error message

complexExpression()
