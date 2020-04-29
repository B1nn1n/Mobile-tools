#!/usr/bin/env python
import subprocess
import argparse
import os

print "  _________                           .__      ________          __          "
print " /   _____/ ____ _____ _______   ____ |  |__   \______ \ _____ _/  |______   "
print " \_____  \_/ __ \\__  \\_  __ \_/ ___\|  |  \   |    |  \\__  \\   __\__  \  "
print " /        \  ___/ / __ \|  | \/\  \___|   Y  \  |    `   \/ __ \|  |  / __ \_"
print "/_______  /\___  >____  /__|    \___  >___|  / /_______  (____  /__| (____  /"
print "        \/     \/     \/            \/     \/          \/     \/          \/ "



parser = argparse.ArgumentParser(description='Pentesting tool to search for a list of strings in a directory.  Searches the current directory and all sub directories.')
parser.add_argument('dataFile', help='The file containing the strings to search for.')
parser.add_argument('path', help='The location to store the output findings, Full path.  Not in the search directory.')

args=parser.parse_args()

userDataFile = args.dataFile
userPath = args.path

# Check for the existance of the directory they want to store all the files in
if os.path.exists(userPath) == 0:
	print "Path for output does not exist, please create or select an existing directory to store output."
	exit(1)

# Open the input file
file = open(userDataFile, 'r')

# Might add support to see and or log the findings.
def put_output(file, out_str):
	#print out_str + "\n"
	file.write(out_str + "\n")


for line in file:
	line = line.rstrip()
	# create the file for each search string, easy to deal with
	fileName = userPath + "data_search_" + line + ".txt"
	file_output = open(fileName, 'w')

	# Display as we go so the user knows what is going on
	print "Creating file: " + fileName
	print "Searching for " + line
	put_output(file_output, "searching for " + line)
	
	#build the cmd for finding the package
	cmd1 = 'grep -iRn ' + line + ' .'

	#kick off the command
	sp1 = subprocess.check_output(cmd1.split())
	results_with_package = sp1.split('\n')
	#tell the user the full name of the package, just in case they want it
	count = 0
	print len(results_with_package)
	for results in results_with_package:
		#print results
		count += 1
		put_output(file_output, results)

	print "{} items writen to file: {}".format(count, fileName)
	file_output.close()

file.close()


