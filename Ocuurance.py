#first occurance of a digit and get the index value of it
'''
arr=list(map(int,input('Enter the value:').split()))
val=int(input('Enter a value:'))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==val:
        ans=mid
        high=mid-1
    elif arr[mid]<val:
        low=mid+1
    else:
        high=mid-1
print(ans)
'''

#last occurance of a digit and get the index value of it
arr=list(map(int,input().split()))
val=int(input('Enter a value:'))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==val:
        ans=mid
        low=mid+1
    elif arr[mid]<val:
        low=mid+1
    else:
        high=mid-1
print(ans)