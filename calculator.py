print("Welcome to Gacheru Calculator")
num1 =  float(input("Input the first number: "))
num2 =  float(input("Input the second number: "))
operator = input("Input the operator of (+,-,*,/): ")
if operator == '+':
    result = num1 + num2

elif operator == '-':
    result= num1 - num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    result = num1/ num2

else:
    print("Invalid operator")
    exit()

print(f"{num1} {operator} {num2} is {result}")

