#binary search
'''
arr=list(map(int,input('Enter elements:').split()))
search=int(input('Enter elements to be searched'))
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==search:
        print('Element found at index:',mid)
        break
    elif arr[mid]<search:
        left=mid+1
    else:
        right=mid-1
else:
    print('Element not found')
'''

# binary search pattern
n=int(input('Enter n:'))
left=0
right=n
while left<=right:
    mid=(left+right)//2
    if mid * mid ==n:
        print('Square root:',mid)
        break
    elif mid*mid<n:
        left=mid+1
    else:
        right=mid-1
else:
    print('Integer square root:', right)
