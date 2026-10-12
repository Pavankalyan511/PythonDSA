#math approach find out GCD
'''
a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
while b!=0:
    a,b=b,a%b
print('GCD:',a)
'''

#check whether the given number is prime or not
'''
n=int(input('Enter a number:'))
c=0
for i in range(1,n+1):
    if n%i==0:
       c+=1
if c==2:
    print('Prime Num')
else:
    print('Not a prime num')
'''

#Bruteforce: find a number in array 2 5 1 6 8 4 9 8 2 2 8
'''
arr=list(map(int,input('Enter elements:').split()))
search=int(input('Enter element to be searched:'))
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print(search,'Found at index:',i)
        found=True
        break
if not found:
    print('Value not in array')
'''
'''
arr=list(map(int,input('Enter elements:').split()))
search=int(input('Enter element to be searched:'))
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print(search,'Found at index:',i)
        found=True
        break
else:
   print('Value not in array')
'''

#find a character in a string
'''
s=input('Enter a word:')
ch=input("enter a char:")
found=False
for i in range(len(s)):
    if s[i]==ch:
        print(ch,'Found at :',i)
        found=True
        break
else:
    print(ch, "Not in the word")
'''

#greedy - coin change
'''
amount=int(input("Enter amount:"))
coins =[20,10,5,2,1]
count=0
for coin in coins:
    count+=amount//coin
    amount%=coin
print('Number of coins needed:',count)
'''

#Back Tracking = print all the binary strings
n=int(input('Enter n:'))
def backtrack(s):
    if len(s)==n:
        print(s)
        return
    backtrack(s+'0')
    backtrack(s+'1')
backtrack('')