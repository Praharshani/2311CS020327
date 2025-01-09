n = int(input("Enter a positive integer: "))


print("Numbers from 1 to", n, "using a for loop:")
for i in range(1, n+1):
    print(i)

sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1

print("The sum of numbers from 1 to", n, "is:", sum_of_numbers)
# Task 1: Define a function calculate_square that takes a single argument n and returns the square of n
def calculate_square(n):
    return n * n

# Task 2: Ask the user to input a positive integer
n = int(input("Enter a positive integer to calculate its square: "))

# Task 3: Call the calculate_square function and display the result
result = calculate_square(n)
print(f"The square of {n} is: {result}")
