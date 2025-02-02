def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = low + (high - low) // 2 #handle potential overflow

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target,low,mid-1) # mid value thus range shifts to left of former mid value
    else:
        return binary_search(arr, target, mid + 1, high) #mid value thus range shifts to right of former mid value
    
arr = [2,10,4,5,6,7,8] 
arr.sort() #binary search works for sorted array
print(binary_search(arr, 5, 0, len(arr)-1))