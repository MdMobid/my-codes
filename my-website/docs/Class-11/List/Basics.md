---
sidebar_position: 1
---

# Basic Questions
Some Basic List Related Programs

## 1. Write A Program To Display Sum of All The Numbers Present in a List:

```

# Assuming that "List1" is defined and consists of Numbers 

sum=0
for j in range (0,len(list1)):
  sum=sum+list1[j]

print("Sum of All Numbers in The List is:", sum)

```

## 2. Write A Program To Display Each Alternate Numbers in a List:

```

for i in range (0,len(list1),2):
  print(list1[i])

```

## 3. Write A Program To Display Highest Number Present in a List:

```

max=list1[0]
for i in range (1,len(list1)):
  if max<list1[i]:
    max=list1[i]

print("The Highest Number in the List is:", max)

```

## 4. Write A Program To Display Location and Frequency of a Given Element in List:

```

count=0
loclst=[]
num=int(input("Enter The Element You Want To Check its Frequency: "))
for i in range (0,len(list1)):
  if num==list1[i]:
    count=count+1
    loclst.append(i)

print(">> Frequency:", count)
print(">> Locations:", loclst)

```
