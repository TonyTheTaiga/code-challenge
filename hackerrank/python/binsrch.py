def binary_search(data, target, left, right):
    if left > right:
        return False
    
    mid = (left + right) // 2

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search(data, target, mid + 1, right)
    else:
        return binary_search(data, target, left, mid - 1)

data = [1,2,3,5,6,7,9,10, 123, 1235, 1236, 123678]

target = 123

left  = 0 

right = len(data) - 1

print(binary_search(data,target,left,right))
