#Taking 'i' As A Variable
i=True

while (i>0):
  x=int(input("Enter Your First Number: "))
  y=int(input("Enter Your Second Number: "))
  
  #This Condition Will Print The Below Instructions Only Once
  if i==1:
    print(
      '''
      1 --> Addition
      2 --> Subtaction
      3 --> Multiplication
      4 --> Division
      '''
      )
    
  oper=int(input("Enter Your Desired Operation: "))
  
  #Taking Repeating or Long Sentences as Variables
  p="You Had Selected For"
  r="And The Result is:"
  
  #For Addition
  if oper==1:
    addresult=x+y
    print(p, "Addition", r, addresult)

  #For Subtraction
  elif oper==2:
    subresult=x-y
    print(p, "Subtraction", r, subresult)
  
  #For Multiplication
  elif oper==3:
    pdtresult=x*y
    print(p, "Multiplication", r, pdtresult)

  #For Division
  elif oper==4:
    
    #If The User Enters the Divisor as Zero
    if y==0:
      print(p, "Division", r, "Undefined")
      
    else:
      divresult=x/y
      print(p, "Division", r, divresult)
  
  #If the User Enters an Invalid Operator
  else:
    print("Enter a Valid Operator")
  
  #If the User again wants to run this Calculator
  print( )
  again=input("Do You Want To Continue? (y/n): ")
  print( )

  if again=='y':
    i=i+1
    continue
  else:
    break

#Thank You Message
print("Thank You For Using This Calculator :)")
print("Created by Mobid")
