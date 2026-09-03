print("___________________________________")
print("      ATM MANAGMENT SYSTEM   ")
print("___________________________________")
print("       Welcome to ATM")
attempt=4
pin=1234
while attempt>0:
    enterpin=int(input("enter a pin"))
    if(enterpin==pin):
        print("Successfully login")
        break
    else:
        attempt-=1
        print("Wrong PIN")
        print("remaining attempt",attempt)
      
if(attempt==0):
    print("Your A/c is locked")
print("1 Balance check")
print("2 Deposite")
print("3 withdrew")
print("4 exit")
choice=int(input("enter your choice no."))
currentbal=1000
if (choice==1):
    print("okh! uh want to check bank balance",currentbal)
    
else if(choice==2):
    print("okh! uh want to depos
