# Propositional Logic evaluator for discrete math for 2-3 variables
print("Propositional logic evaluator for discrete math")

variables = int(input("How many variables? "))
total_combinations = 2 ** variables

combinations_list = []  # store all the possible combinations

# generate the combinations
for i in range(total_combinations):
    bin_equivalent = bin(i)[2:]
    while len(bin_equivalent) < variables:
        bin_equivalent = "0" + bin_equivalent
    
    combinations_list.append(tuple(int(val) for val in bin_equivalent))
    # this will generate a list with values [(0,0), (0,1), (1,0), (1,1)]
    # for two variables

# main program
expression = input("Enter the propositional logic expression: ")
# note: Only the letters A, B, and C are allowed to be used
# example: not(A and B) or (A and C)

if variables == 2:
    print("A B F")
    for A, B in combinations_list:
        evaluated_expression = eval(expression)
        print(A, B, evaluated_expression)

elif variables == 3:
    print("A B C F")
    for A, B, C in combinations_list:
        evaluated_expression = eval(expression)
        print(A, B, C, evaluated_expression)
