import os
import sys

file = sys.argv[1]
for filename in os.listdir(file):
	os.rename(filename, filename.replace(' ', '.'))
	os.rename(filename, filename.replace("'", ""))
	os.rename(filename, filename.replace(",", "."))
	os.rename(filename, filename.replace("[", "."))
	os.rename(filename, filename.replace("]", "."))
	os.rename(filename, filename.replace('_', '.'))
	os.rename(filename, filename.replace('-', '.'))

