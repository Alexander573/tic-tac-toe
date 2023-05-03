import pygame
import random
from time import sleep








WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CORAL = (255,127,88)

WIDTH = 300
HEIGHT = 300

FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Крестики-нолики")
clock = pygame.time.Clock()

field = [['','',''],
         ['','',''],
         ['','','']]

game_over = False

def draw_grid():
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 3)


def tic_tac_toe():
    for i in range(0,3):
        for j in range(0,3):
            if field[i][j] == 'x':
                pygame.draw.line(screen, BLACK, (j*100 + 5, i*100 + 5), (j*100 + 95, i*100 + 95), 3)
                pygame.draw.line(screen, BLACK, (j*100+ 95, i*100 + 5), (j*100 + 5, i*100 + 95), 3)
            elif field[i][j] == '0':
                pygame.draw.circle(screen, BLACK, (j * 100 + 50, i * 100 + 50), 45, 3)


def get_win_check(symbol):
    flag_win = False
    global win
    for line in field:
        if line.count(symbol) == 3:
            flag_win = True
            win = [[0,field.index(line)],[1,field.index(line)],[2,field.index(line)]]
    for u in range(3):
        if field[0][u] == field[1][u] == field[2][u] == symbol:
            flag_win = True
            win = [[u,0],[u,1],[u,2]]
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2, 0]]
    return flag_win

run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if field[pos[1]//100][pos[0]//100]=='':
                field[pos[1] // 100][pos[0] // 100] = 'x'
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != '':
                    x,y = random.randint(0,2), random.randint(0,2)
                field[x][y] = '0'
            player_win = get_win_check('x')
            ai_win = get_win_check('0')
            rezult = field[0].count('x') + field[0].count('0') + field[1].count('x') + field[1].count('0') + field[2].count('x') + field[2].count('0')
            if player_win or ai_win:
                game_over = True
                if player_win:
                    pygame.display.set_caption('вы победили')

                else:
                    pygame.display.set_caption('комп победил')
            elif rezult == 8:
                pygame.display.set_caption('ничья')


    screen.fill(WHITE)
    if game_over:
        pygame.draw.rect(screen,GREEN,(win[0][0] * 100,win[0][1] * 100,100,100))
        pygame.draw.rect(screen,GREEN,(win[1][0] * 100,win[1][1] * 100,100,100))
        pygame.draw.rect(screen,GREEN,(win[2][0] * 100,win[2][1] * 100,100,100))
        sleep(3)
        font = pygame.font.SysFont(None,30)
        a = font.render('игра окончена, закройте игру',True,CORAL)
        screen.blit(a,(0,150))

    tic_tac_toe()
    draw_grid()
    pygame.display.flip()


pygame.quit()