import time as t

user_pin = (0000)
user_balance = 5000
user_name = 'Waheed'
print("Welcome to Account", user_name, user_balance,end="\n\n")

choice= 9

while (True):
    print("\t\t0. Logout and Exit")
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Cash")
    print("\t\t3. Deposit Cash")
    print("\t\t4. Change PIN")
    print("\t\t5. Return Card")
    choice = int(input("Enter number to proceed > "))
    print("\n\n")
    
    if choice == 0:
       print("Exiting...")
       t.sleep(2)
       print("You have been logged out. Thank you!\n\n") 
       break
     
    elif choice in (1,2,3,4,5):
      num_of_tries =3
      while (num_of_tries!= 0):
        input_pin =int(input("please enter your 4-digit PIN >"))
        
        if input_pin== user_pin:
          print("Account Authorized!\n\n")

          if choice == 1:
            print("Loading Account Balance....")
            t.sleep(1.5)
            print("Your Current Balance is Rs.", user_balance, end="n\n\n")
            break
          elif choice == 2:
            print ("Opening Cash Withdrawal....")
            t.sleep(1.5)
            
            withdraw_amt = float(input("Enter the amount you wish to withdraw"))
              
            if withdraw_amt> user_balance:
                withdraw_amt-=user_balance
                print("Can't  withdraw Rs.", withdraw_amt)
                print("Please enter Lower amount!")
                break
                            
            else:
                print("withdrawing Rs.", withdraw_amt)
                confirm = input("confirm? Y/N>")
                if confirm in('Y','y'):
                  user_balance-= withdraw_amt
                  print("Amount withdrawn - Rs.", withdraw_amt)
                  print("Remaining balance -Rs.", user_balance)
                  break
                else:
                  print("Canceling Transaction ....")
                  t.sleep(1)
                  print("Transaction Cancelation!\n\n")
                  break
                
          elif choice == 3:
            print("Loading Cash Deposit")
            t.sleep(1)
                      
            deposit_amt = float(input("Enter you wish to deposit the amount>"))
            print("Depositing Rs", deposit_amt)
            confirm= input("Confirm? Y/N>")
            if confirm in ('Y','y'):
                user_balance+= deposit_amt
                print("Amount deposit - Rs.",deposit_amt)
                print("Update balance - Rs.", user_balance, end ="n\n")
                break
            else:
              print("Cancellation Transaction")
              t.sleep(1.5)
              print("Transaction Cancelled! \n\n")
            continue
           
          elif choice==4:
            print("Loading PIN Change...")
            t.sleep(1.5)
            
            pin_new = int(input("Enter your New PIN >"))
            print("Changing PIN to", pin_new)
            confirm =input("Confirm? Y/N >")
            if confirm in ('Y','y'):
              user_pin= pin_new
              print("PIN Change Successfully! \n\n")
              break
              
            else:
              print("Cancelling PIN Change")
              t.sleep(1)
              print("Process Cancelled")
              continue
            
          
      else:
        num_of_tries +=1
        print("PIN incorrect! Number of tries left - ",num_of_tries, end="\n\n")
        
    else:
      print("Existing....")
      t.sleep(2)
      print("You have been logged out. Thankyou! \n\n")
      break
else:
  print("Invalid Input!")
  print("t\t0. Enter 0 to logout and Exit")
  
    
          
        
          
                 
              
            
              
            