import pygame  
  
pygame.init()  
  
# Screen dimensions  
screen_width = 800  
screen_height = 600  
screen = pygame.display.set_mode((screen_width, screen_height))  
  
# Character settings  
character_width = 50  
character_height = 50  
character_x = screen_width // 2  
character_y = screen_height - character_height  
character_speed = 5  
  
# Jump settings  
is_jumping = False  
jump_velocity = 9  
gravity = 0.1 
  
# Platform settings  
platforms = [  
    pygame.Rect(100, 400, 200, 20),  
    pygame.Rect(400, 300, 200, 20),  
    pygame.Rect(200, 200, 200, 20)  
]  
  
# Token settings  
tokens = [  
    pygame.Rect(150, 370, 20, 20),  
    pygame.Rect(450, 270, 20, 20),  
    pygame.Rect(250, 170, 20, 20)  
]  
  
# Main game loop  
running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
  
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_LEFT] and character_x > 0:  
        character_x -= character_speed  
    if keys[pygame.K_RIGHT] and character_x < screen_width - character_width:  
        character_x += character_speed  
    if not is_jumping:  
        if keys[pygame.K_SPACE]:  
            is_jumping = True  
            jump_velocity = 9  
    else:  
        character_y -= jump_velocity  
        jump_velocity -= gravity  
  
    # Check for platform collisions  
    on_ground = False  
    for platform in platforms:  
        if platform.collidepoint(character_x + character_width // 2, character_y + character_height):  
            if jump_velocity < 0:  # Landing on a platform  
                is_jumping = False  
                character_y = platform.top - character_height  
                on_ground = True  
  
    # Check if on the ground  
    """if character_y >= screen_height - character_height:  
        character_y = screen_height - character_height  
        is_jumping = False  
        on_ground = True  
  
    # Gravity effect when not on a platform or ground  
    if not on_ground:  
        character_y += gravity  """
  
    # Clear screen  
    screen.fill((0, 0, 0))  
  
    # Draw platforms  
    for platform in platforms:  
        pygame.draw.rect(screen, (0, 255, 0), platform)  
  
    # Draw tokens  
    for token in tokens:  
        pygame.draw.rect(screen, (255, 255, 0), token)  
  
    # Draw character  
    pygame.draw.rect(screen, (255, 0, 0), (character_x, character_y, character_width, character_height))  
  
    pygame.display.flip()  
  
pygame.quit()  
