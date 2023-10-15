'''
Этот код решает задачу с использованием процедурной и структурной парадигмы, что делает его понятным и легко читаемым.
'''

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            result = i * j
            print(f"{i} * {j} = {result}")

n = int(input("Введите число n: "))
multiplication_table(n)
