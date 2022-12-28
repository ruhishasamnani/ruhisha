#print('hello world')

#WAP to find the eligibility to vote.
'''
age=int(input('Enter your age:'))
if(age>=18):
    print('Your are eligible to vote')
else:
    print('Your are not eigible to vote')
'''

#WAP to heck whether the number is odd or even.
'''
num=int(input('Enter any number:'))
if(num%2==0):
    print('The number is even')
else:
    print('The number is odd')
'''

#WAP to check if entered year is a leap year or not
'''
year=int(input('Enter any year:'))
if(year%4==0):
    print('The entered year is a leap year')
else:
    print('The entered year is not a leap year')
'''

#WAP to find largest of two numbers
'''
num1=int(input('Enter any number1:'))
num2=int(input('Enter any number2:'))
if(num1>num2):
    print(num1,'is greater than',num2)
else:
    print(num2,'is greater than',num1)
'''

#WAP to find largest of three numbers
'''
num1=int(input('Enter any number1:'))
num2=int(input('Enter any number2:'))
num3=int(input('Enter any number3:'))
if(num1>num2 and num1>num3):
    print(num1,'is greater than',num2,'and',num3)
elif(num2>num3):
    print(num2,'is greater than',num1,'and',num3)
else:
    print(num3,'is greater than',num1,'and',num2)
'''

#WAP to check whether the entered character is a vowel or not
'''
char=input('Enter a character:')
if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
    print('The character',char,'is a vowel')
else:
    print('The character',char,'is not a vowel')
'''

#WAP to find the month by using month number
'''
month=int(input('Enter a number between 1-12:'))
if(month==1):
    print('January')
elif(month==2):
    print('February')
elif(month==3):
    print('March')
elif(month==4):
    print('April')
elif(month==5):
    print('May')
elif(month==6):
    print('June')
elif(month==7):
    print('July')
elif(month==8):
    print('August')
elif(month==9):
    print('September')
elif(month==10):
    print('October')
elif(month==11):
    print('November')
elif(month==12):
    print('December')
else:
    print('Enter a valid number between 1-12')
''' 

#WAP for an Arithmatic Calculator
'''
num1=int(input('Enter a number1:'))
num2=int(input('Enter a number2:'))
print('1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Integar Division 6.Modulus 7.Exponent')
choice=int(input('Enter any choice mentioned above:'))
if(choice==1):
    print('The sum of',num1,'and',num2,'is:',num1+num2)
elif(choice==2):
    print('The difference between', num1 ,'and', num2 ,'is', num1-num2) 
elif(choice==3):
    print('The product of', num1 ,'and', num2 ,'is', num1*num2)
elif(choice==4):
    print('The qoutient of', num1 ,'and', num2 ,'is', num1/num2)
elif(choice==5):
    print('The integar qoutient of', num1 ,'and', num2 ,'is', num1//num2)
elif(choice==6):
    print('The modulus of', num1 ,'and', num2 ,'is', num1%num2)
elif(choice==7):
    print('The exponent of', num1 ,'and', num2 ,'is', num1**num2)
else:
    print('Enter a valid choice from 1-7')
'''

#wAP to implement tuple in python and demonstrate various operations on it

'''
t=(10,20,30,40,50,60,20,30,40,50,20)
print(t)
print(len(t))
print(type(t))

print(t.count(20)) #count the appearance of element'20'
print(t.count(50))
print(t.count(60))

print(t.index(40)) #shows the index value of first occuring element'40'
print(t.index(20))

#Slicing(Cuts tuple into smaller parts)
print(t[0:6])
print(t[:6]) #Bydefault will print from 0th positon element
print(t[2:]) #Bydefault will print till last element
print(t[::]) #Will print whole tuple
print(t[0:10:2]) #Will print the tuple by skipping one value
print(t[0:10:3]) #Will print the tuple by skipping two values
print(t[::-1]) #Will reverse the tuple
print(t[::-2]) #Will reverse th tuple by skipping one value

#Indexing(Assigning location number to element)
print(t[2]) #Shows the element at 2nd index no.
print(t[8])
print(t[-1]) #Shows th element at -1st index no.
print(t[-9])

#Operations on tuple

#Concatenation(Addition)
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)
print(t1+t2)

#Multiplication
t4=t1*2
t5=t1*3
t6=t2*2
print(t4)
print(t5)
print(t6)
print(t1*2)
print(t1*3)
print(t2*2)
'''

#WAP to immplement list in python for suitable program

