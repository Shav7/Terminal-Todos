from PIL import Image, ImageDraw

# Create a new image with a black background
size = 32
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw a terminal-like ">" prompt in green
prompt_color = (0, 255, 0, 255)  # Terminal green
draw.polygon((
    (8, 16),     # Left point
    (16, 12),    # Top point
    (16, 20)     # Bottom point
), fill=prompt_color)

# Draw the cursor line
draw.rectangle((18, 12, 24, 20), fill=prompt_color)

# Save the image as both ICO and PNG
img.save('static/favicon.ico', format='ICO')
img.save('static/favicon.png', format='PNG')
