#merge sort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    result=[]
    while left and right:
        if left[0]< right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result+left+right
arr=list(map(int,input('Enter elements:').split()))
print('Sorted array:',*merge_sort(arr))