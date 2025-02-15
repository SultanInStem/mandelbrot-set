import math
SCREEN_SIZE = (1200, 800)
BOUNDS = 2

def to_math_coords(pixel):
    x, y = pixel
    return [
        (x / SCREEN_SIZE[0]) * 4 - BOUNDS,  # Scale x from [0, SCREEN_WIDTH] to [-2, 2]
        (y / SCREEN_SIZE[1]) * 4 - BOUNDS   # Scale y from [0, SCREEN_HEIGHT] to [-2, 2]
    ]



def to_screen_coords(point):
    x = point[0] + (SCREEN_SIZE[0] // 2)
    y = (SCREEN_SIZE[1] // 2) - point[1]
    return [x,y] 


def square_complex_num(number): 
    return [(number[0]**2) - (number[1]**2),  2*number[0]*number[1]]

def get_complex_mag(number): 
    return math.sqrt(number[0]**2 + number[1]**2)