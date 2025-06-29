import keyword

name = input()

if name in keyword.kwlist:
    print(False)
elif name[0].isdigit():
    print(False)
elif name.count("_") > 1 and name.replace("_", "") == "":
    print(False)
else:
    good = True
    for char in name:
        if char.isupper():
            good = False
        if not (char.islower() or char.isdigit() or char == "_"):
            good = False
    print(good)
