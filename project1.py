# print('hello world')

name = input('Type is your name? ')
print('hello', name , 'welcome to my game!')

should_we_play = input('Do you want to play? ').lower()

if should_we_play == 'yes' or should_we_play == 'y':
    print('ok lets play')
    direction = input('left or right? ').lower()
    if direction == 'left':
        print('you went left and fell of a cliff, ghame over')
    elif direction == 'right':
        print('you went right , right path')
        choice = input('Okay,  you now see a bridge , do you want to swim under it or cross it? (swim/cross)').lower()
        if choice == 'swim':
            print('you got eaten by an alligator, game over')
        else:
            print('you cross the bridge and make it to the other side')     
    else:
        print('sorry not a valid direction')
else:
    print('ok, see you next time')
