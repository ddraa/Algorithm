def solution(money, expected, actual):
    bat = 100
    for ex, ac in zip(expected, actual):
        if ex == ac:
            money += bat
            bat = 100
        else:
            money -= bat
            if money == 0:
                break
            elif 2 * bat > money:
                bat = money
            else:
                bat *= 2
    return money

print(solution(1000, ['H', 'T', 'H', 'T', 'H', 'T', 'H']			,['T', 'T', 'H', 'H', 'T', 'T', 'H']		))