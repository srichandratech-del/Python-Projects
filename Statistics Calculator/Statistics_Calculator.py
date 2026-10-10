# Statistics Calculator

def median_calculator():

    x = input("Enter the values of x separated by commas: ").split(',')
    fr = input("Enter the values of frequencies separated by commas: ").split(',')

    X = []
    FR = []

    for i in x:
        X.append(int(i))

    for f in fr:
        FR.append(int(f))

    cf = []
    total = 0

    if len(X) != len(FR):
        print("Error: The lengths of x and fr must be the same.")

    elif len(X) == 0:
        print("Error: The lists cannot be empty.")

    else:
        for f in FR:
            total = total + f
            cf.append(total)

        N = sum(FR)
        median_position = N / 2

        for i in range(len(cf)):
            if cf[i] >= median_position:
                median = X[i]
                break

        print('-'*30)
        print("Cumulative Frequency:", cf)
        print("Median:", median)
        print('-'*30)     

def mean_calculator():

    x = input("Enter the values of x separated by commas: ").split(',')
    fr = input("Enter the values of frequencies separated by commas: ").split(',')

    X = []
    FR = []
    total = 0
    for i in x:
        X.append(int(i))

    for f in fr:
        FR.append(int(f))

    if len(X) != len(FR):
        print("Error: The lengths of x and fr must be the same.")

    elif len(X) == 0:
        print("Error: The lists cannot be empty.")

    else:
        for i in range(len(X)):
            total += X[i] * FR[i]
        total_freq = sum(FR)
        mean = total / total_freq

        print('-'*30)
        print("Frequencies:", FR)
        print("Mean:", mean)
        print('-'*30)

def mode_calculator():

    x = input("Enter the values of x separated by commas: ").split(',')
    fr = input("Enter the values of frequencies separated by commas: ").split(',')

    X = []
    FR = []

    for i in x:
        X.append(int(i))

    for f in fr:
        FR.append(int(f))

    if len(X) != len(FR):
        print("Error: The lengths of x and fr must be the same.")

    elif len(X) == 0:
        print("Error: The lists cannot be empty.")

    else:
        max_frequency = max(FR)
        mode = X[FR.index(max_frequency)]

        print('-'*30)
        print("Frequencies:", FR)
        print("Mode:", mode)
        print('-'*30)

def main():
    print("-"*len("| Welcome to the Statistics Calculator |"))
    print("| Welcome to the Statistics Calculator |")
    print("-"*len("| Welcome to the Statistics Calculator |"))
    print("Options:")
    print("1. Calculate Median")
    print("2. Calculate Mean")
    print("3. Calculate Mode")
    print("4. Exit")
    print("-"*20)
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            median_calculator()
        elif choice == '2':
            mean_calculator()
        elif choice == '3':
            mode_calculator()
        elif choice == '4':
            print("-"*30)
            print("Exiting the program.")
            print("Thank you for using the Statistics Calculator!")
            print("-"*30)
            exit()
        else:
            print("Invalid choice. Please try again.")

main()            
