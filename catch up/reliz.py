import pygame

pygame.init()

#-- display/window ----
window = pygame.display.set_mode((900,600))
pygame.display.set_caption("MAZE")
bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale( bg , (900, 600))

#-- clock--- for fps
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, x , y ):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture), (65,65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.kilkist = 0
    def stay(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def reset(self):
        self.rect.x = 50
        self.rect.y = 100