#reference: https://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, math, sys, time, scipy.io as sio

pygame.init()
pygame.display.set_caption('Synchronized motion')
s_width = 600
s_height = 200
screen = pygame.display.set_mode((s_width, s_height))
slider_colr = (0, 0, 255)
slider_x = 30
slider_y = 150
slider_width = 150
slider_hit = 15
#RED = (255, 50, 50)
img = pygame.image.load('smalldotrect.png')
img = img.convert_alpha()
img_w, img_h = img.get_size()


X = 600  # screen width
Y = 400  # screen height

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
TRANS = (1, 1, 1)
GREEN = (0,255,0)


class Slider():
    def __init__(self, name, val, maxi, mini, pos):
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = pos  # x-location on screen
        self.ypos = 200
        self.surf = pygame.surface.Surface((600, 200))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(100, 50))

        # Static graphics - slider background #
        self.surf.fill(WHITE)

        pygame.draw.rect(self.surf, RED, [10, 30, 500, 9], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)


    def draw(self):
        """ Combination of static and dynamic graphics in a copy of
    the basic slide surface
    """
        # static
        surf = self.surf.copy()

        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*500), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position

        # screen
        screen.blit(surf, (self.xpos, self.ypos))

    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pygame.mouse.get_pos()[0] - self.xpos) / 500 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi



font = pygame.font.SysFont("Verdana", 12)
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()




user = Slider("", 10, 500, 10, 25)
#computer = Slider("", 20, 800, 10, 500)

MousePos = []
AIPos = []
TimeArray = []
ErrorSum = 0
clickcount = 0
Constants = [0.5, 0.02]
userslider = [user]

def ExitSequence():
    pygame.quit()
    print(MousePos)
    print(AIPos)
    print(TimeArray)
    #If below code doesn't work get rid of the 'r'!!
    sio.savemat(r'C:\Users\Laptop\Downloads\Project3\Project3\mousevals.mat',mdict={'MousePos': MousePos})
    sio.savemat(r'C:\Users\Laptop\Downloads\Project3\Project3\AIvals.mat',mdict={'AIPos': AIPos})
    sio.savemat(r'C:\Users\Laptop\Downloads\Project3\Project3\TimeArray.mat',mdict={'TimeArray': TimeArray})

    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ExitSequence()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickcount += 1
            (target_x, target_y) = pygame.mouse.get_pos()
            if clickcount <= 1:
                start_time = time.time()
            for s in userslider:
                if s.button_rect.collidepoint(target_x, target_y):
                    s.hit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for s in userslider:
                s.hit = False

        for s in userslider:
            if s.hit:
                s.move()
                mouse_x, mouse_y = event.pos
                #PID controller implementation
                Error = mouse_x - slider_x
                print(Error)
                ErrorSum += Error
                Control = Constants[0]*Error + Constants[1]*ErrorSum #+ Constants[0]*
                #print(Control)
                slider_x += Control
                MousePos.append(mouse_x - 30)
                AIPos.append(slider_x - 30)
                TimeArray.append((time.time() - start_time))
                if time.time() - start_time > 20:
                    ExitSequence()

                #print("(%d, %d)" % event.pos)
        screen.fill(WHITE)
        #num += 2

        for s in userslider:
            s.draw()

        rectangle = pygame.draw.rect(screen, GREEN, [35, 147, 500, 9], 0)
        screen.blit(img, (slider_x - img_w / 2, slider_y - img_h / 2))
        time.sleep(0.2)
        pygame.display.update()

        pygame.display.flip()