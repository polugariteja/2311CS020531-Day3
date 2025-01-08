def sum_of_even_numbers(n):
    # Initialize the sum variable
    total_sum = 0

    # Loop through all numbers from 1 to n
    for num in range(2, n+1, 2):
        total_sum += num
    
    return total_sum

# Input from the user
n = int(input("Enter a positive integer: "))

# Call the function and display the result
print("Sum of all even numbers between 1 and", n, "is:", sum_of_even_numbers(n))
