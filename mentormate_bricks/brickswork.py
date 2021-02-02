import numpy as np
col_input = 0
row_input = 0

while col_input == 0:
    m = input("Enter an even number of columns: ").strip()
    if not m.isdigit():
        print("m must be an integer value.")
    elif int(m) < 2 or int(m) > 100:
        print("m must be a number between 2 and 100")
    elif int(m) % 2 != 0:
        print("m must be an even number between 2 and 100.")
    else:
        m = int(m)
        col_input += 1

while row_input == 0:
    n = input("Enter an even number of rows: ").strip()
    if not n.isdigit():
        print("n must be an integer value.")
        continue
    elif int(n) < 2 or int(n) > 100:
        print("n must be a number between 2 and 100")
    elif int(n) % 2 != 0:
        print("n must be an even number between 2 and 100.")
    else:
        n = int(n)
        row_input += 1


def create_layers():
    """
    * Fills a list(layer1) from the user's input and prints it n*m metric layout. If the user's input is not valid
    prints corresponding error message and stops the script.
    * Then creates an actual array(layer2) from the list(layer1) and resizes it to n*m metric array.
    * After that it checks if the bricks are horizontal or vertical and rearranges the array so the bricks from layer2
    are not the same orientation as those from layer1(if the brick is horizontal it flips it to be vertical and if the
    brick is vertical again flips it to be horizontal).
    * Creates another list(list1) with n+1 * m+1 size, so when we make an array out of this list and compare values, the
     array doesn't go out of bounds.
    * Creates an array(layer3) from list1 and fills it with the values from layer2. After that checks the orientation of
    the bricks and puts visual borders(lines) and prints the result.
    """
    layer1 = []
    possible_values = []

    for i in range(int(m*n/2)):
        possible_values.append(i+1)
        possible_values.append(i+1)

    for i in range(n):
        for j in range(m):
            x = input("Enter an integer between 1 and {}, for {} element in {} row: ".format(int((m*n)/2),
                                                                                             j+1, i+1)).strip()
            if not x.isdigit() or int(x) < 1 or int(x) > int((m*n)/2):
                print("x must be an integer between 1 and {}.".format(int((m*n)/2)))
                return
            else:
                layer1.append(int(x))
                if int(x) in possible_values:
                    possible_values.remove(int(x))
                else:
                    print("The layer you are trying to make will not be valid.")
                    return

    print()
    for i, item in enumerate(layer1, 1):
        print(item, end="\n" if i % m == 0 else " " if len(str(item)) == 2 else "  ")

    layer2 = np.array(layer1)
    layer2.resize(n, m)
    x = 1

    for i in range(0, n, 2):
        for j in range(0, m, 2):
            if layer2[i, j] == layer2[i, j+1] or layer2[i+1][j] == layer2[i+1, j+1]:
                layer2[i][j] = x
                layer2[i+1][j] = x
                layer2[i][j+1] = x+1
                layer2[i+1][j+1] = x+1
                x += 2
            else:
                layer2[i][j] = x
                layer2[i][j+1] = x
                layer2[i+1][j] = x+1
                layer2[i+1][j+1] = x+1
                x += 2

    list1 = [[0 for _ in range(m+1)] for _ in range(n+1)]
    layer3 = np.array(list1)

    for i in range(n):
        for j in range(m):
            layer3[i][j] = layer2[i][j]

    brick_border = ""
    for i in range(n):
        print(brick_border)
        if i == 0:
            print(" --- ---" * int(m/2))
        print("|", end="")
        brick_border = "|"
        for j in range(m):
            if layer3[i][j] == layer3[i][j+1]:
                if len(str(layer3[i][j])) == 1 or str(layer3[i][j+1]) == 1:
                    print("", str(layer3[i][j]) + "   " + str(layer3[i][j+1]) + " |", end="")
                    brick_border += "--- ---|"
                    continue
                else:
                    print("", str(layer3[i][j]) + " " + str(layer3[i][j + 1]) + " |", end="")
                    brick_border += "--- ---|"
                    continue
            elif layer3[i][j] == layer3[i][j-1]:
                continue

            if layer3[i][j] == layer3[i+1][j]:
                if len(str(layer3[i][j])) == 1 or len(str(layer3[i+1][j])) == 1:
                    print("", str(layer3[i][j]) + " |", end="")
                    brick_border += "   |"
                else:
                    print("", str(layer3[i][j]) + "|", end="")
                    brick_border += "   |"
            else:
                if len(str(layer3[i][j])) == 1:
                    print("", str(layer3[i][j]) + " |", end="")
                    brick_border += "---|"
                else:
                    print("", str(layer3[i][j]) + "|", end="")
                    brick_border += "---|"
        print()
    print(" --- ---" * int(m / 2))


if __name__ == '__main__':
    create_layers()
