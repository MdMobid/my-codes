#Creating An Grand Empty List
grandlist=[]
std=int(input("TOTAL STRENGTH OF YOUR CLASS? "))

for i in range (1,std+1):
  
  #Creating An Empty List For Student Data
  stdlist=[]
  
  print("\n   DETAILS OF STUDENT NO.",i, "\n")

  #Taking Inputs From User
  name=input("Enter The Student's Name: ")
  stdlist.append(name)
  roll=int(input("Enter The Student's Roll No: "))
  stdlist.append(roll)

  print("Enter The Marks of The Student Correctly:")

  #Creating Loop For Input of Marks
  for j in range (1,6):
    if j==1:
      kj="Mathematics: "
    if j==2:
      kj="Physics: "
    if j==3:
      kj="Chemistry: "
    if j==4:
      kj="Computer Science: "
    if j==5:
      kj="English: "
  
    marks=int(input(kj))
    stdlist.append(marks)
    
  #Total Marks  
  sum=0
  for k in range (2,7):
    sum=sum+stdlist[k]
  stdlist.append(sum)

  #Total Percentage
  per=(sum/500)*100
  per=round(per,2)
  stdlist.append(per)

  #PASS/FAIL
  if stdlist[-2]>=165:
    rslt="PASS"
  else:
    rslt="FAIL"
  stdlist.append(rslt)
  
  #Add Above Student Details To The Grandlist
  grandlist.append(stdlist)

  #Clear Output
  from google.colab import output
  output.clear()

print("\n")
print("YOUR CLASS LIST HAS BEEN MADE SUCCESSFULLY")
print("NOW YOU CAN PROCEED FOR THE NEXT STEPS :)")
