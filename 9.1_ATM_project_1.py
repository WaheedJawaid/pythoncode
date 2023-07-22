# print("we are learning with aamar")
# print("we are learning with aamar")
# print("we are learning with aamar")
# print("we are learning with aamar")
# print("we are learning with aamar")
# print("we are learning with aamar")

# # defining a functions

# def print_codanics():
#     print("we are learning with aamar")
#     print("we are learning with aamar")
    

#print_codanics()

#2
#def print_codanics():
    # text = "we are learning with ammar in codanics, keep up the momentum high"
    # print(text)
    # print(text)
    # print(text)

#print_codanics()

#3
# def print_condanics(text):
#     print(text)
#     print(text)

# print_condanics("we are working in soneri bank")


#defining a function if, elif and else

# def school_calculator(age):
#     if age==5:
#         print("hammad can go to school")
#     elif age>5:
#         print("hammad should join higher secondry school")
#     else:
#         print("hammad is still a baby")

# school_calculator(10)

#defining a future function

# def future_age(age):
#     new_age=age+15
#     return new_age
#     print(new_age)

# future_predicted_age=future_age(5)
# print(future_predicted_age)  


# def sumResult(no1, no2):
#   result = no1 + no2
#   print(result)
  
# waheed_result = sumResult(40, 60)
# raheel_result = sumResult(10, 6)


# def emplyeeResult(na):
#   print("This employee name is: ", na)
#   sumResult(40, 60)
# emplyeeResult("raheel")

print("ATM Transaction - Insert Your Card")

def attempFunc(question,caller):
    question= caller
    attempt = 0
    answer = int(input(question))
  
    if isinstance(answer,int):
      op = input(("Enter option(press 1 to 'start Transaction' / press any other key to 'Exit' )"))
      P='proceed'
      C ='cancel'
      if(caller == "INSERTCARD" and (answer >=1  or answer <=2)):
        print("Next")
        attempt = attempt + 1
      
    if isinstance(answer,int):
      if(caller == "WRITEAMOUNT" and (answer >= 500 and 25000)):
        print("Next")
        attempt = attempt + 1    
        
    if isinstance(answer,int):
      # 0 = English
      # 1 = Urdu
      
      if(caller == "Select_Language" and (answer >= 0 and 1)):
        attempt = attempt + 1  

    else:
      print("Enter Valid Input")
    
    return attempt

try:  
  attempt =0
  attempt += attempFunc("Insert your card", "Insert_Card")
  attempt += attempFunc("Write your amount", "WRITEAMOUNT")
  attempt += attempFunc("Select Your Language", "Select_Language")
  print('attempt',attempt)

  if(attempt >= 4):
    print('Congrat you full fill all the criteria') 

except:
  print('criteria not match')
  exit()    
    
# function()
# switch flask
# github
# django frame work
# web development
# data base

# def withdraw(amount):
#   if amount > balance:
#     raise ValueError("Insufficient funds.")

#   # Subtract the amount from the balance.
#   balance -= amount

#   # Return the amount withdrawn.
#   return amount

# def deposit(amount):
#   """Deposits an amount of money into the account.

#   Args:
#     amount: The amount of money to deposit.

#   Returns:
#     The amount of money deposited.
#   """

#   # Add the amount to the balance.
#   balance += amount

#   # Return the amount deposited.
#   return amount

# def check_balance():
#   """Returns the current balance of the account."""

#   # Return the balance.
#   return balance

# def get_transactions():
#   """Returns a list of all transactions that have been made on the account."""

#   # Return the list of transactions.
#   return transactions