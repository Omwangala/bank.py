print("Welcome to Laville banker's limited\nPlease insert your ATM card")
total = 40000
while True:
    choice = input("What do you want to do ?\n Withdraw cash or Check balance or Top up?")
    if choice == "withdraw cash":
        print(f"Your balance is {total}.How much do you want to withdraw?")
        withdraw = int(input(":"))
        if withdraw < total:
            print("You can proceed!")
        elif withdraw == total:
            print("You can proceed!")
        else:
            print(f"Enter a digit less than your {total}")
        total-=withdraw


    elif choice == "check balance":
        print(f"Your balance is {total}")

    elif choice == "top up":
        addition = int(input("Enter the amount you wanna add:"))
        if addition > 100000:
            print(f"Your top up has to be less than{100000}")
        elif addition < 10000:
            print(f"Your top up has to be more than {10000}")
        else:
            print("Your top up has been recorded!")
        total += addition
    
    else:
        break


print("WELCOME BACK!!!")
