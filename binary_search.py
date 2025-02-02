def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target,low,mid)
    else:
        return binary_search(arr, target, mid, high)
    
arr = [2,3,4,5,6,7,8]
print(binary_search(arr, 5, 0, len(arr)-1))