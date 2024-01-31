presses = 0
while presses < 12:
    ran = int(input())
    presses += ran
    if presses >= 12:
        print(presses - 12)
