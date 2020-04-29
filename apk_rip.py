#!/usr/bin/env python
import subprocess
import argparse

print "   _____ __________ ____  __. __________.__                            "
print "  /  _  \\______   \    |/ _| \______   \__|_____ ______   ___________ "
print " /  /_\  \|     ___/      <    |       _/  \____ \\____ \_/ __ \_  __ \\"
print "/    |    \    |   |    |  \   |    |   \  |  |_> >  |_> >  ___/|  | \/"
print "\____|__  /____|   |____|__ \  |____|_  /__|   __/|   __/ \___  >__|   "
print "        \/                 \/         \/   |__|   |__|        \/       "



#parser setup
parser = argparse.ArgumentParser(description="Rip an APK from an Android device")
parser.add_argument('AppName', help='the name of the application you wish to rip')
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

#build the third command to rip the apk
cmd3 = 'adb pull ' + results_path[1]
print 'Pulling the apk now'
sp3 = subprocess.check_output(cmd3.split())
results_of_pull = sp3.split('\r\n')

#info them of the success of failure of the rip
if (results_of_pull[0].find('100%') != -1):
	print results_path[1] + ' have been pulled.'
else:
	print results_path[1] + ' have not been pulled.'

