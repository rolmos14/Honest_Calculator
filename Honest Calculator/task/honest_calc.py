messages = {0: "Enter an equation",
            1: "Do you even know what numbers are? Stay focused!",
            2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            3: "Yeah... division by zero. Smart move..."}

while True:
    print(messages[0])
    x, oper, y = input().split()
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
        break
    if oper == "-":
        result = float(x) - float(y)
        break
    if oper == "*":
        result = float(x) * float(y)
        break
    if oper == "/" and float(y):
        result = float(x) / float(y)
        break
    print(messages[3])

print(result)
