#!/usr/bin/env python
import subprocess
import argparse

print "________          __           __________.__                            "
print "\______ \ _____ _/  |______    \______   \__|_____ ______   ___________ "
print " |    |  \\__  \\   __\__  \    |       _/  \____ \\____ \_/ __ \_  __ \\"
print " |    `   \/ __ \|  |  / __ \_  |    |   \  |  |_> >  |_> >  ___/|  | \/"
print "/_______  (____  /__| (____  /  |____|_  /__|   __/|   __/ \___  >__|   "
print "        \/     \/          \/          \/   |__|   |__|        \/       "


# Function to copy the directories from the /data/data/package/ to the sdcard so it can be pulled to the local computer.
# Made this a function just in case we want to limit the directories, eg. we know files is useless we could not pull that one.
def copyImportantDirectories(dstDir, packageName):
	cmd = 'adb shell su -c ' + '"cp -r ' + '/data/data/' + packageName + '/ ' + '/sdcard/b1nn1n/"'
	print 'Copying databases directory into /sdcard/b1nn1n/'
	print cmd
	sp = subprocess.check_output(cmd.split())
	results_of_create = sp.split('\r\n')
	print results_of_create


# Create the temporary directory to hold the data from the /data/data/package/ directories.
def createDirectory(path, newDir):
	cmd = 'adb shell su -c ' + '"mkdir ' + path + newDir + '"'
	print 'Creating directory in /sdcard/b1nn1n/' + newDir
	sp = subprocess.check_output(cmd.split())
	results_of_create = sp.split('\r\n')
	print results_of_create

# Issue the pull command to get all the data from the package on the local computer
def pullData(packageName):
	cmd = 'adb pull ' + packageName
	print 'Pulling data from' + packageName
	sp = subprocess.check_output(cmd.split())
	results_of_pull = sp.split('\r\n')

# Clean up the /sdcard/ directory by removing our temporary directory.
def cleanUp(holdingDir):
	cmd = 'adb shell su -c "rm -r ' + holdingDir +' "'
	print 'Deleting all b1nn1n holding directory'
	sp = subprocess.check_output(cmd.split())
	results_of_delete = sp.split('\r\n')
	print results_of_delete

#parser setup
parser = argparse.ArgumentParser(description="Rip an applications data from an Android device")
parser.add_argument('AppName', help='the name of the application you wish to rip data of')
args = parser.parse_args()
print args.AppName
print '======='

#build the cmd for finding the package
cmd1 = 'adb shell pm list packages | grep ' + args.AppName

#kick off the command
sp1 = subprocess.check_output(cmd1.split())
results_with_package = sp1.split('\r\n')
#tell the user the full name of the package, just in case they want it
print results_with_package[0]

#build the next command to find the full path of the package
results_wo_package = results_with_package[0].split(':')
print results_wo_package[1]
cmd2 = 'adb shell pm path ' + results_wo_package[1]

#kick off the second command
sp2 = subprocess.check_output(cmd2.split())
results_of_sp2 = sp2.split('\r\n')

#print the full path of the package
results_path = results_of_sp2[0].split(':')
print results_path[1]

#build the third command to copy the files of the app to /sdcard
cmd3 = 'adb shell su -c ' + '"ls ' + "/data/data/" + results_wo_package[1] +'/"'
print 'Opening shell now'
sp3 = subprocess.check_output(cmd3.split())
results_of_shell = sp3.split('\r\n')
print results_of_shell

#create a directory in /sdcard/b1nn1n to store all the data
package_name = results_wo_package[1]
createDirectory('/sdcard/', 'b1nn1n') 
createDirectory('sdcard/b1nn1n/', package_name)

#Get all the data from the /data/data/package directory into the /sdcard/b1nn1n/ directory so it can be pulled
copyImportantDirectories('/sdcard/b1nn1n/', package_name)

#Pull the data from /sdcard/b1nn1n/
pullData('/sdcard/b1nn1n')

#Clean up the b1nn1n under /sdcard/
cleanUp('/sdcard/b1nn1n')



