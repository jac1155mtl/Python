#set alien's color
alien_color = 'yellow'

#test if alien's color is green
if alien_color == 'green':
    print("The alien's color is green!")
    points = 5
else:
    print("The alien's color is not green!")
    points = 10
print("You have just earned {} points!\n".format(points))

#re-set alien's color to green
alien_color = 'green'

#re-run if-else block
if alien_color == 'green':
    print("The alien's color is green!")
    points = 5
else:
    print("The alien's color is not green!")
    points = 10
print("You have just earned {} points!\n".format(points))
