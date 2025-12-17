import colorsys
import numpy as np

def hex_to_hsv(hex_color):
    """Convert hex color to HSV tuple (H: 0-1, S: 0-1, V: 0-1)"""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return colorsys.rgb_to_hsv(r, g, b)

def hsv_to_hex(h, s, v):
    """Convert HSV tuple to hex color (h,s,v in 0-1 range)"""
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

def linear_gradient_with_hue(start_hex, steps=13, hue_shift=0.0):
    """
    Generate a linear gradient in HSV space with optional hue shift.
    
    Args:
        start_hex: Starting color in hex format
        steps: Number of colors in the gradient (default 13)
        hue_shift: Amount of hue shift per step (0-1 range, typically -0.2 to 0.2)
                   Positive values shift hue forward (red→yellow→green→...),
                   Negative values shift hue backward (red→purple→blue→...)
    
    Returns:
        List of hex colors
    """
    start_h, start_s, start_v = hex_to_hsv(start_hex)
    
    colors = []
    for i in range(steps):
        t = i / (steps - 1)  # t from 0 to 1
        
        # Apply linear hue shift
        h = (start_h + hue_shift * t) % 1.0  # Wrap around 0-1 range
        
        # Saturation and Value decrease linearly to 0
        s = start_s * (1 - t)
        v = start_v * (1 - t)
        
        colors.append(hsv_to_hex(h, s, v))
    
    return colors

orange = linear_gradient_with_hue('#ff6600', steps=13, hue_shift=-0.05)
teal = linear_gradient_with_hue('#00ead2', steps=13, hue_shift=-0.05)
print(f"{orange}\n{teal}")
