from args import receive_input
org_lis = receive_input("Please enter numbers separated by comma:")
x = len(org_lis)
j = 0
while int(j) < x:
    y = org_lis[j]
    org_lis[j] = org_lis[x-1]
    org_lis[x-1] = y
    j = j + 1
    x = x - 1
print(org_lis)
    
    
  
 
   