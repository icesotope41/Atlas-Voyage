import pygame, os

pygame.init()

width,height = 750,600 
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Atlas's Voyage")


#Sprites
##Debris
rock1 = pygame.image.load(os.path.join("assets","rock1.png"))
rock2 = pygame.image.load(os.path.join("assets","rock2.png"))
##Spaceship
atlas = pygame.image.load(os.path.join("assets","atlas.png"))
##Laser beam
laser = pygame.image.load(os.path.join("assets","laser_beam.png"))
##Background
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets","Background.png")),(width,height))


class spaceship:
    def __init__(self,x,y,health=1):
        self.ship_sprite = atlas
        self.laser_sprite = laser
        self.x = x
        self.y = y
        self.laser_cooldown = 0
        self.mask = pygame.mask.from_surface(self.ship_sprite)
        self.max_health = health


    def draw_ship(self,window):
        window.blit(self.ship_sprite,(self.x,self.y))


def main():
    running = True
    FPS = 120
    clock = pygame.time.Clock()
    vel = 5
    player = spaceship(90,365)
    surface = pygame.Surface((750,600))
    score = 00000


    #To get sprites onto window surface
    def draw():
        window.blit(surface,(0,0))
        font = pygame.font.Font("assets\Aliens Among Us.ttf",25)
        #Need to fix score adding system
        text_surface = font.render(f"Score: {score}{score}{score}{score}",1,(255,255,255))
        window.blit(text_surface,(10,10))
        player.draw_ship(window)
        pygame.display.update()
   
    
    y = 0
    while running:
        clock.tick(FPS)
        draw()
        #To check event in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        rel_y = y % bg.get_rect().height
        surface.blit(bg,(0,rel_y - bg.get_rect().height))
        if rel_y < height:
            draw()
            surface.blit(bg,(0,rel_y))
            y += 1
            pygame.display.update()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - vel > -220:
            player.x -= vel
        # vel + 5 = 5.4, this is so that the border spacing on the right side is the same as the left side
        if keys[pygame.K_d] and player.x + vel < 415:
            player.x += vel
        #elif so that by holding eg. d and left arrow keys together, player won't double in speed
        elif keys[pygame.K_LEFT] and player.x - vel > -220:
            player.x -= vel
        elif keys[pygame.K_RIGHT] and player.x + vel < 415:
            player.x += vel


main()
