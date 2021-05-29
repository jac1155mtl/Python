#set alien_color to yellow
alien_color = 'yellow'

#test alien_color
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("The alien's color is {}! \nYou've just earned {} points!\n".format(alien_color,points))

#re-test alien_color to green and re-run test
alien_color = 'green'

#test alien_color
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("The alien's color is {}! \nYou've just earned {} points!\n".format(alien_color,points))

#re-test alien_color to red and re-run test
alien_color = 'red'

#test alien_color
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("The alien's color is {}! \nYou've just earned {} points!\n".format(alien_color,points))
