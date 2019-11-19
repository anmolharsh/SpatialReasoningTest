import pygame, random, sys, os
from os import path




WIDTH = 1000
HEIGHT = 800
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)


#for score
score_file = path.join(path.dirname(__file__),"highest_score_spatial.txt")

def high_score(score,count,total):
    dir = path.dirname(__file__)
    filebuffer = [score,count,float(float(score)/float(count)),float(float(total)/float(count))]
    with open(path.join(dir,"highest_score_spatial.txt"),'r+') as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0
    with open(path.join(dir,"highest_score_spatial.txt"),'w+') as f:
        for value in filebuffer:
            f.write("%s\n" % str(value))
            #f.write("%d\n" for file in filebuffer)


# create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.init()
#window = pygame.display.set_mode((800, 800))

#text for stroop
game_color = [RED,GREEN,BLUE,YELLOW]
game_text = ["RED" , "GREEN" , "BLUE" , "YELLOW" ]
game_key = {"RED":pygame.K_r , "GREEN":pygame.K_g , "BLUE": pygame.K_b , "YELLOW" : pygame.K_y}

#img_folder

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
ques_list = ["q1.jpg","q2.png" , "q3.jpg" , "q4.jpg" , "q5.jpg" , "q6.png" ]
ques_images = []
for i in ques_list:
     	ques_images.append(pygame.image.load(path.join(img_folder, i)).convert())


#create text label
size= 84


# initialize pygame, this must be called before
# doing anything with pygame
pygame.init()



# setup the text
font = pygame.font.Font(None, size)
font_color = random.choice(game_color)
text = font.render(random.choice(game_text), True, font_color)

score=0
score_text = font.render(str(score), True, BLUE)

display = True

keystate = pygame.key.get_pressed()
#for score note ticks
ticks = 0 #  in milli second
time_score = 0;
total =0;
count =0;
total_count=0

location = [ (180,10) , (30,200) , (180,10) , (180,10) , (20,10) , (110,10) ]

pos = location[0]
image = ques_images[0]
#image.set_colorkey(BLACK)
image_rect = image.get_rect()
#screen.blit(opt1[0],WIDTH/2,HEIGHT/2)

# the main loop
while count < 6: # run the program for 60 seconds
     # empty the screen
     screen.fill(BLACK)
     keystate = pygame.key.get_pressed()
     ticks = pygame.time.get_ticks()
     
     #display = not display
     # draw the text to the screen only if display is True
     
     #display = not display
     screen.blit(ques_images[count], location[count])

     if keystate[pygame.K_c] and ( count==0 or count==1 ) :
     	score+=1
     	count+=1
     	total += (pygame.time.get_ticks()-time_score)
     	time_score = pygame.time.get_ticks()
     	high_score(score,count,total)
     elif keystate[pygame.K_a] and count==5 :
     	score+=1
     	count+=1
     	total += (pygame.time.get_ticks()-time_score)
     	time_score = pygame.time.get_ticks()
     	high_score(score,count,total)
     elif keystate[pygame.K_e] and count==4:
     	score+=1
     	count+=1
     	total += (pygame.time.get_ticks()-time_score)
     	time_score = pygame.time.get_ticks()
     	high_score(score,count,total)
     elif keystate[pygame.K_b] and count==2:
     	score+=1
     	count+=1
     	total += (pygame.time.get_ticks()-time_score)
     	time_score = pygame.time.get_ticks()
     	high_score(score,count,total)
     elif keystate[pygame.K_d] and count==3:
     	score+=1
     	count+=1
     	total += (pygame.time.get_ticks()-time_score)
     	time_score = pygame.time.get_ticks()
     	high_score(score,count,total)
     elif keystate[pygame.K_a] or keystate[pygame.K_b] or keystate[pygame.K_c] or keystate[pygame.K_d] or keystate[pygame.K_e]:
     	count+=1
     	total += (pygame.time.get_ticks()-time_score)
     	time_score = pygame.time.get_ticks()
     	high_score(score,count,total)

     
     # update the actual screen
     score_text = font.render(str(score), True, BLUE)
     screen.blit(score_text , (WIDTH/2,HEIGHT-100))
     pygame.display.flip()
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                count =10

     # wait for half second
     pygame.time.wait(150)
pygame.time.wait(300)

