print('Lets play a game')
print('You choose a number and the program will tell you the color hiding on your number.')
print('You should choose from 1 to 4.')

a = int(input('Make your choose here '))

if a == 1:
    print('GREEN')
elif a == 2:
    print('RED')
elif a == 3:
    print('BLUE')
elif a ==4:
    print('ORANGE')
else:
    print('Error, you didnot choose a number from 1 to 4.')