import pygame
import random
import time

pygame.init()

pygame.mixer.music.load("anamenu.mp3")
kaza = pygame.mixer.Sound("crash.wav")
siyril = pygame.mixer.Sound("dodge.wav")


ekranx = 160
ekrany = 310
window = pygame.display.set_mode((ekranx, ekrany))
white = (255,255,255)
black = (0,0,0)
blue = (0,0,200)
enc = (136,0,0)
red = (180,0,0)
parlak_red = (225,0,0)
green = (0,200,0)
parlak_green = (0,255,0)
pygame.display.set_caption("TOP")
clock = pygame.time.Clock()
ball = pygame.image.load("top.png")
icon = pygame.image.load("topicon.png")
pygame.display.set_icon(icon)

def enemy_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Sıyrılma: "+str(count), True, black)
    window.blit(text,(9,8))
def enemy(enx, eny, enw, enh, color):
    pygame.draw.rect(window, enc, [enx,eny,enw,enh])
def top(x,y):
    window.blit(ball,(x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
##    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText, white)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
##            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        window.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("TOP", largeText, black)
        TextRect.center = ((ekranx/2),(125))
        window.blit(TextSurf, TextRect)
        
        button("Başla",50,160,60,30,green,parlak_green,game_loop)
        button("Çık",50,210,60,30,red,parlak_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    pygame.mixer.music.play(-1)
    
    top_x = (55)
    top_y = (250)
    top_width = 48
    
    enemy_startx = [5,55,105]
    enemy_startxx = (random.choice(enemy_startx))
    enemy_starty = -100
    print(enemy_starty)
    enemy_speed = 5
    enemy_width = 48
    enemy_height = 48

    dodged = 0
    
    cikis = False
    while not cikis:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    #--SOL
                    if event.key == pygame.K_LEFT:
                        top_x += -50


                    #--SAĞ
                    if event.key == pygame.K_RIGHT:
                        top_x += 50

                                
##        print(event)
        window.fill(white)
        enemy(enemy_startxx, enemy_starty, enemy_width, enemy_height, red)
        enemy_starty += enemy_speed
        top(top_x,top_y)
        pygame.draw.rect(window,blue,(5,5,150,300),5)
        enemy_dodged(dodged)
        if top_x < 6:
            top_x = 6
        if top_x > 104:
            top_x = 104
            
        
        if enemy_starty > 310:

            enemy_speed += 0.3
            enemy_starty = 0
            dodged += 1
            enemy_startx = [5,55,105]
            enemy_startxx = (random.choice(enemy_startx))
        elif enemy_starty == -48:
            pygame.mixer.Sound.play(siyril)
        
            

        if top_y < enemy_starty + enemy_height:
            if enemy_startxx <= top_x <= enemy_startxx + enemy_width or enemy_startxx <= top_x + top_width <= enemy_startxx + enemy_width :
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(kaza)
                
                myfont = pygame.font.SysFont("Arial.ttf", 30)
                textSurface = myfont.render("YANDIN!", False, black)
                window.blit(textSurface,(45,150))
                pygame.display.update()
                time.sleep(1)
                game_intro()
                
            
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
