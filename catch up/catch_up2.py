from pygame import *

clock = time.Clock()
FPS = 60
#створи вікно гри

#--------------------------------------
window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"), (700, 500))

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))

x1, y1 = 100,200
x2, y2 = 200, 300

game =True

while game:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_UP]:
        y2 -= 10    
    if keys_pressed[K_LEFT]:
        x2 -= 10
    if keys_pressed[K_RIGHT]:
        x2 += 10
    if keys_pressed[K_DOWN]:
        y2 += 10
        
    
    
    clock.tick(FPS)
    display.update()

    
    
    

    



