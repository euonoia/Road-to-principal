def sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]

    print(arr)

sort([10,9,3,55,100,1000])