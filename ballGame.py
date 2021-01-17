from processing import *
import random


def setup():
  frameRate(30)
  size(600, 400)
  global heartPhoto, evilLava, pacmanPhoto, backroundList
  heartPhoto = loadImage("Heart.png")
  evilLava = loadImage("Lava.png")
  pacmanPhoto = loadImage("pacman.png")
  amongusPhoto = loadImage("amongus.jpg")
  chickenPhoto = loadImage("chickens.png")
  pompomPhoto = loadImage("pompoms.jfif")
  sirchickenPhoto = loadImage ("sirchicken.jpg")
  backroundList = [evilLava, pacmanPhoto, amongusPhoto, chickenPhoto, pompomPhoto, sirchickenPhoto]
  
  
#changing variables
ball_x = 20
ball_y = 50
speed_x = random.randint(5,10)
speed_y = random.randint(5,10)
paddle_x = 200
life = 3
backroundNumber = 0
score = 0
isPlaying = False 


#non-changing variables, constants
ball_size = 25
paddle_y = 392
dim_w = 85
dim_h = 30

def moveBall():
  global ball_y
  global ball_x
  ball_x = ball_x + speed_x
  ball_y = ball_y + speed_y
  
def changeDirection():
  global speed_x
  global speed_y
  if ball_x >= 600:
    speed_x = -speed_x
  if ball_x <= 0:
    speed_x = -speed_x
  
  #if ball_y >= 400:
   # speed_y = -speed_y
  if ball_y <= 0:
    speed_y = -speed_y
    
def bounceBall():
  global speed_y
  global score
  if ball_x > paddle_x and ball_x < paddle_x + dim_w and ball_y > paddle_y and ball_y < paddle_y + dim_h:
    #print "ball touching paddle"
    speed_y = -speed_y
    score = score + 10
    
def drawScore():
  textSize(35)
  fill(255,0,0)
  text("Score: "+ str(score),400, 30)
  
    
def hitBottom():
  global life
  global ball_y
  global ball_x
  if ball_y > 400:
    life = life-1
    if life > 0:
      ball_y = 100
      ball_x = 300
      speed_x=random.randint(5,10)
      speed_y=random.randint(5,10)
    if life <= 0:
      gameOver()

def gameOver():
  textSize(100)
  fill(255,0,251)
  text("GAME OVER",1, 200)
  text("Mwahaha",30, 330 )

      
def triangleLives():
  fill(252,3,3)
  if life>=1:
    image(heartPhoto, 3, 30, 40, 40)
    #triangle(21, 54, 31, 30, 47, 53)
  if life>=2:
    image(heartPhoto, 53, 30, 40, 40)
    #triangle(21+30, 54, 31+30, 30, 47+30, 53)
  if life==3:
    image(heartPhoto, 103, 30, 40, 40)
    #triangle(21+60, 54, 31+60, 30, 47+60, 53)
  
def mouseMoved():
  #print mouseX, mouseY
  global paddle_x
  paddle_x = mouseX
  if paddle_x >= 507:
    paddle_x = 507

def keyPressed():
  print "Haha"
  global backroundNumber
  global isPlaying
  if key == "p":
    isPlaying = True
  if key == "b":
    backroundNumber = backroundNumber + 1
    if backroundNumber > len(backroundList) - 1:
      backroundNumber = 0
  
def draw():
  if isPlaying == True:
    image(backroundList[backroundNumber], 0, 0, 600, 400)
    moveBall() # move ball
    fill(255,0,251) # fill and draw ball
    ellipse(ball_x, ball_y, ball_size, ball_size)
    changeDirection()
    fill(194, 194, 194)
    rect(paddle_x,paddle_y,dim_w,dim_h)
    bounceBall()
    hitBottom()
    triangleLives()
    drawScore()
  else:
    image(backroundList[backroundNumber], 0, 0, 600, 400)
    textSize(35)
    fill(0,0,0)
    text("Press b to change the backround",1, 200)
    text("Press p to play",30, 330 )
run()