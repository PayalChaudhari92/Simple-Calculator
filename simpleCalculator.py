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

Calculator()



