for bulls in range(0, 11):
    for cows in range(0, 21):
        for calves in range(0, 201):
            if bulls + cows + calves == 100:
                if 10*bulls + 5*cows + 0.5*calves == 100:
                    print(f"Быки={bulls}, Коровы={cows}, Телят={calves}")