##################################################
#                                                #
#  CopyRight (C)                                 #
#                                                #
#  GitHub link : https://github.com/AndreaXita   #
#  Discord : AndreaXita#9623                     #
#                                                #
##################################################



import curses
from copy import copy
from opcode import hasjabs
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

curses.initscr() 
window = curses.newwin(30, 60, 0, 0)
window.keypad(True)
window.border(0)
window.timeout(10)
snake = [[15,13], [15,12], [15,11]]
fruit = [5,35]
fruit_ = [5,35]
fruit__ = [5,35]
fruit2 = [5,35]
fruit2_ = [5,35]
fruit3 = [5,35]
fakefruit = [5,35]
fakefruit_ = [5,35]
fakefruit__ = [5,35]
fakefruit2 = [5,35]
start = [5,35]
visual = KEY_RIGHT
point = 0
coin = 0
# window.addch(fruit[0], fruit[1], '1')
# window.addch(fruit_[0], fruit_[1], '1')
# window.addch(fruit__[0], fruit__[1], '1')
# window.addch(fruit2[0], fruit2[1], '2')
# window.addch(fruit2_[0], fruit2_[1], '1')
# window.addch(fruit3[0], fruit3[1], '3')
# window.addch(fakefruit[0], fakefruit[1], 'x')
# window.addch(fakefruit_[0], fakefruit_[1], 'x')
# window.addch(fakefruit__[0], fakefruit__[1], 'x')
# window.addch(fakefruit2[0], fakefruit2[1], 'X')
window.addch(start[0], start[1], '5')


while True:
    window.addstr(0, 20, '(Free 5 points event) Score: ' + str(point) + ' ')
    window.addstr(0, 4, 'Coins : ' + str(coin) + ' ')
    tasto = window.getch()
    if tasto != -1:
        visual = tasto
    newhead = copy (snake[0])
    if visual == KEY_DOWN:
        newhead[0] += 1
    elif visual == KEY_UP:
        newhead[0] -= 1
    elif visual == KEY_RIGHT:
        newhead[1] += 1
    elif visual == KEY_LEFT:
        newhead[1] -= 1


    snake.insert(0, newhead)
    if snake[0][0] == 0 or snake[0][0] == 29 or snake[0][1] == 0 or snake[0][1] == 59: 
        break
    if snake[0] in snake[1:]:
        break
    if snake[0] == fruit:
        fruit = []
        point += 1
        coin += 1
        while fruit == []:
            fruit = [randint(1,28), randint(1,58)]
            if fruit in snake:
                fruit = []
        window.addch(fruit[0], fruit[1], '1')
    if snake[0] == fruit_:
        fruit_ = []
        point += 1
        coin += 1
        while fruit_ == []:
            fruit_ = [randint(1,28), randint(1,58)]
            if fruit_ in snake:
                fruit_ = []
        window.addch(fruit_[0], fruit_[1], '1')
    if snake[0] == fruit__:
        fruit__ = []
        point += 1
        coin += 1
        while fruit__ == []:
            fruit__ = [randint(1,28), randint(1,58)]
            if fruit__ in snake:
                fruit__ = []
        window.addch(fruit__[0], fruit__[1], '1')
    if snake[0] == fruit2:
        fruit2 = []
        point += 2
        coin += 1
        while fruit2 == []:
            fruit2 = [randint(1,28), randint(1,58)]
            if fruit2 in snake:
                fruit2 = []
        window.addch(fruit2[0], fruit2[1], '2')
    if snake[0] == fruit2_:
            fruit2_ = []
            point += 2
            coin += 1
            while fruit2_ == []:
                fruit2_ = [randint(1,28), randint(1,58)]
                if fruit2_ in snake:
                    fruit2_ = []
            window.addch(fruit2_[0], fruit2_[1], '2')
    if snake[0] == fruit3:
        fruit3 = []
        point += 3
        coin += 1
        while fruit3 == []:
            fruit3 = [randint(1,28), randint(1,58)]
            if fruit3 in snake:
                fruit3 = []
        window.addch(fruit3[0], fruit3[1], '3')
    if snake[0] == fakefruit_:
        fakefruit_ = []
        point -= 1
        coin -= 1
        while fakefruit_ == []:
            fakefruit_ = [randint(1,28), randint(1,58)]
            if fakefruit_ in snake:
                fakefruit_ = []
        window.addch(fakefruit_[0], fakefruit_[1], 'x')
    if snake[0] == fakefruit__:
        fakefruit__ = []
        point -= 1
        coin -= 1
        while fakefruit__ == []:
            fakefruit__ = [randint(1,28), randint(1,58)]
            if fakefruit__ in snake:
                fakefruit__ = []
        window.addch(fakefruit__[0], fakefruit__[1], 'x')
    if snake[0] == fakefruit:
        fakefruit = []
        point -= 1
        coin -= 1
        while fakefruit == []:
            fakefruit = [randint(1,28), randint(1,58)]
            if fakefruit in snake:
                fakefruit = []
        window.addch(fakefruit[0], fakefruit[1], 'x')
    if snake[0] == fakefruit2:
        fakefruit2 = []
        point -= 2
        coin -= 2
        while fakefruit2 == []:
            fakefruit2 = [randint(1,28), randint(1,58)]
            if fakefruit2 in snake:
                fakefruit2 = []
        window.addch(fakefruit2[0], fakefruit2[1], 'X')
    else:
        lastpart = snake.pop()
        window.addch(lastpart[0], lastpart[1], ' ')

    window.addch(snake[0][0], snake [0][1], '█')


curses.endwin()
print("""

GAME OVER,
you have scored: """ 
         + str(point))
print("and you got : " + str(coin) + """ Coins

 """)
