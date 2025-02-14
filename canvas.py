import pygame
import sys
from globals import square_complex_num, get_complex_mag, SCREEN_SIZE, to_math_coords, to_screen_coords
from complex_num import ComplexNumber
import math
class Canvas: 
    def __init__(self): 
        pygame.init()
        pygame.display.set_caption("Mandelbrot Set")
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.screen_size = self.screen.get_size()

        self.points = []
        self.rest = []
        bounds = 2
        max_iterations = 100

        ### f(z) = z^2 + c 


        for x in range(0, SCREEN_SIZE[0]): 
            for y in range(0, SCREEN_SIZE[1]): 
                ### test a point
                c = to_math_coords([x,y])
                seq = [c]
                is_included = True
                if c[0]**2 + c[1]**2 > bounds**2: 
                    continue
                for z in range(1, max_iterations):
                    num = seq[z-1]
                    res = [num[0]**2 - num[1]**2, 2*num[0]*num[1]]
                    res[0] += c[0]
                    res[1] += c[1]
                    if math.sqrt(res[0]**2 + res[1]**2) > bounds: 
                        is_included = False
                        break
                    seq.append(res)
                if(is_included): self.points.append((x,y))


        
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):        
        pass 
    def render(self): 
        self.screen.fill((0,0,0))

        for p in self.points: 
            pygame.draw.circle(self.screen, (0,0,0),p,1,0)

        pygame.display.flip()
        self.clock.tick(60)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()



