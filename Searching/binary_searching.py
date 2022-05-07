# arr must be sorted by ascending order
def binary_search(arr, x):
    left = 0
    right = len(arr) -1   
    
    while left <= right :        
        center = (left + right) // 2
        if arr[center] > x :
            right = center -1 
        elif arr[center] < x :
            left = center +1
        else :
            return 1        
    return 0