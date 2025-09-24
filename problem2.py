#simple calculator(+,-,/) using two number and an operatin

num1=float(input("Enter first number:"))
num2=float(input("Enter second  number: "))
operator=input("Enter operator number (+,-.*,/): ")

if operator == "+":
    result= num1 + num2
    print("Result:", result)
elif operator == "-" :
    result=num1 - num2
    print("Result:", result)
elif operation =="*":
     result= num1 * num2
     print("Result:", result)
elif      operation =="/":
    if num2 !=0:
     result= num1 / num2
     print("Result:", result)
    else:
        print("Error:Division by Zero!")
else:
        print("invalid operator!")