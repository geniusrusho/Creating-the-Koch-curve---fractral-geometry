import turtle
iterations = input("Enter number of iteration: ")
iterations = int(iterations)
startlength = 200 #length of generations

#pick up the en and move the turte oer to the left
turtle.up()
turtle.setpos(-startLength*3/2,startLength*3/2/2)
turtle.speed(0)
koch='F'
for i in range(iterations):
    koch = koch.replace('F','FLFRFLF')

turtle.down()
turtle.color('red','black')
turtle.begin_fill()

for move in koch:
    if move == 'F':
        turtle.forward(starLength/(3**(iterations-1)))
    elif move == 'R':
        turtle.right(120)
    elif move == 'L':
            turtle.left(60)

turtle.end_fill()
                                                    
