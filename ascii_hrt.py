import numpy as np
import time
import os

# ANSI escape codes for gradients of red
colors = {
    ' ': '\033[0m',      # Default
    '.': '\033[1;31m',   # Light Red
    ':': '\033[0;31m',   # Red
    '-': '\033[0;31m',   # Dark Red
    '=': '\033[1;31m',   # Light Red
    '+': '\033[0;31m',   # Red
    '*': '\033[0;31m',   # Dark Red
    '#': '\033[1;31m',   # Light Red
    '@': '\033[0;31m',   # Red
    'reset': '\033[0m'   # Reset to default
}

def heart_shape(t, scale):
    x = 16 * np.sin(t)**3 * scale
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t) * scale
    return x, y

def plot_heart(x, y, width=40, height=20):
    heart = np.full((height, width), ' ')
    
    chars = [' ', '.', ':', '-', '=', '+', '*', '#', '@']
    
    x_scale = width / 32.0
    y_scale = height / 32.0
    
    max_x = max(abs(min(x)), abs(max(x)))
    max_y = max(abs(min(y)), abs(max(y)))
    
    for xi, yi in zip(x, y):
        ix = int(width / 2 + xi * x_scale)
        iy = int(height / 2 - yi * y_scale)
        
        if 0 <= ix < width and 0 <= iy < height:
            depth = np.sqrt(xi**2 + yi**2)
            char_index = int((depth / max(max_x, max_y)) * (len(chars) - 1))
            heart[iy, ix] = chars[char_index]
    
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in heart:
        print(''.join(colors[ch] + ch for ch in line) + colors['reset'])

# Animation loop
t = np.linspace(0, 2 * np.pi, 1000)
scale = 1.0
scale_direction = 0.05

while True:
    x, y = heart_shape(t, scale)
    plot_heart(x, y)
    
    scale += scale_direction
    if scale > 1.2 or scale < 0.8:
        scale_direction = -scale_direction

    time.sleep(0.1)
