import argparse
from pathlib import Path
import glob

current_setting = open("active", "r")
active = current_setting.readline()
current_setting.close()

all_settings = glob.glob("settings/*")
n = len(all_settings)


def ShowAllAvailable():
    print("Available Settings:")
    for idx, g in enumerate(all_settings):
        if active == g:
            print(idx, g + "*")
        else:
            print(idx, g)


def CreateNewSettingsFile(fileName):
    f1 = open(fileName, "w")
    f2 = open("template.js", "r")
    fileName = fileName[9:-3]

    for ind, line in enumerate(f2):
        new_line = ""
        if ind == 33:
            new_line = f'  flowFile: "{fileName}.json",'
        elif ind == 55:
            new_line = f'  userDir: "/home/cold/.node-red/env/{fileName}",'
        else:
            new_line = line
        f1.write(new_line)
    print(f"Created a new configuration : {fileName}.json")


def ChangeSettings(new_settings_file):
    if new_settings_file not in all_settings:
        CreateNewSettingsFile(new_settings_file)

    f1 = open(new_settings_file, "r")
    f2 = open("settings.js", "w")

    for line in f1:
        f2.write(line)
    current_setting = open("active", "w")
    current_setting.write(new_settings_file)

    print(f"Current settings are now changed to {new_settings_file}")


def OptionPicker():
    x = -1

    while x < 0 or x >= n:
        ShowAllAvailable()
        input_label = f"To activate a setting choose [0, {n-1}] or c to cancel: "
        x = input(input_label)
        if x == "c":
            exit()
        if x < 0 or x >= n:
            print("Input is invalid. Retry.\n")

    ChangeSettings(all_settings[x])


parser = argparse.ArgumentParser()
parser.add_argument("--o", "-Option")
args = parser.parse_args()

if args.o:
    ChangeSettings(f"settings/{args.o}.js")
else:
    OptionPicker()
