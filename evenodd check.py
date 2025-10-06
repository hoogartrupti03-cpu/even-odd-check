# Program to check if a number is even or odd

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get a list of numbers from the user
numbers = input("Enter numbers separated by spaces: ").split()

# Convert input strings to integers
numbers = [int(num) for num in numbers]

# Initialize prime count
prime_count = 0

# Process each number
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

    if is_prime(num):
        prime_count += 1

# Ou
