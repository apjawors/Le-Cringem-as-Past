import pygame
from math import *
import random
pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BROWN    = ( 158,  91,  24)

size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Le Cringem'as Past")

class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("cookie.png").convert()

        self.rect  = self.image.get_rect()

        self.image.set_colorkey(BLACK)

class Wall(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("adderall.png").convert()

        self.rect = self.image.get_rect()

        self.image.set_colorkey(BLACK)
        
cookie   = Player()
adderall = Wall()

# Intital cookie velocity and y_coord
velocity  = 0
cookie_y = 120

# Timer y
timer_y = 30


# Empty lists for star coordinates and wall coordinates
star_list = []

for i in range(50):
    x_star = random.randrange(0.0, 800.0)
    y_star = random.randrange(90.0, 690.0)
    star_list.append([x_star, y_star])


wall_list = []
for i in range(3):
    y_wall = random.randrange(-600, -200)
    wall_list.append(y_wall)

# Score
score      = 0
high_score = 0

# Load graphics
welcome   = pygame.image.load("welcome_to_screen.png").convert()
title     = pygame.image.load("title_screen.png").convert()
remember  = pygame.image.load("wait_screen.png").convert()
get_ready = pygame.image.load("get_ready_to_click.png").convert()
timer     = pygame.image.load("timer.png").convert()
timer.set_colorkey(BLACK)

three     = pygame.image.load("3.png").convert()
two       = pygame.image.load("2.png").convert()
one       = pygame.image.load("1.png").convert()
go        = pygame.image.load("go.png").convert()

sky       = pygame.image.load("black_background_final.png").convert()
ground    = pygame.image.load("ground.png").convert()
ceiling   = pygame.image.load("ceiling.png").convert()

game_over = pygame.image.load("game_over.png").convert()
lel       = pygame.image.load("lel.png").convert()

# Load sound
whom           = pygame.mixer.Sound("whom.ogg")
love           = pygame.mixer.Sound("i_love_you_dear.ogg")
first_sound    = pygame.mixer.Sound("welcome_to.ogg")
nuoo           = pygame.mixer.Sound("nuoo.ogg.")



done = False
clock = pygame.time.Clock()

# Initial x-coordinates of ground and ceiling
x_ceiling  = 0
x_ground   = 0
cookie_x   = 400
x_wall1    = 600
x_wall2    = 1000
x_wall3    = 1400


# Initial gamestate
gamestate = 0

# Plays first sound once at the welcome screen
first_sound.play()

# Loops "I love dear" until actual gameplay
def love_play():
    if gamestate < 2:
        love.play(-1)
    elif gamestate == 2:
        love.fadeout(3000)
    


  
while not done:

    """Welcome Screen"""
    if gamestate == 0:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                gamestate = 1
                love_play()
                                                
        screen.blit(welcome, [0, 0])

    """Title Screen"""
    if gamestate == 1:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                gamestate = 2
                love_play()
                                
        screen.blit(title, [0, 0])

    """Remember Screen"""
    if gamestate == 2:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                gamestate = 3
                love_play()
                                
        screen.blit(remember, [0, 0])

    """Get ready to click Screen"""
    if gamestate == 3:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

        screen.blit(get_ready, [0, 0])
        screen.blit(timer, [0, timer_y])
        
        timer_y += 10
        if timer_y > 800:
            gamestate = 4
            timer_y = 0

    """3 Screen"""
    if gamestate == 4:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

        screen.blit(three, [0, 0])
        screen.blit(timer, [0, timer_y])
        
        timer_y += 10
        if timer_y > 800:
            gamestate = 5
            timer_y = 0

    """2 Screen"""
    if gamestate == 5:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

        screen.blit(two, [0, 0])
        screen.blit(timer, [0, timer_y])
        
        timer_y += 10
        if timer_y > 800:
            gamestate = 6
            timer_y = 0

    """1 Screen"""
    if gamestate == 6:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

        screen.blit(one, [0, 0])
        screen.blit(timer, [0, timer_y])
        
        timer_y += 10
        if timer_y > 800:
            gamestate = 7
            timer_y = 0

    """Go Screen"""
    if gamestate == 7:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

        screen.blit(go, [0, 0])
        screen.blit(timer, [0, timer_y])
        
        timer_y += 10
        if timer_y > 800:
            gamestate = 8

#########################################################################################
    """Game Screen"""
    if gamestate == 8: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                velocity = -17
                whom.play()

                    
        screen.blit(sky, [0, 0])

    
        # Create moving stars
        for i in range(len(star_list)):
            pygame.draw.circle(screen, WHITE, star_list[i], 2)

            star_list[i][0] -= 1

            if star_list[i][0] < 0:
                x_star = random.randrange(810, 850)
                star_list[i][0] = x_star
                y_star = random.randrange(90, 690)
                star_list[i][1] = y_star

        # Adderwalls
        screen.blit(adderall.image, [x_wall1, wall_list[0]])
        screen.blit(adderall.image, [x_wall1, wall_list[0] + 1000])
        
        screen.blit(adderall.image, [x_wall2, wall_list[1]])
        screen.blit(adderall.image, [x_wall2, wall_list[1] + 1000])
        
        screen.blit(adderall.image, [x_wall3, wall_list[2]])
        screen.blit(adderall.image, [x_wall3, wall_list[2] + 1000])
        
               
        # Loop and draw ground/ceiling -------
        screen.blit(ceiling, [0 + x_ceiling, -30])
        screen.blit(ground, [0 + x_ground, 730])
    
        x_ceiling  -= 3
        x_ground   -= 3
        x_wall1    -= 3
        x_wall2    -= 3
        x_wall3    -= 3
    
        
    
        if x_ceiling < -513:
            x_ceiling = 0

        if x_ground < -513:
            x_ground = 0

        if x_wall1 < -200:
            x_wall1 = 1000

        if x_wall2 < -200:
            x_wall2 = 1000

        if x_wall3 < -200:
            x_wall3 = 1000

                  
            
        #-------------------------------------

        
        
           # Text for score
        font = pygame.font.SysFont('Calibri', 25, True, False)

        text1 = font.render("SCORE: " + str(score), True, WHITE)

        screen.blit(text1, [675, 20])

        high_score = max(score, high_score)

        text2 = font.render("HIGHSCORE: " + str(high_score), True, WHITE)

    

        screen.blit(cookie.image, [cookie_x, cookie_y + velocity])

        velocity += 1
        cookie_y += velocity

        
        if x_wall1 % 400 == 0:
            score += 1

        if x_wall2 % 400 == 0:
            score += 1

        if x_wall3 % 400 == 0:
            score += 1

        if cookie_y > 645 or cookie_y < 85:
            gamestate = 9
            nuoo.play()
            cookie_y = 120
            score = 0
            x_wall1    = 600
            x_wall2    = 1000
            x_wall3    = 1400
            

    if gamestate == 9:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                gamestate = 3
            if event.key == pygame.K_n:
                gamestate = 10

        screen.blit(game_over, [0, 0])

        text2 = font.render("HIGHSCORE: " + str(high_score), True, WHITE)
        screen.blit(text2, [550, 275])
        screen.blit(text1, [550, 250])
        

    if gamestate == 10:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

        screen.blit(timer, [0, timer_y])
        screen.blit(lel, [0, 0])
        
        timer_y += 10
        if timer_y > 800:
            done = True
        
          

        

        
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
