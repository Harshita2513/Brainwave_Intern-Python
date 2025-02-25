# Initialize PIN and balance
print("To initialize this, you must set your PIN.")
pin = int(input("Please Enter your PIN (6 digits): "))
print("Your PIN is set successfully.")

amount = int(input("Enter your initial Bank Balance: "))

while True:
    print("\nCHOICES:")
    print("1. Check Account Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Change PIN")
    print("5. EXIT")
    
    choice = int(input("Enter your Choice: "))
    
    if choice == 1:
        print(f"Your Current Bank Balance is: {amount}")
    
    elif choice == 2:
        wd = int(input("Enter amount you want to withdraw: "))
        safety = int(input("Enter your PIN: "))
        if safety == pin:
            if wd <= amount:
                amount -= wd
                print(f"{wd} Amount Withdrawn.")
                print(f"Your remaining balance is: {amount}")
            else:
                print("Insufficient funds.")
        else:
            print("You've Entered Wrong PIN.")
    
    elif choice == 3:
        dm = int(input("Enter amount you want to deposit: "))
        safety1 = int(input("Enter your PIN: "))
        if safety1 == pin:
            amount += dm
            print(f"{dm} Amount Deposited.")
            print(f"Your remaining balance is: {amount}")
        else:
            print("You've Entered Wrong PIN.")
    
    elif choice == 4:
        safety = int(input("Enter your PIN: "))
        if safety == pin:
            pin = int(input("Enter your New 6-digit PIN: "))
            print("Your PIN is changed successfully.")
        else:
            print("You've Entered Wrong PIN.")
    
    elif choice == 5:
        print("THANK YOU")
        break  # Exit the loop
    
    else:
        print("Invalid Choice. Please enter a valid option.")
