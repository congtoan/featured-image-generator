# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:10:48 2024

@author: Admin
"""
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
from slugify import slugify
from gen_gradient_img import generate_gradient
import os

def generate_featured_image(title, output_path):
    # Image size
    width = 1024
    height = 722

    # Generate a complex gradient image (assuming it returns RGBA, convert to RGB)
    gradient_image_bytes = generate_gradient(width, height)
    gradient_image = Image.open(gradient_image_bytes).convert("RGB")

    # Add title text with shadow effect
    draw = ImageDraw.Draw(gradient_image)
    #font_path = "C:/Windows/Fonts/seguiemj.ttf"  # Path to Segoe UI Emoji font (you can choose another variant if needed)
    font_path = "C:/Windows/Fonts/segoeuib.ttf" # Xài font SegoeUI đậm
    max_font_size = 70
    min_font_size = 30
    text_color = (255, 255, 255)  # White color
    shadow_color = (0, 0, 0)       # Black shadow color
    line_spacing = 15               # Adjust line spacing as needed

    # Determine font size and wrap text
    font_size = max_font_size
    wrapped_text = textwrap.fill(title, width=25)  # Adjust wrap width as needed
    #width là số ký tự tối đa cho mỗi dòng
    
    lines = wrapped_text.splitlines()
    if len(lines) > 3:
        font_size = min_font_size

    # Load a font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate total height of text block using textbbox
    total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in lines) + (len(lines) - 1) * line_spacing

    # Calculate text position to center vertically
    text_y = (height - total_text_height) / 2

    # Draw each line of text with center alignment
    for line in lines:
        # Calculate width and height of current line using textbbox
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = (width - text_width) / 2

        # Draw shadow text
        shadow_offset = 3  # Adjust shadow offset as needed
        draw.text((text_x + shadow_offset, text_y + shadow_offset), line, font=font, fill=shadow_color)

        # Draw main text
        draw.text((text_x, text_y), line, font=font, fill=text_color)

        # Move to the next line position
        text_y += text_height + line_spacing
        
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save image as JPEG
    gradient_image.save(output_path, "JPEG")


if __name__ == "__main__":
    #Dùng để test
    title = "Example Post Title"
    slugified_title = slugify(title)
    output_path = f"./{slugified_title}.jpg"
    generate_featured_image(title, output_path)

