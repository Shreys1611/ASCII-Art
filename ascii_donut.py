import math
import time
import random

A = 0
B = 0

def render_frame(A, B):
    output = [[' ' for _ in range(80)] for _ in range(22)]  # Output size
    z_buffer = [[0 for _ in range(80)] for _ in range(22)]  # Depth buffer to track z-axis

    # Luminance characters for shading
    luminance = ".,-~:;=!*#$@"

    # Color gradient for donut
    colors = [
        "\033[35m",  # Magenta (for pink cream)
        "\033[37m",  # White (for lighter pink)
        "\033[35;1m",  # Bright Magenta (for highlights on the cream)
        "\033[31m",  # Red (for shadows on the cream)
        "\033[0m"    # Reset color
    ]

    for theta in range(0, 628, 7):  # theta goes from 0 to 2pi (0 to 6.28)
        for phi in range(0, 628, 2):  # phi goes from 0 to 2pi (0 to 6.28)
            cos_A = math.cos(A)
            sin_A = math.sin(A)
            cos_B = math.cos(B)
            sin_B = math.sin(B)

            cos_theta = math.cos(theta / 100)
            sin_theta = math.sin(theta / 100)
            cos_phi = math.cos(phi / 100)
            sin_phi = math.sin(phi / 100)

            # 3D coordinates of the donut
            circle_x = cos_phi + 2  # x coordinate
            circle_y = sin_phi  # y coordinate
            z = 1 / (sin_theta * circle_x * sin_A + circle_y * cos_A + 5)  # z coordinate

            t = sin_theta * circle_x * cos_A - circle_y * sin_A  # temporary variable
            x = int(40 + 30 * z * (cos_theta * circle_x * cos_B - t * sin_B))  # Projected x
            y = int(11 + 15 * z * (cos_theta * circle_x * sin_B + t * cos_B))  # Projected y

            # Calculate the luminance index
            luminance_index = int(8 * ((sin_phi * sin_A - sin_theta * cos_phi * cos_A) * cos_B - sin_theta * cos_phi * sin_A - cos_theta * cos_phi * cos_A - sin_theta * cos_phi))

            # Ensure luminance index is within valid range
            luminance_index = max(0, min(len(luminance) - 1, luminance_index))

            # Map the luminance index to the colors list
            color_index = luminance_index % len(colors)  # Normalize index to fit colors list

            if 0 <= x < 80 and 0 <= y < 22:
                if z > z_buffer[y][x]:  # Ensure that this pixel is closer
                    z_buffer[y][x] = z  # Update the z-buffer with the new z depth

                    color = colors[color_index]  # Use normalized color index
                    output[y][x] = color + luminance[luminance_index] + "\033[0m"  # Add reset code

    # Print the frame
    print('\x1b[H', end='')
    for row in output:
        print(''.join(row))

# Infinite loop to animate the rotating donut
while True:
    render_frame(A, B)
    A += 0.04
    B += 0.02
    time.sleep(0.03)
