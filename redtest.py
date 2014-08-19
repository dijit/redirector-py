#!/usr/bin/env python

red = '\033[31m '

print red + "This should be red."

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

print bcolors.OKBLUE + 'This is a blue test' + bcolors.ENDC
