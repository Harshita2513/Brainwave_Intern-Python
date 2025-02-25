#                MY ATM INTERFACE
print("WELCOME TO MY ATM INTERFACE")
print("For Intialising the Interface, you've to set your PIN")
history = []

def set_pin():
    pin = input("Please enter your PIN (6-Digits) : ")
    if(len(pin)==6 and pin.isdigit()):  #Checking if the PIN entered by user is of 6-digits or not contain any characters
        print("Your PIN is set Successfully")
        return int(pin)
    else :
        print("Invalid PIN ")
        exit()
pin = set_pin()
amount = int(input("Enter your initial Bank Balance : ₹"))

while True :
    print("\nCHOICES:")
    print("1. Check Account Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. EXIT")
    
    choice = int(input("Enter your Choice : ")) #Asking user to enter their choice
    if(choice == 1):
        print(f"Your Current Bank Balance is : ₹{amount}")
    elif(choice==2) :
        withdraw = int(input("Enter amount you want to withdraw : "))
        if(withdraw < 0) :
            print("Amount can't be negative")
        elif (withdraw<=amount) :
            safety = int (input("Enter your PIN : "))
            if(safety == pin):
                print(f"Amount ₹{withdraw} Withdrawl")
                amount = amount-withdraw
                print(f"Your remaining balance is : ₹{amount}")
                history.append(f"Withdrawl : {withdraw}, Balance : {amount} ")

            else : 
                print("You've Entered Wrong PIN")
        else : 
            print("Insufficient Funds")
    elif(choice==3) :
        deposit = int(input("Enter amount you want to deposit : "))
        if(deposit<0) :
            print("Amount can't be negative")
            continue
        safety = int (input("Enter your PIN : "))
        if(safety == pin):
            print(f"Amount ₹{deposit} Deposited")
            amount = amount+deposit
            print(f"Your remaining balance is : ₹{amount} ")
            history.append(f"Deposited : {deposit}, Balance : {amount} ")

        else : 
            print("You've Entered Wrong PIN")

    elif(choice == 4):
        safety = int (input("Enter your PIN : "))
        if(safety == pin):
            pin1 = int(input("Enter your New PIN : "))
            print("Your PIN is changed Successfully")
            pin = pin1
        else : 
            print("You've Entered Wrong PIN, unable to change")

    elif(choice==5) :
        print("\nTransaction History :\n")
        if not history :
            print("No Transactions yet")
        else : 
            for transaction in history:
                print(transaction)


    elif(choice == 6):
        print("THANK YOU")
        exit() #Exiting if the user choose to end the program

    else :
        print("Wrong Choice, Try Again") 
  