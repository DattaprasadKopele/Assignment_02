def countword():
    f = open("dk1.txt","r")
    d = f.read()
    m = d.split()

    print("The no.of words present in the txt file:",len(m))

countword()