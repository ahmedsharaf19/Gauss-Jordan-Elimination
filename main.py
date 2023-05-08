import getting_info


def gauss_jordan_elimination(a, b):
    """
    :param a: coefficients nested_list
    :param b: constant terms list
    :return: flag --> to indicate if a no solution or infinite solution occurs
             b --> result to be displayed if system returned one solution
    """
    flag = 3
    no_sol_flag = False
    n = len(b)
    lst_temp = [0.0] * n
    # Check if any row is a zero row
    for i in a:
        if i == lst_temp:
            no_sol_flag = True
            flag = 1

    for k in range(n):
        # Replace the row in which the pivot element is with zero
        # Method Called Partial Pivoting
        if round(a[k][k]) == 0:
            for i in range(k + 1, n):
                if abs(a[i][k]) > a[k][k]:
                    for j in range(k, n):
                        temp = a[k][j]
                        a[k][j] = a[i][j]
                        a[i][j] = temp

                    temp = b[k]
                    b[k] = b[i]
                    b[i] = temp
                    break

        # Convert the pivot elements to one to get the unity matrix
        pivot = a[k][k]
        # handle divide by zero and check if no solution
        if pivot == 0:
            flag = 1
        else:
            for j in range(k, n):
                a[k][j] /= pivot
            b[k] /= pivot

        # Apply Gauss Jordan Elimination
        for i in range(n):
            # Skip Elements Already Equal to 0 And Skip Pivot Element
            if i == k or a[i][k] == 0:
                continue
            factor = a[i][k]
            for j in range(k, n):
                a[i][j] -= factor * a[k][j]
            b[i] -= factor * b[k]

    # check if one solution
    if a[-1][-1] == 1 and not no_sol_flag:
        flag = 3

    # check if infinite solution
    elif a[-1][-1] == b[-1]:
        flag = 2

    return flag, b


print("#" * 86)
print(f"# Welcome to the program for solving linear equations using the Gauss Gordon method. #")
print("#" * 86)

getting_info.examples()

print("To learn how to use the program, please go to the file \"user_manual\" in program files ")
x = input("press the letter ( Y or y )  , to solve the equations or 'q' to exit ").lower()

if x == 'y' or x == 'yes':

    factors, result = getting_info.getting_equations()

    special_flag, final_result = gauss_jordan_elimination(factors, result)

    with open(__file__.replace("main.py", "solution.txt"), "w", encoding='utf-8') as f:
        if special_flag == 1:
            f.write("There is no solution")
        elif special_flag == 2:
            f.write("infinite number of solutions")
        else:
            sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
            index = 1
            for x in final_result:
                f.write(f"x{index} ".translate(sub) + f"= {x}\n")
                index += 1

    print("The solution has been saved to a file \"solution\"")
    print(__file__.replace("main.py", "solution.txt"))

print("Thank you for using our software\nSee you soon")
