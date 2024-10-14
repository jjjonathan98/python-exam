
def main():
    # Lists where the numbers will be stored based on value.
    positives = []
    zeros = []
    negatives = []

    # This reads integers from the input, and seperates positive number, zeros and negative numbers into lists.
    while True:
        user_input = input("Enter an integer(blank to quit): ")

        # Check if the user entered a blank line to break the loop.
        if user_input == "":
            break

        # Converts the input to an integer.
        number = int(user_input)
        # Numbers get categorized into positives, zeros and negatives.
        if number > 0:
            positives.append(number)
        elif number == 0:
            zeros.append(number)
        else:
            negatives.append(number)

    # Prints out the lists of numbers in the order: positives, zeros and negatives.
    print("The numbers were:")
    numbers = positives + zeros + negatives
    for num in numbers:
        print(num, end=" ")


# Runs the program
main()
