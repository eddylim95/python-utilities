import numpy as np
import pickle
import sys
import csv

read_path = sys.argv[1]
save_path = sys.argv[2]

def PickleToCsv(read_path, save_path):
    with open(read_path,'rb') as f:
        data = pickle.load(f)

    with open(save_path,'w') as f:
        writer = csv.writer(f)
        for line in data:
            writer.writerow(line)


if read_path.split('.')[-1] == 'pkl' and save_path.split('.')[-1] == 'csv':
    print("Converting pickle to csv...")
    PickleToCsv(read_path, save_path)
    print("Conversion complete")
else:
    print("File format conversion is not supported!")

