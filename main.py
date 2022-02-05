import pygame
import sys
import random
from game_utils import load_image, scale_image, flip_image
from classes import Road, Player, Enemy
pygame.init()


# FPS of the game
FPS = 240

# Font
font = pygame.font.Font('assets/fonts/font.ttf', 34)

# Make screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# load assetes
ROAD_IMAGE = (scale_image(load_image('assets/sprites/road.png'),
              width=SCREEN_WIDTH, height=SCREEN_HEIGHT)).convert()
PLAYER_IMAGE = (scale_image(load_image(
    'assets/sprites/player_car.png'), width=210, height=215)).convert_alpha()
ENEMY_IMAGES = [
    flip_image((scale_image(load_image('assets/sprites/enemy_car_1.png'),
               width=120, height=237)).convert_alpha()),
    flip_image((scale_image(load_image('assets/sprites/enemy_car_2.png'),
               width=120, height=237)).convert_alpha()),
    flip_image((scale_image(load_image('assets/sprites/enemy_car_3.png'),
               width=120, height=237)).convert_alpha()),
    flip_image((scale_image(load_image('assets/sprites/enemy_car_4.png'),
               width=120, height=237)).convert_alpha()),
    flip_image((scale_image(load_image('assets/sprites/enemy_car_5.png'),
               width=120, height=237)).convert_alpha())
]
ICON = load_image('assets/sprites/icon.png')

# Add icon
pygame.display.set_icon(ICON)

# Set title
TITLE_TEXT = "Modon Racer"
pygame.display.set_caption(TITLE_TEXT)

def main():
    clock = pygame.time.Clock()
    road = Road(ROAD_IMAGE, speed=3.5)

    # Configuring the player
    player_x = (156, 315, 470, 632)
    player = Player(PLAYER_IMAGE, x_lanes=player_x, y=SCREEN_HEIGHT-(PLAYER_IMAGE.get_height()+20))

    # Configuring the enemies
    enemy_x = [206, 366, 520, 682]
    enemy_y = [-1*int(ENEMY_IMAGES[0].get_height()) -1, -1*int(ENEMY_IMAGES[0].get_height())-150, -1*int(ENEMY_IMAGES[0].get_height())-200]
    counter = False
    enemies = []

    # Making the track variable
    track = 0
    
    # USEREVENT to spawn the enemy
    SPAWN_ENEMY = pygame.USEREVENT + 0
    ENEMY_SPAWN_TIME = 1000 # miliseconds
    pygame.time.set_timer(SPAWN_ENEMY, ENEMY_SPAWN_TIME)
    enemy_vel = 5

    # Redraws every element to the screen
    def redraw_elements():
        clock.tick(FPS)
        road.display(SCREEN, screen_height=SCREEN_HEIGHT)
        player.blit(SCREEN)

        score = font.render(f"Score: {pygame.time.get_ticks()//1200}", True, (0,0,0))
        score_rect = score.get_rect(topleft=(SCREEN_WIDTH//2 - score.get_width(), 0))
        SCREEN.blit(score, score_rect)

        for enemy in enemies[:]:
            enemy.blit(SCREEN)
            enemy.move()
            if enemy.off_screen(SCREEN_HEIGHT):
                enemies.remove(enemy)
            elif player.collision(enemy):
                sys.exit()

        pygame.display.update()

    while True:
        redraw_elements()
        for event in pygame.event.get():
            # Checking if the user wants to quit 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Checking if ANY keys are pressed
            elif event.type == pygame.KEYDOWN:
                # Checking if left arrow key is pressed     
                if event.key == pygame.K_LEFT:
                    player.move('left')
                # Checking if right arrow key is pressed     
                elif event.key == pygame.K_RIGHT:
                    player.move('right')

            # Spawning the enemies after sometime
            elif event.type == SPAWN_ENEMY:
                temp_enemy_x = enemy_x[:]
                new_enemy_x = random.choice(enemy_x)
                new_enemy_y = random.choice(enemy_y)
                new_enemy_img = random.choice(ENEMY_IMAGES)
                if new_enemy_x == track:
                    temp_enemy_x.remove(new_enemy_x)
                    new_enemy_x = enemy_x[player_x.index(player.x)]
                    track = new_enemy_x
                    enemies.append(Enemy(new_enemy_img, speed=enemy_vel, x=new_enemy_x, y=new_enemy_y))
                else:
                    track = new_enemy_x
                    enemies.append(Enemy(new_enemy_img, speed=enemy_vel, x=new_enemy_x, y=new_enemy_y))
             
            if pygame.time.get_ticks()//1200 == 10 and not counter:
                enemy_vel += 1
                road.speed += 1
                ENEMY_SPAWN_TIME -= 200
                pygame.time.set_timer(SPAWN_ENEMY, ENEMY_SPAWN_TIME)
                counter = not counter
            elif pygame.time.get_ticks()//1200 == 20 and counter:
                enemy_vel += 1
                road.speed += 1
                ENEMY_SPAWN_TIME -= 100
                pygame.time.set_timer(SPAWN_ENEMY, ENEMY_SPAWN_TIME)
                counter = not counter
            elif pygame.time.get_ticks()//1200 == 30 and not counter:
                enemy_vel += 1
                road.speed += 1
                ENEMY_SPAWN_TIME -= 100
                pygame.time.set_timer(SPAWN_ENEMY, ENEMY_SPAWN_TIME)
                counter = not counter
            elif pygame.time.get_ticks()//1200 == 30 and counter:
                enemy_vel += 1
                road.speed += 1
                ENEMY_SPAWN_TIME -= 50
                pygame.time.set_timer(SPAWN_ENEMY, ENEMY_SPAWN_TIME)
                counter = not counter
                    
                
if __name__ == '__main__':
    main()
