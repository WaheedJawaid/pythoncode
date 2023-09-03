thislist =["banana", "mango", "orange"] #list
print(thislist)

thislist =["banana", "apple", "cherry" ,"mango", "orange"]  #duplicate value
print(thislist)

thislist =["banana", "apple", "cherry" ,"mango", "orange"]  #list length identify
print(len(thislist))

thislist =["banana", "apple", "cherry" ,"mango", "orange"]  #list data types like string, int & boolean
thislist01 =["1","2","3","4"]
thislist02 = ["TRUE", "FALSE"]
print(thislist, thislist01, thislist02)

thislist =["banana", "apple", "TRUE", "1", "3"]  #a list with string, int & boolean
print(thislist)

thislist =["banana", "apple", "cherry" ,"mango", "orange"]  #List type -type
print(type(thislist))

#access to python list:

thislist =["banana", "apple", "cherry" ,"mango", "orange"]  #access the list index value
print(thislist[3])

thislist =["banana", "apple", "cherry" ,"mango", "orange"]  #access the list negative index value
print(thislist[-3])

thislist =["banana", "cherry" ,"mango", "orange"]  #access the list index value
print(thislist[1:3])

thislist =["banana", "apple", "cherry" ,"mango", "orange"]  #to access the  index value of no 4 onwards
print(thislist[:3])

thislist =["banana", "apple", "mango", "orange"]  #to access the  index value of no 2 onwards
print(thislist[2:])

thislist =["banana", "apple", "cherry" , "orange"]  #to access the  index value of no 4
print(thislist[-2:-1])

#Check if Item Exists
thislist =["banana", "apple", "cherry" , "orange"]  #to access the item
if "apple" in thislist:
    print("yes, if 'apple' is available")
    
## Change Item Value
thislist =["banana", "apple", "cherry" ]  #to access 2nd index value / repalce with 2nd value
thislist[2] = "KELA"
print(thislist)

thislist =["banana", "apple", "cherry" ]  #to access MULTIPLE index value / repalce  value
thislist[0:2] = ["KELA", "AKELA"]
print(thislist)

thislist =["banana", "apple", "cherry" ]  #INSERT new value
thislist.insert(3, "KELA")
print(thislist)

#Python - Add List Items
thislist =[ "apple", "cherry" ]  #INSERT new value
thislist.append("KELA")
print(thislist)

thislist =[ "apple", "cherry" ]  #INSERT new value
thislist.insert(0,"WATERMELON")
print(thislist)

thislist =[ "apple", "cherry" ]  #EXTEND method two list
thislist01 = [ "Apple 01 Apple", "Cherry 02 Cherry" ]
thislist.extend(thislist01)
print(thislist)

thislist =[ "apple", "cherry" ]  #Add of a Tuple  list
thislist01 = ("KELA", "BANANA")
thislist.extend(thislist01)
print(thislist)

#Remove Specified Item
thislist =[ "apple", "cherry" ]  #remove item from list
thislist.remove("apple")
print(thislist)

thislist =[ "apple", "cherry" ]  #remove all item from list
thislist.pop()
print(thislist)

thislist =[ "apple", "cherry" ,"KELA", "BANANA"]  #del specific item from list
del thislist[1]
print(thislist)

thislist122 =[ "apple", "cherry" ,"KELA", "BANANA"]  #del complete list
del thislist122

thislist122 =[ "apple", "cherry" ,"KELA", "BANANA"]  #clear list
thislist122.clear()
print(thislist122)

#Using a While Loop #1
thislist1 =[ "apple", "cherry" ,"KELA", "BANANA"] 
i = 0
while i < len(thislist1):
    print(thislist1[i])
    i = i +1 

#2
thislist1 =[ "apple", "cherry" ,"KELA", "BANANA"]
[print (x) for x in thislist1]

#3
thislist1 =[ "apple", "cherry" ,"KELA", "BANANA"]  # add item in one list    
add = [10]

for x in  thislist01:
    if "a" in x:
       thislist01.append(x)

#4
#thislist1 =[ "apple", "cherry" ,"KELA", "BANANA"]  #loop refering to there index number
#for i in range (len(thislist1)):
    #print(thislist1[i])

#List Comprehension
#1
#thislist1 =[ "apple", "cherry" ,"KELA", "BANANA"]  # using for statement in loop continous
#newlist = ["10"]

#for x in  thislist1:
 #   if "a" in x:
  #      thislist1.append(x)
   #     print(newlist)

#2
thislist1 =[ "apple", "cherry" ,"KELA", "BANANA"]  # one line loop code list    
newlist = [x for x in thislist1 if "a" in x]
print  (newlist)

#3 
newlist =[ x for x in thislist1 if x != "apple"]  # only accept items that are not "apple"
print (newlist)

#4
newlist = [ x for x in range (6)] # use range function to create iterable 
print (newlist)

#5
newlist = [ x for x in range (12) if x < 9] # accept only no lower than 9
print (newlist)  

#6 upper case
newlist = [x.upper() for x in thislist1]
print (newlist)

#7 return function / not equal to the value
newlist = [x if x != "BANANA" else "KELA" for x in thislist1]
print(newlist)

#Python - Sort Lists
thislist1 =[ "apple", "cherry" ,"KELA", "BANANA"]  # sort by number / alphabetic
list2 = ["1", "5", "30", "2", "10"]
thislist1.sort()
list2.sort()
print (thislist,  list2)

#Customize Sort Function
#1
def myfunc(number):             # sort number
    return abs(number - 49)

list2 = [100, 250, 65, 40, 80]
list2.sort(key = myfunc)
print(list2)

#2
thislist1 =[ "apple", "cherry" ,"KELA", "BANANA"] 
thislist1.sort (key = str.lower)
thislist1.reverse()
print (thislist1)


