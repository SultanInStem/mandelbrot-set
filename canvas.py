import pygame
import sys
from complex_num import ComplexNumber
class Canvas: 
    def __init__(self, size): 
        pygame.init()
        pygame.display.set_caption("Mandelbrot Set")
        self.max_iterations = 100
        self.running = True
        self.screen = pygame.display.set_mode(size)
        self.screen_size = size
        self.clock = pygame.time.Clock()
        self.screen_size = self.screen.get_size()

        bounds = 2
        


        for x in range(0, len(self.screen_size[0])): 
            for y in range(0,len(self.screen_size[1])): 
                ### test a point 
                c = [x,y]
                sequence = [c]
                for z in range(1, self.max_iterations): 
                    # sequence[z].append(sequence[z-1])
                    pass
                pass



    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):                     
        pass 
    def render(self): 
        self.screen.fill((0,0,0))


        pygame.display.flip()
        self.clock.tick(60)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()



