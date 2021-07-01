def countuppercase():
    f = open("dk1.txt","r")
    d = f.read()
    m = d.split()
    count = 0
    for i in d:
        if i.isupper():
            count+=1
    print("The uppercase character is",count,"times")

countuppercase()