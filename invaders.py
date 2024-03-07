import pygame #brings in module to handle graphocs, input, etc

pygame.init() #set up pygame
pygame.display.set_caption("space invaders!") # sets the window title
screen = pygame.display.set_mode((800, 800)) # creates game screen
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
#player variables
xpos = 400
ypos = 750
moveLeft = False
moveRight = False
shoot = False
timer = 0;
class Bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False

    def move(self, xpos, ypos):
        if self.isAlive == True: #only shoot live bullets 
            self.ypos-=5 #move up when shot
        if self.ypos < 0: #check if you've hit the top of the screen
            self.isAlive = False #set to dead
            self.xpos = xpos #reset to player position 
            self.ypos = ypos

    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))

bullet = Bullet(xpos+28, ypos)

class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction=1
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 40, 40)) #push Alien object into list
    def move(self, time):

        if timer % 800 == 0:
            self.ypos += 100
            self.direction *=-1
            return 0
            
        if time % 100 == 0:
            self.xpos+=50*self.direction

        

        
armada = []
for i in range (4): #create empty list
    for j in range (9): # handles rows
        armada.append(Alien(j*60+50, i*50+50)) # handles columns
while not gameover: #GAME LOOP#########################################################################################
    clock.tick(60) #FPS
    timer += 1;
#input section ---------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True #quit game if x is pressed in top corner
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
                print("Move Left")
            if event.key == pygame.K_RIGHT:
                moveRight = True
                print("Move Right")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False

    # physics section----------------------------------------------------------------------------------------------------
    for i in range (len(armada)):
        armada[i].move(timer)
    # check variables from the input section
    if moveLeft == True:
        vx =- 3
    elif moveRight == True:
        vx =+ 3
    else:
        vx = 0
        
    #update player position
    xpos += vx

    if shoot == True:
        bullet.isAlive = True

    if bullet.isAlive == True:
        bullet.move(xpos+28, ypos)

    else:
        bullet.xpos = xpos + 28
        bullet.ypos = ypos 
 #render section-----------------------------------------------------------------------------------------------------
    
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    pygame.draw.rect(screen, (0, 200, 0), (xpos, 750, 60, 20)) #draw player
    pygame.draw.rect(screen, (0, 200, 0), (xpos + 4, 740, 50, 10))
    pygame.draw.rect(screen, (0, 200, 0), (xpos + 24, 730, 10, 10))
    pygame.draw.rect(screen, (0, 200, 0), (xpos + 26, 724, 5, 10))
#     a1 = Alien(400, 400)
#     a1.draw()
    for i in range (len(armada)):
        armada[i].draw()

        

    pygame.display.flip()#this flips the buffer (memory) where stuff has been "drawn" to the actual screen
    
#end game loop####################################################################################################
    
pygame.quit()
