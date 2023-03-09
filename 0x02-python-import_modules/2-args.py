#!/usr/bin/python3
from sys import argv

arg_length = len(argv) - 1
if (arg_length == 0):
    print("{:d} arguments.".format(arg_length))
elif (arg_length == 1):
    print("{:d} argument:".format(arg_length))
else:
    print("{:d} arguments:".format(arg_length))

for i in range(1, arg_length + 1):
    print("{:d}: {:s}".format(i, argv[i]))
