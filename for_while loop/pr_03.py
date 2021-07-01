##  How to skip some iteration from the loop


l1=[1,2,3,4,5,6,7,8]
for i in l1:

    if i==4:
        continue   # it will skip no.4
    print(f'processing integer{i}')

    print("Done")