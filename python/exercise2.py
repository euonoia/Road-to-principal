def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] + arr[j] == target:
                    print(f"{arr[i]} + {arr[j]} = {target}")
                    return True
    return False
twoSum([3,2,4],6)