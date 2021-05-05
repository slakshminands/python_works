#sum of pairs of elements in a list 
inp_list = input("Enter the numbers seperated by commas: " )
num_list = inp_list.split(",")
ret_lis = []
for num in num_list:
    ret_lis.append(int(num))

ret_list = []
for i in range(len(ret_lis)):
    if len(ret_lis) == i+1:
       break
    else:
        ret_sum = ret_lis[i] + ret_lis[i+1]
    ret_list.append(ret_sum)
print(ret_list)    
    
    
    