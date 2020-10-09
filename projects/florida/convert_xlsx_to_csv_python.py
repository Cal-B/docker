import argparse
import os
import subprocess

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input folder directory")
arg_parser.add_argument("-o", "--output", required=False, help="Output folder directory, default location is inside the input folder")
args = vars(arg_parser.parse_args())

src = args['input']
output = args['output']

filenames = (f for f in os.listdir(src) if f.endswith('.xlsx'))
for pos, file in enumerate(filenames):
    print("Loading " + os.path.join(src,file) + "...")
    spaces = "/home/h302/Downloads/conv_csvs/" + os.path.splitext(file)[0] + ".csv"
    filename = "".join(spaces.split())
    subprocess.run([
        "touch",
        filename
    ])
    subprocess.run([
        "/home/h302/pelias/docker/projects/florida/xlsx2csv.py",
        "--sheetname",
        "Primary Elections",
        os.path.join(src,file),
        filename
    ])
    subprocess.run([
        "/home/h302/pelias/docker/projects/florida/xlsx2csv.py",
        "--sheetname",
        "PrimaryElections",
        os.path.join(src,file),
        filename
    ])
    subprocess.run([
        "/home/h302/pelias/docker/projects/florida/xlsx2csv.py",
        "--sheetname",
        "PrimaryElection",
        os.path.join(src,file),
        filename
    ])
    subprocess.run([
        "/home/h302/pelias/docker/projects/florida/xlsx2csv.py",
        "--sheetname",
        "Primary Election",
        os.path.join(src,file),
        filename
    ])
    subprocess.run([
        "/home/h302/pelias/docker/projects/florida/xlsx2csv.py",
        "--sheetname",
        "Primary Election 2020",
        os.path.join(src,file),
        filename
    ])

    