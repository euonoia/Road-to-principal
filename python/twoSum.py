def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] + arr[j] == target:
                    return print([i,j])
twoSum([3,2,4],6)