import subprocess
import re
"""
--------------------------------
If you are using this program for your research please cite:
Detecting the overlapping and hierarchical community structure in complex networks, 
Andrea Lancichinetti et al 2009 New J. Phys. 11 033015
"""


def normalized_mutual_information(file1, file2):
    res = subprocess.check_output(['mutual3/mutual', file1, file2])
    res = res.decode('utf-8')
    result = re.split("\n", re.split("\t", res)[1])[0]
    return float(result)
