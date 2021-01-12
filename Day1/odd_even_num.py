#seperate odd even numbers from a list

inp_lis = input("Enter the numbers separated by commas: ")
modi_list = inp_lis.split(',')
odd_lis =[]
even_lis =[]
for i in modi_list:
    if int(i) % 2 == 0:
      even_lis.append(i)
    else:
        odd_lis.append(i)
    
print(odd_lis)
print(even_lis)    
    