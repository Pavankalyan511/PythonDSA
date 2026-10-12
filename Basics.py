#Write a program to find the sum of digits of a number
'''n=int(input("Enter a number: "))
sum=0
while n!=0:
    digit=n%10
    sum+=digit
    n//=10
print('Sum:',sum)
print('Polymorphed to:',n)
'''

#Write a program to find reverse of a number
'''n=int(input("Enter a number: "))
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print('Reversed:',rev)
'''

'''
n=int(input("Enter a number: "))
while n!=0:
    digit=n%10
    print(digit,end='')
    n//=10
'''

#Harshad's number or Niven's number
'''
n=int(input("Enter a number: "))
sum=0
temp=n
while n!=0:
    digit=n%10
    sum+=digit
    n//=10
if temp%sum==0:
    print("Harshad's number")
else:
    print("not a Harshad's number")
'''