'''
l=[1,2,3,4,5,6,6]
print(l)
print(type(l))
print(len(l))

print(l.count(6)) #Counts the occurance of element'6'
print(l.count(2))


#Indexing
print(l[0])
print(l[3])
print(l[-1])
print(l[-4])

#Slicing
print(l[0:6])
print(l[:5])
print(l[2:])
print(l[::])
print(l[::2])
print(l[::-1])
print(l[::-2])

l.reverse() #reverse the list
print(l)

a=l.copy()
print(a)

print(5 in l)
print(50 in l)

print(5 not in l)
print(50 not in l)

print(sum(l))
print(max(l))
print(min(l))

#Concatenation(Addition)
l1=[10,20,30]
l2=[40,50,60]
l3=l1+l2
print(l1+l2)
print(l3)

#Multiplication
print(l1*2)
print(l1*3)


l.clear()
print(l)

del l
print(l)
'''

#WAP to implement dictionaries in python with suitable examples

'''
d={1:'a',2:'b',3:'c',4:'d',5:False}
print(d)
print(type(d))
print(len(d))

d={1:(10,20,30),2:[40,50,60]} #adding list an tuple in dictionary
print(d)

d={1:'a',2:'b',3:'c',4:'d'} #to add an element in the dictonary
d[5]='e'
print(d)

d.pop(4) #removes the specified key and values
print(d)

print(any(d)) #if any key and values is there or not

print(d.items()) #prints as tuple
print(d.keys()) #prints only keys
print(d.values()) #print only values

d1=d.copy() #copies the dictionary
print(d1)

d[5]='d' #replaces the old value by new value by mentioninh the key
print(d)

d.update({6:'e'}) #adds element at the end of dictionary
print(d)

print(3 in d) #In function
print(8 in d) #Not in function
print(3 not in d)
print(8 not in d)

d.clear() #clears the element of the dictionary
print(d)

del d
print(d)
'''

#WAP to implement and use loops

'''
#WAP to find if string is a palindrome or not
str1=input('Enter a character:')
l=len(str1)
p=l-1
index=0
while index<p:
    if str1[index]==str1[p]:
        index+=1
        p-=1
        print('String is palindrome')
        break
    else:
        print('String is not a palindrome')
        break
'''

#WAP to find a fibbonaci series

'''
num=int(input('How many terms:'))
n1,n2=0,1
if num<=0:
    print('Please enter a positive number')
else:
    print('It is a fibbonaci series')
for i in range(0,num):
    print(n1)
    sum=n1+n2
    n1=n2
    n2=sum
'''

#WAP to find if a number is amstrong

'''

sum=0
rem=0
num=int(input('Enter the number'))
temp=num
while(num>0):
 rem=num/10
 sum=sum+(rem*rem*rem)
 num=num//10
 if(sum==temp):
     print('It is an amstrong number')
 else:
     print('It is not an amstrong number')
'''



#Perform Various Operations On Strings Using Python.

'''
s='welcome to fycs'
print(s)

#Slicing in string
print(s[2:5])
print(s[:10])
print(s[:])
print(s[11:])
print(s[::2])

#Indexing in string
print(s[8])
print(s[-7])

#In and Not In operator
print('f' in s)
print('z' in s)
print('z' not in s)
print('f' not in s)

#Concatencation(Addition)
s1='welcome'
s2='to'
s3='python'
s4=s1+s2+s3 #Without blank space
print(s4)

s5=s1+' '+s2+' '+s3 #Method 1 for blank space
print(s5)

s0=' ' #Method 2 for blank space
s6=s1+s0+s2+s0+s3
print(s6)

#Built-in function

a='hello'
b='Hello There'
print(a.capitalize()) #Capitalize the first letter of string

print(a.center(15,'X')) #Push string to the center and fills rest with x
print(a.center(15,' '))

print(a.count('l',0,4)) #Count the occurance of l in string

print(a.endswith('o',0)) #Checks if string ends with element
print(a.endswith('a',0))

print(a.find('o',0)) #Prints the index value

print(a.index('h',0))

print(a.islower()) #Checks if all elements are in lowercase
print(b.islower()) 

print(a.istitle()) #Checks if 1st alphabets of string is capital
print(b.istitle()) 

print(type(a))

print(len(a))

print(b.lower())
print(a.upper()) 

print(max(a)) #Print maximal alphabetical number of string
print(min(a)) #Print minimal alphabetical number of string

print(b.startswith('Hello',0)) #Checks if string starts with Hello

print(b.endswith('There',0)) #Checks if string ends with There

print(a.rfind('l',0)) #Print index value of last occuring

print(a.rindex('l',0)) #Print index value of last occuring

print(b.swapcase()) #Conert lower to upper and vice-versa

print(a.title())  #Convert first letter of every word to capital

print(b.replace('There','Friends')) #Replace words

print(a.isalpha()) #Checks if string has alphabet

print(a.isdecimal()) #Checks if string has decimal number

print(a.isdigit()) #Checks if string has number

print(b.split()) #treats string as list and separe elements

c='     Teslas are the best     '
print(c.strip()) #Removes space from both side
print(c.lstrip()) #Removes space form left
print(c.rstrip()) #Removes spce from right

'''














