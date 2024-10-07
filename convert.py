import os
import subprocess
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
INKSCAPE_PATH = "C:\\Program Files\\Inkscape\\bin\\inkscape.exe"


def convert_cdr_to_png(cdr_file, output_file):
    try:
        subprocess.run([INKSCAPE_PATH, cdr_file, '--export-filename', output_file], check=True)
        print(f"Converted {cdr_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {cdr_file}: {e}")

def convert_tif_to_png(tif_file, output_file):
    try:
        with Image.open(tif_file) as img:
            img.save(output_file, 'PNG')
        print(f"Converted {tif_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {tif_file}: {e}")

def convert_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        input_file = os.path.join(input_dir, filename)
        name, ext = os.path.splitext(filename)

        if ext.lower() == '.cdr':
            output_file = os.path.join(output_dir, f"{name}.png")
            convert_cdr_to_png(input_file, output_file)

        elif ext.lower() in ['.tif', '.tiff']:
            output_file = os.path.join(output_dir, f"{name}.png")
            convert_tif_to_png(input_file, output_file)

input_directory = "."
output_directory = "."

convert_files(input_directory, output_directory)
