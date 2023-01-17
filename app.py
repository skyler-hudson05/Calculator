# Variables
num1 = float(input("Please enter first number: "))
num2 = float(input("Please enter second number: "))
operations = input("Please enter an operation: ")


# Operations
def calculations():
  if(operations == "+"):
    add = num1 + num2
    print(add)
  elif(operations == '-'):
    subtract = num1 - num2
    print(subtract)
  elif(operations == '*'):
    multiply = num1 * num2
    print(multiply)
  elif(operations == "/"):
    divide = num1 / num2
    print(divide)
  elif(operations == '**'):
    sqr = num1 ** num2
    print(sqr)
  else:
    print("Invalid Operation")

calculations()
