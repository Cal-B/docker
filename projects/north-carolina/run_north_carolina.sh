#!/bin/sh
echo "Enter input CSV path (including filename and extension):"
read input_csv
echo "Enter output CSV path (including filename and extension):"
read output_csv
echo "Enter the integer corresponding to the desired option:"
echo "1: Generate NC Library latlongs"
echo "2: Generate NC Schools latlongs"
echo "3: Generate NC Voters latlongs"

read choice

case ${choice} in
    1) python generatelatlong_library.py -i ${input_csv} -o ${output_csv}
    ;;
    2) python generatelatlong_schools.py -i ${input_csv} -o ${output_csv}
    ;;
    3) python generatelatlong_voters.py -i ${input_csv} -o ${output_csv}
    ;;
    *)
        echo "Please enter a valid integer, exiting..."
        exit 1
    ;;
esac
