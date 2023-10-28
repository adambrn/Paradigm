def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Элемент найден, возвращаем индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент справа от центра
        else:
            right = mid - 1  # Искомый элемент слева от центра
    
    return -1  # Элемент не найден

# Пример использования:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Элемент {target} найден в массиве, его индекс: {result}")
else:
    print(f"Элемент {target} не найден в массиве.")
