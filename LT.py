import random
print(f'ENTER THE NUMBER OF LINES')
for _ in range(int(input())):
    print(sorted(random.sample(range(1, 46), 6)))