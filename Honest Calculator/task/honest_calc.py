def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages[6]
    if (v1 == "1" or v2 == "1") and v3 == "*":
        msg += messages[7]
    if (v1 == "0" or v2 == "0") and v3 in ["*", "+", "-"]:
        msg += messages[8]
    if msg != "":
        msg = messages[9] + msg
        print(msg)


def is_one_digit(v):
    # Check if v is integer, or if it is a float check if it has decimals
    if (v.isdigit() or v.replace(".", "", 1).isdigit() and float(v) % 1 == 0.0) and -10 < float(v) < 10:
        output = True
    else:
        output = False
    return output


messages = {0: "Enter an equation",
            1: "Do you even know what numbers are? Stay focused!",
            2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            3: "Yeah... division by zero. Smart move...",
            4: "Do you want to store the result? (y / n):",
            5: "Do you want to continue calculations? (y / n):",
            6: " ... lazy",
            7: " ... very lazy",
            8: " ... very, very lazy",
            9: "You are"}

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
        check(x, y, oper)
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
