#2d arrays and add all the elements of the array
'''
n=int(input('Enter the size of matrix:'))
arr=[]
sum=0
for i in range(n):
    row=list(map(int,input('Enter elements:').split()))
    arr.append(row)
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
'''

'''
n=int(input('Enter the size of matrix:'))
arr=[]
sum=0
for i in range(n):
    row=list(map(int,input('Enter elements:').split()))
    arr.append(row)
for i in range(n):
    for j in range(n):
        sum+=arr[i][j]
print('Sum:', sum)
'''

'''
n=int(input('Enter the size of matrix:'))
arr=[]
largest=arr[0][0]
for i in range(n):
    row=list(map(int,input('Enter elements:').split()))
    arr.append(row)
for i in range(n):
    for j in range(n):
        if arr[i][j]>largest:
            largest=arr[i][j]
print('Largest element:', largest)
'''

'''
n=int(input('Enter the size of matrix:'))
arr=[]
smallest=arr[0][0]
for i in range(n):
    row=list(map(int,input('Enter elements:').split()))
    arr.append(row)
for i in range(n):
    for j in range(n):
        if arr[i][j]<smallest:
            smallest=arr[i][j]
print('Smallest element:', smallest)
'''

'''
n=int(input('Enter the size of matrix:'))
arr=[]
for i in range(n):
    row=list(map(int,input('Enter elements:').split()))
    arr.append(row)
print('Array:')
for i in range(n):
    for j in range(n):
        print(arr[j][i],end=' ')
    print()
'''

'''
n=int(input('Enter the size of matrix:'))
arr1=[]
arr2=[]
for i in range(n):
    row1=list(map(int,input('Enter elements of first matrix:').split()))
    arr1.append(row1)
for i in range(n):
    row2=list(map(int,input('Enter elements of second matrix:').split()))
    arr2.append(row2)
print('Array sum:')
for i in range(n):
    for j in range(n):
        print(arr1[i][j]+arr2[i][j],end=' ')
    print()
'''

n=int(input('Enter the size of matrix:'))
arr=[]
for i in range(n):
    row=list(map(int,input('Enter elements:').split()))
    arr.append(row)
for i in range(n):
    total=0
    for j in range(n):
        total+=arr[i][j]
    print('Sum of row', i+1, ':', total)
for j in range(n):
    total=0
    for i in range(n):
        total+=arr[i][j]
    print('Sum of column', j+1, ':', total)