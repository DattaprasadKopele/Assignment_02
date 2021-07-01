list=[10,20,30,40,10,40,20,50,60,70,80,100,80,80,80]
# list2=[]
# count=0
#
# for item in list:
#     list[i]==

# unique=[]
#
# dic={item:"key" if item in unique else unique.append(item) for item in list}
# duplicates=[item for item in dic if dic[item]=="key"]
#
# print(duplicates)




#### Remove duplicates

list2=[]
list3=[]

for item in list:
    # list2.append(item)
    # print(list2)

    if item not in list2:
        list2.append(item)
        # print(list2)

    else:
        list3.append(item)
print(list3)
print(set(list3))