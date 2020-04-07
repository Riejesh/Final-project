#!/usr/bin/env python3
import emails
import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 80
# If there's not enough disk, or not enough CPU, print an error




if not check_disk_usage('/'):
  email = emails.generate_na("automation@example.com", "student-00-d50b7297b142@example.com", "Error - Available disk space is less than 20%",
"Please check your system and resolve the issue as soon as possible.")

if not check_cpu_usage():
  email = emails.generate_na("automation@example.com", "student-00-d50b7297b142@example.com", "Error - CPU usage is over 80%",
"Please check your system and resolve the issue as soon as possible.")

