for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                s = a**5 + b**5 + c**5 + d**5
                e = int(s**0.2)
                if e <= 150 and e**5 == s:
                    print(a, b, c, d, e, "cумма >>>", a+b+c+d+e)
