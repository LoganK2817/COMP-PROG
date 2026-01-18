import pygame

pygame.init()
screen_dimensions = 800,600


screen = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("Picture")

back_color = (2,0,4)

pos_rect = (0,0,800,600)
color_rect = (32, 84, 117)

pic1 = pygame.image.load("sem 2/assets/Pic1.jpeg")
pic2 = pygame.image.load("sem 2/assets/Pic2.jpeg")
pic3 = pygame.image.load("sem 2/assets/Pic3.jpeg")
pic4 = pygame.image.load("sem 2/assets/Pic4.jpeg")
pic5 = pygame.image.load("sem 2/assets/Pic5.jpeg")

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        

    pygame.draw.rect(screen,color_rect,pos_rect)


    screen.blit(pic1,(0,0))
    screen.blit(pic2,(400,0))
    screen.blit(pic3,(0,200))
    screen.blit(pic4,(400,200))
    pygame.draw.rect(screen,"cyan",(190,390,340,320))
    screen.blit(pic5,(200,400))
    
    
    
    pygame.display.flip()