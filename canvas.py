import pygame
import sys
from globals import SCREEN_SIZE, to_math_coords
from complex_num import ComplexNumber
class Canvas: 
    def __init__(self): 
        pygame.init()
        pygame.display.set_caption("Mandelbrot Set")
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.screen_size = self.screen.get_size()

        self.points = []
        self.bounds = 2
        self.max_iterations = 100



        for x in range(0, SCREEN_SIZE[0]): 
            for y in range(0, SCREEN_SIZE[1]): 
                ### test a point
                c = to_math_coords([x,y])
                is_included = True
                if c[0]**2 + c[1]**2 > self.bounds**2: 
                    continue
                num = c

                for z in range(self.max_iterations):
                    num = [num[0]**2 - num[1]**2 + c[0], 2*num[0]*num[1] + c[1]]
                    if num[0]**2 + num[1]**2 > self.bounds**2:
                        print("Exited at ", z) 
                        is_included = False
                        break  # Escaped
                if(is_included): self.points.append((x,y))


        print(len(self.points))


        
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):  
        pass 
    def render(self): 
        self.screen.fill((0,0,128))


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



