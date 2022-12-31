import pygame
from gridgenerator import solve
from userinput import insert
pygame.init()

# INITIALISE DISPLAY #
WIDTH = 1100
background_colour = (255,255,255)
text_colour = (255, 255, 255)
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku")
win.fill(background_colour)
pygame.display.update()
myfont = pygame.font.SysFont('Calibri', 32)

# LEVELS #
intro = True
instruction = False
game_start = False
difficulty = ""

# GAME LOAD SECTION #
page1 = pygame.image.load("main/startscreen.png").convert_alpha()
page2 = pygame.image.load("main/instructions.png").convert_alpha()
easy_button = pygame.Rect(200, 640, 250, 100) #xy width height
medium_button = pygame.Rect(400, 640, 250, 100)
hard_button = pygame.Rect(700, 640, 250, 100)

# LOOP #
while True:
    # GAME START MENU # 
    if intro:
        win.blit(page1, (0,0))
        pos = pygame.mouse.get_pos()
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP and easy_button.collidepoint(pos[0], pos[1]):
            difficulty = "Difficuly: Easy"
            intro = False
            instruction = True
        if event.type == pygame.MOUSEBUTTONUP and medium_button.collidepoint(pos[0], pos[1]):
            difficulty = "Difficulty: Medium"
            intro = False
            instruction = True
        if event.type == pygame.MOUSEBUTTONUP and hard_button.collidepoint(pos[0], pos[1]):
            difficulty = "Difficulty: Hard"
            intro = False
            instruction = True
        
    # CHOOSE DIFFICULTY MENU #
    if instruction:
        win.fill(background_colour)
        win.blit(page2, (0,0))
        difficultystring = myfont.render(difficulty, True, text_colour)
        instructionstring = myfont.render("Press Enter to Continue", True, (text_colour))
        win.blit(difficultystring, (20,20))
        win.blit(instructionstring, (400,800))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    instruction = False
                    game_start = True
                    
    if game_start:
        grid = solve()
        print(grid) # I want this to print the completed solution, which was updated in gridgenerator.py
        display()
    
    def display():   
        pygame.display.set_caption("Sudoku")
        win.fill(background_colour)

        myfont = pygame.font.SysFont('Calibri', 90)
        
        for i in range(0,10):
            if(i%3 == 0):
                pygame.draw.line(win, (0,0,0), (100 + 100*i, 100), (100 + 100*i ,1000 ), 4)
                pygame.draw.line(win, (0,0,0), (100, 100 + 100*i), (1000, 100 + 100*i), 4)
            pygame.draw.line(win, (0,0,0), (100 + 100*i, 100), (100 + 100*i ,1000 ), 2)
            pygame.draw.line(win, (0,0,0), (100, 100 + 100*i), (1000, 100 + 100*i), 2)
        
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):
                if(0<grid[i][j]<10):
                    value = myfont.render(str(grid[i][j]), True, (0,0,0))
                    win.blit(value, ((j+1)*100 + 30, (i+1)*100 + 15))
        pygame.display.update()

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    insert(win, (pos[0]//100, pos[1]//100))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return


    


    

