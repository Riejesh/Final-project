#!/usr/bin/env python3

import requests


url = "http://localhost/upload/"
with open('/home/student-00-d50b7297b142/supplier-data/images/008.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})

with open('/home/student-00-d50b7297b142/supplier-data/images/001.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
with open('/home/student-00-d50b7297b142/supplier-data/images/003.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
with open('/home/student-00-d50b7297b142/supplier-data/images/002.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
with open('/home/student-00-d50b7297b142/supplier-data/images/006.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
with open('/home/student-00-d50b7297b142/supplier-data/images/007.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
with open('/home/student-00-d50b7297b142/supplier-data/images/004.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
with open('/home/student-00-d50b7297b142/supplier-data/images/009.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
with open('/home/student-00-d50b7297b142/supplier-data/images/005.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
with open('/home/student-00-d50b7297b142/supplier-data/images/010.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
