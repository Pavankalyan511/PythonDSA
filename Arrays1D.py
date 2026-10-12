#print n natural numbers using while loop
'''n=int(input('Enter the value:'))
num=1
while num<=n:
    print(num,end=' ')
    num+=1
'''

#print n even numbers by using a loop
'''n=int(input('Enter the value:'))
num=1
while num<=n:
    if num%2==0:
        print(num,end=' ')
    num+=1
'''

#print n odd numbers by using a loop
'''n=int(input('Enter the value:'))
num=1
while num<=n:
    if num%2!=0:
        print(num,end=' ')
    num+=1
'''

#print sum of n numbers
'''
n=int(input())
i=1
sum=0
while n>=i:
    sum+=i
    i=i+1
print(sum)
'''

#print sum of even 
'''
n=int(input())
i=1
s=0
while i<=n:
    if i%2==0:
        s+=i
    i+=1
print(s)
'''

#print sum of odd
'''
n=int(input())
i=1
s=0
while i<=n:
    if i%2!=0:
        s+=i
    i+=1
print(s)
'''

n=int(input())
i=1
c=0
while c<n:
    if i%2==0:
        print(i,end=' ')
        c+=1
    i+=1