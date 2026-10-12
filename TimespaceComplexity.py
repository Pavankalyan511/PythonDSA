#O(1)--> T.C=O(1) constant, S>C=O(n)
'''
arr=list(map(int,input('Enter elements:').split()))
print('last element:', arr[-1]) 
print('First element:',arr[0])
'''

#linear time T>C-O(n) constant S>C-O(1)
'''
arr=list(map(int,input('Enter elements:').split()))
maximum=arr[0]
for val in arr:
    if val>maximum:
        maximum=val
print('Maximum element:', maximum)
'''

#linear time T>C-O(n^2) constant S>C-O(1)
'''
n=int(input('Enter value of n:'))    
for i in range(n):
    for j in range(n):
        print(i,j, end='  ')
    print()
'''
'''
n=int(input('Enter value of n:'))    
for i in range(n):
    for j in range(n):
        for k in range(n):
          print(i,j,k, end='  ')
        print()
    print()
'''

#log(n) time T>C-O(log n) constant S>C-O(1)
'''
n=int(input('Enter value of n:'))
while n>1:
    n=n//2
    print(n)
'''

n=int(input('Enter value of n:'))
num=1
for i in range(n):
    for j in range(n):
        print(num,end=' ')
        num+=1
    print()