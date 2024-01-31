p1 = input()
p2 = input()
p3 = input()

if p1 == p2 == p3:
    print("OK")
elif (p2 != p1) and (p3 != p1):
    print("BOTH MISMATCH")
elif (p1 == p3) and (p2 != p1):
    print("ENTRY 2 MISMATCH")
else:
    print("ENTRY 3 MISMATCH")
