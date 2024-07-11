math = int(input("math: "))
science = int(input("science: "))
geometry = int(input("geometry: "))
chmestry = int(input("chmestry: "))
avg = (math + science + geometry + chmestry) / 4

if (
    math >= 0
    and math <= 20
    and geometry >= 0
    and geometry <= 20
    and science >= 0
    and science <= 20
    and chmestry >= 0
    and chmestry <= 20):

    if avg >= 16:
        print(f"your average is {avg} so your grade is A")
    elif avg >= 14:
        print(f"your average is {avg} so your grade is B")
    elif avg >= 12:
        print(f"your average is {avg} so your grade is C")
    elif avg >= 10:
        print(f"your average is {avg} so your grade is D")
    else:
        print("fail...")
else:
    print("average is false...")