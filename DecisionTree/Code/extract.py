import csv
import math

print 'Enter file name'
fname=raw_input().strip()

original = file(fname, 'rU')
reader = csv.reader(original)

dataset = []
for row in reader:
	dataset.append(row)
attribute_list = dataset[0][:]
	

