import random

options = ['A', 'A','2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K']

for i in range(10):
    print(options[random.randint(0, len(options)-1)], options[random.randint(0, len(options)-1)])
    print(options[random.randint(0, len(options)-1)])
    print()