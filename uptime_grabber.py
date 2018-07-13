#!/usr/bin/python

from socket import gethostname
import subprocess
from sys import platform

hostname = gethostname()

location_of_file_to_copy = "/root/machine_monitoring/uptime.txt"
subprocess.call(["uptime -p > {}".format(location_of_file_to_copy)], shell=True)

domain = "banana.cnsm.csulb.edu"
folder_to_place_in_banana = "/home2/www/banana"


if ".cnsm.csulb.edu" in hostname:
    hostname = hostname.replace(".cnsm.csulb.edu", "")


scp_command = "scp {} server@{}:{}/{}_uptime.txt".format(location_of_file_to_copy, domain, folder_to_place_in_banana, hostname)

subprocess.call(scp_command, shell=True)
