# arr = [12,11,13,5,6] => [5,6,11,12,13]

def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)

arr = [12,11,13,5,6]
bubble_sort(arr)

# Time Complexity O(n^2) Auxiliary Space O(1)