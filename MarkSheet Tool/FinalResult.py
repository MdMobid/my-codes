#@title **CLASS MARK SHEET**
#RUN THIS CELL TO GET THE OUTPUT

from tabulate import tabulate

print(tabulate(grandlist, headers=["NAME:","ROLL NO","MATHEMATICS","PHYSICS","CHEMISTRY","COMPUTER SCIENCE","ENGLISH","TOTAL","PERCENTAGE","PASS/FAIL"]))
