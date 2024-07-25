import argparse
import readline
import os
import sys
import glob as globpy

from termcolor import colored

import utils.glob as glob

shared = {"args": None}


def init():
    version = "1.0"

    default_path = glob.get_cwd()
    default_out = glob.join_path(glob.get_cwd(), "cover-arts")
    default_title = ""

    parser = argparse.ArgumentParser(description="Generates cover arts for Jellyfin library in batch")
    parser.add_argument("-p", "--path", help="Path of the image or folder for batch processing", type=str, metavar="")
    parser.add_argument("-o", "--out", help="Output folder for generated cover-arts", type=str, metavar="")
    parser.add_argument("-t", "--title", help="Title name", type=str, metavar="")
    parser.add_argument("-sp", "--samepath", help="The output will be generated in the input path folder", action="store_true")
    parser.add_argument("-cli", "--cli", help="Run as a CLI without changing default args", action="store_true")
    parser.add_argument("-v", "--version", help="Prints version info", action="store_true")

    args = parser.parse_args()

    if any(value is not None and value is not False for value in vars(args).values()):
        args.cli = True

    shared["args"] = vars(args)

    if args.version == True:
        print(version)
        sys.exit()

    if not any(value is not None and value is not False for value in vars(args).values()):
        def pathCompleter(text, state):
            matches = []
            for x in globpy.glob(text + '*'):
                if not os.path.isfile(x):
                    x += "/"
                matches.append(x.replace("\\", "/"))
            return matches[state]

        try:
            readline.set_completer_delims('\t')
            readline.parse_and_bind("tab: complete")
            readline.set_completer(pathCompleter)

            input_path = input(colored(f"Path of the image or folder ({colored(default_path, 'yellow')}): ", "blue")).strip()
            args.path = glob.get_abs_path(glob.correct_path(input_path)) if input_path != "" else default_path

            if glob.is_file(args.path):
                default_out = glob.join_path(glob.get_dirname(args.path), "cover-arts")
            else:
                default_out = glob.join_path(args.path, "cover-arts")
            input_out = input(colored(f"Output folder ({colored(default_out, 'yellow')}): ", "blue")).strip()
            args.out = glob.get_abs_path(glob.correct_path(input_out)) if input_out != "" else default_out

            readline.set_completer(None)

            input_title = input(colored(f"Title: ", "blue"))
            args.title = input_title if input_title != "" else default_title

            os.system('cls')
        except Exception as err:
            print()
            if ("invalid literal for int()" in str(err)):
                print(colored("Invalid input type, That field only accepts numbers", "red"))
            else:
                print(colored("Invalid input type", "red"))

            exit_program()

    else:
        args.path = glob.get_abs_path(glob.correct_path(args.path)) if args.path != None and args.path != "" else default_path
        args.out = glob.correct_path(args.out) if args.out != None and args.out != "" else default_out
        args.title = args.title if args.title != None else default_title

        print()

    args.version = version

    if (args.samepath):
        if(default_out != args.out):
            if(glob.is_abs(args.out)):
                print(colored("Outpath should be a relative path when using --samepath", "red"))
                exit_program()
        else:
            args.out = "."

        print(args.path, args.out)
    else:
        args.out = glob.get_abs_path(args.out)

    shared["args"] = vars(args)
    return args


def log_args(args):
    print(colored("Configuration:", "yellow", attrs=["bold", "underline"]))
    print()
    print(colored(f"Input Path:", "blue"), colored(f"{args.path}", "yellow"))
    print(colored(f"Output path:", "blue"), colored(f"{args.out}", "yellow"))
    print(colored(f"Title:", "blue"), colored(f"{args.title}", "yellow"))
    print()


def get_args():
    return shared["args"]


def exit_program():
    print()
    if shared["args"]["cli"] != True:
        input(colored("Press enter to exit...", "green"))
    sys.exit()
