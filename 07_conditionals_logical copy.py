# logical operators are either true or false, yes or no, 0 or 1
# equal to                              ==
# not equal to                          !=
# less than                             <
# greater than                          >
# less than or equal to                 <=
# greater than or equal to              >=

# 4 is equal to 4
# print(4==4)
# print(4!=4)
# print(4<53)
# print(4>2)
# print(4>=4)

# application of logical operators
# payment_cash=1000
# withdrawal_limit=500
# print(payment_cash==withdrawal_limit)

# input functions and logical operators

print("Our School Start Addmission required age 5 to 12")
try:
  age = int(input("Enter your child age?")) 
  if age >= 5 or age <= 12:
    print("Your Child is eligible")
  else:
    print("Sorry! Your Child is not eligible")
except:
  print("Enter Valid Input")
  
#College admission
#age limit / level of senior
#CGPA
#Experience Level
#Marks below 2.0 CGPA
#


# age_at_school=4
# required_age = 4
# if age_at_school == required_age

# else:
#   print('if age is <=4, tr ')

# print(age_at_school==required_age)


# hammad_age=input("how old are you? ")
# hammad_age=int(hammad_age)
# print(type(hammad_age))
# print(age_at_school==hammad_age)
