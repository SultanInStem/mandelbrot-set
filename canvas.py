import pygame
import sys
class Canvas: 
    def __init__(self, size): 
        pygame.init()
        pygame.display.set_caption("Mandelbrot Set")
        self.max_iterations = 100
        self.running = True
        self.screen = pygame.display.set_mode(size)
        self.screen_size = size
        self.clock = pygame.time.Clock()
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self): 
        for x in range(0, self.screen_size[0]): 
            for y in range(0, self.screen_size[1]): 
                z = 0 
                # c = a + bi
                # f(z) = z^2 + c
                # f(0) = c 
                # f(c) = c^2 + c 
                # f(c ^2 + c) = (c^2 + c)^2 + c
                # for _ in range(0, self.max_iterations): 
                
                    
                    
                self.screen.set_at((x,y), (255,0,255))
    def render(self): 
        # self.screen.fill((0,0,0))


        pygame.display.flip()
        self.clock.tick(60)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()



