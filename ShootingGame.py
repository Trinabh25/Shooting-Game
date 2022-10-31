import pygame
import sys
import math
import random

pygame.init()

winHeight = 600
winWidth = 800
window = pygame.display.set_mode((winWidth, winHeight))

def isCollison(bulletX,bulletY, enemyX,enemyY):
    distance = math.sqrt(math.pow(bulletX-enemyX,2) + math.pow(bulletY-enemyY,2))
    if distance < 30:
        return True
    else:
        return False

playerX = winWidth/2 - 30
playerY = winHeight - 100

clock = pygame.time.Clock()
fps = 60

bulletShoot = False

speed = 0
enemy_speed = 2

def load_image(img, size):
    a = pygame.image.load(img)
    a = pygame.transform.scale(a, size)
    return a


bg = load_image("BackgroundShootingGame.jfif", (winWidth, winHeight))

enemy = load_image("Enemy.png", (50, 50))

bullet = load_image("Bullet.png",(30,30))

bulletX = playerX + 14
bulletY = playerY
bullet_speed = 5

no_of_enemies = 10
enemy_pool = []
enemy_x = [10,80,150,230,300,370,440,510,580,650]
enemy_y = []

for i in range(no_of_enemies):
  enemy_pool.append(enemy)
  enemy_y.append(random.randrange(10,200,10))
  


player = load_image("Spaceship.png", (60, 60))

rotate = 0

score = 0

def show_score(abc):
  font = pygame.font.Font("freesansbold.ttf",30)
  text = font.render(abc, True, (255,0,0),(0,255,0))
  textRect = text.get_rect()
  textRect.center=(winWidth/2, 50)
  window.blit(text, textRect)


while True:
  window.blit(bg, (0, 0))
  window.blit(bullet,(bulletX,bulletY))
  window.blit(player, (playerX, playerY))
  show_score(str(score))

  for i in range(no_of_enemies):
    window.blit(enemy_pool[i], (enemy_x[i], enemy_y[i]))

  for i in range(no_of_enemies):
    if enemy_x[i] < 0 or enemy_x[i] > winWidth-50:
      enemy_speed *= -1
      # for j in range(10):
      #   enemy_y[j] += 2
    enemy_x[i] = enemy_x[i] + enemy_speed
  
    

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
      # bulletY = playerY
      # bulletX = playerX + 12

      if event.key == pygame.K_LEFT:
        speed = -5

      if event.key == pygame.K_RIGHT:
        speed = 5

      if event.key == pygame.K_SPACE:
       
        bulletShoot = True

    elif event.type == pygame.KEYUP:
      speed = 0

  playerX = playerX + speed
  
  if not bulletShoot:
    bulletY = playerY
    bulletX = playerX + 13


  if bulletShoot:
    bulletY = bulletY - bullet_speed

  if bulletY <= 0:
    bulletShoot = False
    bulletY = playerY
    bulletX = playerX + 13

  if playerX >= winWidth - 55:
    playerX = playerX - 5
    
  if playerX <= 0:
    playerX = playerX + 5

  for i in range(len(enemy_x)):
    if isCollison(bulletX, bulletY, enemy_x[i], enemy_y[i]):
      bulletShoot = False
      bulletY = playerY
      bulletX = playerX + 13
      print('Collided with spaceship')
      enemy_y[i] = -10000
      score = score + 1

  clock.tick(fps)
  pygame.display.update()
