# Python Featured Image Generator

This repository contains Python scripts to generate featured images with custom titles and gradients.

This Python tool generates featured images for WordPress posts quickly and efficiently.

## Features

- **Gradient Image Generation:** Utilizes a custom module to create complex gradient images.
- **Title Overlay:** Adds formatted titles with customizable fonts and text effects.
- **Bulk Generation:** Supports batch processing of titles from an input file to output featured images.
- **Excel Output:** Outputs a summary Excel file with generated image filenames.


## File Structure

- **gen_featured_img.py**: Python script to generate featured images with customized titles and gradients.
- **bulk_gen_featured.py**: Script to bulk generate featured images from a list of titles.
- **gen_gradient_img.py**: Module for generating customizable gradient images.

## Requirements

- Python 3.x
- Pillow library (`pip install Pillow`)
- `slugify` library (`pip install python-slugify`)
- OpenPyXL

## Usage

### Single Image Generation

**gen_featured_img.py:** Generates a single featured image with a specified title.

```bash
python gen_featured_img.py
```
   
Modify the title variable within the script for different titles.

### Customization

To customize image size, font, and other parameters:
- **Image Size:** Modify the width and height variables in the generate_featured_image function in gen_featured_img.py.
- **Font:** Change the font_path variable to point to your desired font file. Ensure the font file is accessible to the script.
- **Additional Parameters:** Adjust other parameters such as max_font_size, min_font_size, text_color, shadow_color, and line_spacing in gen_featured_img.py to suit your requirements.

### Bulk Image Generation:

**bulk_gen_featured.py:** Generates featured images in bulk from a list of titles in input_title.txt.
   
```bash
python bulk_gen_featured.py
```

Edit input_title.txt to include the desired titles for image generation. 



### Usage Notes
Ensure the required fonts are installed and accessible to the script.
Modify parameters and configurations directly in the scripts for customization.
