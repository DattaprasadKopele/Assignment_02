def countthe():
    f = open("dk1.txt","r")
    d = f.read()
    m = d.split()
    count = 0
    for i in m:
        if i=='the':
            count+=1
    print("The count",count,"times")

countthe()