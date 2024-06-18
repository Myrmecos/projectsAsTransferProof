import numpy as np

def generate_perlin_noise(width, height, scale):
    # Generate a grid of random gradient vectors
    np.random.seed(200)
    gradient = np.random.randn(width, height, 2)

    #print('gradient: ', gradient)

    # Generate a grid of coordinates
    x = np.linspace(0, scale, width, endpoint=False)
    y = np.linspace(0, scale, height, endpoint=False)
    x_grid, y_grid = np.meshgrid(x, y)

    print(x_grid)

    # Calculate the indices of the four surrounding grid points for each coordinate
    x0 = x_grid.astype(int)
    x1 = (x0 + 1) % width
    y0 = y_grid.astype(int)
    y1 = (y0 + 1) % height

    #print(x1)

    # Calculate the distances between the coordinates and the four surrounding grid points
    dx = x_grid - x0.astype(float)
    dy = y_grid - y0.astype(float)

    # Calculate the dot products between the gradient vectors and the distance vectors
    dot_product_top_left = np.einsum('ijk,ijk->ij', gradient[x0, y0], np.stack([dx, dy], axis=-1))
    dot_product_top_right = np.einsum('ijk,ijk->ij', gradient[x1, y0], np.stack([dx - 1, dy], axis=-1))
    dot_product_bottom_left = np.einsum('ijk,ijk->ij', gradient[x0, y1], np.stack([dx, dy - 1], axis=-1))
    dot_product_bottom_right = np.einsum('ijk,ijk->ij', gradient[x1, y1], np.stack([dx - 1, dy - 1], axis=-1))

    # Interpolate the dot products using smoothstep function
    u = fade(dx)
    v = fade(dy)
    interpolated_top = lerp(dot_product_top_left, dot_product_top_right, u)
    interpolated_bottom = lerp(dot_product_bottom_left, dot_product_bottom_right, u)
    interpolated_noise = lerp(interpolated_top, interpolated_bottom, v)

    return interpolated_noise

# Fade function for smooth interpolation
def fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3

# Linear interpolation function
def lerp(a, b, t):
    return a + t * (b - a)

# Example usage
width = 5
height = 5
scale = 1.0
perlin_noise = generate_perlin_noise(width, height, scale)

# Print the generated Perlin Noise array
#print(perlin_noise)