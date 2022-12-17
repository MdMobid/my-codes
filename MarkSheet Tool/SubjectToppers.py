#Subject Toppers

for i in range (1,6):
    
    if i==1:
      zi="MATHEMATICS: "
      yi=2
    if i==2:
      zi="PHYSICS: "
      yi=3
    if i==3:
      zi="CHEMISTRY: "
      yi=4
    if i==4:
      zi="COMPUTER SCIENCE: "
      yi=5
    if i==5:
      zi="ENGLISH: "
      yi=6

    maxi=grandlist[0][yi]
  
    for j in range (0,len(grandlist)):
        
        if maxi>grandlist[j][yi]:
            maxi=maxi
        else:
            maxi=grandlist[j][yi]
            stpri=j
      
    stprlsti=grandlist[stpri]

    print("THE TOPPER IN", zi)
    print("Name:", stprlsti[0])
    print("Roll No:", stprlsti[1])
    print("Marks Obtained in", zi, stprlsti[yi])
    print("\n")
