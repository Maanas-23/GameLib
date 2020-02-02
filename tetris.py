import pygame
import random

pygame.font.init()

S = [['-----',
      '-----',
      '--00-',
      '-00--',
      '-----'],
     ['-----',
      '--0--',
      '--00-',
      '---0-',
      '-----']]

Z = [['-----',
      '-----',
      '-00--',
      '--00-',
      '-----'],
     ['-----',
      '--0--',
      '-00--',
      '-0---',
      '-----']]

I = [['--0--',
      '--0--',
      '--0--',
      '--0--',
      '-----'],
     ['-----',
      '0000-',
      '-----',
      '-----',
      '-----']]

O = [['-----',
      '-----',
      '-00--',
      '-00--',
      '-----']]

J = [['-----',
      '-0---',
      '-000-',
      '-----',
      '-----'],
     ['-----',
      '--00-',
      '--0--',
      '--0--',
      '-----'],
     ['-----',
      '-----',
      '-000-',
      '---0-',
      '-----'],
     ['-----',
      '--0--',
      '--0--',
      '-00--',
      '-----']]

L = [['-----',
      '---0-',
      '-000-',
      '-----',
      '-----'],
     ['-----',
      '--0--',
      '--0--',
      '--00-',
      '-----'],
     ['-----',
      '-----',
      '-000-',
      '-0---',
      '-----'],
     ['-----',
      '-00--',
      '--0--',
      '--0--',
      '-----']]

T = [['-----',
      '--0--',
      '-000-',
      '-----',
      '-----'],
     ['-----',
      '--0--',
      '--00-',
      '--0--',
      '-----'],
     ['-----',
      '-----',
      '-000-',
      '--0--',
      '-----'],
     ['-----',
      '--0--',
      '-00--',
      '--0--',
      '-----']]
shapes_list = [S, Z, I, O, J, L, T]
colors = [(0, 0, 255), (255, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255)]


class obj():
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = random.choice(colors)
        self.rotation = 0


def create_grid(dic={}):
    grid = [[(0,0,0) for i in range(10)] for i in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in dic:
                c = dic[(j,i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 3)

    return positions


def valid_pos(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True


def check_lost(positions):
    for pos in positions:
        i, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    return obj(5, 0, random.choice(shapes_list()))


def text_draw(text, size, color, screen):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    screen.blit(label, (90,325))


def draw_grid(screen, row, col):
    sx = 50
    sy = 100
    for i in range(row):
        pygame.draw.line(screen, (128,128,128), (sx, sy+ i*25), (sx + 250, sy + i * 25))  
    for j in range(col):
        pygame.draw.line(screen, (128,128,128), (sx + j * 25, sy), (sx + j * 25, sy + 500)) 


def clear_rows(grid, dic, score):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0,0,0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del dic[(j,i)]
                except:
                    continue

    if inc > 0:
        print(ind, inc)
        for key in sorted(list(dic), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                dic[newKey] = dic.pop(key)

    return score+inc*400


def draw_next_shape(shape, screen):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    k = shape.shape[shape.rotation % len(shape.shape)]

    for i, m in enumerate(k):
        row = list(m)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(screen, shape.color, (350+j*30, 200+i*30, 30, 30), 0)

    screen.blit(label, (360, 170))


def draw_screen(screen, grid):
    screen.fill((0,0,0))

    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))

    screen.blit(label, (50 + 250 // 2 - (label.get_width() // 2), 30))

    for i in range(20):
        for j in range(10):
            pygame.draw.rect(screen, grid[i][j], (50 + j* 25, 100 + i * 25, 25, 25), 0)

    draw_grid(screen, 20, 10)
    pygame.draw.rect(screen, (255, 0, 0), (50, 100, 250, 500), 5)


def main():
    screen = pygame.display.set_mode((500, 650))
    pygame.display.set_caption('Tetris')
    dic = {}
    grid = create_grid(dic)

    change_obj = False
    running = True
    current_obj = get_shape()
    next_obj = get_shape()
    clock = pygame.time.Clock()
    k=0
    score = 0
    
    while running:

        grid = create_grid(dic)
        clock.tick(6+int(k))

        current_obj.y += 1
        if not (valid_pos(current_obj, grid)) and current_obj.y > 0:
            current_obj.y -= 1
            change_obj = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_obj.x -= 1
                    if not valid_pos(current_obj, grid):
                        current_obj.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_obj.x += 1
                    if not valid_pos(current_obj, grid):
                        current_obj.x -= 1
                elif event.key == pygame.K_UP:
                    current_obj.rotation = (current_obj.rotation + 1) % len(current_obj.shape)
                    if not valid_pos(current_obj, grid):
                        current_obj.rotation = (current_obj.rotation - 1) % len(current_obj.shape)
                elif event.key == pygame.K_DOWN:
                    current_obj.y += 1
                    if not valid_pos(current_obj, grid):
                        current_obj.y -= 1

        shape_pos = convert_shape_format(current_obj)
        
        for i,y in shape_pos:
            if y > -1:
                grid[y][i] = current_obj.color

        if change_obj:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                dic[p] = current_obj.color
            current_obj = next_obj
            next_obj = get_shape()
            change_obj = False
            score+= int((6+k)*10)
            k+=0.3
            score = clear_rows( grid, dic, score)

        draw_screen(screen, grid)
        draw_next_shape(next_obj, screen)
        
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render("Score", 1, (255, 255, 255))
        screen.blit(label, (370, 400))

        label2 = font.render(str(score), 1, (255, 255, 255))
        screen.blit(label2, (370+(label.get_width()-label2.get_width())//2, 450))
        
        pygame.display.flip()

        if check_lost(dic):
            running = False

    text_draw("Game Over", 40, (255,255,255), screen)
    pygame.display.update()
    pygame.time.delay(1000)
    text_draw(f"Final Score: {score}", 40, (255,255,255), screen)
    pygame.display.update()
    pygame.time.delay(100)
    mainloop()


def mainloop():
    screen = pygame.display.set_mode((500, 650))
    pygame.display.set_caption('Tetris')
    while True:
        screen.fill((0,0,0))
        text_draw('Press any key to continue', 40, (255, 255, 255), screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                main()
mainloop()                
