arr=list(map(int,input('Enter elements:').split()))
search=int(input('Enter element to be searched:'))
for i in range(len(arr)):
    if arr[i]==search:
        print('Element found at index',i)
        break
else:
    print('Element not found')