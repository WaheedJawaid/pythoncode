from time import time
start_time =time()

name =input('Enter your name:-')
print("Hello %s Welcome to the Quiz "%(name.upper()))
print("-----------------------------------------")
while True:
  total_question =5
  correct = 0

  print("-----------------------------------------")
  print('1. Start Quiz')  
  print('2. Exit')
  print("-----------------------------------------")

  op = input(("Enter option(press 1 to 'start' / press any other key to 'Exit' )"))
  print()
  print()
  
  if op == '1':
    print("Q1. What is single line comment in python?")
    print("a)//   b)**/   c)#   d)/")
    ans = input("Enter your answer (a/b/c/d):").lower()
    if ans == 'c':
      correct +=1
      print()
      print()
     
    print("Q2. s='python programmer', the output of s [-8:-2]=?")
    print("a)mmargo   b)programmer   c)remmargo   d)ogramm")
    ans = input("Enter your answer (a/b/c/d):-").lower()
    if ans == 'd':
      correct+=1
      print()
      print()

    print("Q3. Statement to do nothing?")
    print("a)continue   b)pass  c)stop   d)break")
    ans= input("Enter your answer(a/b/c/d):").lower()
    if ans== 'b':
      correct+=1
      print()
      print()
      
    print("Q4. x=[i**2 for i in range (1,10) if i%2==0] what is output?")
    print("a)[2,4,6,8,10]   b)[0,4,16,36,64]   c)[4,16,36,64]   d)[0,4,16,36]")
    ans= input("Enter your answer(a/b/c/d):").lower()      
    if ans == 'c':
      correct+=1
      print()
      print()
      
    print("Q5. what is the output of the program?")
    print("if not 0:")
    print("   print('statement-1')")
    print("else:")
    print("   print('statement-2')")     
    print('a) statement-1   b) statement-2  c) error  d)none')
    ans= input("Enter your answer(a/b/c/d):").lower()      
    if ans == 'a':
      correct+=1
      print()
      print()
    
    end_time = time()
    total_time = end_time - start_time  
    
    print("-----------------------")
    print("%s Your Score %d out of %d...in %2f seconds.! "%(name.upper(),correct,total_question,total_time))
    print("-----------------------")
    
else:
      exit()  
  


# print('thankyou you are out of a game.')
# quit()