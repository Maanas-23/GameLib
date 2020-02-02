import pygame
import random

pygame.font.init()
width = 1000
height = 600
clr = [255, 255, 255]
a_clr = [255, 0, 0]
f = pygame.font.SysFont("comicsansms", 40, bold=True)


def new_apple():
    return [[random.randint(0, 39), random.randint(0, 29)]]


class Snake:
    def __init__(self, body):
        self.body = body
        self.dirn = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.dirn = 0
                if event.key == pygame.K_RIGHT:
                    self.dirn = 1
                if event.key == pygame.K_DOWN:
                    self.dirn = 2
                if event.key == pygame.K_LEFT:
                    self.dirn = 3

        for a, b in enumerate(self.body):
            x, y = b
            if x == -1:
                x = 39
            if x == 40:
                x = 0
            if y == -1:
                y = 29
            if y == 30:
                y = 0

            self.body[a] = [x, y]

    def append_body(self):
        last = self.body[-1]
        last2 = self.body[-2] if len(self.body) != 1 else last

        if (last2[0] == last[0] and last2[1] + 1 == last[1]) or (last2 == last and self.dirn == 0):
            new = [last[0], last[1] + 1]
            self.body.append(new)

        elif (last2[0] == last[0] and last2[1] - 1 == last[1]) or (last2 == last and self.dirn == 1):
            new = [last[0], last[1] - 1]
            self.body.append(new)

        elif (last2[1] == last[1] and last2[0] + 1 == last[0]) or (last2 == last and self.dirn == 2):
            new = [last[0] + 1, last[1]]
            self.body.append(new)

        elif (last2[1] == last[1] and last2[0] - 1 == last[0]) or (last2 == last and self.dirn == 3):
            new = [last[0] - 1, last[1]]

            self.body.append(new)


def update_win(screen, l, color):
    for i, j in l:
        pygame.draw.rect(screen, color, (i * 20, j * 20, 20, 20))
        pygame.draw.rect(screen, (0, 0, 0), (i * 20, j * 20, 20, 20), 2)


def main():
    snake = Snake([[3, 3]])
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")
    apple = new_apple()
    running = True

    while running:
        clock.tick(10 + len(snake.body))
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (800, 0), (800, 600))
        snake.move()
        update_win(screen, snake.body, clr)
        update_win(screen, apple, a_clr)

        for i in range(len(snake.body)-1, 0, -1):
            snake.body[i][0] = snake.body[i-1][0]
            snake.body[i][1] = snake.body[i-1][1]

        if snake.dirn == 0:
            snake.body[0][1] -= 1
        if snake.dirn == 1:
            snake.body[0][0] += 1
        if snake.dirn == 2:
            snake.body[0][1] += 1
        if snake.dirn == 3:
            snake.body[0][0] -= 1

        if snake.body[0] == apple[0]:
            snake.append_body()
            apple = new_apple()

        label = f.render("Score", 1, (255, 255, 255))
        screen.blit(label, (900-label.get_width()//2, 200))

        label2 = f.render(str(len(snake.body)*10 - 10), 1, (255, 255, 255))
        screen.blit(label2, (900 - label2.get_width()//2, 400))

        k = 0
        for i in snake.body:
            if i == snake.body[0] and k > 0:
                running = False
            k += 1

        pygame.display.update()
        
    mainloop(1, str(len(snake.body)*10 - 10))


def mainloop(k=0, score=""):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")
    screen.fill((0, 0, 0))
    while True:
        label = f.render("Press any key to continue" if k==0 else "Game Over", 1, (255, 255, 255))
        screen.blit(label, (500 - label.get_width() // 2, 200))

        if k:
            label = f.render(f"Final Score: {score}", 1, (255, 255, 255))
            screen.blit(label, (500 - label.get_width() // 2, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                main()
                
        pygame.display.update()
