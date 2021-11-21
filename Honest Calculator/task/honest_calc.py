messages = {"msg_0": "Enter an equation",
            "msg_1": "Do you even know what numbers are? Stay focused!",
            "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?"}

while True:
    print(messages["msg_0"])
    x, oper, y = input().split()
    if (x.isdigit() or x.replace(".", "", 1).isdigit() and x.count(".") < 2) and \
            (y.isdigit() or y.replace(".", "", 1).isdigit() and y.count(".") < 2):
        pass
    else:
        print(messages["msg_1"])
        continue
    if oper not in ["+", "-", "*", "/"]:
        print(messages["msg_2"])
        continue
    break
