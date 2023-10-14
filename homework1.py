def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def sort_list_declarative(numbers):
    sorted(numbers, reverse=True)

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers)
sort_list_declarative(numbers)
print(numbers)