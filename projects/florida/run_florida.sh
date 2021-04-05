#!/bin/sh

echo "Enter the integer corresponding to the desired option:"
echo "1: Generate FL Early Polling latlongs"
echo "2: Generate FL Libraries latlongs"
echo "3: Generate FL Voters latlongs"

read choice

case ${choice} in
    1) 
    echo "Enter path to the FOLDER containing early polling CSVs:"
    read input_csv
    echo "Enter output CSV path (including filename and extension):"
    read output_csv
    
    python generate_early_polling_fl.py -i ${input_csv} -o ${output_csv}
    ;;
    2) 
    echo "Enter input CSV path (including filename and extension):"
    read input_csv
    echo "Enter output CSV path (including filename and extension):"
    read output_csv
    
    python generatelatlong_schools.py -i ${input_csv} -o ${output_csv}
    ;;
    3)
    echo "Enter path to the FOLDER containing early polling CSVs:"
    read input_csv
    echo "Enter output CSV path (including filename and extension):"
    read output_csv
    
    python generatelatlong_voters.py -i ${input_csv} -o ${output_csv}
    ;;
    *)
        echo "Please enter a valid integer, exiting..."
        exit 1
    ;;
esac
