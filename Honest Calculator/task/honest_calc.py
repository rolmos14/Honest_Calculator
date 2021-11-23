messages = {0: "Enter an equation",
            1: "Do you even know what numbers are? Stay focused!",
            2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            3: "Yeah... division by zero. Smart move...",
            4: "Do you want to store the result? (y / n):",
            5: "Do you want to continue calculations? (y / n):"}

memory = 0
end = False

# Main loop
while not end:

    # Calculation loop
    while True:
        print(messages[0])
        x, oper, y = input().split()
        x = str(memory) if x == "M" else x
        y = str(memory) if y == "M" else y
        if (x.isdigit() or x.replace(".", "", 1).isdigit() and x.count(".") < 2) and \
                (y.isdigit() or y.replace(".", "", 1).isdigit() and y.count(".") < 2):
            pass
        else:
            print(messages[1])
            continue
        if oper not in ["+", "-", "*", "/"]:
            print(messages[2])
            continue
        if oper == "+":
            result = float(x) + float(y)
            break  # jump to print result
        if oper == "-":
            result = float(x) - float(y)
            break  # jump to print result
        if oper == "*":
            result = float(x) * float(y)
            break  # jump to print result
        if oper == "/" and float(y):
            result = float(x) / float(y)
            break  # jump to print result
        print(messages[3])

    print(result)

    # Store the result loop
    while True:
        print(messages[4])
        answer = input()
        if answer == "y":
            memory = result
            break  # jump to continue calculations loop
        elif answer != "n":
            continue
        break  # jump to continue calculations loop

    # Continue calculations loop
    while True:
        print(messages[5])
        answer = input()
        if answer == "y":
            break  # jump back to calculation loop
        if answer != "n":
            continue
        end = True  # finish main loop
        break
