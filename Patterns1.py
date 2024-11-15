#Half diamonds for numbers and alphabets(ASKII)
for i in range(0, 6):
    for j in range(1, i+1):
        print(chr(64+j), end="")
    print("")
for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(chr(64+j), end="")
    print("")
for z in range(0, 6):
    for y in range(1, z+1):
        print("y", end="")
    print("")
for q in range(6, 0, -1):
    for r in range(1, q + 1):
        print("r", end="")
    print("")
