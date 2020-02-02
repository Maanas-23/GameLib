import pygame

w = (255, 255, 255)
b = (0, 0, 0)
pygame.font.init()
f = pygame.font.SysFont("comicsansms", 30)


def draw_grid(screen):
    for i in range(1, 8):
        pygame.draw.line(screen, b, (i * 40, 0), (i * 40, 320))

    for j in range(1, 8):
        pygame.draw.line(screen, b, (0, j * 40), (320, j * 40))


def new_piece(x, y, dic):
    for i in range(1, 11):
        for j in range(1, 11):
            if (i, j) in dic:
                if i == x:
                    if j == y - 1:
                        k = j
                        while (i, k) in dic and dic[(i, k)] != dic[(x, y)]:
                            dic[(i, k)] = dic[(x, y)]
                            k -= 1
                    if j == y + 1:
                        k = j
                        while (i, k) in dic and dic[(i, k)] != dic[(x, y)]:
                            dic[(i, k)] = dic[(x, y)]
                            k += 1

                if j == y:
                    if i == x - 1:
                        k = i
                        while (k, j) in dic and dic[(k, j)] != dic[(x, y)]:
                            dic[(k, j)] = dic[(x, y)]
                            k -= 1
                    if i == x + 1:
                        k = i
                        while (k, j) in dic and dic[(k, j)] != dic[(x, y)]:
                            dic[(k, j)] = dic[(x, y)]
                            k += 1

                if (i, j) == (x + 1, y + 1):
                    m, n = i, j
                    while (m, n) in dic and dic[(m, n)] != dic[(x, y)]:
                        dic[(m, n)] = dic[(x, y)]
                        m += 1
                        n += 1

                if (i, j) == (x - 1, y + 1):
                    m, n = i, j
                    while (m, n) in dic and dic[(m, n)] != dic[(x, y)]:
                        dic[(m, n)] = dic[(x, y)]
                        m -= 1
                        n += 1

                if (i, j) == (x - 1, y - 1):
                    m, n = i, j
                    while (m, n) in dic and dic[(m, n)] != dic[(x, y)]:
                        dic[(m, n)] = dic[(x, y)]
                        m -= 1
                        n -= 1

                if (i, j) == (x + 1, y - 1):
                    m, n = i, j
                    while (m, n) in dic and dic[(m, n)] != dic[(x, y)]:
                        dic[(m, n)] = dic[(x, y)]
                        m += 1
                        n -= 1


def mouse_pos():
    x, y = pygame.mouse.get_pos()

    for i in range(1, 9):
        if (i - 1) * 40 <= x <= i * 40:
            x = i
            break
    for i in range(1, 9):
        if (i - 1) * 40 <= y <= i * 40:
            y = i
            break
    return (x, y)


def draw_window(screen, dic):
    for a, b in dic:
        pygame.draw.circle(screen, dic[(a, b)], (a * 40 - 20, b * 40 - 20), 17)


def main():
    screen = pygame.display.set_mode((420, 320))
    screen.fill((0, 100, 0))
    pygame.display.set_caption("Othello")
    dic = {(5, 5): w, (4, 5): b, (4, 4): w, (5, 4): b}

    running = True
    turns = 0
    while running:
        white = 0
        black = 0
        draw_window(screen, dic)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = mouse_pos()
                if pos not in dic and pos[0] <= 320:
                    dic[pos] = (0, 0, 0) if turns % 2 == 0 else (255, 255, 255)
                    new_piece(pos[0], pos[1], dic)
                    turns += 1

        draw_grid(screen)

        for i in dic:
            if dic[i] == w:
                white += 1
            else:
                black += 1

        if len(dic) == 64:
            screen.fill((0, 100, 0))
            font = pygame.font.SysFont("comicsansms",50)
            if black > white:
                txt = font.render(str("Black Wins"), 1, b)
            else:
                txt = font.render("White Wins", 1, w)
            screen.blit(txt, (210 - txt.get_width() // 2, 100))
            pygame.display.update()
            pygame.time.delay(2500)
            main()

        pygame.draw.rect(screen, (0, 50, 0), (320, 0, 100, 360))

        if turns % 2 == 0:
            pygame.draw.rect(screen, (255, 50, 0), (340, 20, 60, 140), 4)

        if turns % 2 :
            pygame.draw.rect(screen, (255, 50, 0), (340, 160, 60, 140), 4)

        pygame.draw.circle(screen, b, (370, 60), 20)
        label = f.render(str(black), 1, w)
        screen.blit(label, (370-label.get_width()//2, 100))

        pygame.draw.circle(screen, w, (370, 200), 20)
        label2 = f.render(str(white), 1, b)
        screen.blit(label2, (370-label2.get_width()//2, 240))

        pygame.display.update()