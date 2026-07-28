## =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest


def find_minimum(numbers):
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    count = int(input("How many numbers? "))

    # Stop if N is 0 or negative
    if count <= 0:
        print("Error: Please enter a positive number.")
    else:
        numbers = []

        # Get each number from the user
        for i in range(1, count + 1):
            val = float(input(f"Enter number {i}: "))
            numbers.append(val)

        # Print all results
        print("\nResults:")
        print(f"Sum:     {calculate_sum(numbers)}")
        print(f"Average: {calculate_average(numbers)}")
        print(f"Maximum: {find_maximum(numbers)}")
        print(f"Minimum: {find_minimum(numbers)}")