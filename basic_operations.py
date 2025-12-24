class Account:
  def __init__(itself,name, number, balance):
    itself.name = name
    itself.number = number
    itself.balance = balance


  def deposit(itself):
    if itself.balance > 0:
      deposit = int(input("How much do you want to deposit: "))
      itself.balance = itself.balance + deposit
      print(f"R{deposit} deposited successfully")
    else:
      print(f"Cannot deposited on a negative balance")


  def withdraw(itself):
    while True:
      withdraw = int(input("How much do you want to withdraw: "))
      if withdraw > itself.balance or itself.balance == 0: 
        print(f"Insufficient Funds!!")
      else:
        itself.balance = itself.balance - withdraw
        print(f"R{withdraw} withdrew successfully")

        break
  
  def checking_balance(itself):
    print(f"Account Holder: {itself.name}")
    print(f"Account Number: {itself.number}")
    print(f"You have R{itself.balance}")

account1 = Account("Washington", 5001, 10000 )
account1.withdraw()
account1.checking_balance()

# class Bank():
#   def __init__(itself, account_number):
#     itself.account_number = account_number

#   def create_account(itself):




# def account(options:int) -> int:
#   account_balance = 1000

#   if options == 1:
#     deposit = int(input("How much are you depositing: "))
#     account_balance = account_balance + deposit
    
#     choice = input("Do you still want to deposit again (Y/N): ")
#     if choice.lower() == "y":
#       deposit = int(input("How much are you depositing: "))
#       account_balance = account_balance + deposit
#       print(f"Your account balance is now R{account_balance}")
#     elif choice.lower() == "n":
#       print("process done")
      
#   elif options == 2:
#     withdraw = int(input("How much do you want to withdraw: "))
    
#     if account_balance >= withdraw:
#       account_balance = account_balance - withdraw
      
#       choice = input("Do you still want to withdraw again (Y/N): ")
#       if choice.lower() == "y":
#         withdraw = int(input("How much do you want to withdraw: "))
        
#         if account_balance >= withdraw:
#           account_balance = account_balance - withdraw
#           print(f"Your remaining balance is now R{account_balance}")
#         else:
#           print("Insufficient Funds")
          
#       elif choice.lower() == "n":
#         print("process done")
        
#     else:
#       print("Insufficient Funds")
      
      
#   elif options == 3:
#     print(f"Your account balance is R{account_balance}")
    
#   else:
#     print("Invalid option. Please select available options.")
    
#   return f"THANK YOU FOR BANKING WITH US!!"

# options = int(input("1. Deposit 2. Withdraw 3. View Balance: "))
# results = account(options)
# print(results)