class Calculator():
    
    def add(self,a,b):
        addition=a+b
        return addition
    
    def subtract(self,a,b):
        sustraction=a-b
        return sustraction
    
    def multiplication(self,a,b):
        multiply=a*b
        return multiply
    
    def division(self,a,b):
        div_value=a/b
        return div_value
    
    def declareOption(self):

        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
    
    def userInput(self):
    
        while True:
            self.declareOption()

            
            # take input from the user
            choice = input("Enter choice(1/2/3/4): ")

            # check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if choice == '1':
                    print(num1, "+", num2, "=", self.add(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", self.subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", self.multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", self.div_value(num1, num2))
                
                # check if user wants another calculation
                # break the while loop if answer is no
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation == "no" or next_calculation =="n":
                    break
            else:
                print("Invalid Input")

     
    def __init__(self):
        self.declareOption()
        self.userInput()

#CalculatorSimple()



class ComplexCal:
    def declareOption(self):

        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

    def _doAction(self,choice,inputs):
        match choice:
            case 1:
                print(self.add(inputs))

            case 2:
                print(self.sub(inputs))
            case 3:
                print(self.multiply(inputs))
            case 4:
                print(self.divide(inputs))
            

    



    def _takeInput(self, choice):
        inputs=[]
        i=1
        while True:


            #try
            
            if choice in (1,2,3):

                num= float(input("Enter number " + str(i) + ": "))
                inputs.append(num)
            elif choice ==4:
                num= float(input("Enter number " + str(i) + ": "))
                if num == 0:
                    print("Please enter a valid number. 0 is not acceptable.")
                    
                else:
                    inputs.append(num)
            else:
                print("Please enter valid number")
                continue


                
            #except ValueError:
                #print("Please enter valid number")
                #continue

            next_number=input("Do you want add another number then press yes or else no: ")
            if next_number == "yes" or next_number =="y" or next_number =="YES" or next_number == "Y" or next_number =="Yes":
                i=i+1
                #print(i)
                continue
            else:
                self._doAction(choice,inputs)
                print("Your operation is successful")
                break      



    def userInput(self):
        #print("Now you can insert numbers to perform operations")
        while True:
            try:
                choice= int(input("Please select option to perform operations: "))
            except ValueError:
                print("You have to insert choices as integers ")
                continue

            if choice in (1,2,3,4):
                self._takeInput(choice)
                break
            else:
                print("Invalid Input")
        
    
    def add(self,args):
        sum=0
        for i in args:
            sum= sum+i
        return sum
    
    def sub(self,args):
        sub=0
        for i in args:
            sub= sub-i
        return sub

    def multiply(self,args):
        multiply=1
        for i in args:
            multiply= multiply*i
        return multiply

    def divide(self,args):
        divide=args[0]
        for i in args[1:]:
            divide= divide//i


    def __init__(self):
        self.declareOption()
        self.userInput()
        

ComplexCal()  



