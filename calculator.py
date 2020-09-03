import math


repeat = True

user_name = input("Hello.Please enter your name: ")

print("Welcome to basic calculator " + "dear " + user_name)

    
    
def calculation():
    user_operation = input("Which operation do you want to use? (+,-,*,/,squareroot,power) Please enter: ")
    first_number = float(input("Please enter first number: "))

    
    if user_operation == "+":
        second_number = float(input("Please enter second number: "))
        result = first_number + second_number
    elif user_operation == "-":
        second_number = float(input("Please enter second number: "))
        result = first_number - second_number
    elif user_operation == "*":
        second_number = float(input("Please enter second number: "))
        result = first_number * second_number
    elif user_operation == "/":
        second_number = float(input("Please enter second number: "))
        result = first_number/second_number
    elif user_operation == "square":
        result = math.sqrt(first_number)
    elif user_operation == "power":
        second_number = float(input("Please enter second number: "))
        result = math.pow(first_number, second_number)

    print(result)


while repeat:

    calculation()

    ask_user = input(f"Dear {user_name}, do you want to continue? Please enter Y or N: ")

    if (ask_user == "N" or "n"):
        repeat = False
    else:
        continue




        


    
