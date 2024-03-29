import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageEnhance
from termcolor import colored

import utils.commander as commander
import utils.glob as glob


def generate_cover_arts(args, image_files):
    if not args.samepath:
        glob.create_folder(args.out)

    if len(image_files):
        for image_file in image_files:
            try:

                file_name = glob.get_file_name(image_file)
                file_extension = glob.get_file_name(image_file, "ext")

                # Variables
                height = 720
                font = glob.join_path(glob.get_script_path(), "Fact-Bold.ttf")
                font_size = 150

                # Open an Image and resize
                img = Image.open(image_file)
                # Calculate width to maintain aspect ratio for 720p height
                original_width, original_height = img.size

                new_width = int((original_width / original_height) * height)
                img = img.resize((new_width, height), Image.LANCZOS)  # Use Image.LANCZOS for antialiasing

                # Lower brightness to 50%
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(0.5)  # 0.5 means 50% brightness

                # Call draw Method to add 2D graphics in an image
                I1 = ImageDraw.Draw(img)

                # Custom font style and font size
                myFont = ImageFont.truetype(font, font_size)

                # Calculate text position to center it
                text_x = img.width // 2
                text_y = img.height // 2

                # Add Text to an image
                I1.text((text_x, text_y), args.title, font=myFont, fill=(255, 255, 255), anchor="mm")

                # Save final image
                img.save(f"{args.out}/{args.title}-{file_name}.jpg")

                print(colored(f"{file_name}.{file_extension}", "green"))
            except:
                print(colored(f"{file_name}.{file_extension}", "red"))
    else:
        print(colored("No images found in the specified folder", "red"))


if __name__ == "__main__":
    args = commander.init()
    commander.log_args(args)

    image_files = glob.get_all_image_files(args.path)
    if image_files == False:
        commander.exit_program()
    else:
        generate_cover_arts(args, image_files)

    commander.exit_program()
