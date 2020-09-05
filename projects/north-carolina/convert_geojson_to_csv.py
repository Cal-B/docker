import os
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input folder directory")
arg_parser.add_argument("-o", "--output", required=False, help="Output folder directory, default location is inside the input folder under /csvs")
args = vars(arg_parser.parse_args())

src = args['input']
output = args['output']


if output is None:
    output = os.path.join(src, 'csvs')
if not os.path.exists(output):
    os.mkdir(output)

print("Source directory set to: " + src)
print("Output directory set to: " + output)

filenames = (f for f in os.listdir(src) if f.endswith('.geojson'))
for pos, file in enumerate(filenames):
    file_path =  song_path = os.path.join(src, file)
    filename_pruned = file.split('-')[0]
    filename_no_extension = os.path.splitext(filename_pruned)[0]
    print('Converted ' + file + ' to ' + filename_no_extension + ".csv")
    convert_to_csv = f"ogr2ogr -f csv {filename_no_extension}.csv {file_path}"
    os.system(convert_to_csv)


