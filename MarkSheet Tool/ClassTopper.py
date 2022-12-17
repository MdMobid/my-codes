#CLASS TOPPER

max=grandlist[0][7]
for i in range (0,len(grandlist)):
  if max>grandlist[i][7]:
    max=max
  else:
    max=grandlist[i][7]
    toprindx=i

toprlist=grandlist[toprindx]

print("THE TOPPER OF THE CLASS IS: \n")
print("Name:", toprlist[0])
print("Roll No:", toprlist[1])
print("Mathematics:", toprlist[2])
print("Physics:", toprlist[3])
print("Chemistry:", toprlist[4])
print("Computer Science:", toprlist[5])
print("English:", toprlist[6])
print("Total Marks:", toprlist[7])
