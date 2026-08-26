#calculator
num1=int(input("enter a num1"))
num2=int(input("enter a num2"))
choice=input("enter a arithmetic")
if(choice=="+"):
    print("addition: ",num1+num2)
elif(choice=="-"):
    print("subtraction: ",num1-num2)
elif(choice=="%"):
    print("division: ",num1 % num2)
elif(choice=="*"):
    print("multipication: ",num1*num2)
else:
    print("power ",num1**num2)
