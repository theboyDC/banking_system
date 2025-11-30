def account(options:int) -> int:
  account_balance = 1000

  if options == 1:
    deposit = int(input("How much are you depositing: "))
    account_balance = account_balance + deposit
    
    choice = input("Do you still want to deposit again (Y/N): ")
    if choice.lower() == "y":
      deposit = int(input("How much are you depositing: "))
      account_balance = account_balance + deposit
      print(f"Your account balance is now R{account_balance}")
    elif choice.lower() == "n":
      print("process done")
      
  elif options == 2:
    withdraw = int(input("How much do you want to withdraw: "))
    
    if account_balance >= withdraw:
      account_balance = account_balance - withdraw
      
      choice = input("Do you still want to withdraw again (Y/N): ")
      if choice.lower() == "y":
        withdraw = int(input("How much do you want to withdraw: "))
        
        if account_balance >= withdraw:
          account_balance = account_balance - withdraw
          print(f"Your remaining balance is now R{account_balance}")
        else:
          print("Insufficient Funds")
          
      elif choice.lower() == "n":
        print("process done")
        
    else:
      print("Insufficient Funds")
      
      
  elif options == 3:
    print(f"Your account balance is R{account_balance}")
    
  else:
    print("Invalid option. Please select available options.")
    
  return f"THANK YOU FOR BANKING WITH US!!"

options = int(input("1. Deposit 2. Withdraw 3. View Balance: "))
results = account(options)
print(results)