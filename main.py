'''
import cv2
import math

print("Hello world")
print(math.gcd(3,6))
age = 45
if(age<19):
    print("not adult person")

print("adult person")

# for comments

'''
a=10
b = "Sagar"
#typeA = type(a)
#print(typeA)
#print(type(b))


# type casting
'''
e="33"
print(type(e))
e=int(e)
print(e)
e = float(e)
print(e)

'''

#  strings

name = "Harry"
#print(name[2 : 4])
#print(name.upper())
#print(name.lower())
#print(len(name))
var= name.replace("r","t")
var2 = name.replace("H","M")
#print(var2)

str1 = "This is a "
str2 = "This is a good boy named is"
name1 ="mohit"
name2 ="akshay"
#print(str1+str2)
str3 = "this is a {1} and he is a good boy named {0}".format(name1,name2)
#print(str3)

# concept of f string
str4 = f"this is a {name1} and he is a good boy name {name2}"
#print(str4)

# other operators

a = 5
b= 3
# print (a**b)
# print(a//b)
# print(a%b)

'''
  python collection:
    1. list
    2. tuple
    3. set
    4. dictionary

'''

# list is a type of array which we did use in c++

lst = [4,8,6,7,9,10]
# print(type(lst))

var = lst
lst[2]=20
lst.append(50)
lst.remove(9)
lst.pop()
lst.insert(1,89)
#del lst[2]
#lst.clear()
#print(var)

# tuple : in the tuple we can not change the value inside it

t = ("himanshu","sagar","yeshwant")
# we can not do this operation in tuple t[0]="Vikrant"
# print(t[0:2])
# print(t[::-1])
# print(type(t))
#print(t)

# addition of tuple

x=(1,2,3,4,5)
y=(6,8,3,9,8)
#print(x+y)

# multiplication simply lead to the repition

# print(x.count(5))
# print(len(x))
# print(max(x))
# print(min(x))

# set
s1 = {7,1,8,6,6,4,7,4,4,4,8,5,7,4,4,}
#s1.remove(1)
# use discard in place of remove to avoid the error
s1.discard(5)
s1.add(2)
s1.update([12,45,62,34,55,89])
s1.pop()
#s1.clear()
# del s1
#print(s1)
# Dictionary 
            
# SagarDict = {
#  "Name" : "Harry Sockets", 
# "Course" : "Mechanical Engineering",
#  "Cgpa"  :  9.3,
#  "ID" :  201
#  }     
# conditions 

# age=input("Enter your age\n")
# age= int(age)
# #print(type(age))
# if(age > 18):
#       print("you can drive car")
    
# elif(age==18):
#   print("boy is in middle age")

# else:
#   print("boy can not drive car bcoz you are minor")


# Loop concept

#for i in range(0,100):
#  print(i)

# for item in range(1,25):
#      print(item)

# variable = 0
# while(variable<100):
#     variable=variable+1
#     if variable == 85 :
#       continue
#     print(variable)
    

# Functions 

# def sum(a , b):
#   print("your Calculation is going on..........")
#   return a+b

# d=sum(2,4)
# print(d)

# class 

# class Employee:
#   def __init__(self,Ename,Esalary):
#     self.name= Ename
#     self.salary= Esalary


# harry =Employee("Sagar","50000 per month")
# print(harry.name)
# print(harry.salary)

# Testing loop 

#lst =[12,32,45,43,"Engineer","Doctor","Cricketer","Tennis player"]

# for item in lst:
#   print(item)

# def Find_position(lst):
#   for item in lst:
#     if item=="Cricketer":
#       return True
  

# if Find_position(lst):
#   print("your player is found in this lst")

sagarDict = {
    
    1: "Sagar koli",
    2: "Software Developer",
    3: "Netaji Subhas Institute of Technology",
    4: "Thesqua.re",
    5: "50000",
}
 
# for i in sagarDict:
#   print(sagarDict[i])

def Details(sagarDict):
  for item in sagarDict:
    if sagarDict[item]=="Thesqua.re":
      print("we found your company")
      break
    
Details(sagarDict)







































































































