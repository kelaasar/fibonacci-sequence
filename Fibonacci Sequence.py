# this prints the fibonacci sequence


def main():
    amount_of_elements = 0
    end = False

    while not end:
        amount_of_elements = int(input("How many numbers should be generated from the Fibonacci Sequence? "))
        print()
        generateFibonacci(amount_of_elements)
        print()
        finished = input("Would you like to exit (Y/N)? ")
        print()
        if finished == "Yes" or finished == "YES" or finished == "y" or finished == "Y" or finished == "yes":
            end = True

    print()
    print("-------Program Terminated-------")


def generateFibonacci(amount_of_elements):
    first_element = 1
    second_element = 1
    print("Fibonacci Sequence: ", end='')
    print(str(first_element) + ", " + str(second_element), end='')
    for i in range(1, amount_of_elements-2):
        j = first_element + second_element
        print(", " + str(j), end='')
        first_element = second_element
        second_element = j
    print()


main()
