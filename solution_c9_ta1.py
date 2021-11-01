# Importing 'pygame'
import pygame

# Initializing 'pygame'
pygame.init()

# Creating a display screen of width 400 and height 600
screen=pygame.display.set_mode((400,600))

# Setting a title for the game as 'Infinite Flying Bird Game'
pygame.display.set_caption('Infinite Flying Bird Game')

# Creating an empty dictionary 'images'
images={}

# Loading the images into the dictionary
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()

# Creating a rectangle and naming it 'bird'
bird=pygame.Rect(100,250,30,30)

# Creating a 'game loop'
while True:
  
  # Displaying the background image at [0,0]
  screen.blit(images["bg"],[0,0])
  # Displaying the ground image at [0,550]
  screen.blit(images["ground"],[0,550])
  # Displaying the bird image over the rectangle 'bird'
  screen.blit(images["bird"],bird)
  
  # Handling the event to QUIT the game
  # Creating a for loop to list the events one by one
  for event in pygame.event.get():
    # Checking if the 'QUIT' button is pressed
    if event.type==pygame.QUIT:
        # Quitting the game
        pygame.quit()
        
  # Updating the display
  pygame.display.update()
  
  # Mentioning the number of frames as 30 to create motion effect
  pygame.time.Clock().tick(30)
