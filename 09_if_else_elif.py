#This program demonstrates the use of the if, else, and elif statements.

print("---------------------------")
print("Admission_School = 18")
print("---------------------------")

name= input('Enter Your Name')
age = int(input("Enter your age"))

if age < 18:
  print("You are a minor.")
  exit()
    
elif age == 18:
  print("You are an adult.")
  exit()
    
elif age > 18 and age < 21:
  print("You are a young adult.")
  exit()
    
else:
  print("You are an older adult.")
  exit()
