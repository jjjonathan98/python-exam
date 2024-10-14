import random


# This function generates the random list from 1 - 50.
def generate_random_list():
    return [random.randint(1, 50) for _ in range(10)]


# This function substitutes the square of the element if it´s multiply by 5.
def substitute(gen_list):
    for i in range(len(gen_list)):
        if gen_list[i] % 5 == 0:
            gen_list[i] = gen_list[i] ** 2


def main():
    # This takes the generated list and applies it to the random list variable.
    random_list = generate_random_list()

    # This will print that random list, before the substitution is calculated.
    print(f"Before substitution, the list is: {random_list}")

    # This function call applies the substitute function to the generated random list.
    substitute(random_list)

    # This prints the modified list, after the substitution is applied.
    print(f"After substitution, the list is: {random_list}")


# Runs the program
main()
