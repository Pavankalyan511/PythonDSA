'''
n=int(input('Enter n:'))
arr=[[0] * n for _ in range(n)]
#print(arr)
left=0
right=n-1
top=0
bottom=n-1
num=1
while top<=bottom and left<=right:
    for i in range(left, right+1):
        arr[top][i]=num
        num+=1
    top+=1
    for i in range(top,bottom+1):
        arr[i][right]=num
        num+=1
    right-=1
    for i in range(right, left-1,-1):
        arr[bottom][i]=num
        num+=1
    bottom-=1
    for i in range(bottom, top-1,-1):
        arr[i][left]=num
        num+=1
    left+=1
for row in arr:
    print('  '.join(f'{x:2}' for x in row))
'''

n=int(input('Enter size of matrix:'))
a=[]
for i in range(n):
    row=list(map(int,input('Enter elements:').split()))
    a.append(row)
print(a)
top=0
bottom=n-1
left=0
right=n-1
while top<=bottom and left<=right:
    for i in range(left,right+1):
        print(a[top][i],end=' ')
    top+=1
    for i in range(top,bottom+1):
        print(a[i][right],end=' ')
    right-=1
    for i in range(right, left-1,-1):
        print(a[bottom][i],end=' ')
    bottom-=1
    for i in range(bottom, top-1,-1):
        print(a[i][left],end=' ')
    left+=1