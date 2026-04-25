num = int(input("Введите натуральное число "))

count_3 = 0
count_last_digit = 0
count_even = 0
sum_more_5 = 0
product_more_7 = 1
count_0_or_5 = 0

if num == 0:
    count_last_digit = 1
    count_even = 1
    count_0_or_5 = 1
else:
    last_digit = num % 10
    temp = num
    count_gt_seven = 0
    while temp > 0:
        digit = temp % 10

        if digit == 3:
            count_3 += 1

        if digit == last_digit:
            count_last_digit += 1

        if digit % 2 == 0:
            count_even += 1

        if digit > 5:
            sum_more_5 += digit

        if digit > 7:
            product_more_7 *= digit
            count_gt_seven += 1

        if digit == 0 or digit == 5:
            count_0_or_5 += 1
        temp //= 10

    if count_gt_seven == 0:
        product_more_7 = 1

print(f"Кол-во цифр 3: {count_3}")
print(f"Кол-во раз встречается последняя цифра: {count_last_digit}")
print(f"Кол-во четных цифр: {count_even}")
print(f"Сумма цифр больших 5: {sum_more_5}")
print(f"Произведение цифр больших 7: {product_more_7}")
print(f"Кол-во раз встречаются цифры 0 и 5: {count_0_or_5}")