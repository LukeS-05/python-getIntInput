def getIntInput(prompt, min_value=-1_000_000_000, max_value=1_000_000_000, showRange=False):
    # Infinite loop until valid input is received
    while True:
        try:
            # Get user input and convert to integer
            if showRange == True:
                result = int(input(f"{prompt} ({min_value}-{max_value})"))
            else:
                result = int(input(f"{prompt}"))
            # Check if the input is within the specified range
            if result < min_value or result > max_value:
                print(f"Please enter an integer in the range of {min_value} and {max_value}.")
                continue
            break
        except ValueError:
            # If the input is not an integer
            print("Invalid input. Please enter a valid integer.")

    return result

# Example usage
num1 = getIntInput("Enter a number: ")
print(num1)
