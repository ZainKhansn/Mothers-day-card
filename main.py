import threading
import mixer
import pygame
import time
import replit
pygame.init()
red = 255, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
pygame.font.init()
pygame.mixer.init()
mother = pygame.image.load(r'mothersday.jpg')
star = pygame.image.load(r'star2.png')
heart = pygame.image.load(r'heart.png')
image = pygame.transform.scale(mother, (700,700))
image2 = pygame.transform.scale(star, (450,450))
image3 = pygame.transform.scale(heart, (300,300))
print("Click the checkmark on the bottom right to hear sound")
X = 700
Y = 700
X2 = 350
Y2 = 350
Y3 = 360

Y4 = 370

Y5 = 380
Y6 = 390
piano = pygame.mixer.Sound('piano.wav')

screen = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Show Text')

font = pygame.font.Font('COURIER.TTF', 10)

para = pygame.font.Font('COURIER.TTF', 10)
para2 = pygame.font.Font('COURIER.TTF', 10)
para3 = pygame.font.Font('COURIER.TTF', 10)
para4 = pygame.font.Font('COURIER.TTF', 10)
para5 = pygame.font.Font('COURIER.TTF', 10)
f = open('mothersday.txt',"r")
lines = f.readlines()

def fore():

  screen.blit(image, (0, 0))
  screen.blit(image2, (440, -150))
  screen.blit(image3, (-80, -35))

  while True:
        
    pygame.mixer.Sound.play(piano)
  pygame.display.update()
x = threading.Thread(target=fore)
x.start()
z = -1
while True:

  for i in lines:
    z -=9
    thisline = i.split(" ");
    text = font.render(i, True, green, blue)
    paragraph = para.render('''Thank you for being the best mother ever!'''
                            , True, green, blue)
    paragraph2 = para2.render('''I could have made a postcard but that would be too easy.'''
                            
                      , True, green, blue)
    
    paragraph3 = para3.render('''so i decided to do it on a computer to show how much you take care of us.''' , True, green, blue)     
    paragraph4 = para4.render('''If you werent taking care of us the house'''
                            , True, green, blue)
    paragraph5 = para5.render('''would be like hurricane Katrina and there would be clothes and etc everywhere.'''
                            
                      , True, green, blue)
                        
    textRect = text.get_rect()
    textRect.center = (320, 0 -z)
    textRect2 = paragraph.get_rect()
    textRect2.center = (X2, Y2)
    textRect3 = paragraph2.get_rect()
    textRect3.center = (X2, Y3)
    textRect4 = paragraph3.get_rect()
    textRect4.center = (X2, Y4)
    textRect5 = paragraph4.get_rect()
    textRect5.center = (X2, Y5)
    textRect6 = paragraph5.get_rect()
    textRect6.center = (X2, Y6)
    screen.blit(text, textRect) 
    screen.blit(paragraph, textRect2)
    screen.blit(paragraph2, textRect3)
    screen.blit(paragraph3, textRect4)
    screen.blit(paragraph4, textRect5)
    screen.blit(paragraph5, textRect6)
    time.sleep(.5)
    pygame.display.update()
  time.sleep(10)
  quit()

time.sleep(1)
replit.clear()



    		# Draws the surface object to the screen.

