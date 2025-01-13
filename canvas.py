import pygame
import sys
class Canvas: 
    def __init__(self, size): 
        pygame.init()
        self.running = True
        pygame.display.set_caption("Mandelbrot Set")
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
    def handle_events(self): 
        pass 
    def update(self): 
        pass 
    def render(self): 
        pass 
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()



