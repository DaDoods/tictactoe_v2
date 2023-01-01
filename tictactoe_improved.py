import turtle
import random

#====Setup====#
red_turn = False
win_cond = [[[0,1,2], [3, 4, 5], [6,7,8]], #Horiz Win Con
            [[0,3,6], [1,4,7], [2,5,8]], #Vert Win Con
            [[0,4,8],[2,4,6]]] #Diagonal Win Con
turn_color = {True: 'red', False: 'blue', 'Tie': 'green'}
winner = {False: "'s Turn", True: 'wins', 'Tie': 'It is a'}
wn = turtle.Screen()
wn.addshape('restart_button.gif')
#====Game====#
def declare(result, turn, tie = False):
    global announce
    announce.clear()
    color = turn_color[result]
    announce.pencolor(color)
    if not tie:
        announce.write(f'{color.title()} {winner[turn]}', align='center', font=('Arial', 50,'bold'))
    else:
        announce.write(f'{winner[result]} Tie', align='center', font=('Arial', 50,'bold'))
    if turn:
        wn.tracer(False)
        announce.sety(250)
        announce.shape('restart_button.gif')
        announce.showturtle()
        announce.onclick(game)
        wn.tracer(True)

def check_winner():
    global game_over
    test = []
    for con in win_cond:
        for method in con:
            for num in method:
                test.append(grid[num].fillcolor())
            if len(set(test)) == 1 and 'black' not in test:
                game_over = True
                return test[0]
            else:
                test = []
    return False
                
def clicked(turtle):
    global red_turn,turn, game_over
    if turtle.fillcolor() == 'black' and not game_over:
        turtle.color(turn_color[red_turn])
        red_turn = not red_turn
        if turn <= 8 and check_winner():
            red_turn = not red_turn
            declare(red_turn, game_over) 
        elif turn >=8 and not check_winner():
            game_over = True
            declare('Tie','Tie', True)
        else:
            declare(red_turn, game_over)
        turn +=1

def game(*args):
    global announce, wn, grid, turn, game_over
    wn.clear()
    wn.bgcolor('black')
    turn  = 0
    game_over = False
    grid = [] #Create the grid
    wn.tracer(False)
    for column in range(1,-2,-1):
        for rows in range(-1,2):
            square= turtle.Turtle()
            square.shape('square')
            square.pu()
            square.pencolor('white')
            square.turtlesize(5)
            square.goto(125*rows, 125*column)
            grid.append(square)
    
    announce = turtle.Turtle() #To annouce text at the top
    announce.pu()
    announce.hideturtle()
    announce.sety(300)
    curr_turn = random.choice([1,2])
    if curr_turn == 1:
        red_turn = True
    else:
        red_turn = False
    declare(red_turn, game_over)
    wn.tracer(True)
    grid[0].onclick(lambda x ,y: clicked(grid[0]))
    grid[1].onclick(lambda x ,y: clicked(grid[1]))
    grid[2].onclick(lambda x ,y: clicked(grid[2]))
    grid[3].onclick(lambda x ,y: clicked(grid[3]))
    grid[4].onclick(lambda x ,y: clicked(grid[4]))
    grid[5].onclick(lambda x ,y: clicked(grid[5]))
    grid[6].onclick(lambda x ,y: clicked(grid[6]))
    grid[7].onclick(lambda x ,y: clicked(grid[7]))
    grid[8].onclick(lambda x ,y: clicked(grid[8]))
game()
wn.mainloop()