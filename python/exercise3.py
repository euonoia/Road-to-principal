def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] == arr[j]:
                    return True
    return False

print(has_duplicate([1, 5, 7, 3, 7])) # Should print True
print(has_duplicate([1, 5, 7, 3]))