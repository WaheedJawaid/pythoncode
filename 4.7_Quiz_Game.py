from time import time
start_time =time()


name =input('your name\n')
print("Hello! %s Welcome to the Quiz "%(name.upper()))
print("-----------------------------------------")
question_no =0
score= 0
percentage = 0
  
question_no += 1
ques = input(f'\n{question_no}. what does CPU stand for? ').lower()
if ques == 'central processing unit':  
  score +=1
  print('correct')
else :
  print('Incorrect!')
  print(f'current answer is --> central processing unit,Central processing Unit ')
        
#------1
question_no += 1
ques = input(f'\n{question_no}. what does GPU stand for? ').lower()
    
if ques == 'graphics processing unit':
  score +=1
  print('correct')        
else:
  print('Incorrect!')
  print(f'current answer is --> graphics processing unit')

# # -----2
question_no += 1
ques = input(f'\n{question_no}. what does RAM stand for? ').lower()
    
if ques == 'random access memory':
  score +=1
  print('correct')
else:
  print('Incorrect!')
  print(f'current answer is --> random access memory')

# # -----3
question_no += 1
ques = input(f'\n{question_no}. what does PSU stand for? ').lower()
    
if ques == 'power supply unit':
  score +=1
  print('correct')       
else:
  print('Incorrect!')
  print(f'current answer is --> power supply unit')

# # -----4
question_no += 1
ques = input(f'\n{question_no}. what does ROM stand for? ').lower()
    
if ques == 'read only memory':
  score +=1
  print('correct')    
else:
  print('Incorrect!')
  print(f'current answer is --> read only memory')

# # ------5 :

try:
  percentage = (score *100)/question_no
except ZeroDivisionError:
  print('0% quetions are correct')

# print ("percentage",percentage)

print(f'{int(percentage)}% questions are correct,')

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')

end_time = time()
total_time = end_time - start_time

print('thankyou you are out of a game.')
quit()