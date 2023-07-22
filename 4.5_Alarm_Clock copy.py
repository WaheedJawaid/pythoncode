from datetime import datetime
from playsound import playsound

# name = "Hello world! Enter the time of alarm to be set Enteree the time of alarm to be set"
# print('namevariable:', len(name))

# print(name[47:54])

# for index, n in enumerate(name):
#   print('index:', index , 'word:',n)

# name = input("Enter your name:\n")
# print('your name is :',name)
  
  

# print(len(name))

alarm_time = input("Enter the time of alarm to be set:H:M:S\n")
# print('alarm_time', alarm_time)
alarm_hour=alarm_time[0:2]
# print('alarm_hour', alarm_hour)
alarm_minutes=alarm_time[3:5]
# print('alarm_minutes', alarm_minutes)
alarm_seconds=alarm_time[6:8]
# print('alarm_second', alarm_seconds)
alarm_period = alarm_time[9:11].upper()
# print('alarm_period',alarm_period)

print("setting up alarm..")




while True:       #isy smjhna ha pehle:
  now=datetime.now()
  print('now',now)
  current_hour=now.strftime("%I")
  # print('current_hour',current_hour)
  current_minutes=now.strftime("%M")
  # print('current_minutes',current_minutes)
  current_seconds=now.strftime("%S")
  # print('current_seconds',current_seconds)
  current_periods=now.strftime("%p")
  # print('current_periods',current_periods)
  if (alarm_period==current_periods):
    print('current_periods Wake up',current_periods)
    if(alarm_hour==current_hour):
      print('current_hour Wake up',current_hour)    
      if(alarm_minutes==current_minutes):
        print('current_minutes Wake up',current_minutes) 
        playsound('C:/Users/Dell/Desktop/Python/audio/Jingle-Bells-Ella.wav')
        break
      
      #   print("Wake up")
  
  
  
  
  
# apple = 1
# banana = 5     
        
# while apple <= banana:    #isy smjhna ha pehle:
#   print(apple)
#   apple = apple + 1
#   break
      

      
      

# if(2 != 4):
#   print('right')
# else:
#   print('wrong')



# while True:       #isy smjhna ha pehle:
  # now=datetime.now()
  # current_hour=now.strftime("%I")
  # current_minutes=now.strftime("%M")
  # current_seconds=now.strftime("%S")
  # current_periods=now.strftime("%p")
  # if (alarm_period==current_periods):
  #   if(alarm_hour==current_hour):
  #     if(alarm_minutes==current_minutes):
  #       if(alarm_seconds==current_seconds):
  #         print("Wake up")
  #         playsound('audio.mp3')
          # break
          
