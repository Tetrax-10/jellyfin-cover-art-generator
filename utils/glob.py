import os
import sys
import shutil
from pathlib import Path

from termcolor import colored


def get_cwd():
    return os.getcwd()


def join_path(*args):
    return os.path.join(*args)


def get_dirname(path):
    return os.path.dirname(path)


def is_file(path):
    p = Path(path)
    return p.is_file()


def is_abs(path):
    return os.path.isabs(path)


def get_abs_path(path):
    if path == ".":
        return get_cwd()

    path = os.path.normpath(path)
    path = path[1:] if path.startswith("\\") else path

    if not is_abs(path):
        path = join_path(get_cwd(), path)

    return path


def correct_path(path):
    path = path[1:-1] if path.startswith('"') and path.endswith('"') else path
    path = path[1:-1] if path.startswith('"') and path.endswith('"') else path

    path = os.path.normpath(path)

    path = path[1:] if path.startswith("\\") else path

    return path


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


# not used
def delete_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def get_file_name(file, type="name"):
    if type == "ext":
        return Path(file).suffix[1:]
    else:
        return Path(file).stem


def get_all_image_files(path):
    image_files = []
    image_extensions = ["jpg", "jpeg", "png", "webp", "bmp", "gif", "tiff", "tif", "ico", "ppm", "pgm", "pnm", "spi", "im"]

    if os.path.isfile(path):
        image_files.append(Path(path))
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                extension = get_file_name(file, "ext").lower()
                if extension in image_extensions:
                    image_files.append(Path(root) / file)
    else:
        print(colored("Input path does not exist", "red"))
        return False

    return image_files


def get_script_path():
    # If the script is run as a standalone script
    if getattr(sys, "frozen", False):
        # Frozen executable (e.g., pyinstaller)
        return os.path.dirname(sys.executable)
    else:
        # Regular Python script
        return join_path(get_cwd(), "fonts")
