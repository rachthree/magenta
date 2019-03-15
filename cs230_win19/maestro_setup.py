# Sorts into train/val/test given directory of Maestro dataset
# Steps:
# 1. Download Maestro dataset from here:
# https://storage.googleapis.com/magentadata/datasets/maestro/v1.0.0/maestro-v1.0.0-midi.zip
# 2. Unzip to wherever location
# 3. run this script in terminal as:
# python -m maestro_setup.py --dir=<directory of unzipped maestro dataset>

import argparse
import os
import pandas
from shutil import copyfile

FUNC_DIR = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("--dir", default=os.path.join(FUNC_DIR, "maestro-v1.0.0"),
                    type=str, help="Directory for unzipped Maestro dataset")
args = parser.parse_args()

try:
    os.mkdir(os.path.join(args.dir, 'train'))
except Exception as e:
    pass

try:
    os.mkdir(os.path.join(args.dir, 'validation'))
except Exception as e:
    pass

try:
    os.mkdir(os.path.join(args.dir, 'test'))
except Exception as e:
    pass

# Open and read csv
data_info = pandas.read_csv(os.path.join(args.dir, 'maestro-v1.0.0.csv'))

# Go through CSV, copy files over to respective train/val/test directories
for ind, row in data_info.iterrows():
    split_type = row["split"]
    midi_filename = row["midi_filename"]
    midi_fileOnly = midi_filename[5:]
    copyfile(os.path.realpath(os.path.join(args.dir, midi_filename)), os.path.join(args.dir, split_type, midi_fileOnly))

