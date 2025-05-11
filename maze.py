from pygame import *
mixer.init()
font.init()
wdoniw = display.set_mode((700, 500))
f0nt = font.SysFont('ComicSans', 55)
win = f0nt.render('Шлепок съел свой пельмен', True, (0, 0, 255))
lose = f0nt.render('Шлепка выпнули из этой реальности', True, (255, 0, 0))
display.set_caption('Мазик')
direction = 'right'
fon = transform.scale(image.load('pelmennaya.jfif'), (700, 500))
class CocaCola(sprite.Sprite):
    def __init__(self, x, y, imagename, w, h, speed):
        super().__init__()
        self.img = transform.scale(image.load(imagename), (w, h))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sPEEd = speed
    def reset(self):
        wdoniw.blit(self.img, (self.rect.x, self.rect.y))
class CocaColaDiet(CocaCola):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.sPEEd
        elif keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.sPEEd
        elif keys_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.sPEEd
        elif keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.sPEEd
class CocaColaPlusSugar(CocaCola):
    def update(self):
        global direction
        if self.rect.x <= 520:
            direction = 'right'
        if self.rect.x >= 700 - 65:
            direction = 'left' 
        if direction == 'left':
            self.rect.x -= self.sPEEd
        else:
            self.rect.x += self.sPEEd
class Wall(sprite.Sprite):
    def __init__(self, w, h, colour, x, y):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def drawWall(self):
        wdoniw.blit(self.image, (self.rect.x, self.rect.y))
#mixer.music.load('fortnite-death.mp3')
#mixer.music.play()
kcik = mixer.Sound('fortnite-death.ogg')
meony = mixer.Sound('pelmeni.ogg')
her = CocaColaDiet(50, 400, 'shlepok-Photoroom.png', 65, 65, 10)
cyborgubivtsa = CocaColaPlusSugar(500, 350, 'dogge.png', 65, 65, 8)
wall1 = Wall(10, 400, (255, 250, 200), 300, 100)
wall2 = Wall(10, 200, (255, 250, 200), 200, 200)
wall3 = Wall(200, 10, (255, 250, 200), 100, 100)
wall4 = Wall(200, 10, (255, 250, 200), 0, 200)
wall5 = Wall(10, 400, (255, 250, 200), 400, 0)
wall6 = Wall(10, 400, (255, 250, 200), 500, 100)
wall7 = Wall(100, 10, (255, 250, 200), 500, 100)
wall8 = Wall(100, 10, (255, 250, 200), 600, 200)
wall9 = Wall(100, 10, (255, 250, 200), 500, 300)
walls = sprite.Group()
walls.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9)
podarochka = CocaCola(550, 430, 'pelmenka-Photoroom.png', 65, 65, 0 )
sotp = True
coclk = time.Clock()
FPS = 30
finish = False
while sotp:
    for e in event.get():
        if e.type == QUIT:
            sotp = False
    if not finish:
        wdoniw.blit(fon, (0, 0))
        her.update()
        cyborgubivtsa.update()
        her.reset()
        wall1.drawWall()
        wall2.drawWall()
        wall3.drawWall()
        wall4.drawWall()
        wall5.drawWall()
        wall6.drawWall()
        wall7.drawWall()
        wall8.drawWall()
        wall9.drawWall()
        cyborgubivtsa.reset()
        podarochka.reset()
        if len(sprite.spritecollide(her, walls, False)) > 0:
            her.rect.x = 50
            her.rect.y = 400
        if sprite.collide_rect(her, podarochka):
            wdoniw.blit(win, (0, 200))
            finish = True
            meony.play()
        if sprite.collide_rect(her, cyborgubivtsa):
            wdoniw.blit(lose, (0, 200))
            finish = True
            kcik.play()
    coclk.tick(FPS)
    display.update()