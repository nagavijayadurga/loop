numbers = [1, 2, 3, 4, 5]
total = 0
for i in numbers:
    total = total + i * i
print(total)


def print_characters(text):
    for ch in text:
        print(ch)

# Example
print_characters("Python")


numbers = [12, 45, 7, 89, 34, 99, 23]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum number:", maximum)


n = 10
a, b = 0, 1
print("First 10 Fibonacci numbers:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


    student = {"name": "Ravi", "age": 20, "city": "hyderabad"}
for key, value in student.items():
    print(f"{key}: {value}")