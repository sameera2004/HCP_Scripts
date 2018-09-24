from __future__ import print_function
import csv
import sys

def pull_data_from_csv(csv_file):

    with open(csv_file, 'rb') as f:
    	reader = list(csv.reader(f))

    print (reader[0])

    print ("CBF_mean_values", reader[1])
    print (" CBF_SD_values", reader[2])
    print ("len CBF mean ", len(reader[1]))
    print ("len CBF std ", len(reader[2]))


if __name__ == "__main__":
   csv_file = sys.argv[1]
   pull_data_from_csv(csv_file)
