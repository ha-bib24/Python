from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a dark blue background
image_width, image_height = 800, 400
background_color = (18, 41, 61)  # Dark blue color
image = Image.new("RGB", (image_width, image_height), background_color)

# Draw the logo
draw = ImageDraw.Draw(image)

# Load the font
try:
    # Use the path to the downloaded Roboto font
    font = ImageFont.truetype("path/to/Roboto-Regular.ttf", 60)  # Update the path here
except IOError:
    font = ImageFont.load_default()

# Draw the text
text = "Learnium Academic Care"
# Use draw.textbbox to get the size of the text
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_position = ((image_width - text_width) // 2, image_height - 100)
text_color = (255, 255, 255)  # White color
draw.text(text_position, text, fill=text_color, font=font)

# Draw a simple light bulb icon with brain-like lines
icon_color = (72, 182, 194)  # Teal color
icon_size = 100
icon_center = (image_width // 2, 150)

# Draw a circle for the bulb
draw.ellipse(
    (icon_center[0] - icon_size // 2, icon_center[1] - icon_size // 2,
     icon_center[0] + icon_size // 2, icon_center[1] + icon_size // 2),
    outline=icon_color, width=4
)

# Draw simple lines inside the bulb to represent a brain-like structure
brain_lines = [
    (icon_center[0] - 20, icon_center[1] - 30, icon_center[0] + 20, icon_center[1] - 30),
    (icon_center[0] - 25, icon_center[1] - 10, icon_center[0] + 25, icon_center[1] - 10),
    (icon_center[0] - 15, icon_center[1] + 10, icon_center[0] + 15, icon_center[1] + 10)
]
for line in brain_lines:
    draw.line(line, fill=icon_color, width=3)

# Draw the base of the light bulb
draw.rectangle(
    (icon_center[0] - 10, icon_center[1] + 50, icon_center[0] + 10, icon_center[1] + 80),
    fill=icon_color
)

# Save and display the image
image.save("logo.png")
image.show()