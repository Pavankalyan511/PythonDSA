#processing of an array
'''
arr=list(map(int,input('enter elements:').split()))
for value in arr:
    print(value,end=' ')
'''

'''
arr=list(map(int,input('enter elements:').split()))
sum=0
for value in arr:
    sum+=value
print(sum)
'''

#maximum number in a list
'''
arr=list(map(int,input('Enter elements:').split()))
max=0
for value in arr:
    if value>max:
      max=value
print(max)
'''

#count the even odd numbers in an array
'''
arr=list(map(int,input().split()))
even=0
odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print('Num of even:',even)
print('Num of odd:',odd)
'''

arr=list(map(int,input('Enter elements:').split()))
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]>arr[j]:
            arr[i], arr[j]=arr[j], arr[i]
print('sorted array is:',*arr)


