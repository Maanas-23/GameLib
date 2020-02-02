import pygame

width = 550
height = 380
radius = 25
clr = [(255, 0, 0), (255, 255, 0)]
pygame.font.init()
f = pygame.font.SysFont("comicsansms", 30, bold=True)


class obj:
    def __init__(self, x, y, num):
        self.clr = num
        self.x = x
        self.y = y


def make_grid(dic):
    grid = [[(255, 255, 255) for _ in range(7)] for _ in range(6)]
    for i in range(6):
        for j in range(7):
            if (j, i) in dic:
                grid[i][j] = dic[(j, i)]

    return grid


def draw(win, grid, turns):
    for i in range(7):
        for j in range(6):
            pygame.draw.circle(win, grid[j][i], ((i * 125 + radius + 50) // 2, (j * 125 + radius + 50) // 2),
                               radius)
    pygame.draw.rect(win, (0, 0, 0), (width - 100, 0, 100, height))
    pygame.draw.circle(win, (255, 0, 0), (500, 200), 25)
    pygame.draw.circle(win, (255, 255, 0), (500, 300), 25)

    if turns % 2 == 0:
        pygame.draw.rect(win, (255, 125, 0), (465, 165, 70, 70), 5)
    else:
        pygame.draw.rect(win, (255, 125, 0), (465, 265, 70, 70), 5)


def mouse_pos():
    x = -1
    pos = pygame.mouse.get_pos()
    a, b = pos
    dist = 12.5
    for i in range(7):
        if dist <= a <= dist + 50:
            x = i
        dist += 62.5
    return x


def valid_pos(obj):
    boolean = False
    if obj.x in range(7) and obj.y in range(6):
        boolean = True
    return boolean


def stop_piece(obj, grid):
    if obj.y == 6:
        return True
    if grid[obj.y][obj.x] != (255, 255, 255):
        return True
    return False


def main():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Connect 4")
    screen.fill((0, 0, 255))
    dic = {}
    grid = make_grid(dic)
    draw(screen, grid, 0)
    running = True
    turns = 0
    clock = pygame.time.Clock()
    piece = obj(-1, 0, (255, 255, 255))

    while running:
        clock.tick(12)
        lbl1 = f.render(f"{turns}", 1, (255, 255, 255))

        if piece.x != -1:
            piece = obj(piece.x, piece.y, piece.clr)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if pygame.MOUSEBUTTONDOWN == event.type:
                x = mouse_pos()
                if piece.x == -1 and grid[0][x] == (255, 255, 255):
                    piece = obj(x, 0, clr[turns % 2])

        grid = make_grid(dic)
        if valid_pos(piece) and piece.y == 0:
            turns += 1

        if valid_pos(piece) and not stop_piece(piece, grid):
            grid[piece.y][piece.x] = piece.clr
            piece.y += 1

        if stop_piece(piece, grid):
            piece.y -= 1
            dic[(piece.x, piece.y)] = piece.clr
            piece = obj(-1, 0, (255, 255, 255))
        draw(screen, grid, turns)
        screen.blit(lbl1, (500 - lbl1.get_width() // 2, 100))
        lbl = f.render("Turns", 1, (255, 255, 255))
        screen.blit(lbl, (500 - lbl.get_width() // 2, 50))
        pygame.display.update()

        for i in dic:
            a, b = i
            if (a + 1, b) in dic and (a + 2, b) in dic and (a + 3, b) in dic:
                if dic[(a, b)] == dic[(a + 1, b)] == dic[(a + 2, b)] == dic[(a + 3, b)]:
                    s = dic[(a, b)]
                    dic[(a, b)], dic[(a + 1, b)], dic[(a + 2, b)], dic[(a + 3, b)] = (0, 0, 0), (0, 0, 0), (0, 0, 0), (
                        0, 0, 0)

                    grid = make_grid(dic)
                    draw(screen, grid, turns)
                    pygame.display.update()

                    pygame.time.delay(2000)

                    running = False

            if (a, b + 1) in dic and (a, b + 2) in dic and (a, b + 3) in dic:
                if dic[(a, b)] == dic[(a, b + 1)] == dic[(a, b + 2)] == dic[(a, b + 3)]:
                    s = dic[(a, b)]
                    dic[(a, b)], dic[(a, b + 1)], dic[(a, b + 2)], dic[(a, b + 3)] = (0, 0, 0), (0, 0, 0), (0, 0, 0), (
                        0, 0, 0)

                    grid = make_grid(dic)
                    draw(screen, grid, turns)
                    pygame.display.update()

                    pygame.time.delay(2000)

                    running = False

            if (a + 1, b + 1) in dic and (a + 2, b + 2) in dic and (a + 3, b + 3) in dic:
                if dic[(a, b)] == dic[(a + 1, b + 1)] == dic[(a + 2, b + 2)] == dic[(a + 3, b + 3)]:
                    s = dic[(a, b)]
                    dic[(a, b)], dic[(a + 1, b + 1)], dic[(a + 2, b + 2)], dic[(a + 3, b + 3)] = (0, 0, 0), (0, 0, 0), (
                        0, 0, 0), (0, 0, 0)

                    grid = make_grid(dic)
                    draw(screen, grid, turns)
                    pygame.display.update()

                    pygame.time.delay(2000)

                    running = False

            if (a - 1, b + 1) in dic and (a - 2, b + 2) in dic and (a - 3, b + 3) in dic:
                if dic[(a, b)] == dic[(a - 1, b + 1)] == dic[(a - 2, b + 2)] == dic[(a - 3, b + 3)]:
                    s = dic[(a, b)]
                    dic[(a - 1, b + 1)], dic[(a - 2, b + 2)], dic[(a, b)], dic[(a - 3, b + 3)] = (0, 0, 0), (0, 0, 0), (
                        0, 0, 0), (0, 0, 0)

                    grid = make_grid(dic)
                    draw(screen, grid, turns)
                    pygame.display.update()

                    pygame.time.delay(2000)

                    running = False

    mainloop(s)


def mainloop(clr=(0, 0, 0)):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Connect 4")
    screen.fill((0, 0, 0))
    while True:
        txt = f.render("Press any key to continue", 1, (255, 255, 255))
        screen.blit(txt, ((width - txt.get_width()) // 2, height // 3))

        pygame.display.update()
        if clr == (255, 0, 0):
            txt = f.render("Red Wins", 1, (255, 0, 0))
            screen.blit(txt, (width // 2 - txt.get_width() // 2, 2 * (height // 3)))

        if clr == (255, 255, 0):
            txt = f.render("Yellow Wins", 1, (255, 255, 0))
            screen.blit(txt, (width // 2 - txt.get_width() // 2, 2 * (height // 3)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                main()