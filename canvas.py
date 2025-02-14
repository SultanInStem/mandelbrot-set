import pygame
import sys
from globals import square_complex_num, get_complex_mag, SCREEN_SIZE, to_math_coords, to_screen_coords
from complex_num import ComplexNumber
class Canvas: 
    def __init__(self): 
        pygame.init()
        pygame.display.set_caption("Mandelbrot Set")
        self.max_iterations = 100
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.screen_size = self.screen.get_size()

        self.points = []
        bounds = 2

        


        for x in range(0, SCREEN_SIZE[0],10): 
            for y in range(0, SCREEN_SIZE[1],10): 
                ### test a point
                c = [x,y]
                seq = [c]
                for z in range(1, self.max_iterations): 
                    res = [seq[z - 1][0]**2 - seq[z - 1][1]**2, 2*seq[z - 1][0]*seq[z - 1][1]]
                    res[0] += c[0]
                    res[1] += c[1]
                    seq.append(res)
                    if res[0]**2 + res[1]**2 > 4: pass

    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):     
        print(self.points)                
        pass 
    def render(self): 
        self.screen.fill((0,0,0))

        for p in self.points: 
            pygame.draw.circle(self.screen, (0,80,255),p,1,0)

        pygame.display.flip()
        self.clock.tick(60)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()



