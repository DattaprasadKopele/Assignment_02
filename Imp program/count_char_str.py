""" Q. Write a program for count charecter from string after each charecter is changed ex=aaaabahhhhhaaa"""


s="aaaabahhhhhaaa"
print("Input string:", s)
output=""
previous=s[0]
c=1
i=1

while i<len(s):
    if s[i]==previous:
        c=c+1

    else:
        output=output+previous+str(c)
        previous = s[i]
        c=1

    if i == len(s)-1:
        output = output+previous+str(c)
    i=i+1

print("output: ",output)