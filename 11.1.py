total_month = 12
total_day = 365

flag = False

for n in range(1, 13):
    for k in range(1, 13):
        m = total_month - n - k
        if (28*n + 30*k + 31*m) == total_day:
            print(f"n = {n}, k = {k}, m = {m}")
            flag = True

