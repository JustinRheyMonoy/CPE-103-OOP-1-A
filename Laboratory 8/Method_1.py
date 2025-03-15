#TUI Form
def main():
    L = []  # Find the largest number among three numbers

    num1 = float(input("Enter the first number: "))
    L.append(num1)
    num2 = float(input("Enter the second number: "))
    L.append(num2)
    num3 = float(input("Enter the third number: "))
    L.append(num3)
    print("The largest number among the three is:", max(L))

main()
