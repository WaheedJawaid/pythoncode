# logical operators are either true or false, yes or no, 0 or 1
# equal to                              ==
# not equal to                          !=
# less than                             <
# greater than                          >
# less than or equal to                 <=
# greater than or equal to              >=

# input functions and logical operators

# print("Hello! Enter your name")
# print("university Start Addmission required age 20 to 30")
# print("Passing marks 50 for admission")
# print("level of Education")
# print("Below 50 is not eligible for admission in university")

print("Admission in university")


def attempFunc(question,caller):
  attempt = 0
  awnser = int(input(question))

  if isinstance(awnser, int):
    if(caller == "AGE" and (awnser >= 20 and awnser <= 30)):
       print("Next")
       attempt = attempt + 1
    
    if(caller == "LEVELEDU" and (awnser >= 10 and awnser <= 12)):
       print("Next")
       attempt = attempt + 1
       
    if(caller == "PASSMASK" and (awnser >= 10 or awnser <= 50)):
       print("Next")
       attempt = attempt + 1
    
    if(caller == "BELOW50" and awnser>= 50):
       attempt = attempt + 1
  else:
    print("Enter Valid Input")
    
  return attempt
    
try:
  attempt = 0
  attempt += attempFunc("University Start Addmission required age 20 to 30?", "AGE")
  attempt += attempFunc("Level of Education 11 to 12 ?", "LEVELEDU")
  attempt += attempFunc("Passing marks 50 for admission?", "PASSMASK")
  attempt += attempFunc("Below 50 is not eligible for admission in university?", "BELOW50")
  print('attempt',attempt)
  
  if(attempt >= 4):
    print('Congrat you full fill all the criteria') 
except:
  print('criteria not match')
  exit()

# try:
#   attempt = 0
#   age = int(input("University Start Addmission required age 20 to 30?"))
  
#   if isinstance(age, int):
#     if age >= 20 and age <= 30:
#       print("Next")
#       attempt = attempt + 1
#     else:
#       print("Sorry! you may try next time")
#       exit()
#   else:
#     print("Enter Valid Input")
  
#   level_of_education = int(input("Level of Education 1 to 12 ?"))
#   if isinstance(level_of_education, int):
#     if level_of_education >= 10 and level_of_education <= 12:
#       print("Next")
#       attempt = attempt + 1
#     else:
#       print("Sorry! you may try next time")
#       exit()
#   else:
#     print("Enter Valid Input")
  
#   marks_obtained = int(input("Passing marks 50 for admission?"))
#   if isinstance(marks_obtained, int):
#     if marks_obtained >= 10 or marks_obtained <= 50:
#       print("Next")
#       attempt = attempt + 1
#   else:
#     print("Sorry! you may try next time")
#     exit()
    
#   eligiblity_criteria = int(input("Below 50 is not eligible for admission in university?"))
#   if isinstance(eligiblity_criteria, int):
#     if eligiblity_criteria>= 50:
#       attempt = attempt + 1
#   else:
#     print("Sorry! you may try next time")
#     exit() 
    
#   if(attempt >= 4):
#     print('Congrat you full fill all the criteria')
# except:
#   print('criteria not match')
#   exit()

#College admission
#age limit / level of senior
#CGPA
#Experience Level
#Marks below 2.0 CGPA

