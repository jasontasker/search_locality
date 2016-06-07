#!/usr/bin/python

import re
import argparse
import os
import glob

# Start main
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--min', dest='min_words', default="0", required=False, help="Minimum words between contexts (Default is 0)")
	parser.add_argument('--max', dest='max_words', default="10", required=False, help="Maximum words between contexts (Default is 10)")
	parser.add_argument('--context1', dest='context1', default="context1", required=True, help="Search context term 1")
	parser.add_argument('--context2', dest='context2', default="context2", required=True, help="Search context term 2")
	parser.add_argument('--directory', dest='directory', default=".", required=False, help="Directory with text files to search (Default is local Directory)")
	parser.add_argument('--extension', dest='extension', default="txt", required=False, help="Directory with text files to search (Default is txt)")
	args = parser.parse_args()

search_string_1 = r"\b(" + re.escape(args.context1) + r")(?:\W+\w+){" + re.escape(args.min_words) + r"," + re.escape(args.max_words) + r"}?\W+(" + re.escape(args.context2) + r")\b"
search_string_2 = r"\b(" + re.escape(args.context2) + r")(?:\W+\w+){" + re.escape(args.min_words) + r"," + re.escape(args.max_words) + r"}?\W+(" + re.escape(args.context1) + r")\b"


for root, dirs, files in os.walk(args.directory):
	for file in files:
		if file.endswith("." + args.extension):
			filename = os.path.join(root, file)
			textfile = open(filename, 'r')
			filetext = textfile.read()
			textfile.close()
			matches1 = re.findall(search_string_1, filetext, re.I)
			matches2 = re.search(search_string_2, filetext, re.I)

			if matches1:
				print "This file matches the 2 contexts:"
				print filename

			elif matches2:
				print "This file matches the 2 contexts:"
				print filename
