inp_list = input("Enter numbers separated by commas")
lis_ele = inp_list.split(",")
ret_lis = []
maxi = float('-inf')
for i in lis_ele:
    ret_lis.append(int(i))

for j in range(len(ret_lis)):
    if ret_lis[j] >= maxi:
        maxi = ret_lis[j]
print(maxi)