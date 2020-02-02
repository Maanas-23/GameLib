import tetris
import connect4
import Snake
import pygame
import othello

screen = pygame.display.set_mode((300,450))

pygame.font.init()

f = pygame.font.SysFont("comicsansms", 20, bold = True)
lbl = f.render("Choose a game to play",1, (255, 255, 255))
screen.blit(lbl, (150 - lbl.get_width()//2, 30))

pygame.draw.rect(screen, (255, 84, 128), (50, 100, 200, 330), 10)

lbl = f.render("Tetris",1, (255,0, 0))
screen.blit(lbl, (150 - lbl.get_width()//2, 140))

lbl = f.render("Connect 4",1, (255, 255, 0))
screen.blit(lbl, (150 - lbl.get_width()//2, 210))

lbl = f.render("Snake", 1,  (0,255, 255))
screen.blit(lbl, (150 - lbl.get_width()//2, 280))

lbl = f.render("Othello",1, (0,255, 0))
screen.blit(lbl, (150 - lbl.get_width()//2, 350))

pygame.display.update()

while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 50 <= pos[0] <= 250:
                if 100 <= pos[1] < 175:
                    tetris.main_menu()
                if 175 <= pos[1] < 245:
                    connect4.mainloop()
                if 245 <= pos[1] < 315:
                    Snake.mainloop()
                if 315 <= pos[1] < 385:
                    othello.main()
