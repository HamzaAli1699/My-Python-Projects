num1 = float(input("Enter number :"))
op = input("+,-,*,/,%,^ :") # op mean oprators.
num2 = float(input("Enter number :"))

if (op == "+"): 
    print(num1+num2)

elif(op == "-"):
    print(num1-num2)

elif(op == "*"):
    print(num1*num2)

elif(op == "/"):
    print(num1/num2)

elif(op == "^"): #check power of number.
    print(num1**num2)

elif(op == "%"): #check percentage.
    print(int((num1*num2)/100))

else:
    print("Please try again.")

print("Thank You.")
